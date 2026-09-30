# Audit Comp | Firedancer v0.1

- Page: https://immunefi.com/bug-bounty/firedancer-boost/scope/
- Max bounty: $1,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium
- End date: 2024-08-21T08:00:00.000Z

## Assets in scope (1)

- [blockchain_dlt] https://github.com/firedancer-io/firedancer/tree/e60d9a6206efaceac65a5a2c3a9e387a79d1d096 — Firedancer v0.1 Testnet (only directory and file listed in this file [https://asymmetric-assets.s3.amazonaws.com/fdctl-scope.txt?utm_source=immunefi] are within the scope)

## Asset notes

The Firedancer validator builds as a single binary: `fdctl`.  All code and functionality linked and reachable by the main function of this binary is in scope, including from the primary `run` command, but also `configure`, `monitor`, and others. Bugs in linked but unreachable code (for example: cryptography implementations that are behind a development flag or library utility code that is never called) are in scope but are not exploitable and will be considered informational (aka insight reports).

The Firedancer repository contains code for two validators:

- Firedancer v0.1, lovingly nicknamed “Frankendancer”, a split between Firedancer and the existing Agave validator written in Rust
- A full C-only Firedancer completely replacing the existing Agave validator.

The full Firedancer code is behind a development flag, and findings in code that is only reachable in full Firedancer will be considered informational (aka insight reports).

The Firedancer v0.1 validator interfaces with the existing Agave validator written in Rust via an FFI interface. This FFI interface and the modifications to Agave to support such FFI are in scope, but bugs in the Agave validator itself that would impact existing Solana validators should be reported to the [Agave bug bounty](https://github.com/anza-xyz/agave/security#bounty) and are not considered in scope for the contest.

The [directory and file listing](https://asymmetric-assets.s3.amazonaws.com/fdctl-scope.txt) are provided to help navigate the codebase and determine what is in scope. The ground truth for scope and impact will follow the production binary.

The Firedancer v0.1 sandbox (and machine model) are explicitly **in-scope**. This means that a researcher could **assume** a tile’s already been breached, and any findings downstream of that “contrived” tile breach are valid. As an example: Assume the “Net” tile has been breached, such that the researcher has full RCE within the sandbox of the Net tile. If the attacker is able to cause malicious effects in any of the “downstream” tiles or on the system itself, these findings would also be in scope.

__Mid-Contest Code Updates__

In this contest bug fixes may be applied mid-contest.

The project is to keep changes private as far as possible. When changes need to be made public, then the changelog will be updated here & in the [Firedancer Audit Competition Discord channel](https://discord.com/invite/immunefi?utm_source=immunefi). Publicly fixed bugs are invalid and the scope is updated to the new code.

All bug reports before the fix was public will earn a reward. All bug reports after are invalid. If a new bug is introduced by their fix then it is valid for a reward.

__Mid-Contest Changelog__

- July 16 :: improve balance between votes and non-votes https://github.com/firedancer-io/firedancer/pull/2404

Asset in scope link updated from https://github.com/firedancer-io/firedancer/tree/v0.106.11814 to https://github.com/firedancer-io/firedancer/tree/e60d9a6206efaceac65a5a2c3a9e387a79d1d096

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

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

__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement outlined in this program and cannot be:
- On OFAC SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Employees of Solana Foundation or any other Solana client project
- Security auditors who directly or indirectly participated in the audit review

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this program and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

The project may receive valid reports (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the bug's impact, which are not feasible or would require unconventional action and, hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) that, by default, state what security researchers and projects can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Firedancer has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (7)

- [blockchain_dlt] Critical: Any bug leading to loss of funds or acceptance of forged / invalid signatures
- [blockchain_dlt] Critical: Any sandbox escape
- [blockchain_dlt] Critical: Key compromise/exfiltration exploit chain
- [blockchain_dlt] High: Process to process RCE between sandboxed tiles
- [blockchain_dlt] Medium: Any bug leading Firedancer v0.1 to produce an invalid block or skip its leader slot
- [blockchain_dlt] Medium: Consensus issues causing Firedancer v0.1 validators to fork
- [blockchain_dlt] Medium: Liveness issues that cause Firedancer v0.1 validators to crash or be unavailable

## Impact notes

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Whitehat Educational Resources & Technical Info__

- Documentation: [https://firedancer-io.github.io/firedancer/](https://firedancer-io.github.io/firedancer/)
- Technical education: 
     - [https://github.com/firedancer-io/firedancer/blob/main/README.md](https://github.com/firedancer-io/firedancer/blob/main/README.md)
     - [https://github.com/firedancer-io/firedancer/blob/main/src/disco/README.md](https://github.com/firedancer-io/firedancer/blob/main/src/disco/README.md)
     - All header files contain sufficient documentation about each component's function
- Non-technical education:
     - Solana Docs: https://solana.com/docs

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

This is a complete ground-up implementation of a Solana protocol client. It was based on the Agave client ([https://github.com/anza-xyz/agave](https://github.com/anza-xyz/agave)), which is written in Rust, but this implementation is written from scratch in C.

__Where do you suspect there may be bugs? Valuable aspects of this question are:__

**Which parts of the code are you most concerned about?**
- Signing Tile ([https://github.com/firedancer-io/firedancer/tree/v0.106.11814/src/disco/keyguard](https://github.com/firedancer-io/firedancer/tree/v0.106.11814/src/disco/keyguard)) 
- QUIC Tile ([https://github.com/firedancer-io/firedancer/tree/v0.106.11814/src/waltz/quic](https://github.com/firedancer-io/firedancer/tree/v0.106.11814/src/waltz/quic)) 
- Sandbox ([https://github.com/firedancer-io/firedancer/tree/v0.106.11814/src/util/sandbox](https://github.com/firedancer-io/firedancer/tree/v0.106.11814/src/util/sandbox)) 

**What attack vectors are you most concerned about?**
- Any attack vector that results in the loss of funds
- Remote Code Execution, leading to compromise of validator key material or arbitrary transaction signing
- Denial of Service, leading to degradation or loss of service availability
- Global Denial of Service, leading to consensus failure, excessive forking, or chain halts

**Which part(s) of the system do you want whitehats to attempt to break the most?**
- Signature Verification Tile (Denial of Service / RCE / Arbitrary Signing)
- Network and QUIC Tiles (Denial of Service / RCE)
- Sandbox Escape or Violation (Abusing the sandbox or violation of sandbox policies for unexpected outcomes)
- Inconsistencies between Firedancer / Agave behavior that lead to unsafe outcomes.

**Are there any assumed invariants that you want whitehats to attempt to break?**
- If any tile is compromised, the sandbox should contain its effects on that tile. It should not allow the compromise to significantly impact other tiles and/or the system.

__Would you consider any bug report requiring their involvement to be out of scope as long as they operate within the privileges attributed to them?__

- Any bug reports that assume a pre-existing compromise of the validator operating system, applications, or any administrative control over the operating system.
- Any bug dependent on exploiting vulnerabilities in the agave client codebase. 
- Any bug reports that require social engineering or physical attack on a person or the system.
- Any bug reports that assume a malicious operator or the like.
- Any bug that is not exploitable on the latest stable and supported Linux distributions ([Ubuntu](https://ubuntu.com/about/release-cycle), [Debian](https://www.debian.org/releases/), [Fedora](https://docs.fedoraproject.org/en-US/releases/), or [Red Hat](https://access.redhat.com/support/policy/updates/errata) Distributions).
- Any bug that is not focused on x86 architecture.
- Any bug that is not exploitable on the latest stable and supported GCC versions.
- Any bug that has an initial vector of compromise in a dependency.
- Any bug in a dependency that is not exclusive to Firedancer should instead be reported to the upstream repo. (For example, If you find a bug in Agave that also affects Agave, you should report it to the [Agave bug bounty program](https://github.com/anza-xyz/agave/security#bounty) instead).

__What external dependencies are there?__

**Build Dependencies:** perl, autoconf, gettext, automake, autopoint, flex, bison, build-essential, gcc-multilib, protobuf-compiler, llvm, lcov, libgmp-dev, cmake.

__Where might whitehats confuse out-of-scope code to be in-scope?__

Code exists in the repository, which is in development but not yet executed by the validator, while it currently leverages the Agave client for these functions - for example, `src/flamenco/runtime/`, `src/ballet/sbpf/`.  Attempts have been made above to make this very clear in the file dump listing at the bottom of the scope table, but there may be some minor exceptions that we can clear up if there are questions.

__Are there any unusual points about your protocol that may confuse whitehats?__

TLS stack handwritten only contains the parts absolutely necessary for Firedancer

__What is the test suite setup information?__

- GitHub Actions: [https://github.com/firedancer-io/firedancer/tree/main/.github/workflows](https://github.com/firedancer-io/firedancer/tree/main/.github/workflows)
- Additionally, M1 fuzzing harnesses do exist in the main repo, you can find them with this command: find . -type f -name 'fuzz_*.c' -path './src/*'
- Fuzzing harnesses can be built with a modern Clang compiler (recommended: 17): `MACHINE=linux_clang_x86_64 EXTRAS="asan fuzz" make -j fuzz-test`

__How to build and run the node?__

[https://firedancer-io.github.io/firedancer/guide/getting-started.html](https://firedancer-io.github.io/firedancer/guide/getting-started.html)

__Public Disclosure of Known Issues__

Bug reports covering previously discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix,” necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 
- [https://github.com/firedancer-io/firedancer/issues](https://github.com/firedancer-io/firedancer/issues) (any public issues before submission)
- [https://github.com/firedancer-io/firedancer](https://github.com/firedancer-io/firedancer) (any fixes in the main repo before submission)

__Previous Audits__

Firedancer v0.1 completed audit reports can be found at [https://github.com/firedancer-io/audits](https://github.com/firedancer-io/audits). Any unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary; read our [Firedancer v0.1 Reward Distribution Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/26610998104465-Firedancer-v0-1-Audit-Competition-Reward-Terms) for the full details.

The reward pool will be entirely distributed among participants. The size depends on the bugs found:
- If no valid bugs are found, the reward pool will be **$50,000 USD**
- If no High or Critical severity bugs are found, the reward pool will be **$250,000 USD**
- If one or more High severity bugs are found, the reward pool will be **$500,000 USD**
- If 1 Critical severity bug is found, the reward pool will be **$700,000 USD**
- If 2 Critical severity bugs are found, the reward pool will be **$800,000 USD**
- If 3 or more Critical severity bugs are found, the reward pool will be **$1,000,000 USD**

For this Audit Competition, duplicates are valid for a reward. Private known issues are **not** valid.

Rewards are distributed according to the impact of the vulnerability based on the Immunefi [Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Payment Terms__

Payouts are handled by the Firedancer team directly and are denominated in USD. However, payments are done in USDC on Solana.

After the event has concluded and the final bug reports have been resolved, rewards will be distributed all at once based on Immunefi’s distribution formula.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi).

## Out of scope (program-specific)

(none)

## Out of scope and rules

These impacts are out of scope for this bug bounty program. 

__All Categories:__

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program

__Websites and Apps__

- Theoretical impacts without any proof or demonstration
- Impacts involving attacks requiring physical access to the victim device
- Impacts involving attacks requiring access to the local network of the victim
- Reflected plain text injection (e.g. url parameters, path, etc.)
    - This does not exclude reflected HTML injection with or without JavaScript
    - This does not exclude persistent plain text injection
- Any impacts involving self-XSS
- Captcha bypass using OCR without impact demonstration
- CSRF with no state modifying security impact (e.g. logout CSRF)
- Impacts related to missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”) without demonstration of impact
- Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces
- Impacts causing only the enumeration or confirmation of the existence of users or tenants
- Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows
- Lack of SSL/TLS best practices
- Impacts that only require DDoS
- UX and UI impacts that do not materially disrupt use of the platform
- Impacts primarily caused by browser/plugin defects
- Leakage of non sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)
- Any vulnerability exploit requiring browser bugs for exploitation (e.g. CSP bypass)
- SPF/DMARC misconfigured records)
- Missing HTTP Headers without demonstrated impact
- Automated scanner reports without demonstrated impact
- UI/UX best practice recommendations
- Non-future-proof NFT rendering

__Blockchain/DLT & Smart Contract Specific:__

- Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks

__Prohibited Activities:__

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
