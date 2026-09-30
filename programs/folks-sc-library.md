# Audit Comp | Folks Smart Contract Library

- Page: https://immunefi.com/bug-bounty/folks-sc-library/scope/
- Max bounty: $30,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - medium, smart_contract - low, smart_contract - high, smart_contract - critical
- End date: 2025-07-21T10:00:00.000Z

## Assets in scope (6)

- [smart_contract] https://github.com/Folks-Finance/algorand-smart-contract-library/blob/main/contracts/library/AccessControl.py — AccessControl - Contract module that allows children to implement role-based access control mechanisms.
- [smart_contract] https://github.com/Folks-Finance/algorand-smart-contract-library/blob/main/contracts/library/Initialisable.py — Initialisable - Contract that allows children to be initialisable
- [smart_contract] https://github.com/Folks-Finance/algorand-smart-contract-library/blob/main/contracts/library/RateLimiter.py — RateLimiter - Contract module that allows children to implement rate limiting mechanisms.
- [smart_contract] https://github.com/Folks-Finance/algorand-smart-contract-library/blob/main/contracts/library/UInt64SetLib.py — UInt64SetLib - Subroutines to mimic the behaviour of a “set” data structure for uint64 values.
- [smart_contract] https://github.com/Folks-Finance/algorand-smart-contract-library/blob/main/contracts/library/Upgradeable.py — Upgradeable - Contract module that allows children to implement scheduled upgrade mechanisms.
- [smart_contract] https://github.com/Folks-Finance/algorand-smart-contract-library/blob/main/contracts/library/extensions/InitialisableWithCreator.py — InitialisableWithCreator - Extension to Initialisable Contract which ensures caller of "initialise" method is contract creator.

## Asset notes

__Asset Accuracy Assurance__

- Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

- Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Primacy of Impact vs Primacy of Rules__

- Folks Finance adheres to the Primacy of Rules, which means that the whole Audit Competition program is run strictly under the terms and conditions stated within this page.

__KYC Requirement__

- No KYC is required for the Folks Smart Contract Library Audit Competition

__Eligibility Criteria__

- Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
   - On OFACs SDN list 
   - Official contributor, both past or present
   - Employees and/or individuals closely associated with the project 
   - Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

- Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
   - Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

- Immunefi may publish bug reports submitted to this Audit Competition and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

- When there is uncertainty about how feasible an attack is Immunefi will use our feasibility limitation standards to determine the severity of the report.

__Immunefi Standard Badge__

- By adhering to Immunefi’s best practice recommendations, Folks Finance has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (8)

- [smart_contract] Critical: Bypass of the address permissions during an upgrade
- [smart_contract] Critical: Bypass of the rate limit beyond set parameters
- [smart_contract] Critical: Unauthorized escalation of privileged roles which deviate from the original permissions
- [smart_contract] High: Permanent denial of service of a smart contract functionality
- [smart_contract] Medium: Impacts caused by griefing with no economic damage other than transaction fees where fix requires a change or a pause of a smart contract
- [smart_contract] Medium: Temporary denial of service for more than one block
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Temporary denial of service (smart contract is made unable to operate for one block, functionality is restored in the next block)

## Impact notes

**Build commands, Test commands, and instructions on how to run them:**

Follow the setup instructions in the project README.

- To generate the TEAL code and ARC56 specs for the contracts, run the command: npm run pre-build

- To build the TS clients to interact with the contracts, run the command: npm run build

- Start an Algorand localnet with AlgoKit and Docker using: algokit localnet start

- Run all tests from root directory using: npm run test

- Or single test file using: PYTHONPATH="./contracts" npx jest <PATH_TO_TEST_FILE>


**Where might Security Researchers confuse out-of-scope code to be in-scope?**

- All the smart contracts in “contracts/library/test” are out of scope and only included to facilitate the unit testing. 


**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

- Ensuring addresses only operate within their assigned privileges. Also checking the logic of the smart contracts is sound. 


**Which chains and/or networks will the code in scope be deployed to?**

- Algorand


**What external dependencies are there?**

- Algorand Python Compiler 

**What are the most valuable educational resources already available?**

- Folks Smart Contract Library [Documentation](https://docs.google.com/document/d/1asxwEYzNtG2cTTvuTwBszMmEUKMtkL8s7bBROeD1LlU/edit?usp=sharing.)
- Details of [Unit testing](https://github.com/Folks-Finance/algorand-smart-contract-library/tree/main/tests) which may help in understanding how the smart contracts are intended to be called and operate. 
- Algorand Python [Language Guide](https://algorandfoundation.github.io/puya/language-guide.html)


**Previous Audits**

- Folks Finance Smart Contract Library has no audit report as of 7 July 2025.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of Reward Pool, pocRequired=True

## Reward notes

__Audit Competition Flat Reward Pool__

The following reward terms are a summary. For the full details read our [Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program](https://immunefi.com/allstars/) participants

The reward pool is **$30,000 USD** if any bug is found. That means that even if 1 Low severity bug is found, the whole reward pool is unlocked and has to be fully distributed between security researchers. 

If not a single bug is found (Insights do not count as bugs) the reward pool is $4,500 USD.

Private known issues, meaning known issues that were not publicly disclosed, are valid and unlock the corresponding reward pool.

Duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

*Insight Rewards*: Portion of the Rewards Pool

*The "Insight" severity was introduced on Boost (Audit Competitions) & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

**Duplicates of Insight reports are not eligible for a reward.**

__Proof of Concept (PoC) Requirements__

For this program, runnable PoC code is not required. Whitehats are instead required to write a step-by-step explanation of the PoC and impact.
For unclear reports or to resolve disputes Immunefi may still require a runnable PoC.Read more about it in [Audit Competition Proof-of-Concept Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/33260632501777-Audit-Competition-Proof-of-Concept-Rules)

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Funds used for the minimum balance of a smart contract account are implicitly required and not refunded (https://docs.google.com/document/d/1asxwEYzNtG2cTTvuTwBszMmEUKMtkL8s7bBROeD1LlU/edit?tab=t.0)
