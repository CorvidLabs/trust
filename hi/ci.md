---
hi: 1
families: [CI]
---

# The one check on a proposed change

## Intent

A reviewer should see one required check, not five, and should be able to tell from its result alone which layer objected. The check works out for itself which commits are being proposed, from the event that triggered it, and nothing supplied by a workflow can quietly widen or move that comparison. There is a third outcome between pass and fail — degraded — and it means exactly one thing: signed provenance is still being adopted. It must never be able to hide anything else.

## Criteria

- **CI-1**  A proposed change gets one required check instead of five separate ones.
- **CI-2**  The check reports each layer's result separately so I can see what objected without reading the log.
- **CI-3**  The overall result is one of passed, degraded, or failed.
  - **CI-3.a**  Degraded means only that signed provenance is still being adopted.
  - **CI-3.b**  Degraded never hides a failed verification, contract, or risk layer.
- **CI-4**  The check works out which commits to judge from the event that triggered it.
  - **CI-4.a**  A proposed change is judged exactly from its base commit to its head commit.
  - **CI-4.b**  A workflow input cannot redirect a proposed change away from its real base and head.
  - **CI-4.c**  A push is judged from where the branch was to where it now is.
  - **CI-4.d**  The first push of a new branch is judged as a whole commit rather than against nothing.
- **CI-5**  A repository checked out elsewhere on the runner is never judged by the host's event.
  - **CI-5.a**  A governed directory whose origin does not match the event repository has to be given its range outright.
- **CI-6**  The generated workflow asks for no more permission than reading the repository.
  - **CI-6.a**  Permission to publish pages lives only in the job that deploys the coverage map.
- **CI-7**  The coverage map is published only from a push, never from a proposed change.
- **CI-8**  A bad policy stops the check before any component tool is installed or run.
- **CI-9**  A checkout too shallow for risk and provenance to judge is called out rather than quietly producing a wrong verdict.
