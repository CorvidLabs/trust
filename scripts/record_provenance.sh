#!/usr/bin/env bash
set -euo pipefail

: "${ATTEST:?ATTEST must name the pinned Attest binary}"
: "${AUGUR:?AUGUR must name the pinned Augur binary}"
: "${RANGE:?RANGE must identify the landed comparison}"
: "${REPORT:?REPORT must identify the Augur JSON output}"

POLICY="${POLICY:-.attest.json}"
NOTE="${NOTE:-Trust main CI matrix passed}"

"$AUGUR" check --range "$RANGE" --json > "$REPORT"
git config user.email "github-actions[bot]@users.noreply.github.com"
git config user.name "github-actions[bot]"

git fetch origin "+refs/notes/attest:refs/notes/attest-remote" 2>/dev/null || true
git notes --ref=attest merge -s cat_sort_uniq attest-remote 2>/dev/null || true
if ! "$ATTEST" verify --commit HEAD --policy "$POLICY" >/dev/null 2>&1; then
    "$ATTEST" sign --commit HEAD --reviewer agent:ci --confidence 1 --tests-passed \
        --from-augur "$REPORT" --note "$NOTE"
fi

published=false
for attempt in 1 2 3; do
    git fetch origin "+refs/notes/attest:refs/notes/attest-remote" 2>/dev/null || true
    git notes --ref=attest merge -s cat_sort_uniq attest-remote 2>/dev/null || true
    "$ATTEST" verify --commit HEAD --policy "$POLICY"
    if git push origin refs/notes/attest; then
        published=true
        break
    fi
    echo "provenance push raced on attempt $attempt; retrying after merge"
done
if [ "$published" != true ]; then
    echo "error: could not publish refs/notes/attest after three verified attempts" >&2
    exit 1
fi
git ls-remote --exit-code origin refs/notes/attest >/dev/null
