# Contributing

1. Open or reference an issue describing the behavior change.
2. Create a feature branch; do not push directly to `main`.
3. Update `.trust.toml`, specs, tests, and documentation when their contracts change.
4. Run `fledge lanes run verify` locally.
5. Open a pull request using the repository template and wait for required checks and approval.

Trust orchestration must never silently weaken a committed gate. Security
reports belong in private vulnerability reporting, not public issues.
