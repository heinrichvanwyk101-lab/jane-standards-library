# Jane Construction Standards Library — Public Corpus

Status date: 2026-09-20

## Acquisition result

- 35 official-source candidates attempted.
- 32 valid PDFs acquired and stored in the developer standards library.
- 3 unresolved or invalid responses: `ISGL-00`, `TAQA-04`, and `TAQA-05`.
- Every acquired source has a retrieval timestamp, byte size, page count, SHA-256 fingerprint, and canonical source URL in `verified-download-manifest.csv`.

## Important catalogue correction

The document stored as `DMT-05` identifies itself as **Unified As-Built GeoSpatial Data Submission Standards**, Final, 30 March 2022 (446 pages). It must not be represented as an IDAS V7/2024 manual unless a separate official source is located and verified.

## Storage rule

The PDFs are stored outside Git. Git contains catalogue and provenance metadata only. A Jane deployment should store developer-managed standards in object storage using immutable source objects keyed by SHA-256, with version/supersession records in the database.

## Status semantics

- `downloaded`: a PDF payload was retrieved from the official URL and passed PDF validation.
- `invalid-response`: the official URL returned a non-PDF or placeholder response.
- `failed`: no payload could be acquired.
- `invalid-pdf`: the payload began as a PDF but failed structural validation.

Acquisition is not the same as rule readiness. Before a document drives an automated compliance result, it must pass title/version verification, text/OCR assessment, structured rule extraction, and human validation against the source page.
