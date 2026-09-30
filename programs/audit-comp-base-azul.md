# Audit Comp | Base Azul

- Page: https://immunefi.com/bug-bounty/audit-comp-base-azul/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Smart Contract
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: 2026-05-04T20:00:00.000Z

## Assets in scope (3)

- [blockchain_dlt] https://github.com/base/base/tree/v0.8.0-rc.28 — Offchain Components
- [smart_contract] https://github.com/base/contract-deployments — Base Azul
- [smart_contract] https://github.com/base/contracts/tree/v8.1.0/src/multiproof — Implementation Contracts

## Asset notes

__Build Commands, Test Commands, and How to Run Them__

Detailed build commands, test commands, and run instructions are available in the README files and documentation within each GitHub repository:
- For offchain components: [https://github.com/base/base/](https://github.com/base/base/)
- For Base Azul: [https://github.com/base/contract-deployments](https://github.com/base/contract-deployments)
- For implementation contracts: [https://github.com/base/contracts](https://github.com/base/contracts)

__Mid-Contest Code Updates__

In this contest bug fixes may be applied mid-contest.

The project is to keep changes private as far as possible. When changes need to be made public, then the changelog will be updated here & in the Base Azul Audit Competition Discord channel. Publicly fixed bugs are invalid and the scope is updated to the new code.
All bug reports before the fix was public will earn a reward. All bug reports after are invalid. If a new bug is introduced by their fix then it is valid for a reward.

__Mid-Contest Changelog__

- **Challenges does not update AnchorStateRegistry for resolved games**
The AnchorStateRegistry is never updated, causing proving costs to increase over time as games prove from a stale anchor, and third-party integrations reading the anchor as a finality signal see a stuck chain.
PR: [https://github.com/base/base/pull/2372](https://github.com/base/base/pull/2372)

- **fix(consensus): iterate all transactions in is_deposits_only**
Option<Vec<Bytes>>::iter() yields at most one item — the inner Vec<Bytes> itself — not its elements. The old closure received &Vec<Bytes>, so .first() returned the first Bytes (first transaction), and [0] checked only that transaction's type byte. Blocks with a leading deposit followed by user transactions were incorrectly classified as deposits-only.
PR: [https://github.com/base/base/pull/2429](https://github.com/base/base/pull/2429)

- **PROOF_THRESHOLD of 2 should not be used**
Requiring 2 proofs for resolution causes problems with bonds if the second proof was not provided in time.
PR: [https://github.com/base/contracts/pull/263](https://github.com/base/contracts/pull/263)

- **Unused error in ZKVerifier**
The only error in ZKVerifier was not used.
PR: [https://github.com/base/contracts/pull/263](https://github.com/base/contracts/pull/263)

- **NitroEnclaveVerifier timestamp documentation inconsistent with code**
The comments in NitroEnclaveVerifier for when an attestation's timestamp would be invalid did not match the code.
PR: [https://github.com/base/contracts/pull/263](https://github.com/base/contracts/pull/263)

- **Nullifications cannot occur when system is paused**
The verifiers require a game to be proper to cause a nullification, and properness requires the system to not be paused. However, verifiers should be allowed to be nullified in this situation as it concerns the validity of the prover, not if the system is paused or not.
PR: [https://github.com/base/contracts/pull/263](https://github.com/base/contracts/pull/263)

- **Resolution is not changed if a global verifier is nullified**
A game's resolution changes if a verifier is nullified by going through the game, but doesn't change if a verifier is nullified by going through a different game.
PR: [https://github.com/base/contracts/pull/263](https://github.com/base/contracts/pull/263)

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope are valid.

__Duplicate Rewarding__

Duplicate submissions of bugs are valid under the following conditions:
- Duplicate reports for the same unfixed bug are valid 
- Once a fix is publicly disclosed, new reports for that bug are invalid
- Reports submitted before the fix are still eligible

Duplicate submissions of Insights are invalid.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are **not** valid for a reward.

__Primacy of Impact vs Primacy of Rules__

Base adheres to the Primacy of Rules, meaning the whole bug bounty program is run strictly under the terms and conditions stated on this page.

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

By adhering to Immunefi’s best practice recommendations, Base has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (29)

- [blockchain_dlt] Critical: Direct loss to Base or users ≥ 10% of funds held within Bridge.
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] Critical: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Causing network processing nodes to process transactions from the mempool beyond set parameters
- [blockchain_dlt] High: RPC API crash affecting programs with greater than or equal to 25% of the market capitalization on top of the respective layer
- [blockchain_dlt] High: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments
- [blockchain_dlt] High: Unintended chain split (network partition)
- [blockchain_dlt] Medium: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network
- [smart_contract] Critical: Circumventing the dispute/challenge mechanism to prevent correction of an invalid proposal before finalization
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion
- [smart_contract] Critical: Draining or stealing funds from the L1 bridge portal through invalid withdrawal proofs constructed against a forged finalized state
- [smart_contract] Critical: Forging or bypassing TEE or ZK proof verification in AggregateVerifier to finalize an invalid state root on L1
- [smart_contract] Critical: Permanent freezing of funds in the bridge or in dispute game bonds with no available recovery path
- [smart_contract] Critical: Unauthorized upgrade or replacement of verifier contract implementations (AggregateVerifier, TEEVerifier, or dispute game implementations via DisputeGameFactory)
- [smart_contract] High: Bypassing the soundness alert mechanism — two conflicting valid proofs of the same type (both TEE or both ZK) fail to trigger automatic game nullification
- [smart_contract] High: Forcing a dispute game into an incorrect resolved state (e.g., DEFENDER_WINS when CHALLENGER_WINS should apply, or vice versa)
- [smart_contract] High: Incorrect finalization timing — a proposal finalizes before the required proof window elapses (7 days for single proof, 1 day for dual proof)
- [smart_contract] High: Registering a malicious or unauthorized TEE enclave signer in the TEEProverRegistry without valid attestation (PCR0 mismatch or missing attestation)
- [smart_contract] High: Temporary freezing of funds for at least 24 hours (e.g., stuck withdrawal proofs, locked dispute game bonds)
- [smart_contract] Medium: Griefing that causes damage to users or the protocol without direct profit motive for the attacker
- [smart_contract] Medium: Manipulating dispute game bond mechanics to economically grief proposers or prevent legitimate proposals from being submitted
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour but less than 24 hours
- [smart_contract] Medium: Theft of gas through gas-token minting or similar mechanisms in in-scope contracts
- [smart_contract] Medium: Unbounded gas consumption in any in-scope contract function callable by external parties

## Impact notes

__Proof of Concept (PoC) Requirements__

Proof of Concept (PoC) Requirements A runnable PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Optional Project Info__

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

Given our previous status as an OP Stack chain, participants may confuse OP Stack components (op-node, op-geth, op-batcher) as in scope. Only Base-native code in the Assets in Scope section (EL, CL, Batcher, TEE/ZK components, etc.) is in scope. Additionally, any Optimism audit reports (listed in this competition) represent out-of-scope code. The ZK prover and its associated circuits are also out of scope. The core Op-Succinct program is out-of-scope, but changes we have made to it are in-scope.

For base/base, following folders are considered to be out-of-scope:
- [https://github.com/base/base/tree/main/actions](https://github.com/base/base/tree/main/actions)
- [https://github.com/base/base/tree/main/devnet](https://github.com/base/base/tree/main/devnet)
- [https://github.com/base/base/tree/main/baseup](https://github.com/base/base/tree/main/baseup)
- [https://github.com/base/base/tree/main/etc](https://github.com/base/base/tree/main/etc)

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

Yes. Base Azul is Base's first independent upgrade after transitioning from the OP Stack. Main differences:
- Client consolidation – migrating from op-geth/op-node to base-reth-node (EL) and base-consensus (CL); 
- Proof system migration – replacing Optimistic fault proofs (Cannon) with a dual-proof system (TEE + ZK) for faster finality;
- Custom features – Fusaka EIP support and future protocol innovations. 
See: [https://specs.base.org/upgrades/azul/overview](https://specs.base.org/upgrades/azul/overview) for more details.

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

Primary concerns: 
- Offchain consensus/execution logic – state root derivation bugs in base-consensus and base-reth-node.
- Proof system integration – TEE/ZK dispute game submission logic, verifier contract bugs, and soundness issues in ZK recursion; 
- Protocol transitions – incorrect hardfork activation logic, backwards compatibility breaks, and edge cases in EIP-1559 fee calculation; 
- Multi-client discrepancies – execution differences between CL and EL that cause chain forks.

**What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?**

- Downgrade valid reports if the attack requires compromising Base-operated infrastructure (not discoverable via code review alone). 
- Any report that assumes we will not dispute/blacklist/retire an invalid proposal within the proof system, unless it can be shown that such an action cannot be taken.
- Any report relying on an invalid TEE or ZK proof will be downgraded, especially TEE proofs unless it can be shown that a key compromise is unnecessary.
- Any report that assumes a service/program will not be manually restarted with possibly different configurations will be downgraded

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

- TEE Proposer/Registrar signers (AWS Nitro, Intel TDX enclaves) –  if operating within attestation-backed signature authority; 
- Security Council multisig (governance-controlled upgrades) – if approving changes within their mandate; 
- Sequencer – if transaction ordering is within normal MEV parameters.

**What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?**

- L1 Ethereum validators and stakers – not relevant to Base consensus;
- Third-party bridge validators (Relay, Across, Axelar, etc.) – outside Base's control;
- Base corporate infrastructure – non-protocol (KMS, deployment pipelines, etc.).

**Which chains and/or networks will the code in scope be deployed to?**

- Base Sepolia testnet (post-April 20 Azul activation) – competition environment.
- Base mainnet (planned May 13, 2026) – target deployment. Base mainnet is not considered to be in scope for the purpose of this competition.

**What external dependencies are there?**

- Ethereum mainnet (L1) – state root anchoring, EIP-4844 blob data availability, gas price feeds;
- RiscZero SP1 ZK prover – v6.0.2+ (soundness fix required);
- AWS Nitro Enclaves – TEE attestation infrastructure;
- Optimism upstream libraries (op-batcher, optimism/contracts) – for bridge and withdrawal logic. No modifications to these libraries are in scope.
- [https://github.com/base/node/tree/main/reth](https://github.com/base/node/tree/main/reth)

**Are there any unusual points about your protocol that may confuse Security Researchers?**

- Single-proof finality model – a TEE or ZK proof is needed to finalize. A ZK proof can be used to challenge a TEE proof, but not vice-versa
- Intermediate output roots – proofs cover block ranges and include commitments to intermediary roots within a proposal to allow disputes to cover a much smaller range of blocks;
- Soundness alert mechanism – if two different state roots both have valid proofs of the same type (i.e. both are TEE or both are ZK), the game can be automatically nullified;
- Private vs. public known issues – some Kona bugs are private (not yet disclosed publicly) but valid for reward.

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

- [https://specs.base.org/upgrades/v1/overview](https://specs.base.org/upgrades/v1/overview) – full V1 (Base Azul) specification;
- [https://docs.base.org/base-chain/node-operators/base-v1-upgrade](https://docs.base.org/base-chain/node-operators/base-v1-upgrade) – operator migration guide;
- [http://github.com/base/base](http://github.com/base/base) – open-source code with README and architecture docs;
- [https://blog.base.dev](https://blog.base.dev) – technical blog posts on proofs and stack migration.

__Public Disclosure of Known Issues__

[Known Vulnerabilities in Base Azul](https://drive.google.com/file/d/1CwxsIZnRcjTXIkYFEw_xF4_rOwePQ55t/view?usp=sharing)

Bug reports for publicly disclosed bugs are not eligible for a reward. 

__Private Known Issues Reward Policy__

We are aware of an issue in this codebase that has not yet been publicly disclosed. The Base team has provided a Hash Variant as evidence of pre-existing knowledge concerning this specific vulnerability. Researchers will not receive credit for its discovery. Should this issue become public knowledge during the competition, this section will be updated accordingly. 

__Previous Audits__

Base’s completed audit reports can be found at the links provided below. Unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

Audits for multiproof smart contracts:
- Multiproof contracts audit 1: [https://cantina.xyz/portfolio/25ba64ea-d6f3-411e-8338-419ffc385ba6](https://cantina.xyz/portfolio/25ba64ea-d6f3-411e-8338-419ffc385ba6)
- Multiproof contracts audit 2: [https://cantina.xyz/portfolio/b72c7078-f6da-4074-a3bd-4f938f469fb7](https://cantina.xyz/portfolio/b72c7078-f6da-4074-a3bd-4f938f469fb7)
- TEE contracts audit 1: [https://cantina.xyz/portfolio/423a9f33-b710-4445-a125-950b0a7771d7](https://cantina.xyz/portfolio/423a9f33-b710-4445-a125-950b0a7771d7)
- TEE contracts audit 2: [https://cantina.xyz/portfolio/a4f952cf-1c5b-4e3c-8153-c3adff899613](https://cantina.xyz/portfolio/a4f952cf-1c5b-4e3c-8153-c3adff899613)

Audit reports for Optimism smart contracts and components (includes Kona): [https://github.com/ethereum-optimism/optimism/tree/develop/docs/security-reviews#security-reviews](https://github.com/ethereum-optimism/optimism/tree/develop/docs/security-reviews#security-reviews)

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False

## Reward notes

Rewards are distributed among SRs according to Immunefi's [Standardized Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program](https://immunefi.com/allstars/) participants. 

The reward pool is determined by the greatest severity bug found.

- If one or more Critical severity bug is found, the reward pool will be **$250,000 USD**
- If one or more High severity bug is found, the reward pool will be **$125,000 USD**
- If one or more Medium severity bug is found, the reward pool will be **$70,000 USD**
- If one or more Low severity bug is found, the reward pool will be **$30,000 USD**
- If none of the above conditions apply then the reward pool is **$20,000 USD**

For this Audit Competition, duplicates are valid for a reward under the following conditions:
- Duplicate reports for the same unfixed bug are valid
- Once a fix is publicly disclosed, new reports for that bug are invalid
- Reports submitted before the fix are still eligible

Fixes may be applied mid-contest.

Private known issues, meaning known issues that were not publicly disclosed, are not valid. Currently, there is only one which cannot be disclosed. We have a commit containing the resolution to that issue disclosed within a private repository. The commit hash and additional evidence will be made available to the Immunefi team.

__Reward Payment Terms__

Payouts are handled by the Base team directly and are denominated in USD. However, payments are done in USDC on Base.

After the event has concluded and the final bug reports have been resolved, rewards will be distributed all at once based on Immunefi’s distribution formula.

## Out of scope (program-specific)

Following folders for base/base are considere to be out-of-scope:
- [https://github.com/base/base/tree/main/actions](https://github.com/base/base/tree/main/actions)
- [https://github.com/base/base/tree/main/devnet](https://github.com/base/base/tree/main/devnet)
- [https://github.com/base/base/tree/main/baseup](https://github.com/base/base/tree/main/baseup)
- [https://github.com/base/base/tree/main/etc](https://github.com/base/base/tree/main/etc)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
