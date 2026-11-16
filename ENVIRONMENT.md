# Environment

Owner: learner requests changes. Status of every entry below: **unvalidated proposal**. No installation steps have been run by Claude on a learner machine. When the learner runs a verification command, record the result in the "Validated on" column (with the learner's approval).

## Principles

1. Install a tool only when an unlock needs it (column "Needed from").
2. Never assume a tool exists because it existed before. Run its verification command.
3. Use official installers or package managers. Follow each tool's own current instructions; this file does not reproduce them because they change.
4. No machine-specific paths in this repository. Use environment variables or relative paths and document them here.
5. Supported platforms: **Linux**, **macOS**, **Windows via WSL2** (Ubuntu). Native Windows is not supported for the course tooling.

## Tools

Versions are minimums chosen for features the course uses. Check them against official release pages before relying on them.

| Tool | Why | Minimum version (proposed) | Verify | Needed from | Platform notes | Validated on |
|---|---|---|---|---|---|---|
| Git | Everything | 2.30 | `git --version` | start | — | — |
| Python 3 | Run `tools/check_course.py`; later AI work | 3.9 for checker; 3.11 for Phase 5 | `python3 --version` | optional at start | — | — |
| Go | Main backend language | 1.22 (enhanced HTTP routing); prefer latest stable | `go version` | `P0-GO-01` | — | — |
| Node.js + TypeScript | SDK, TS comparisons | Node LTS; TS 5.x | `node --version`, `npx tsc --version` | `P1-SDK-01` | — | — |
| PostgreSQL + `psql` | Datastore | 16 | `psql --version`; `psql -c 'select version()'` | `P1-PG-01` | Run via Docker or native install | — |
| Docker (or compatible) | Containers, local Postgres | current stable | `docker version` | `P1-PG-01` (optional) / `P4-DOC-01` (required) | On macOS/Windows needs a VM-backed engine | — |
| `strace` | Observe system calls | any | `strace -V` | `P0-OS-01` | **Linux only.** macOS: use a Linux VM, WSL2, or a Linux container | — |
| kind or k3d + `kubectl` | Local Kubernetes | current stable | `kubectl version --client`; `kind version` | `P4-K8S-01` | Needs Docker | — |
| OpenTelemetry tooling | Traces/metrics | per unlock | per unlock | `P4-OBS-02` | — | — |
| Rust (`rustup`, `cargo`) | Stretch only | stable | `cargo --version` | `PX-RUST-01` | — | — |

## When a tool is missing

Tell the learner what is needed and why (one sentence), give the official source, have them run the verify command, and wait. If they cannot install it, switch to an unlock that does not need it.

## Environment record

Learner OS, hardware and resource limits are unknown. Ask at the start of `P0-GO-01` and record them here with the learner's approval:

- OS: unknown
- CPU/RAM: unknown
- Docker available: unknown
