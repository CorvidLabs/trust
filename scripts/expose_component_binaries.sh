#!/usr/bin/env bash
set -euo pipefail

: "${AUGUR:?AUGUR must identify the pinned Augur binary}"
: "${ATTEST:?ATTEST must identify the pinned Attest binary}"
: "${GITHUB_PATH:?GITHUB_PATH must identify the Actions path file}"

COMPONENT_BIN="${COMPONENT_BIN:-${RUNNER_TEMP:?RUNNER_TEMP must be set}/trust-component-bin}"
mkdir -p "$COMPONENT_BIN"

case "$AUGUR" in
    /*) ;;
    *) AUGUR="$PWD/$AUGUR" ;;
esac
case "$ATTEST" in
    /*) ;;
    *) ATTEST="$PWD/$ATTEST" ;;
esac

ln -sfn "$AUGUR" "$COMPONENT_BIN/augur"
ln -sfn "$ATTEST" "$COMPONENT_BIN/attest"

if [ ! -x "$COMPONENT_BIN/augur" ] || [ ! -x "$COMPONENT_BIN/attest" ]; then
    echo "error: component command links are not executable" >&2
    exit 1
fi

printf '%s\n' "$COMPONENT_BIN" >> "$GITHUB_PATH"
