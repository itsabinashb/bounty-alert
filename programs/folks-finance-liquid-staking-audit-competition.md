# Audit Comp | Folks: Liquid Staking

- Page: https://immunefi.com/bug-bounty/folks-finance-liquid-staking-audit-competition/scope/
- Max bounty: $30,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: 2024-12-19T10:00:00.000Z

## Assets in scope (1)

- [smart_contract] https://github.com/Folks-Finance/algo-liquid-staking-contracts/blob/8bd890fde7981335e9b042a99db432e327681e1a/contracts/xalgo/consensus_v2.py — ConsensusV2 [651]

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Build commands, Test commands, and instructions on how to run them:__

You can find the smart contract repository at [https://github.com/Folks-Finance/algo-liquid-staking-contracts](https://github.com/Folks-Finance/algo-liquid-staking-contracts). Follow the instructions in the README to get setup and be able to run the tests

__Impact Terms__

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 
- You cannot delete an added proposer.
- A proposer’s balance may go below the minimum balance needed in order to be eligible for consensus rewards.
- A decrease in the max proposer balance may lead to some proposer balances being temporarily above the limit. 
- Unclaimed fees are generating additional yield for everyone.
- Unclaimed fees can be slightly reduced through often updates because of rounding down.
- Loss of precision over time as the value of xALGO accumulates.
- The smart contract doesn’t check for box cost payments - instead they are implicitly required.

__Previous Audits__

Folks Finance’s completed audit reports can be found at [https://github.com/Folks-Finance/audits/blob/50831a54420ed3e4513c8fa17a42f2bbd0338df1/Coinspect%20-%20Audit%20of%20Liquid%20Staking%20-%20August%202024.pdf](https://github.com/Folks-Finance/audits/blob/50831a54420ed3e4513c8fa17a42f2bbd0338df1/Coinspect%20-%20Audit%20of%20Liquid%20Staking%20-%20August%202024.pdf). Note that this is an audit on the previous version of the smart contract which shares similarities with the new version. Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward equal to that of a bug one severity lower.

__Primacy of Impact vs Primacy of Rules__

Folks Finance adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page.

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this audit competition and a leaderboard of the participants and their earnings.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Folks Finance has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (9)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 1 hour
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Whitehat Educational Resources & Technical Info__

__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?__

Algorand has native support for tokens with ASAs (Algorand Standard Assets). The liquid staking token which is distributed is an Algorand ASA.

__What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

We can update the deployed application in an emergency so some issues e.g. freezing of funds, may be mitigated from a permanent issue to a temporary issue.  We also have the ability to pause immediate and/or delayed minting. 

__What monitoring systems may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

None

__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

The four admins:
- The “admin” which is the super admin.
- The “register_admin” which can add proposers, set the proposer admin and register a proposer offline.
- The “xgov_admin” which can subscribe and unsubscribe proposers to xgov.
- The “proposer_admin” which can register a proposer online and offline.

__What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?__

None

__Security Researcher Education__

__Project educational resources__

- Design Overview for ALGO Staking Smart Contract [https://docs.google.com/document/d/1w-0ZmpWGTGrFl46PNhjmguEKj3ChnnFnMM3X_is1R9M/edit?usp=sharing](https://docs.google.com/document/d/1w-0ZmpWGTGrFl46PNhjmguEKj3ChnnFnMM3X_is1R9M/edit?usp=sharing)
- Smart Contract deployed on Testnet [https://lora.algokit.io/testnet/application/730430673](https://lora.algokit.io/testnet/application/730430673)
- Algorand Consensus Incentivisation Whitepaper [https://assets-global.website-files.com/62d96b0e9ea60fd1c96a1b50/65a7c0863805fd8b83cf34d5_upload_consensus-incentives.pdf](https://assets-global.website-files.com/62d96b0e9ea60fd1c96a1b50/65a7c0863805fd8b83cf34d5_upload_consensus-incentives.pdf)
- The xGov Integration Requirements [https://docs.google.com/document/d/1zB8-t0vHtkQVZeNgVlI5W8z38ugD8IhBK8uRrkoRAxM/edit?usp=sharing](https://docs.google.com/document/d/1zB8-t0vHtkQVZeNgVlI5W8z38ugD8IhBK8uRrkoRAxM/edit?usp=sharing)
- Docs for old version of ALGO Staking [https://docs.folks.finance/functionalities/xalgo-liquid-staking](https://docs.folks.finance/functionalities/xalgo-liquid-staking)

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

Yes it is an upgrade of the old version of ALGO Liquid Staking deployed at [https://lora.algokit.io/mainnet/application/1134695678](https://lora.algokit.io/mainnet/application/1134695678). The main differences are:
- Support for subscribing and unsubscribing from the xGov program. 
- Support for 3rd party node runners where now each proposer has its own admin which can register it online and offline. 
- The smart contract enforces the splitting of stake between the proposers. 
- Removed “min_proposer_balance” checks.

Note that the existing state of the smart contract will persist after the update (global/local state and box storage). 

__Where do you suspect there may be bugs?__

The calculations for “immediate_mint”, “delayed_mint”, “claim_delayed_mint” and “burn” cannot be manipulated. In addition, the smart contract should enforce an approximate equal stake split between the proposers.

You should also check privileged operations are safely guarded.

__What external dependencies are there?__

The main external dependency is the Algorand Consensus participation. Each proposers; participation keys will reside on its own Algorand Node and will receive ALGO rewards each time it proposes a block.

Another external dependency is the xGov program. The xGov power is given to block proposers and the smart contract allows delegating the control of the votes to an external address supplied by the “xgov_admin”.

Lastly some of the proposers’ Algorand Nodes may be run by trusted projects and/or key community members. 

__Are there any unusual points about your protocol that may confuse Security Researchers?__

The smart contract is an update of an existing smart contract which is already deployed on mainnet. Therefore there is no application create call supported. In addition you should consider the existing state of the smart contract [https://lora.algokit.io/mainnet/application/1134695678](https://lora.algokit.io/mainnet/application/1134695678) (global/local state and box storage) as these will persist between updates. The accompanying Design Overview Document provides further details on this.

When an account is marked online/offline, the moment a key registration transaction is confirmed by the network it takes 320 rounds for the change to take effect. So, if a key registration is confirmed in round 5000, the account will stop participating at round 5320.

The same applies for changes in stake.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Folks: Liquid Staking Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/30675078530449-Folks-Finance-Liquid-Staking-Audit-Competition-Reward-Terms).

Rewards are denominated in USD and distributed in USDC on Algorand.

Rewards are distributed all at once after the competition has ended. No rewards are distributed during the competition.

The reward pool is **$30,000 USD and will be fully distributed among whitehat participants in the form of USDC on Algorand**.

Duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the Immunefi [Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

__Reward Payment Terms__

Payouts are handled by the Folks Finance team directly and are denominated in USD. However, payments are done in USDC on Algorand.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

- The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi).

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
