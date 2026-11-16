# Session Handoff

Owner: Claude rewrites at each session end. A hint only; `LEARNER_STATE.md` wins on conflict.

- **Written:** 2026-11-16 (revision 4 session)
- **Session type:** curriculum design and correction. No teaching occurred.
- **Curriculum status:** PROPOSED. Not approved.
- **Learner state:** nothing completed, nothing in progress.
- **Repository:** candidate committed on `review/final-curriculum-candidate`; not merged.

## What happened (revision 4, correction pass, D-005)

Cut order repaired (Phase 4 recovery path kept whole), delivery guarantees G1–G4 stated and `P2-CONS-01` authored, just-in-time authoring rule drafted, evidence bundle contract and manifest added, checker rewritten with 50 tests, restart semantics split into three operations, five prerequisite gaps fixed, career snapshot narrowed. Essential plan is now 362 h. The proposal is committed on branch `review/final-curriculum-candidate` for independent review (base: `6e1b12ae18ce1af2458d2fcadaa9092472cd7903`, the only commit on `ccr-b573edbb-crcfsw`, which is unchanged). Review finding F3 was resolved in `P2-CONS-01` acceptance criterion 4 (D-006). Review material: `FINAL_REVIEW_PACKAGE.md` and `FINAL_REVIEW_PACKAGE.patch`.

## Earlier history

Learner decisions recorded in D-002: 10 h/week, declarative workflow graphs with persisted step results, replay as optional experiment, three career directions to investigate, no technique-naming in lessons. Budget redone (now 362 h essential, 124 h optional; `python3 tools/check_course.py --budget`). Preliminary career evidence in `career/CAREER_RESEARCH.md` (search summaries only; posting pages could not be opened because the session network blocked those hosts).

## Next step

Learner reads `REVIEW_REPORT.md`, answers section 6, approves or amends. On approval: record it in `DECISION_LOG.md`; set `CURRICULUM.md` `status: APPROVED`, `approved_by`, `approved_on`, and `catalog_fingerprint` to the output of `python3 tools/check_course.py --fingerprint`. Without approval: no teaching.

## Still open

`KNOWLEDGE_STANDARD.md` supplied, unchanged, governing (D-003); reconciliation confirmation pending. Single-repository decision applied (D-004): `knowledge/`, `project/`, `career/` directories; no other repository assumed. Career priority not chosen. OS and Go/SQL experience unknown. The learner's workspace is described at the start of `P0-GO-01` (no other repository is assumed).

## Do not

- Start teaching before approval.
- Treat estimates as measured. Re-measure after the first 27 estimated hours.
- Treat `career/CAREER_RESEARCH.md` conclusions as confirmed.
