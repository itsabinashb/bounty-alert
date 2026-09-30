# Audit Comp | Anvil

- Page: https://immunefi.com/bug-bounty/audit-comp-anvil/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - medium, smart_contract - high, smart_contract - low
- End date: 2024-11-06T08:00:00.000Z

## Assets in scope (3)

- [smart_contract] https://etherscan.io/address/0x5d2725fdE4d7Aa3388DA4519ac0449Cc031d675f — CollateralVault.sol - 606 SLOC
- [smart_contract] https://etherscan.io/address/0xd042C267758eDDf34B481E1F539d637e41db3e5a — TimeBasedCollateralPool.sol - 778 SLOC
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Known Issue Assurance__

Anvil commits to providing Known Issue Assurance to bug submissions through their program. This means that Anvil will either disclose known issues publicly, or at the very least, privately via a self-reported bug submission. 

In a potential scenario of a mediation, this allows for a more objective and streamlined process, in order to prove that an issue is known. Otherwise, assuming the bug report is valid, it would result in the report being considered as in-scope, and due a reward.

__Primacy of Impact vs Primacy of Rules__

Anvil adheres to the Primacy of Impact for all impacts.

Primacy of Impact means that the impact is prioritized rather than a specific asset. This encourages security researchers to report on all bugs with an in-scope impact, even if the affected assets are not in scope. For more information, please see Best Practices: Primacy of Impact 
When submitting a report on Immunefi’s dashboard, the security researcher should select the Primacy of Impact asset placeholder. If the team behind this project has multiple programs, those other programs are not covered under Primacy of Impact for this program. Instead, check if those other projects have a bug bounty program on Immunefi.
If the project has any testnet and/or mock files, those will not be covered under Primacy of Impact.
All other impacts are considered under the Primacy of Rules, which means that they are bound by the terms and conditions set within this program.

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
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds within the CollateralVault for at least 48 hours
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Temporary freezing of funds within the TimeBasedCollateralPool for at least 48 hours

## Impact notes

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

No. This is a new protocol. 

__Where do you suspect there may be bugs? Useful aspects of this question are:__


- Which parts of the code are you most concerned about?

TimeBasedCollateralPool accounting
- What attack vectors are you most concerned about?
Tokens being stuck in the CollateralVault or stolen from the TimeBasedCollateralPool or CollateralVault
- Which part(s) of the system do you want whitehats to attempt to break the most?
TimeBasedCollateralPool accounting
- Are there any assumed invariants that you want whitehats to attempt to break?

- **CollateralVault**

1. Owner cannot take tokens associated with account balances, only balances that are not associated with accounts (max withdrawable by owner is - -- 
2. CollateralVault balance - SUM(accountBalances))
3. Collateralizable contracts can only reserve & claim account tokens up to their account allowance, which decreases on reservation
4. CollateralReservations may not be changed, claimed, or released by any party other than the reserving collateralizable contract
5. CollateralReservations are resilient to contract governance actions (e.g. disabling the CollateralToken being used, changing the withdrawal fee, etc.)
6. Account balances for distinct ERC-20 tokens will be accounted for separately at all times (never mixed up)

- **TimeBasedCollateralPool**

1. - Accounts always receive units proportional to their staked tokens for staking operations and receive tokens proportional to their pool units for unstaking operations
2. - Tokens being unstaked are still claimable for at least 1 epoch after initiating unstaking
3. - Tokens being unstaked are never claimable after the end of the epoch following the epoch in which unstaking was initiated
4. - Units and balances for distinct ERC-20 tokens will be accounted for separately at all times (never mixed up)

__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?__

ERC-20 tokens that are subject to governance review ahead of support. That is to say that attacks that stem from malicious code within a token contract should be out of scope for this program, as any complex / non-standard ERC-20 token will be restricted by governance until proven safe. Fee-on-Transfer tokens, rebasing tokens, and tokens with upgradeable contracts should assume to never be supported, as well as other tokens that could present a security risk.  


__What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__


- For each emergency action, how does it work, how would it affect a bug report, and when would you utilize it?

If this is listed in your documentation, then a link to that part of the documentation would suffice.

- Note that normally, not all emergency actions are accepted as a valid reason to invalidate or downgrade an otherwise valid bug report, such as chain rollbacks.

This project is not a chain of its own and does not have the ability to rewrite history, so no emergency actions should be possible as a way to mitigate an otherwise possible theft. The TimeBasedCollateralPool contract is meant to be referenced by upgradeable proxies, so bug reports of “frozen” tokens that may be mitigated by a contract upgrade are less of a concern and therefore out of scope. Anvil will likely pay those out as low severity bugs reported via our forthcoming bug bounty program, but not as a part of this Audit Competition. 


__What monitoring systems may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

None to our knowledge. 

There are possible admin actions in CollateralVault and TimeBasedCollateralPool, including contract upgrades for the latter, but those are only possible via governance, which is much slower than any attack and could not reasonably front-run an attack. 

__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

There are various roles defined in the CollateralVault and TimeBasedCollateralPool contracts that should be assumed to act in any way explicitly permitted by that role, and that is a valid non-bug use case. That is to say that if accounts with an Admin/Owner role, for instance, may withdraw tokens from the contract, registering an attack of the Admin/Owner stealing tokens is invalid because that is not theft – that is an explicitly permitted action.

That said, in the CollateralVault for instance, the design of the contract is such that the contract Owner should not be able to take tokens that are earmarked for an individual account (it may only take contract balance - SUM(user account balance). If an attack were to be found such that the owner could take funds that were earmarked for one or more accounts, that would be a valid bug because it undermines the trust assumptions of the contract. 


__What external dependencies are there?__

There are external dependencies on ERC-20 tokens. Governance attacks, such as the approval of a malicious ERC-20 token is out of scope. 

There are also dependencies on open source contracts such as OpenZeppelin. While those are 3rd party contracts, they are referenced from within Anvil’s contracts, so any vulnerabilities in Anvil contracts made possible by issues in dependency contracts such as OZ are in scope.

__Where might whitehats confuse out-of-scope code to be in-scope?__

The code for the TimeBasedCollateralPool contract is meant to be referenced by proxies as their implementation. A TimeBasedCollateralPool contract could be deployed and not initialized, since it is not meant to be called directly, leaving it open to some 3rd party initializing it. If that happens, it is not a valid attack on the contract, as it is not meant to be used directly.  
Since the TimeBasedCollateralPool contract is meant to be referenced by upgradeable proxies, finding some loophole in contract logic such that tokens reserved by that contract become stuck would be a lower severity bug than it would be if the contract were not upgradeable. For that reason, token theft as a bug is very much in scope, whereas issues that could be solved via a successful contract upgrade are less critical and therefore out of scope.

__Are there any unusual points about your protocol that may confuse whitehats?__

There is rather complicated accounting in TimeBasedCollateralPool to allow for permissionless time-based unstaking. While that design may be hard to understand on first read, contract-, function-, and code-level comments should provide useful context to help interpret the logic 
In TimeBasedCollateralPool, the term “units” is used to represent an account’s proportional involvement in the pool. If not immediately apparent, please note units imply a percentage (account units / total pool units).


__What is the test suite setup information?__

No tests have been made public at the moment.

__Public Disclosure of Known Issues__
Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

There are no known issues that fall within the defined scope of this program

__Previous Audits__
Anvil’s completed audit reports can be found at [https://docs.anvil.xyz/contracts/audits]. Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary. For the full details read our [Anvil Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/29281157644689-Anvil-Audit-Competition-Reward-Terms)

A reward pool of $50,000 USD will be distributed among participants, even if no valid bugs are found. 

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
