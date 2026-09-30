# Audit Comp | Firedancer V1

- Page: https://immunefi.com/bug-bounty/firedancer-v1-audit-comp/scope/
- Max bounty: $1,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low
- End date: 2026-05-09T17:00:00.000Z

## Assets in scope (1)

- [blockchain_dlt] https://github.com/firedancer-io/firedancer/tree/v1.0 — Firedancer v1.0 branch (firedancer binary and all reachable code)

## Asset notes

The firedancer binary and all linked, reachable code are in scope. The full codebase is~636,000 lines of C. Compiler-dependent bugs are in scope for GCC 8.5, 13, and 14 only. Clang is not in scope.

__Key Areas of Concern__

**Runtime**

Where to look: `src/flamenco/runtime/ src/flamenco/vm/`
Conformance mismatches with Agave leading to LOA or LOF. Largest new surface area.

**Replay / Banks**

Where to look: `src/discof/replay/`
Transaction dispatch, bank lifetime management, fork-aware state transitions. Banks accessed concurrently via shared memory — look for race conditions, refcounting bugs, and use-after-free on bank structures.

**Accounts DB**

Where to look: `src/funk/ src/vinyl/ src/flamenco/accdb/`
Funk is accessed concurrently via shared memory; vinyl is accessed client-server style via shared memory. Look for race conditions, memory corruption,  attacker-reachable io_uring misuse, data corruption, and heap/workspace corruption.

**Repair**

Where to look: `src/discof/repair/`
Complex structures (forest, reassembly). DoS, overflows, UAF, wrong invariant assumptions.

**Gossip**

Where to look: `src/discof/gossip/`
Stateful structures, invariant mismatches causing bandwidth amplification.

**Consensus / Tower**

Where to look: `src/choreo/ src/discof/tower/`
Equivocation, liveness, fork choice bugs.

**RPC**

Where to look: `src/discof/rpc/`
New HTTP server, large attack surface.

**GUI**

Where to look: `src/disco/gui/`
Expanded HTTP-exposed interface.

**Signing Tile**

Where to look: `src/disco/sign/`
Private key leak

**Sandbox**

Where to look: `src/util/sandbox/`
Tile isolation, shared memory boundaries.

**Snapshot Loader**

Where to look: `src/discof/restore/`
Staging corrupt data for later exploitation.

**Cryptography**

Where to look: `src/ballet/`
Ed25519, SHA-256, AES, ChaCha20, BLS, secp256k1.

**Networking**

Where to look: `src/waltz/`
XDP, QUIC, HTTP, TLS. New QUIC client for vote transactions.

__Feature Gates__ 

Feature gates are only eligible for the bounty if they are activated on mainnet or present in this list: [Feature Gates](https://github.com/firedancer-io/firedancer/wiki/Feature-Gates). Bugs related to feature gates that are not activated on mainnet and not on the list are out of scope.

__Review tag__ 

[https://github.com/firedancer-io/firedancer/tree/v1.0](https://github.com/firedancer-io/firedancer/tree/v1.0)
Mid-contest bug fixes are possible.

__Mid-Contest Code Updates__

In this contest bug fixes may be applied mid-contest.

The project is to keep changes private as far as possible. When changes need to be made public, then the changelog will be updated here & in the Firedancer Audit Competition Discord channel. Publicly fixed bugs are invalid and the scope is updated to the new code.
All bug reports before the fix was public will earn a reward. All bug reports after are invalid. If a new bug is introduced by their fix then it is valid for a reward.

__Mid-Contest Changelog__

TBD

__Build Commands, Test Commands, and How to Run Them__

[Firedancer Localnet Setup Cluster Documentation](https://docs.google.com/document/d/12phZcetNGTdl_0eMjg8f7LbhyJfzFNuxSq6UQPbSrMM/edit?usp=sharing)

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope are valid.

__Duplicate Rewarding__

Duplicate submissions of bugs are valid under the following conditions:
- Duplicate reports for the same unfixed bug are valid 
- Once a fix is publicly disclosed, new reports for that bug are invalid
- Reports submitted before the fix are still eligible

Duplicate submissions of Insights are invalid.

The project commits to keeping private all info related to bug findings until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

__Attacker Position__

**Remote only:** All attacks must be exploitable by a remote attacker with no pre-existing access on the validator. The compromised-tile model (assuming code execution on another tile within the sandbox) is out of scope for this contest.

Firedancer may be in majority, supermajority, or minority position. Attacker controls up to ~20% of stake.

__Reference configuration__ 

All attacks must be valid against this configuration [TOML](https://docs.google.com/document/d/12phZcetNGTdl_0eMjg8f7LbhyJfzFNuxSq6UQPbSrMM/edit?usp=sharing), section 8c. It defines which components are network-exposed, including enabled RPC methods, GUI, and telemetry endpoints.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are **not** valid for a reward.

__Primacy of Impact vs Primacy of Rules__

Firedancer adheres to the Primacy of Rules, meaning the whole bug bounty program is run strictly under the terms and conditions stated on this page.

__KYC Requirement__

Immunefi will be requesting KYC information to pay for successful bug submissions. The following information will be required:
- Full name 
- Date of birth
- Proof of address (either a redacted bank statement with the address or a recent utility bill)
- Copy of Passport or other Government ID

Security researchers are required to submit KYC within 14 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement outlined in this program and cannot be:
- On OFAC SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Employees of Solana Foundation or any other Solana client project
- Security auditors who directly or indirectly participated in the audit review

__Insight Reporting__

Insight reports may be reported to this program and do not require a PoC. Insights are rewarded according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

__Dispute Resolution__

If there is any dispute over bug reports between projects and security researchers, Immunefi has final say on validity and severity based on the terms of this program.

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this program and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

The project may receive valid reports (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the bug's impact, which are not feasible or would require unconventional action and, hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) that, by default, state what security researchers and projects can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Firedancer has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (12)

- [blockchain_dlt] Critical: Any bug leading to loss of funds or acceptance of forged/invalid signatures
- [blockchain_dlt] Critical: Infinite mint — any bug allowing unauthorized token creation
- [blockchain_dlt] Critical: Key compromise or exfiltration exploit chain
- [blockchain_dlt] Critical: Runtime conformance bugs leading to loss of funds
- [blockchain_dlt] High: Accounts database corruption enabling delayed loss of funds
- [blockchain_dlt] High: Any sandbox escape (excluding tile-to-tile attacks)
- [blockchain_dlt] High: Arbitrary write primitives in execution (execle and execrp) tiles
- [blockchain_dlt] High: Bank hash mismatch or consensus bug causing all Firedancer validators to fork from the network (cluster-wide consensus failure)
- [blockchain_dlt] High: Remotely triggerable liveness failure affecting the entire cluster at once (all Firedancer validators crash simultaneously)
- [blockchain_dlt] Medium: Any bug leading Firedancer v1.0 to produce an invalid block or skip its leader slot
- [blockchain_dlt] Medium: Remotely triggerable crash or liveness failure for leader validators
- [blockchain_dlt] Low: Liveness issues triggerable only in certain configurations or limited time windows (exposed GUI/RPC, during snapshot boot)

## Impact notes

__Proof of Concept (PoC) Requirements__

Proof of Concept (PoC) Requirements A runnable PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

**A valid PoC should:**
- Build and run against the in-scope branch with clear setup instructions
- Demonstrate the impact - show the actual outcome (crash, corruption, Bank Hash Mismatch, etc.), not just a hypothesis
- Be self-contained - a reviewer should be able to reproduce the issue by following the steps in the report without additional guesswork
- Include the attacker model - specify what position the attacker is in (Current leader, staked validator, gossip participant, etc.) and what inputs they control.

**Examples of what qualifies:**
- A crafted network packet or sequence of packets that crashes the validator or leads to a bank hash mismatch in a local cluster
- A solfuzz-agave harness input (protobuf) that triggers a crash or bank hash mismatch between Firedancer and Agave. Accepted harness targets: instr_execute, txn_execute, elf_loader, vm_interp, vm_syscall_execute, shred_parse, pack_compute_budget. Inputs must include the harness target name. As a counterexample, an error code mismatch will crash the harness but does not result in a validator crash/bank hash mismatch and would not be eligible for submission.
- A minimally modified validator or client that exploits a consensus or replay bug **WITH CLEAR EXPLANATION AND JUSTIFICATION** of why the modification is necessary and how it’s still possible on mainnet.
- A PoC that demonstrates sandbox escape.

**Examples of what does not qualify:**
- A report describing a potential issue with no reproduction steps
- Static analysis output or code snippets without demonstrated impact
- Reports that only show a code path is reachable without showing it is exploitable

__Whitehat Educational Resources & Technical Info__

- Documentation: [firedancer-io.github.io/firedancer/](firedancer-io.github.io/firedancer/)
- Repository: [https://github.com/firedancer-io/firedancer](https://github.com/firedancer-io/firedancer)

__Optional Project Info__

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

Out of Scope:
- firedancer-dev development binary and tool
- Frankendancer codebase (code that is ONLY reachable from fdctl/fddev) - not the focus of this contest, please report issues via the standing bug bounty.
- Development scripts, tools, CI environment
- Solana protocol bugs (report to Anza/Jito)
- Social engineering or phishing attacks
- Test files and test-only code (unless they reveal a production vulnerability)
- Tile-to-tile attacks (compromised-tile attacker model).

**Directory Structure Reference**

```
src/
├── app/firedancer/ - Binary entry point, topology, CLI
├── ballet/         - Cryptography
├── choreo/         - Consensus (tower, ghost, equivocation)
├── disco/          - Shared tiles (net, pack, verify, dedup, GUI, shred)
├── discof/         - Full Firedancer tiles (replay, repair, gossip, tower, RPC, snapshots)
├── flamenco/       - Runtime, accounts DB API, sBPF VM, bank, program cache
├── funk/           - In-memory fork-aware database
├── vinyl/          - Persistent storage database
├── tango/          - IPC, shared memory messaging
├── util/           - Core utilities, sandbox, tile runtime
└── waltz/          - Networking (XDP, QUIC, HTTP, TLS)
```

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

Firedancer v1.0 is the successor to Frankendancer, the hybrid validator client that combines Firedancer's networking stack with the Agave runtime. In v1.0, all Agave dependencies have been replaced with native C implementations — making it the first fully independent Solana validator client. Key new components include the runtime, accounts database (funk + vinyl), replay system, repair, gossip, consensus, RPC server, and snapshot loader.

**Which chains and/or networks will the code in scope be deployed to?**

Solana mainnet.


__Public Disclosure of Known Issues__

Known issues are not eligible. The known issues trackers (linked in this page) are updated throughout the contest. Any bug added to a tracker before a researcher submits is not eligible for a reward. This includes known issues that the project is aware of but has consciously decided not to “fix,” necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 
- [bundle: known issues in bundle client](https://github.com/firedancer-io/firedancer/issues/9154)
- [consensus: known issues in tower, ghost, choreo](https://github.com/firedancer-io/firedancer/issues/9157)
- [eqvoc: known issues in equivocation detection](https://github.com/firedancer-io/firedancer/issues/9159)
- [gossip: known issues in gossip subsystem](https://github.com/firedancer-io/firedancer/issues/9160)
- [pack/bank: known issues in pack, bank, and execle](https://github.com/firedancer-io/firedancer/issues/9161)
- [poh: known issues in proof of history](https://github.com/firedancer-io/firedancer/issues/9162)
- [progcache: known issues in program cache](https://github.com/firedancer-io/firedancer/issues/9164)
- [quic/net: known issues in QUIC and networking](https://github.com/firedancer-io/firedancer/issues/9165)
- [repair: known issues in repair, forest, blockstore](https://github.com/firedancer-io/firedancer/issues/9166)
- [restore: known issues in snapshot, vinyl, and restore subsystem](https://github.com/firedancer-io/firedancer/issues/9176)
- [rpc: known issues in RPC and HTTP/2](https://github.com/firedancer-io/firedancer/issues/9168)
- [runtime: known issues in execution and runtime](https://github.com/firedancer-io/firedancer/issues/9171)
- [runtime: known issues in VM, SBPF, and ELF loader](https://github.com/firedancer-io/firedancer/issues/9170)
- [sandboxing: known issues in seccomp filters](https://github.com/firedancer-io/firedancer/issues/9172)
- [shred: known issues in shred processing](https://github.com/firedancer-io/firedancer/issues/9173)
- [sign: known issues in sign tile](https://github.com/firedancer-io/firedancer/issues/9175)
- [util: known issues in utilities and infrastructure](https://github.com/firedancer-io/firedancer/issues/9177)
- [verify/dedup/resolv: known issues in verify, dedup, resolv](https://github.com/firedancer-io/firedancer/issues/9178)
- Forged TPU TowerSync vote can create false forward confirmations
- fd_rdisp 128 requested-writable transaction counter wrap crashes replay
- Mid-slot invalid chained Merkle root child FEC can crash Firedancer replay scheduler

__Previous Audits__

Firedancer V1’s haven’t completed any audits yet.

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False

## Reward notes

# Frankendancer codebase (code that is ONLY reachable from fdctl/fddev) is not the focus of this contest, please report issues via the [standing bug bounty](https://immunefi.com/bug-bounty/firedancer/information/).

The following reward terms are a summary; read our [Standardized Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) for full context.

The reward pool will be entirely distributed among participants. The size depends on the bugs found:
- If no valid bugs are found, the reward pool will be **$50,000 USD**
- If no High or Critical severity bugs are found, the reward pool will be **$250,000 USD**
- If one or more High severity bugs are found, the reward pool will be **$500,000 USD**
- If one or more Critical severity bug is found, the reward pool will be **$1,000,000 USD**

For this Audit Competition, duplicates are valid for a reward under the following conditions:
- Duplicate reports for the same unfixed bug are valid
- Once a fix is publicly disclosed, new reports for that bug are invalid
- Reports submitted before the fix are still eligible

Fixes may be applied mid-contest.

Private known issues are **not** valid.

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program](https://immunefi.com/allstars/) participants. 

__Reward Payment Terms__

Payouts are handled by the Firedancer team directly and are denominated in USD. However, payments are done in USDC on Solana.

After the event has concluded and the final bug reports have been resolved, rewards will be distributed all at once based on Immunefi’s distribution formula.

## Out of scope (program-specific)

Issues referring TODO/FIXME comments are considered out of scope

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
