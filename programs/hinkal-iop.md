# IOP | Hinkal

- Page: https://immunefi.com/bug-bounty/hinkal-iop/scope/
- Max bounty: $0
- KYC required: yes
- Paused: no
- Invite only: yes
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: 2024-05-07T21:00:00.000Z

## Assets in scope (0)

(none)

## Asset notes

(none)

## Impacts in scope (9)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs for more than 3 hours
- [smart_contract] High: Temporary freezing of funds for more than 3 hours
- [smart_contract] High: Theft of unclaimed yield

## Impact notes

**Proof of Concept (PoC) Requirements**

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

**Eligibility Criteria**

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review

**Responsible Publication**

Whitehats may not publish their bug reports from this program.

However Immunefi will publish a leaderboard and high-level summary of the results of this program which whitehats can use for their portfolio.

**Feasibility Limitations**

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

**Immunefi Standard Badge**

By adhering to Immunefi’s best practice recommendations, Hinkal has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Rewards

- [smart_contract] Critical: level=critical, payout=$2,500 USD, pocRequired=True
- [smart_contract] High: level=high, payout=$1,500 USD, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Hinkal Invite Only Program Reward Distribution Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/24006220866065-Hinkal-Invite-Only-Program-Reward-Distribution-Terms). 

Each participating whitehat will receive a guaranteed reward $2,500

On top of this, there are additional rewards per-unique-bug found:
- $2,500 per Critical
- $1,500 per High

For this Invite Only Program, duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

**Reward Payment Terms**

Payouts are handled by the Hinkal team directly and are denominated in USD. However, payments are done in USDC.

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

## Out of scope (program-specific)

(none)

## Out of scope and rules

These impacts are out of scope for this bug bounty program. 

**All Categories:**

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program

**Blockchain/DLT & Smart Contract Specific:**

- Incorrect data supplied by third party oracles
- Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks


**Prohibited Activities:**

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
