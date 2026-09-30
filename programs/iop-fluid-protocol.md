# IOP | Fluid Protocol

- Page: https://immunefi.com/bug-bounty/iop-fluid-protocol/scope/
- Max bounty: $80,000
- KYC required: yes
- Paused: no
- Invite only: yes
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2024-12-12T10:00:00.000Z

## Assets in scope (0)

(none)

## Asset notes

(none)

## Impacts in scope (12)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for more than one week
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Whitehat Educational Resources & Technical Info__

- [https://docs.hydrogenlabs.xyz/fluid-protocol-community/](https://docs.hydrogenlabs.xyz/fluid-protocol-community/)
- Ottersec audit: [https://drive.google.com/file/d/1qhiI26aB9MTXfo-hLW8Qy9ki2ueCudKN/view?usp=sharing](https://drive.google.com/file/d/1qhiI26aB9MTXfo-hLW8Qy9ki2ueCudKN/view?usp=sharing)


__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

This is a rewrite of Liquity (v1) from Solidity into Sway, with numerous design changes. The main differences are the lack of recovery, multi-collateral system with single stability pool, and partial liquidations.

__Where do you suspect there may be bugs? Useful aspects of this question are:__

Yes, please see required functions across all the contracts. Specifically in FPT staking, there are the same assumed invariants as in this report for Liquity: [https://github.com/trailofbits/publications/blob/master/reviews/LiquityProtocolandStabilityPoolFinalReport.pdf](https://github.com/trailofbits/publications/blob/master/reviews/LiquityProtocolandStabilityPoolFinalReport.pdf)
Additionally, math rounding throughout the contracts, since we are using 9 decimals of precision whereas liquity is using 18. 

__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?__

SRC-20 Token Standard

__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

An Owner is out of scope. 


__What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?__

Owner Address.

__What external dependencies are there?__

Fuel standard library primarily. Sway libs. Pyth, Redstone. 


__Are there any unusual points about your protocol that may confuse whitehats?__

The Fluid Proocol docs overview covers the main design changes from Liquity. There are some other minor changes that are not documented. 

__What is the test suite setup information?__

The tests for the smart contracts are included in the GitHub repo: [https://github.com/Hydrogen-Labs/fluid-protocol](https://github.com/Hydrogen-Labs/fluid-protocol)

**Test Structure:**
Unit tests for some smart contracts are located in ./contracts/[contract-name]/src/utils.sw
Integration tests are located in <!-- ./contracts/[contract-name]/tests -->
The interfaces and setup for integration tests are in <!-- ./test-utils -->

**Running the Tests:**
Make sure you have fuelup, fuel-core, cargo, and rust installed
Use command: make build-and-test

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

__Previous Audits__

Fluid Proocol’s completed audit reports can be found here [https://drive.google.com/file/d/1qhiI26aB9MTXfo-hLW8Qy9ki2ueCudKN/view?usp=sharing](https://drive.google.com/file/d/1qhiI26aB9MTXfo-hLW8Qy9ki2ueCudKN/view?usp=sharing). Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the reward pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Fluid Protocol Invite-only program Reward Distribution Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/29970475885457-Fluid-Protocol-Invite-Only-Program-Reward-Terms). 

A reward pool of $80,000 USD will be distributed among participants, even if no valid bugs are found. 

Duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

* The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)


Private known issues will unlock higher reward pools as though they were one severity level lower. For example, a Critical severity bug which was a private known issue would unlock the reward pool conditional on a High severity bug being found.

The severity level of private known issues remains unchanged and whitehats earn their portion of the reward pool and position on the leaderboard according to this unchanged severity level.
Rewards are distributed according to the impact of the vulnerability based on the Immunefi Vulnerability Severity Classification System V2.3.

## Out of scope (program-specific)

The following contract is to be considered out-of-scope:


https://github.com/Hydrogen-Labs/fluid-protocol/tree/main/contracts/token-contract/src/main.sw

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
