# Audit Comp | Anvil: Letters of Credit

- Page: https://immunefi.com/bug-bounty/audit-comp-anvil-letters-of-credit/scope/
- Max bounty: $30,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - high, smart_contract - critical, smart_contract - medium, smart_contract - low
- End date: 2024-11-22T10:00:00.000Z

## Assets in scope (3)

- [smart_contract] https://etherscan.io/address/0x5d2725fdE4d7Aa3388DA4519ac0449Cc031d675f — CollateralVault - 606 SLOC
- [smart_contract] https://github.com/AcronymFoundation/anvil-contracts/blob/main/contracts/LetterOfCredit.sol — LetterOfCredit - 904 SLOC
- [smart_contract] https://github.com/AcronymFoundation/anvil-contracts/blob/main/contracts/PythPriceOracle.sol — Pyth Price Oracle - 112

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Primacy of Impact vs Primacy of Rules__

Anvil adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page.

__KYC Requirement__

Anvil will be requesting KYC information in order to pay for successful bug submissions. The following information will be required:
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

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Anvil has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (9)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds (note: if a LetterOfCredit proxy update may fix the issue, it is temporary)
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Smart contract unable to operate due to lack of token funds
- [smart_contract] High: Temporary freezing of funds within the CollateralVault for at least 48 hours
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Low: Temporary freezing of funds set to 48 hrs within the LetterOfCredit contract

## Impact notes

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

No. This is a new protocol. 

__Where do you suspect there may be bugs? Useful aspects of this question are:__

**Which parts of the code are you most concerned about?**
- Dynamic LOC calculations
- Dynamic LOC liquidation mechanics
- LOCs always being redeemable for their credited token value
    - Note: ignore adverse market conditions as a concern

**What attack vectors are you most concerned about?**
- Tokens being stolen from the LetterOfCredit contract
- Tokens being stuck in the LetterOfCredit contract
- LOCs being created using an account’s collateral without that account’s permission

**Which part(s) of the system do you want whitehats to attempt to break the most?**
- LOC operations

**Are there any assumed invariants that you want whitehats to attempt to break?**
- LetterOfCredit
    - LOCs should always be redeemable for their credited token amount (ignoring adverse market condition cases)
    - Dynamic LOCs can only be converted by:
        - The creator
        - Any party presenting the creator’s signed authorization
        - Anyone if the LOCs current CollateralFactor based on oracle price meets the LOC’s stored collateralFactorBasisPoints
    - LOCs may only be redeemed by
        - The LOC.beneficiary
        - Any party presenting the beneficiary’s signed authorization
    - The following LOC operations should always fail after a LOC’s expiration timestamp passes:
        - redeemLOC()
        - convertLOC()
        - modifyLOCCollateral()
        - extendLOC()
    - A LOC may be canceled by:
        - The LOC.beneficiary
        - Any 3rd party presenting the beneficiary’s signed authorization
        - Any party after the LOC is expired
    - The result of cancelLOC() for a LOC with remaining collateral is always one of the following:
        - The CollateralReservation is released in the CollateralVault, making any reserved collateral associated with the LOC available within the         LOC.creator’s vault account
        - The collateral stored within the LOC contract for the converted LOC is sent directly to the LOC.creator’s address


__What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

This project is not a chain of its own and does not have the ability to rewrite history, so no emergency actions should be possible as a way to mitigate an otherwise possible theft. The `LetterOfCredit` contract is meant to be referenced by upgradeable proxies, so bug reports of “frozen” tokens that may be mitigated by a contract upgrade are less of a concern. Anvil will likely pay those out as low severity bugs.


__What monitoring systems may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

None to our knowledge. 

There are possible admin actions in `CollateralVault` and `LetterOfCredit`, including contract upgrades for the latter, but those are only possible via governance, which is much slower than any attack and could not reasonably front-run an attack. 

__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

There are various roles defined in the `CollateralVault` and `LetterOfCredit` contracts that should be assumed to act in any way explicitly permitted by that role, and that is a valid non-bug use case. That is to say that if accounts with an Admin/Owner role, for instance, may withdraw tokens from the contract, registering an attack of the Admin/Owner stealing tokens is invalid because that is not theft – that is an explicitly permitted action.

That said, in the `CollateralVault` for instance, the design of the contract is such that the contract Owner should not be able to take tokens that are earmarked for an individual account (it may only take `contract balance - SUM(user account balance`). If an attack were to be found such that the owner could take funds that were earmarked for one or more accounts, that would be a valid bug because it undermines the trust assumptions of the contract. 

__What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?__

None that we can think of.


__What external dependencies are there?__

There are external dependencies on ERC-20 tokens. Governance attacks, such as the approval of a malicious ERC-20 token is out of scope. 

The `LetterOfCredit` contract depends on a PriceOracle to give it valid prices. Market-based oracle attacks are out of scope for this competition. If the `LetterOfCredit` contract’s logic incorrectly uses oracle data, though, that would be in scope.

There are also dependencies on open source contracts such as OpenZeppelin. While those are 3rd party contracts, they are referenced from within Anvil’s contracts, so any vulnerabilities in Anvil contracts made possible by issues in dependency contracts such as OZ are in scope.

__Where might whitehats confuse out-of-scope code to be in-scope?__

- The code for the `LetterOfCredit` contract is meant to be referenced by proxies as their implementation. Any use case that requires deploying and directly using the LetterOfCredit contract rather than via a proxy would be out of scope. 
- Since the `LetterOfCredit` contract is meant to be referenced by upgradeable proxies, finding some loophole in contract logic such that tokens reserved by that contract become stuck would be a lower severity bug than it would be if the contract were not upgradeable. For that reason, token theft as a bug is very much in scope, whereas issues that could be solved via a successful contract upgrade are less critical and therefore low impact .
- Precision loss is not a valid bug since it is impossible to divide without the possibility of precision loss.
- Using a signature before someone else uses a signature (i.e. front-running) is not a valid bug. If the signature permits an operation, that operation is welcome and encouraged.
- “If you were to upgrade the `LetterOfCredit` contract to a contract with a bug, then it would have a bug” is not a valid bug. If there is an issue with the upgrade process itself, that is valid, but simply using the proxy pattern is not a valid bug.
- The ILiquidator interface is meant to be implemented by sophisticated liquidators external to the protocol / protocol team. An example implementation is included in the codebase as the “UniswapLiquidator” contract, but that contract is not in scope.
- Avoiding the CollateralVault protocol fee by claiming / withdrawing extremely small amounts repeatedly is not a feasible attack on Ethereum mainnet so it is out of scope.

__Are there any unusual points about your protocol that may confuse whitehats?__

- The concept of CollateralFactors is a bit nuanced. The same concept is used in Compound and other DeFi protocols. In the context of a LOC, a CollateralFactor is the percentage of the collateral token amount that would be necessary to liquidate to receive the LOC’s credited token amount, ignoring all fees and slippage. 
- The maximum CollateralFactor for LOC creation and the CollateralFactor at which point LOCs become liquidatable is stored for each distinct asset-pair that supports dynamic LOCs. It is assumed that all fees are baked into that configuration and that the CollateralFactor is padded to handle trading slippage, liquidator incentive, claim fee, etc.

__What is the test suite setup information?__

No tests have been made public at the moment.

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

- The fee applied to CollateralVault claims and withdrawals is the same, but the amount the fee is relative to is different such that the absolute fee assessed via withdraw() is higher than claimCollateral() when the amount released by the CollateralVault is the same.
- ERC165 calls within CollateralVault may prevent addition/removal of collateralizable contracts. Governance should verify this will not be an issue when collateralizable contact addition is proposed.


__Previous Audits__

Anvil’s completed audit reports can be found at [https://docs.anvil.xyz/contracts/audits](https://docs.anvil.xyz/contracts/audits). Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary. For the full details read our [Anvil: Letters of Credit Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/29954569847697-Anvil-Letters-Of-Credit-Audit-Competition-Reward-Terms)

A reward pool of $30,000 USD will be distributed among participants, even if no valid bugs are found. 

Duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

*Insight Rewards*: Portion of the Rewards Pool

*The "Insight" severity was introduced on Boost (Audit Competitions) & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

Duplicates of Insight reports are not eligible for a reward.

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
