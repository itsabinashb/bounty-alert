# TruYields

- Page: https://immunefi.com/bug-bounty/trufin/scope/
- Max bounty: $20,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (3)

- [smart_contract] https://explorer.solana.com/address/6EZAJVrNQdnBJU6ULxXSDaEoK6fN7C3iXTCkZKRWDdGM?cluster=devnet — Solana staker and whitelist contracts on testnet
- [smart_contract] https://github.com/TruFin-io/smart-contracts-solana-public — Solana staker and whitelist contracts on GitHub
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (14)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$20,000, primacy=primacy_of_impact, rewardCalculationPercentage=0, rewardModel=fixed
- [smart_contract] High: fixedReward=$10,000, primacy=primacy_of_impact, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$3,000, primacy=primacy_of_impact, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Repeatable Attack Limitations__

In cases of repeatable attacks for smart contract bugs, only the first attack will be counted, regardless of whether the smart contract is upgradable, pausable, or killable.

__Public Disclosure of Known Issues__

Bug reports covering previously discovered bugs acknowledged below are not eligible for any reward through the bug bounty program. 

- Slashing is only enabled for Injective. Any issue related to slashing for other stakers will not be considered.
- Apart from the Solana staker, all TruFin stakers offer an allocation feature that enables a user to allocate rewards from the staked token. The amount allocated may exceed the total value currently staked by the user, which is fine. The user will still be required to have enough tokens in their wallet at the point at which distributions are made, hence no issue related to users not having enough to cover allocation’s distributions will be considered a bug.


__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Smart Contract - Critical
- Smart Contract - High
- Smart Contract - Medium

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules) Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

Payouts are handled by the Trufin team directly and are denominated in USD. However, payments are done in USDC.

## Out of scope (program-specific)

- Impacts caused by bugs found in external libraries used by the contract
- Best practice recommendations

## Out of scope and rules

These impacts are out of scope for this bug bounty program. 

__All Categories__

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program

__Smart Contracts__

- Incorrect data supplied by third party oracles
   - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks
- Impacts caused by bugs found in external libraries used by the contract
- Best practice recommendations

The following activities are prohibited by this bug bounty program:

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
