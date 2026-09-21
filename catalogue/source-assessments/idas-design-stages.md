# IDAS design-stage source assessment

Date assessed: 2026-09-21

## Decision

The supplied narrative is useful as a research hypothesis. The **30%, 60%, 90% and 100% IDAS submission gates are practitioner-confirmed by Heinrich van Wyk on 2026-09-21** and should be retained as the current operational gate model. The supplied citations reviewed to date do not independently establish those percentages, so Jane must distinguish this practitioner-confirmed rule from an authority-document-verified rule.

The detailed per-discipline deliverables remain candidate checks until each is mapped to an official source, a real submission package, or CRS evidence. Jane should retain every claim with its evidence level rather than flattening all material into one authority checklist.

## Verified official findings

Source: DMT / Abu Dhabi City Municipality, **ADM-BIM-002 BIM Documentation
Guidelines for Infrastructure**, Version 1.0, October 2020.

- Design-to-tender submissions are routed through Smart Hub; the guideline says
  construction-phase submissions were planned for PMWeb (section 5.2, PDF page
  33).
- BIM submission phase codes are:
  - Concept Design - CD
  - Preliminary Design - PD
  - Detailed Design - DD
  - For Tender - FT
  - Construction / regular PIM submissions - PIM
  - As-Built - AB
  - Asset handover - AIM
- BIM deliverables are cumulative from Preliminary Design to As-Built. Concept
  is explicitly treated as the exception.
- Detailed deliverable lists are project-specific and must be agreed in the
  Task Information Delivery Plan (TIDP) and Master Information Delivery Plan
  (MIDP).
- File naming, submission status and revision codes control mapping into the
  Employer CDE; incorrectly named files may fail BIM quality checking.
- The official sample discipline codes are RG Road Geometry, SM Signage and
  Marking, RS Road Safety, RP Road Pavement, L Lighting, SW Stormwater, GS
  Geotechnical Study, ST Structural, LS Landscape, IR Irrigation, MT Materials,
  EM Electro-mechanical and AD Addressing.

## Practitioner-confirmed operating rule

The current IDAS design gates are fixed at **30%, 60%, 90% and 100%**. This confirmation is operational evidence supplied by Heinrich van Wyk. Jane may use the four gates to structure workflows and package completeness reviews, while displaying provenance as `practitioner_confirmed` until an authority-issued source is attached.

Do not collapse the four percentage gates into the ADM-BIM-002 BIM phase-code table. The two classifications may be related, but the mapping must be evidenced before Jane treats it as deterministic.

## Claims not established by the supplied citations

| Supplied claim | Assessment | Jane treatment |
|---|---|---|
| IDAS has exactly three mandatory core stages | Superseded by practitioner confirmation of four gates: 30%, 60%, 90% and 100%. ADM-BIM-002 separately lists CD, PD, DD and FT BIM phase codes. | Use four percentage gates with `practitioner_confirmed` provenance; keep BIM phase codes separate. |
| Concept is always a 30% submission | 30% is practitioner-confirmed as an IDAS gate; its formal phase label and official documentary source remain pending. | Encode the gate, not an unsupported phase equivalence. |
| Detailed Design is universally 60%-90% | 60% and 90% are practitioner-confirmed as separate IDAS gates; official phase mapping remains pending. | Encode two distinct gates with provenance. |
| Final/Tender is a 100%/IFC submission | 100% is practitioner-confirmed as an IDAS gate. ADM-BIM-002 uses For Tender (FT), and no reviewed source yet proves FT = IFC = 100%. | Encode the gate; do not conflate FT and IFC. |
| The listed discipline deliverables are mandatory at each stated stage | The official guideline says detailed deliverables vary by project and are agreed through TIDP/MIDP. | Treat the supplied lists as candidate checks only. |
| WGS84 / UTM Zone 40N is required by ADM-BIM-002 | Not found in the downloaded guideline. It may exist in another GIS or survey standard. | Source separately before enforcing. |
| A Combined Utility Layout must demonstrate zero conflicts | Coordination and clash-free models are BIM objectives, but this exact universal deliverable statement is not established here. | Candidate rule pending an official checklist. |

## Source quality

- **Official / rule-capable:** DMT ADM-BIM-002, the official ISGL umbrella
  guideline, and the official Abu Dhabi Urban Street Design Manual.
- **Secondary / corroborative only:** Super Arc's 4 December 2024 IDAS article.
  It confirms a general process, agencies and examples of documents but contains
  no staged itemized checklist.
- **Secondary / weak:** Das & Partners' 16 January 2026 article. It is a general
  marketing overview and supplies no stage matrix.
- **Mirror only:** VTPI and Scribd copies. Use the official DMT files already in
  the corpus instead.

## Implementation consequence

The first IDAS checker should use a two-layer ruleset:

1. **Verified rules** - exact naming, phase codes, revision/status metadata and
   requirements directly supported by official documents.
2. **Practitioner-confirmed workflow rules** - currently the 30%, 60%, 90% and 100% IDAS gate structure, retained with named provenance and date.
3. **Candidate practice checks** - discipline deliverables derived from practitioner material, clearly labelled advisory until confirmed against a current IDAS/Smart Hub manual, real submission package or CRS evidence.

## Remaining evidence needed

- Current official IDAS/Smart Hub service manual and portal user guide.
- Authority-issued stage/discipline deliverables matrix.
- Current submission forms and folder structure.
- Municipality/applicability rules for Abu Dhabi, Al Ain and Al Dhafra.
- Real approved/rejected packages and CRS cycles to validate candidate checks.
- Official GIS/survey source for coordinate reference system requirements.

## Source links

- [Official ADM-BIM-002 PDF](https://www.dmt.gov.ae/adm/-/media/Project/DMT/ADM/E-Library/0001-Jan-2022-Doc/ADM-BIM-002Documentation-Guidelines-for-Infrastructure-projects.pdf)
- [Official ISGL umbrella guideline](https://www.dmt.gov.ae/adm/-/media/Project/DMT/ADM/E-Library/Abu-Dhabi-Emirate-Guideline-for-Infrastructure-Services-Standards.pdf)
- [Official Abu Dhabi Urban Street Design Manual](https://www.dmt.gov.ae/-/media/Project/DMT/DMT/E-Library/0001-Manuals/Abu-Dhabi-Urban-Street-Design-Manual.pdf)
- [Super Arc secondary overview](https://superarc.net/insights/what-is-idas-approval/)
- [Das & Partners secondary overview](https://www.dasandpartners.com/blog/idas-infrastructure-design-approval-system)
