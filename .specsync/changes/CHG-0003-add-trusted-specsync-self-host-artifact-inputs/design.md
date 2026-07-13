---
change: CHG-0003-add-trusted-specsync-self-host-artifact-inputs
artifact: design
---

# Design

Add `specsync-version` and `specsync-download-base-url` action inputs. Defaults remain `5.0.1` and empty. Resolve and validate them before lifecycle execution, expose only validated values as step outputs, and pass those outputs to the immutable nested SpecSync action. A non-empty override must be a local `file://` URL with no authority whose resolved directory is strictly beneath `RUNNER_TEMP`; missing directories, traversal, encoded traversal, and symlink escapes fail closed.
