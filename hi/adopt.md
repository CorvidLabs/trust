---
hi: 1
families: [ADOPT]
---

# Adding the gate to a repository

## Intent

Adopting Trust should be a single small decision that a cautious person is willing to make on a repository they care about. It shows you what it would do before it does anything, writes all of its files or none of them, and never touches a file you wrote yourself. It works out how your project verifies itself rather than asking you to describe it, and it refuses to proceed at all rather than inventing a verification lane it cannot actually run. Anything you decline is recorded with the reason you gave, so a year later nobody has to guess why a layer is off.

## Criteria

- **ADOPT-1**  One command adds the whole trust gate to a repository that already exists.
- **ADOPT-2**  I can see every file adoption would touch before it touches anything.
  - **ADOPT-2.a**  A dry run leaves the working tree exactly as it found it.
- **ADOPT-3**  Adoption never overwrites a file I wrote myself.
  - **ADOPT-3.a**  Replacing a file that is already there takes an explicit force.
- **ADOPT-4**  Running adoption again on an adopted repository changes nothing.
- **ADOPT-5**  Adoption writes every file or none of them.
  - **ADOPT-5.a**  A failure partway through puts back everything it had already changed.
- **ADOPT-6**  Adoption works out the project's verification lane from the project itself.
  - **ADOPT-6.a**  A project whose stack it cannot recognize is refused rather than given an invented lane.
  - **ADOPT-6.b**  A project with no way to run its tests is refused rather than given a hollow lane.
  - **ADOPT-6.c**  A verification lane I already wrote is kept exactly as it is.
- **ADOPT-7**  Adoption leaves behind a CI workflow that runs the gate without further editing.
- **ADOPT-8**  Adoption leaves a short block of trust rules where coding agents will read them.
  - **ADOPT-8.a**  That block appears exactly once however many times adoption runs.
  - **ADOPT-8.b**  My own instructions above and below the block survive every update to it.
  - **ADOPT-8.c**  Damaged or duplicated markers stop adoption instead of it guessing where the block belongs.
- **ADOPT-9**  Every layer I decline during adoption is recorded with the reason I gave for declining it.
- **ADOPT-10**  The published coverage map stays off unless I ask for it during adoption.
- **ADOPT-11**  I can adopt straight into the strict profile instead of tightening later.
- **ADOPT-12**  Adoption tells me what to look at myself before I rely on the gate it just installed.
