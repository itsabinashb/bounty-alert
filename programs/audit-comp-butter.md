# Audit Comp | Butter

- Page: https://immunefi.com/bug-bounty/audit-comp-butter/scope/
- Max bounty: $30,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-02-01T10:00:00.000Z

## Assets in scope (2)

- [smart_contract] https://github.com/immunefi-team/audit-comp-butter-cfm-v1
- [smart_contract] https://github.com/immunefi-team/audit-comp-butter-cfm-v1-playmoney

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Primacy of Impact vs Primacy of Rules__

Butter adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page.

__KYC Requirement__

Butter will be requesting KYC information in order to pay for successful bug submissions. The following information will be required:
- Full name 
- Date of birth
- Proof of address (either a redacted bank statement with address or a recent utility bill)
- Copy of Passport or other Government issued ID

Security researchers are required to submit KYC within 14 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this Audit Competition bug bounty and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

When there is uncertainty about how feasible an attack is Immunefi will use our feasibility limitation standards to determine the severity of the report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Butter has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (13)

- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 1 hour
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 10 minute
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

**Build commands, Test commands, and instructions on how to run them:**

- forge soldeer install
- forge build
- forge test
- FOUNDRY_PROFILE=itest forge test # integration tests with actual ConditionalTokens and Wrapped1155Factory contracts
- FOUNDRY_PROFILE=ftest forge test # fork tests

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?**

Tokens that we will recommend to use as ERC20 collateralToken (We will filter out of our frontend any instances of FlatCFM that don’t follow guidelines):
- The play money collateral token generated through cfm-v1-playmoney factory
- USDC
- DAI
- sDAI [](https://github.com/makerdao/sdai)
- USDS [](https://github.com/makerdao/usds)
- sUSDS [](https://github.com/makerdao/sdai/tree/susds)
- GHO (https://github.com/aave/gho-core/tree/main/src/contracts/gho)
- USDe (https://github.com/ethena-labs/code4arena-contest/tree/main/protocols/USDe/contracts)
- StakedUSDeV2 (https://github.com/ethena-labs/code4arena-contest/tree/main/protocols/USDe/contracts)

**Which chains and/or networks will the code in scope be deployed to?**

Unichain

**Where do you suspect there may be bugs?**

- In the way payouts are reported to ConditionalTokens
- In Reality state management: we need to make sure our questions don’t get stuck
- In handling unknown ERC20 tokens as part of ConditionalScalarMarket functions
- State management (reentrancy…) in the factory and in ConditionalScalarMarket

**What external dependencies are there?**

- RealityETH v3
- ConditionalTokens
- Wrapped1155Factory

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

See all dependencies, plus ERC20 tokens that might be used as input -> these are all out of scope but need to be understood in great detail.

**Are there any unusual points about your protocol that may confuse Security Researchers?**

It’s making use of conditional tokens which aren't obvious to understand.

**Which chains?**

Deployment is planned on Unichain mainnet as soon as available. Other EVM deployments can happen in the future.

**What external contracts (dependencies) is this project relying on?**

There are two main dependencies: ConditionalTokens and RealityETH.

ConditionalTokens is a contract produced by Gnosis. Butter is planning on deploying identical versions to Unichain mainnet (see repositories: 

[ConditionalTokens](https://github.com/butterygg/conditional-tokens-contracts) and [Wrapped1155Factory](https://github.com/butterygg/1155-to-20)),  These contracts reuse an exact version that has already been audited, with no changes to the Solidity version. However, **they are not included in the scope of this Audit Competition**.

RealityETH version 3.0 is used. It is expected that the Arbitrator used is Kleros. Kleros might require some arbitration fee (see [here](https://forum.kleros.io/t/kip-72-court-proposal-on-ethereum-oracle-court/1279)).

**Previous Audits**

Butter’s completed audit reports can be found at https://github.com/immunefi-team/audit-comp-butter-cfm-v1/tree/main/audits. Any unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary. For the full details read our [Butter Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/32014062101009-Butter-Audit-Competition-Reward-Terms)

A reward pool of $30,000 USD will be distributed among participants, if any valid bugs are found. 

If not a single bug is found (Insights do not count as bugs) the reward pool is $15% of $30,000 USD rewards.

Duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

*Insight Rewards*: Portion of the Rewards Pool

*The "Insight" severity was introduced on Boost (Audit Competitions) & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

**Duplicates of Insight reports are not eligible for a reward.**

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (8)

- Known Issue (https://gist.github.com/lajarre/61495716497c704b2258b32e41a57d64)
- Known Issue (https://gist.github.com/lajarre/8aba7f4ac04583fdd6339279e14c3486)
- Known Issue (https://gist.github.com/lajarre/8f2b808ee7549785e9cc0afbf002e900)
- Known Issue (https://gist.github.com/lajarre/92cd0ba594f6e4490bf4763020509d96)
- Known Issue (https://gist.github.com/lajarre/94f7af6a980da30f756654a2ca0f7a25)
- Known Issue (https://gist.github.com/lajarre/d8c9741773272919d110dc5f728295c0)
- Known Issue (https://gist.github.com/lajarre/fb7b857bdaa5765167e77220258049c8)
- Previous Audits (https://github.com/immunefi-team/audit-comp-butter-cfm-v1/tree/main/audits)
