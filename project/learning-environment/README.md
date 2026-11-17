# Engineering Learning Environment

Owner: learner approves changes. Status: the decisions below are recorded owner decisions (2026-11-17, `DECISION_LOG.md` D-012). The plan is a proposal. This area is not part of the curriculum approved in D-007.

A desktop-first, persistent engineering simulation and learning environment. This directory holds its **plans and architecture decisions**. It does not hold source code.

It is a separate product from the Go/PostgreSQL workflow platform described in [`../PLAN.md`](../PLAN.md). That platform is unchanged.

## Purpose

The learner builds capability by working, not by reading passively. Each topic moves through five steps:

| Step | Meaning |
|---|---|
| 1. Manual | Do it by hand |
| 2. Procedural | Follow a defined procedure |
| 3. Mechanized | Use a tool or mechanism |
| 4. Automated | Let a system do it |
| 5. Scaled | Apply it at larger size |

It is not a learning management system and not a sequence of passive tutorials.

First learning world: **Computer Foundations**. The intended end of the first slice is a working binary adder built from logic gates. That is a direction, not a committed design (Hypothesis).

## Ownership

| Item | Owner | Where |
|---|---|---|
| Concepts and curriculum | This repository | `knowledge/`, [`CURRICULUM.md`](../../CURRICULUM.md) |
| Product plans and architecture decisions | This repository | this directory |
| Source code, tests, implementation docs | Application repository | See "Application repository" below |
| Knowledge Standard | This repository | [`KNOWLEDGE_STANDARD.md`](../../KNOWLEDGE_STANDARD.md) (canonical, unchanged) |
| Standard extensions | This repository | [`KNOWLEDGE_STANDARD_ADDENDUM.md`](../../KNOWLEDGE_STANDARD_ADDENDUM.md) (subordinate to the standard) |

Rules:
1. The application links to this content and never copies it.
2. The application repository is not needed to read or maintain the curriculum ([`DECISION_LOG.md`](../../DECISION_LOG.md) D-012).
3. Product decisions go in [LE-DECISIONS.md](LE-DECISIONS.md). Curriculum and repository-wide decisions go in [`DECISION_LOG.md`](../../DECISION_LOG.md).
4. Rust is the application's native technology. It creates no learner requirement (LE-004).

## Application repository

- **Location:** workspace path `repositories/engineering-projects/projects/engineering-learning-environment`, inside the `engineering-projects` repository of the engineering workspace. This is a plain-text path, not a link. The repository has no remote, and this repository can't link to it in a way that works on GitHub or in another clone.
- **Workspace record:** the workspace decision log (outside this repository) holds entry WD-005, "Engineering Learning Environment is an independent repository under engineering-projects".
- It is not a Git submodule.

## Files

| File | Contents |
|---|---|
| [LE-PLAN.md](LE-PLAN.md) | Product direction, technical direction, first milestone, open items |
| [LE-DECISIONS.md](LE-DECISIONS.md) | Product and architecture decisions (LE-001 onward) |

The `LE-` prefix is needed because the course checker reserves the file names PLAN.md and DECISIONS.md for the `project/` folder itself.

## Claim labels

Documents here use the six labels of the Knowledge Standard section 6.1: Fact, Assumption, Interpretation, Observation, Hypothesis, Unknown. The workspace's five-label set applies only to workspace governance documents.

## Links

- [Knowledge Standard](../../KNOWLEDGE_STANDARD.md)
- [Addendum](../../KNOWLEDGE_STANDARD_ADDENDUM.md)
- [Project area README](../README.md)
