---
hi: 1
families: [RELEASE]
---

# Proving a release before anyone installs it

## Intent

A tool that tells other repositories to prove themselves has to prove itself first, and against the exact artifact people will install rather than the source it was built from. Every release is installed into a throwaway repository, adopted, checked, and run through its own gate under enforced provenance before anything is published. The moving major channel only ever goes forward, and moving it stays a deliberate human act. A tag that turns out to be unusable is left exactly where it is and recorded as void, because rewriting history is the one thing a provenance tool must never do.

## Criteria

- **RELEASE-1**  A release proves itself against its exact tag before anyone can install it.
  - **RELEASE-1.a**  The tag and the version in the plugin manifest have to agree.
  - **RELEASE-1.b**  The tagged source is checked against its own contract before installation is tested.
  - **RELEASE-1.c**  The proof installs the published tag rather than reusing the source it was built from.
  - **RELEASE-1.d**  That freshly installed copy is taken through adoption, checkup, and the gate in a throwaway repository.
  - **RELEASE-1.e**  That proof has to satisfy enforced provenance, not merely soft provenance.
- **RELEASE-2**  Nothing is published until every proof has passed.
- **RELEASE-3**  A release candidate is published as a prerelease.
  - **RELEASE-3.a**  A release candidate never moves the stable channel.
- **RELEASE-4**  The moving major channel only ever goes forward.
  - **RELEASE-4.a**  Republishing an older release explains why the channel stays where it is instead of rolling back.
- **RELEASE-5**  Trust holds its own repository to the same gate it asks mine to pass.
  - **RELEASE-5.a**  Trust's own repository is gated on the same events a consumer's repository would be.
- **RELEASE-6**  The package formula is generated from the real released version, digest, and component versions.
  - **RELEASE-6.a**  The formula's own test proves the command is discoverable after installation.
- **RELEASE-7**  A tag that turned out to be unusable is left exactly where it is rather than quietly moved.
  - **RELEASE-7.a**  That tag is recorded as void so nobody installs it by accident.
- **RELEASE-8**  Moving a release channel stays something a person asks for, never a side effect of something else.
