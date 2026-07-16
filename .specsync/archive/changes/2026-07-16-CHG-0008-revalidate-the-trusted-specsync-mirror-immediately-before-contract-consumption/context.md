---
change: CHG-0008-revalidate-the-trusted-specsync-mirror-immediately-before-contract-consumption
artifact: context
---

# Context

Trust validates a runner-local SpecSync mirror while resolving action configuration, then executes the governed repository's lifecycle command before the nested SpecSync action consumes that mirror. Because lifecycle commands are pull-request-controlled and inherit `RUNNER_TEMP`, they can replace a previously validated archive or checksum with a symlink after validation.

The contract gate therefore needs a second validation boundary after lifecycle execution. No repository-controlled process runs between this boundary and the immutable SpecSync action.
