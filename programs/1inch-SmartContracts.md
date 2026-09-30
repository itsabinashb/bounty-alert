# 1inch - Smart Contracts

- Page: https://immunefi.com/bug-bounty/1inch-SmartContracts/scope/
- Max bounty: $500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (8)

- [smart_contract] https://github.com/1inch/cross-chain-swap — Cross-chain Swap
- [smart_contract] https://github.com/1inch/delegating — Delegating Contracts
- [smart_contract] https://github.com/1inch/farming — Farming Contracts
- [smart_contract] https://github.com/1inch/fusion-protocol — Limit Order Settlement
- [smart_contract] https://github.com/1inch/limit-order-protocol — Limit Order Protocol
- [smart_contract] https://github.com/1inch/solana-crosschain-protocol — Solana Crosschain
- [smart_contract] https://github.com/1inch/solana-fusion — Solana Fusion
- [smart_contract] https://github.com/1inch/token-plugins — Token-plugins

## Asset notes

(none)

## Impacts in scope (10)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of coins or tokens (e.g gas) in a smart contract intended for transaction fees
- [smart_contract] Low: Impacts caused by griefing with no economic damage other than transaction fees where fix requires a change or a pause of a smart contract
- [smart_contract] Low: Smart contract fails to deliver promised token amounts but the remaining token amounts is not stolen or lost and can still be claimed

## Impact notes

***Note: The program applies only to the latest tag/releases.***

## Rewards

- [smart_contract] Critical: maxReward=$500,000, minReward=$30,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$30,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$2,000, rewardModel=range
- [smart_contract] Low: maxReward=$2,000, minReward=$100, rewardModel=range

## Reward notes

### Rewards by Threat Level

Rewards are distributed according to the impact of the vulnerability based on the Impacts in Scope table. 

***Note: The program applies only to the latest tag/releases.***

#### Reward Calculation for Critical Level Reports

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 500000\. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 30000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

#### Repeatable Attack Limitations

* If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. 

* If the attack impacts a smart contract directly holding funds that cannot be upgraded or paused, the amount of funds at risk will be calculated with the first attack being at 100% of the funds that could be stolen and then a reduction of 25% from the amount of the first attack for every 1 hour the attack needs for subsequent attacks from the first attack, rounded down.

#### 

#### Reward Calculation for High Level Reports

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of 10000 to 30000 capped at the maximum high reward.  This is calculated at 100% of the funds affected. 

In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the High severity reward.

#### Additional Terms

In order to qualify for a Critical reward, the demonstrated impact must not only be possible in the in-scope code listed in the Assets in Scope table, but also live on a mainnet deployment. Otherwise, the severity level will be attributed as High and the reward will be determined within the full High severity range (USD 10,000 – USD 30,000) based on the demonstrated impact at the full discretion of the 1inch team. The 1inch team reserves the right to further downgrade and reduce the reward amount for any impact resulting from vulnerabilities or attack vectors involving code that is not deployed on mainnet. 

Impacts resulting from vulnerabilities in imported contracts are considered as out of scope.  

Any vulnerability discovered must be reported no later than 24 hours after the initial discovery. Reports submitted after this window may be considered at 1inch's discretion but are not guaranteed eligibility for a reward.

In cases where the same vulnerability is reported through multiple platforms, priority will be determined by the earlier submission timestamp, regardless of the platform used.

Medium impacts have a base reward of USD 2 000\. At the sole discretion of the 1inch team, it may decide to reward above USD 2 000, though no higher than USD 10 000\. Low impacts have a base reward of USD 100\. At the sole discretion of the 1inch team, it may decide to reward above USD 100, though no higher than USD 2 000\.

#### Reward Payment Terms

Payouts are handled by the 1inch team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability. 

*Reports and payout details may be checked against OFAC, EU, and UK sanctions lists prior to payment. Payment may be withheld, delayed, or refused entirely if prohibited by applicable law, sanctions regimes, or 1inch's compliance obligations. Researchers are responsible for ensuring their participation does not violate the laws of their jurisdiction.*

## Out of scope (program-specific)

These impacts are out of scope for this bug bounty program. 

**All Categories:**

* Impacts requiring attacks that the reporter has already exploited themselves, leading to damage  
* Impacts caused by attacks requiring access to leaked keys/credentials  
* Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible  
* Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code  
* Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production  
* Best practice recommendations  
* Feature requests  
* Impacts on test files and configuration files unless stated otherwise in the bug bounty program  
* Impacts requiring phishing or other social engineering attacks against project's employees and/or customers
* Redundant code
* Old compiler version
* Code style guide violations
* The compiler version is not locked
* Theoretical or purely speculative exploits without demonstrated business impact


**Blockchain/DLT & Smart Contract Specific:**

* Incorrect data supplied by third party oracles  
  * Not to exclude oracle manipulation/flash loan attacks  
* Impacts requiring basic economic and governance attacks (e.g. 51% attack)  
* Lack of liquidity impacts  
* Impacts from Sybil attacks  
* Impacts involving centralization risks  
* Micro gas optimizations (less than 1k of gas)  
* Lack of support for Fee-on-Transfer (FoT) tokens

**Prohibited Activities:**

* Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet  
* Any testing with pricing oracles or third-party smart contracts (Testing the integration logic on local forks is permitted)  
* Attempting phishing or other social engineering attacks against our employees and/or customers  
* Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)  
* Any denial of service attacks that are executed against project assets  
* Automated testing of services that generates significant amounts of traffic
* Public disclosure of an unpatched vulnerability in an embargoed bounty
* Accessing or modifying data belonging to other users  
* Submitting AI-generated reports  
* Spamming forms or account creation flows (even with low volume)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
