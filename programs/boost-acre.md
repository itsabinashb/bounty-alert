# Audit Comp | Acre

- Page: https://immunefi.com/bug-bounty/boost-acre/scope/
- Max bounty: $50,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2024-09-03T08:00:00.000Z

## Assets in scope (5)

- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://sepolia.etherscan.io/address/0x6c2c643c90383Cba125E4b8DD01344eA35A75F27 — BitcoinDepositor - 355
- [smart_contract] https://sepolia.etherscan.io/address/0x7e184179b1F95A9ca398E6a16127f06b81Cb37a3 — stBTC - 552
- [smart_contract] https://sepolia.etherscan.io/address/0xF4011FD0C77Bd4d909Ae05c7390b88455294dAeA — BitcoinRedeemer - 180
- [smart_contract] https://sepolia.etherscan.io/address/0xd5EbDD6fF384a465D56562D3a489c8CCE1B92dd0 — MezoAllocator - 253

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Known Issue Assurance__

Acre commits to providing Known Issue Assurance to bug submissions through their program. This means that Acre Finance will either disclose known issues publicly, or at the very least, privately via a self-reported bug submission. 

In a potential scenario of a mediation, this allows for a more objective and streamlined process, in order to prove that an issue is known. Otherwise, assuming the bug report is valid, it would result in the report being considered as in-scope, and due a reward.

__Primacy of Impact vs Primacy of Rules__

Acre adheres to the Primacy of Impact for the following impacts:

**Critical**

- Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- Permanent freezing of funds
- Protocol insolvency


**High**

- Theft of unclaimed yield
- Permanent freezing of unclaimed yield
- Temporary freezing of funds


**Medium**

- Smart contract unable to operate due to lack of token funds
- Block stuffing
- Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- Theft of gas
- Unbounded gas consumption

**Low**

- Contract fails to deliver promised returns, but doesn't lose value


Primacy of Impact means that the impact is prioritized rather than a specific asset. This encourages security researchers to report on all bugs with an in-scope impact, even if the affected assets are not in scope. For more information, please see Best Practices: Primacy of Impact 
When submitting a report on Immunefi’s dashboard, the security researcher should select the Primacy of Impact asset placeholder. If the team behind this project has multiple programs, those other programs are not covered under Primacy of Impact for this program. Instead, check if those other projects have a bug bounty program on Immunefi.
If the project has any testnet and/or mock files, those will not be covered under Primacy of Impact.
All other impacts are considered under the Primacy of Rules, which means that they are bound by the terms and conditions set within this program.

__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:

- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this [Program Type]ed bug bounty and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Acre has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (13)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the Immunefi PoC Guidelines and Rules

__Whitehat Educational Resources & Technical Info__

- Technical documentation currently lives on GitHub: https://github.com/thesis/acre/tree/main/solidity
- For a non-technical overview, please see our docs: https://docs.acre.fi

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

This is not an upgrade.

__Where do you suspect there may be bugs? Useful aspects of this question are:__

The stBTC contract is based on the ERC4626 token vault. Attacks resulting in breaking the vault invariants and manipulating the shares conversion ratio are considered significant threats. We want to focus on users funds security.

__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?__

Acre’s stBTC implements the ERC-4626 tokenized vault standard. By staking tBTC, users acquire a liquid staking token called stBTC, commonly referred to as "shares". Users have the flexibility to redeem stBTC, enabling them to withdraw their deposited tBTC along with the accrued yield. stBTC is a non-rebasing ERC4626 token.

__What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

Pausing stBTC contract, upgarde of contracts, adjusting minimum deposit limits


__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

Contracts Owners, Pause Admin, Mezo Portal, Maintainers

__What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?__

Contracts Owners, Pause Admin

__What external dependencies are there?__

In order to support a native bitcoin-in, bitcoin-out experience, Acre has integrated Threshold Network’s tBTC bridge, which is an existing technology. Deposited funds are allocated to the Mezo Portal contract.

__Where might whitehats confuse out-of-scope code to be in-scope?__

External libraries are out-of-scope (i.e. @openzeppelin).

__What is the test suite setup information?__

https://github.com/thesis/acre/tree/main/solidity#testing

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

__Previous Audits__

Acre’s completed audit reports can be found at:

- https://github.com/Thesis-Defense/Security-Audit-Reports/blob/main/PDFs/240517_Thesis_Defense-Acre_Smart_Contracts_Security_Audit_Report.pdf
- https://github.com/Thesis-Defense/Security-Audit-Reports/blob/main/PDFs/240808_Thesis_Defense-Mezo-Acre_stBTC_Smart_Contracts_Security_Audit_Report.pdf

Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Acre Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/27470648000273-ACRE-Audit-Competition-Reward-Terms)

The reward pool of **$50,000 USD** will be entirely distributed among participants. 

- 10% of the total reward pool or a maximum of $50k, whichever is lower, is allocated to guaranteed rewards for Insight reports, regardless of whether 0 or more bugs are found or not.

For this audit competition, duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the Immunefi [Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Payment Terms__

Payouts are handled by the Acre team directly and are denominated in USD. However, payments are done in USDC

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

* The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi). Duplicates of Insight reports weren't rewarded in any previous Audit Competitions, neither they will be rewarded in this Audit Competition or any other Audit Competition going forward.

## Out of scope (program-specific)

(none)

## Out of scope and rules

These impacts are out of scope for this bug bounty program

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
