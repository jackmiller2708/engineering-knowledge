# Manifest — <UNLOCK-ID> — <YYYY-MM-DD>-<n>

Lives at `EVIDENCE/<UNLOCK-ID>/<YYYY-MM-DD>-<n>/manifest.md`. A fresh session without the learner's workspace must be able to tell from this file, and the files it lists, exactly what was demonstrated. Keep it concise. Keep only the files needed to reproduce this specific verification. Never copy a whole workspace, dependency folders, or build output.

unlock: <UNLOCK-ID>
capability: <one sentence: what the learner demonstrated>
evidence_kind: preserved
implementation_attempt: 1
provenance: <where the work came from: project area, source locations relative to the workspace root, version-control reference or per-file hashes. No machine paths>
reproduced_by: n/a

`evidence_kind` is one of:
- `preserved`: the files and outputs were captured from the learner's own run. Nobody else re-ran them.
- `independently-reproduced`: an evaluator re-ran the commands below from this bundle in a clean environment and the observed results matched. Then set `reproduced_by` to who and when (for example `Claude session, 2027-02-14`).

## Environment
- os: <name and version>
- arch: <cpu architecture>
- toolchain: <tool version, e.g. go 1.xx>
- toolchain: <one line per tool used>

## Setup
- <dependency or setup step needed before the commands work, or "none">

## Artifacts
| path (relative to artifacts/) | sha256 | role | description |
|---|---|---|---|
| src/example.go | <64 hex characters> | code | what it is |

Roles: code, test, data, output, script, doc, config. Every file under `artifacts/` must be listed. Hash with `sha256sum`.

## Commands
| # | command | working dir | expected | observed | exit |
|---|---|---|---|---|---|
| 1 | <exact command> | artifacts/ | <expected result> | <what actually happened> | 0 |

## Limitations
- <known limits and unverified conditions, or "none known">
