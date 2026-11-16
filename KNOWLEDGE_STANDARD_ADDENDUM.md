# Knowledge Standard Addendum

Owner: learner approves changes.

`KNOWLEDGE_STANDARD.md` (repository root, supplied by the learner, copied unchanged) is **canonical**. This file may only *extend* it for this course. If the two ever conflict, the standard wins and this file is corrected. Do not edit the standard from this repository.

Pinned sha256: `223f2e5242ead15d24a0ed4d8c259a009557c448faafb7dd83938672d1a62f8a`. The checker compares the standard against this hash so that an unapproved edit is caught. If the learner approves a change to the standard, update this pin and log it in `DECISION_LOG.md`.

The standard's own status line reads "Proposed". The learner has directed that it govern this curriculum, and that its status line and contents not be changed without the learner's explicit approval (`DECISION_LOG.md` D-003, D-004).

## How the standard applies here (no restatement)

| Standard section | How this course uses it |
|---|---|
| §1–2 Philosophy, understanding model | Governs teaching. Each unlock's challenge and questions should reach underlying reality, model, mechanism and consequences, not only a working program. |
| §2.5 Languages | Show TypeScript / Go / Rust contrasts only where they teach something language-independent vs language-specific. Rust is a stretch track. Never force all three. |
| §3 Concept document structure, §12 Complete module | Applies to **concept documents**. See "Boundaries inside this repository" below. Unlock files are challenge definitions, not concept documents; they stay short and link to concept documents when those exist. |
| §4.2 Analogies | Any analogy used in teaching names what maps, where it helps, where it breaks, and moves to the real model. |
| §5 Classification | Keep theory, practice, evidence and judgment distinguishable in anything written. |
| §6 Claim labels, source quality, verification, uncertainty | Applies to everything Claude writes here, including unlock text and `career/CAREER_RESEARCH.md`. Do not promote assumptions or hypotheses to facts. |
| §7 Experiments | `TEMPLATES/EXPERIMENT.md` uses the standard's seven headings. Preserve failed experiments. |
| §8 Mastery L0–L5 | Used exactly as written for mastery targets and evaluation. Not repeated here. |
| §8.2 Understanding gaps | When a learner cannot explain something, go back to the earliest unresolved prerequisite and repair the model. Do not add advanced material. Written into `CLAUDE.md`. |
| §9.2 Corrections | If an authored unlock or note is found wrong, correct it (with approval), list dependent unlocks, and re-check completed work that relied on it. |
| §11 Writing | Plain language, define terms, separate essential from optional depth (matches the essential/optional classes in `UNLOCKS/CATALOG.md`). |

## Extensions (not in the standard; each with its reason)

| Extension | Reason |
|---|---|
| **Evidence records.** A completed unlock needs `EVIDENCE/<ID>/` with a reproducible reference (project and commit, or experiment path) and the learner's actual hours. | State must be portable across machines and sessions; standard §8.1 names evidence types but not where they live. |
| **Recorded mastery is what was shown**, even if below the target; the unlock then stays open. | Prevents inflated progress. |
| **Retrieval check after 4+ weeks idle** on the last 2–3 completed unlocks. | Long breaks are expected; completion records should not imply retained skill. |
| **Explanation pacing (internal).** Explain in layers: what it is and why it matters; a working picture; the mechanism; edge cases and limits. Reveal a layer when the problem needs it. Claude does not announce or teach this method. | Learner preference: no full theory landscape up front, no method talk (`D-002`). The standard fixes what to cover, not the order of disclosure. |
| **Market-data sources** (for `career/CAREER_RESEARCH.md`): best = posting read in full with its date; then a survey with stated method and sample; then recruiter or vendor estimates; search-result summaries are pointers only. State sample size. | Standard §6.2's ranking covers technical sources, not job-market data. |
| **Hour estimates** per unlock (build, study, verify, consolidate), re-measured against actuals. | Feasibility control for a fixed deadline. |

## Boundaries inside this repository

The standard describes a larger ecosystem with separate repositories. This course is one self-contained repository (learner's decision, D-004). Its principles are preserved by directories, not by separate Git repositories: **canonical ownership of concepts** and **separation of kinds of knowledge**.

| Standard boundary (§10) | Directory here | Holds |
|---|---|---|
| Engineering Knowledge | `knowledge/<domain>/` | Canonical language-independent concept documents |
| Engineering TypeScript / Go / Rust | `knowledge/languages/{typescript,go,rust}/` | Language-specific behavior only, linking to the concept document |
| Engineering Projects | `project/` | Plans, architecture decisions, design documents. Not source code |
| Engineering Career | `career/` | Market research, direction analysis, later credentials and interview notes |
| Course control (not in the standard) | repository root, `PHASES/`, `UNLOCKS/`, `LEARN/`, `EVIDENCE/`, `ARCHIVE/`, `TEMPLATES/`, `tools/` | Curriculum, learner state, evidence, instructions |

Rules, from §10.1, applied across directories:
1. A concept has one canonical home. Link to it; do not copy it.
2. Language directories explain language-specific realization only.
3. `project/` references `knowledge/`; it does not copy it.
4. `career/` documents reference demonstrated skills and project evidence (`EVIDENCE/`, `project/`), not claims.
5. Platform architecture decisions go in `project/DECISIONS.md`; curriculum decisions in `DECISION_LOG.md`.
6. Historical experiments (`EVIDENCE/`) stay distinguishable from current verified guidance (`knowledge/`).

Concept documents are created on demand, not in advance (`knowledge/README.md`).

**Learning material is not a concept document.** `LEARN/<ID>/` presents one unlock to the learner: its steps, exercises and answer keys. It teaches from the standard's concept structure (problem, model, mechanism, consequences, limits) but is not the canonical home of a concept. When a language-independent concept needs a canonical document, that goes in `knowledge/`, and the learning material links to it instead of repeating it.

**Teaching examples are the one place code may live in this repository.** Runnable code that a lesson refers to sits under `LEARN/<ID>/examples/`. It is teaching material, not the learner's work and not PRJ-ENGINE; the learner's own code stays in their workspace. The checker rejects code anywhere else.
