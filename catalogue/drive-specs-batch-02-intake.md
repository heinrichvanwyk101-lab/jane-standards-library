# Google Drive Specs 2 intake

Intake status: **upload declared complete by the owner on 2026-09-21**

The source files remain in the owner's private Google Drive folder. This repository records catalogue metadata and provenance, not private access URLs.

## Intake scope observed

The completed batch materially expands the corpus across:

- IDAS / infrastructure-service and BIM documentation
- roads, traffic, detours, parking, transport and freight
- master-plan submission requirements and development-management templates
- urban design, façades, storefronts, signage and rooftop-service concealment
- public realm, pedestrian paving, outdoor seating, lighting / dark-sky policy
- Estidama PCRS, PBRS and PRRS manuals, calculators and submission templates
- Sahel community, building and public-realm handbooks / scorecards
- policies, legislation, procurement references and operational ITC material

Cataloguing a file does not make every document a deterministic rule. Each file still requires authority, version, currency, applicability and rule-extraction review.

## Exact-duplicate removal

Only byte-identical files were removed. Matching names or sizes alone were not treated as proof.

| Canonical retained file | SHA-256 | Duplicate copies permanently deleted |
|---|---|---:|
| ADM-BIM-002_BIM-Documentation-Guidelines-for-Infrastructure_V1.0_Oct-2020.pdf | `b9302965ac77970e51c913c6cc829c479894a9429c1aac1dca212a9f2da0f242` | 3 |
| Abu-Dhabi-Emirate-Guideline-for-Infrastructure-Services-Standards.pdf | `a5a9e38d663b8fae06924fe7b5d96ae5a06c8a5b6aa8ecfec669c0c8336f7d7b4` | 3 |
| utility demand calculations v2 March 2021.xlsx | `3e6088018b46aa22e6bcd07f2d846b24c902d18eaccf7e6f697286fdad9bb297` | 1 |
| PVRS Waste Calculator 1 Pearl v10.xls | `6ef2df3008a6de567ed9ab555fe74b43b7c0be833b2b49ec268b1809aa5fb89d` | 1 |
| CMP Masterplan Submission Guidelines Requirements20260818 (1).pdf | `15f49acb8aa793dc233fb717344086c69bac8ed090caa020f8f8a3cf6c6ff07a` | 1 |
| DMP Masterplan Submission Guidelines Requirements20260818.pdf | `1e3d30f3ccb8fae06924fe7b5d96ae5a06c8a5b6aa8ecfec669c0c8336f7d7b4` | 1 |

Total duplicate files deleted in this pass: **10**.

Potential cross-batch duplicates and alternate editions remain until their bytes or substantive content are compared against the first Specs batch. In particular, the alternate Urban Street Design Manual must not be deleted merely because another edition exists.

## IDAS gate correction

The working IDAS gate structure is **30%, 60%, 90% and 100%**, practitioner-confirmed by Heinrich van Wyk on 2026-09-21.

This is stored separately from the ADM-BIM-002 phase codes (CD, PD, DD and FT). Jane must not infer a one-to-one mapping between percentage gates and BIM phase codes until documentary or package/CRS evidence establishes it.

## Next catalogue pass

1. Generate a row for every surviving file with Drive ID, filename, MIME type, byte size and checksum.
2. Detect cross-batch exact duplicates.
3. Inspect archives and list their contents without treating archive members as current standards.
4. Classify each item as rule-capable, reference-only, template/calculator, superseded, duplicate, or pending review.
5. Extract stage-, discipline- and authority-specific requirements with page-level citations.
6. Validate extracted IDAS checks against real submission packages and CRS outcomes.
