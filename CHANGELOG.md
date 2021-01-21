# CHANGELOG
All notable changes to this project will be documented in this file.

The format is adapted from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
---
### Added:
- 

### Changed:
-

### Removed:
-

### Fixed:
- 

### Security
-


## [0.1.0-alpha] - 2021-Jan-21
---
### Added:
- README.md file created
- KindleToMD.py file created
- Ability to read in files
- Ability to scan files for keywords
- Ability to create markdown files for export
- Ability for the program to differentiate between notes and highlights
- Error message for if the user does not use the program correctly (Usage: 'python KindleToMD.py {TITLE OF BOOK})

### Fixed:
- Programming searching for only first keyword instead of all keywords as a string by adding a " ".join(argv[1:])
