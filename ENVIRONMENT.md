# Environment

Owner: learner requests changes. Status of every entry below: **unvalidated proposal**. No installation steps have been run by Claude on a learner machine. When the learner runs a verification command, record the result in the "Validated on" column (with the learner's approval).

## Principles

1. Install a tool only when an unlock needs it (column "Needed from").
2. Never assume a tool exists because it existed before. Run its verification command.
3. Use official installers or package managers. Follow each tool's own current instructions; this file does not reproduce them because they change.
4. No machine-specific paths in this repository. Use environment variables or relative paths and document them here.
5. Supported platforms: **Linux** (primary; any distribution, no distribution-specific steps), **Windows 11/10 with PowerShell 7** (native, for Go and course work), macOS, and WSL2. Instructions give both a Linux (Zsh) and a Windows (PowerShell 7) form where they differ. A tool that is Linux-only (for example `strace`) is marked as such in the table below, and the unlock offers the Linux machine, WSL2 or a Linux container. **Native Windows has not been validated by any run yet.** Where `python3` is not defined on Windows, `py -3` or `python` is expected to work; this is also unvalidated.

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
| Rust (`rustup`, `cargo`) | Optional leisure track | stable | `cargo --version` | when the learner chooses to explore Rust | — | — |

## When a tool is missing

Tell the learner what is needed and why (one sentence), give the official source, have them run the verify command, and wait. If they cannot install it, switch to an unlock that does not need it.

## Environment record

Reported by the learner on 2026-11-16, at the start of `P0-GO-01`:

- OS: **Linux** at home (primary; no particular distribution; shell Zsh) and **Windows** at work (shell PowerShell 7).
- Portability: the learner wants the workflow to stay portable across both. Linux is the primary environment for the initial Go work.
- CPU/RAM: unknown.
- Docker: beginner (understands the purpose, little hands-on use). Whether it is installed is unknown.
- Go: no prior experience. Whether it is installed on either machine is unknown until the learner runs `go version`.
