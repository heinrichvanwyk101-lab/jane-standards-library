# Jane Standards Library

This directory is the prepared source set for a future dedicated GitHub repository. The authoritative source files are also held in persistent storage so the corpus does not depend on the temporary working directory.

## Recommended repository

Create a private repository such as `jane-standards-library`. Do not mix the binary standards corpus into the Jane application repository.

## Initial contents

- `sources/official/` — verified official-source PDFs
- `catalogue/verified-download-manifest.csv` — machine-readable provenance and fingerprints
- `catalogue/verified-download-manifest.json` — JSON equivalent
- `catalogue/coverage-gap-register.csv` — domain coverage and acquisition backlog
- `catalogue/unresolved-sources.csv` — failed or invalid source links requiring replacement
- `docs/PUBLIC-CORPUS.md` — acquisition result and rules
- `scripts/download_public_standards.py` — reproducible acquisition script

## Git strategy

The initial valid PDF corpus is approximately 298 MiB and no current file exceeds GitHub's 100 MiB single-file limit. A dedicated normal Git repository is workable initially and avoids Git LFS billing dependencies. If the corpus grows substantially, migrate immutable binary sources to release assets or object storage while retaining the full catalogue, hashes and version records in Git.

## Integrity rule

Treat `sha256` in the manifest as the fingerprint of the authority-supplied payload retrieved from the recorded URL. Never silently replace a file. A changed payload must become a new version with a new hash, retrieval date and supersession decision.

## Readiness rule

Downloaded does not mean approved for automated compliance. A source becomes rule-ready only after:

1. title, authority, revision and effective date are verified;
2. applicability and supersession status are determined;
3. text/OCR quality is assessed;
4. requirements are extracted with page-level citations;
5. a competent human validates the extracted rule set.

## Known unresolved sources

- `ISGL-00` — umbrella URL failed; the separate official ISGL catalogue was acquired.
- `TAQA-04` — official AADC link returned a non-PDF placeholder.
- `TAQA-05` — official AADC link returned a non-PDF placeholder.

## Known metadata correction

`DMT-05` is the 446-page **Unified As-Built GeoSpatial Data Submission Standards**, Final, dated 30 March 2022. It is not presently verified as an IDAS V7/2024 manual.
