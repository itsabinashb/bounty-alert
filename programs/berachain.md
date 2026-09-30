# Berachain

- Page: https://immunefi.com/bug-bounty/berachain/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (4)

- [blockchain_dlt] https://github.com/berachain/beacon-kit — Beacon Kit
- [blockchain_dlt] https://github.com/berachain/bera-reth — A high-performance Rust execution client for Berachain, built with the Reth SDK.
- [smart_contract] https://github.com/berachain/airdrop-contracts — Berachain Airdrop Contracts
- [smart_contract] https://github.com/berachain/contracts — Berachain Smart Contracts

## Asset notes

(none)

## Impacts in scope (31)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] Medium: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Medium: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments
- [blockchain_dlt] Medium: Unintended chain split (network partition)
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network
- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

Only the following impacts are accepted within this bug bounty program. All other impacts are not considered in scope, even if they affect something in the assets in the scope table.

__For Blockchain/DLT__

The set of attack vectors listed in this bullet list represents potential exploits that may result in one or more of the impacts defined in the table.

- Remote code execution on validator node
- Exposure of cryptographic key material
- Impersonation of validator’s authenticated actions, e.g. forging of signatures or votes
- Bugs that would allow the extraction, or the destruction, or the generation of surplus monetary rewards other than what is designated in the protocol
- Any bug that would lead to a perceivable advantage other than the validator’s voting power, e.g. election bias
- Confused deputy on equivocating or slashable behavior, e.g. the validator node is induced into voting twice involuntarily
- Attacks lead a percentage of nodes to crash, halting the chain
- Bugs leading to a percentage of nodes into an inconsistent state, without stopping the chain
- Non-generic attacks lead to a chain halt or make the chain unable to progress
- Safety and correctness flaws that would require the combination of extraordinary conditions to occur
- Extended degradation of performances by non-generic means 
- Non-generic attacks mean that there must be an omission or a defect in the code that would result in any significant computational advantage.

## Rewards

- [blockchain_dlt] Critical: maxReward=$100,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] Medium: maxReward=$10,000, minReward=$2,000, rewardModel=range
- [blockchain_dlt] Low: fixedReward=$2,000, rewardModel=fixed
- [smart_contract] Critical: maxReward=$100,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$25,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$2,000, rewardModel=range
- [smart_contract] Low: fixedReward=$2,000, rewardModel=fixed

## Reward notes

***STOP!*** **Is your report `Web/Apps` related?**

**If yes, please visit:** https://immunefi.com/bug-bounty/berachain-webapps/information/

___

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical Blockchain/DLT bugs, the reward amount is 10% of the funds directly affected, capped at the maximum critical reward listed above. However, a minimum reward as listed above will be rewarded to incentivize security researchers against withholding a bug report.

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to the maximum listed above. Calculating the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward as listed above will be rewarded to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 


- For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. The project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High-Level Reports__

- High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within the range listed above depending on the funds at risk, capped at the maximum high reward.

- In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for more significant damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures more substantial incentives for bug disclosure of this nature.
 
__Reward Payment Terms__

Payouts are handled by the Berachain team directly and are denominated in USD. However, payments are made in BERA on Berachain.

The net amount rewarded is calculated based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

This Program, as it pertains to the [Berachain Airdrops Contract](https://github.com/berachain/airdrop-contracts), is specifically designed to address reports that result in financial loss. In particular, any exploit related to airdrop components already claimed by users, which consequently cannot translate in any financial losses, will not be considered.

The following assets are OOS of this program:
 - https://github.com/berachain/airdrop-contracts/blob/main/src/Distributor1.sol

For all other contracts, which means all except the `Airdrops Contract`, the following impacts are out of scope of this bug bounty program.

__All Categories:__

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program
- Impacts caused by attacks requiring access to privileged addresses (including, but not limited to: governance and strategist contracts) without additional modifications to the privileges attributed
- Impacts requiring phishing or other social engineering attacks against project's employees and/or customers
- Impacts relying on theoretical user interactions without any demonstration of regular or significant occurrence

__Blockchain/DLT & Smart Contract Specific:__

For bera-reth, our Berachain fork of the Rust Ethereum client, *any upstream bugs are out of scope*
Please report only bugs specific to Berachain's fork
https://github.com/berachain/bera-reth


- Incorrect data supplied by third-party oracles
  - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks
- Node REST API (/eth/v1/beacon/*) is out of scope
- DoS against default-off components doesn't qualify

__Prohibited Activities:__

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Out of scope and rules

These impacts are out of scope of this bug bounty program. 

__All Categories:__

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program
- Impacts caused by attacks requiring access to privileged addresses (including, but not limited to: governance and strategist contracts) without additional modifications to the privileges attributed
- Impacts requiring phishing or other social engineering attacks against project's employees and/or customers
- Impacts relying on theoretical user interactions without any demonstration of regular or significant occurrence

__Blockchain/DLT & Smart Contract Specific:__

- Incorrect data supplied by third-party oracles
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

## Known issues (1)

- src/pol/BeaconDeposit.sol operator address is prone to front-running (https://github.com/berachain/contracts/issues/2)
