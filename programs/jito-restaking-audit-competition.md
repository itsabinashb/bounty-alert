# Audit Comp | Jito Restaking

- Page: https://immunefi.com/bug-bounty/jito-restaking-audit-competition/scope/
- Max bounty: $150,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: 2024-12-02T10:00:00.000Z

## Assets in scope (4)

- [smart_contract] https://github.com/jito-foundation/restaking/tree/master/restaking_core — Restaking Core [1009]
- [smart_contract] https://github.com/jito-foundation/restaking/tree/master/restaking_program — Restaking Program [1370]
- [smart_contract] https://github.com/jito-foundation/restaking/tree/master/vault_core — Vault Core [3356]
- [smart_contract] https://github.com/jito-foundation/restaking/tree/master/vault_program — Vault Program [2660]

## Asset notes

Jito’s up-to-date codebase can be found at [https://github.com/jito-foundation/restaking](https://github.com/jito-foundation/restaking). Documentation and further resources can be found at [https://docs.restaking.jito.network](https://docs.restaking.jito.network).

__Mid-Contest Code Updates__

In this contest bug fixes may be applied mid-contest. 

The project is to keep changes private as far as possible. When changes need to be made public, then the changelog will be updated here & in the Jito Restaking Audit Competition Discord channel. Publicly fixed bugs are invalid and the scope is updated to the new code.

All bug reports before the fix was public will earn a reward. All bug reports after are invalid. If a new bug is introduced by their fix then it is valid for a reward.

__Mid-Contest Changelog__

None

__KYC Requirement__

Jito will be requesting KYC information in order to pay for successful bug submissions. The following information will be required:
- Full name 
- Date of birth
- Proof of address (either a redacted bank statement with address or a recent utility bill)
- Copy of Passport or other Government issued ID

Security researchers are required to submit KYC within 14 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward equal to that of a bug one severity lower.

__Primacy of Impact vs Primacy of Rules__

Jito adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page.

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this audit competition and a leaderboard of the participants and their earnings.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Jito has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (7)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Theft of protocol revenue
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds

## Impact notes

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Whitehat Educational Resources & Technical Info__

The documentation for the restaking programs is located at [https://docs.restaking.jito.network/](https://docs.restaking.jito.network/).

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

This will be the maiden deployment of Jito’s restaking protocol. This is a new codebase, not a fork. Slashing will not be enabled at launch, as an initial guardrail, but the protocol otherwise resembles existing restaking protocols.

__Where do you suspect there may be bugs?__

As previously mentioned, slashing will not be implemented at launch. However, any bug which might allow an operator to avoid or frontrun being slashed would be an interesting insight. Rounding issues around vault shares would be interesting. There might be bugs around fees and rewards, allowing an attacker to either avoid fees or collect a larger share of rewards. There is some complexity around validating, tracking, and updating vault state, so any issues involving out-of-date/out-of-sync vault state would be interesting. 

__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?__

The Vault and Restaking programs support the SPL Token and SPL Token 2022 standards 

__What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

None that are relevant. There is an `admin` role which can be used to pause vault accounts. However, we’re interested in any impact which could deny or impair functionality, or lead to loss of funds or adverse outcomes for either the protocol or its users;These would still be valid findings even if they can be partially mitigated by pausing+migrating to a new vault.

__What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?__

We’re still interested in impacts involving permissioned roles in the protocol (malicious NCN operators, malicious slashers, malicious delegates). However, any report involving compromise of the private keys of any Jito Foundation-associated account would be out of scope.

__What external dependencies are there?__

External dependencies are pretty minimal. The programs depend on the Solana Program Library, and the SPL ATA, SPL Token, and SPL Token 2022 programs.

__Where might whitehats confuse out-of-scope code to be in-scope?__

All the client code is in the same git repository as the assets-in-scope, but it’s not particularly interesting. The code for the frontend clients is generated using kinobi, and the IDLs for the client are generated with shank. Since it is all auto-generated and simply represents an interface for interacting with the underlying protocol, it is not included in the contest scope.

__Are there any unusual points about your protocol that may confuse whitehats?__

Slashing is not implemented at present, as the protocol is in its initial phase. 

__What is the test suite setup information?__

It is recommended to use cargo nextest. The instructions for running tests can be found here: [https://github.com/jito-foundation/restaking/blob/master/README.md](https://github.com/jito-foundation/restaking/blob/master/README.md)

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 
- VRTs are tokenized shares of a vault’s underlying deposits. Vault deposits are calculated by getting the total amount of assets held by the vault token account. An attacker could inflate the exchange rate of shares to underlying assets by “donating” directly to a vault. If the attacker is the first depositor to a vault, they could deprive subsequent depositors of shares relative to their amount of deposited assets. This can be mitigated by requiring or suggesting that integrators mint some small amount of shares in the same transaction in which the vault is initialized. Relevant PRs: [https://github.com/jito-foundation/restaking/pull/150](https://github.com/jito-foundation/restaking/pull/150)
- The amount of fees charged can change between the time when a withdrawal ticket is enqueued and when the withdrawal ticket is burned. Withdrawals should account for the difference. The issue hasn’t been resolved yet but a mitigation is in the works.
- In the case where an operator’s state has been updated but a vault update epoch was missed or close_vault_update_state_tracker has not been called, the vault should be updated to reflect the operator’s new state. Otherwise, the amount reserved for cooldown can be too large. Relevant PRs: [https://github.com/jito-foundation/restaking/pull/163/](https://github.com/jito-foundation/restaking/pull/163/)

__Previous Audits__

Jito’s completed audit reports can be found at [https://jito-foundation.gitbook.io/mev/resources/audits](https://jito-foundation.gitbook.io/mev/resources/audits). Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Jito Restaking Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/29877415850769-Jito-Restaking-Audit-Competition-Reward-Terms)

The reward pool will be entirely distributed among participants. The size depends on the bugs found:
- If one or more Critical severity bugs are found, **the reward pool will be 100% of the respective reward pool, $150,000 USD**
- If one or more High severity bugs are found, **the reward pool will be 75% of the respective reward pool, $112,500 USD**
- If one or more Medium severity bugs are found, **the reward pool will be 50% of the respective reward pool, $75,000 USD**
- If Low severity bugs or no bugs are found, **the reward pool will be 25% of the respective reward pool, $37,500 USD**

**Duplicates of Insight reports are not eligible for a reward.**

For this Audit Competition, duplicates and private known issues are valid for a reward. 

Private known issues will unlock higher reward pools according to their severity level without any downgrade. For example, a Critical severity bug which was a private known issue would unlock the reward pool conditional on a Critical severity bug being found.

Rewards are distributed according to the impact of the vulnerability based on the Immunefi [Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

__Reward Payment Terms__

Payouts are handled by the Jito team directly and are denominated in USD. However, payments are done in JTO on Solana.

The calculation of the net amount rewarded is based on the 7-day [TWAP](https://en.wikipedia.org/wiki/Time-weighted_average_price) of JTO at the time of settlement. No adjustments are made based on liquidity availability.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi).

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
