# Stargate

- Page: https://immunefi.com/bug-bounty/stargate/scope/
- Max bounty: $10,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (15)

- [smart_contract] https://etherscan.io/address/0x1041D127b2d4BC700F0F563883bC689502606918 — Treasurer
- [smart_contract] https://etherscan.io/address/0x268Ca24DAefF1FaC2ed883c598200CcbB79E931D — StargatePoolmETH
- [smart_contract] https://etherscan.io/address/0x3E368B6C95c6fEfB7A16dCc0D756389F3c658a06 — FeeLibV1ETH
- [smart_contract] https://etherscan.io/address/0x52B35406CB2FB5e0038EdEcFc129A152a1f74087 — FeeLibV1USDC
- [smart_contract] https://etherscan.io/address/0x5871A7f88b0f3F5143Bf599Fd45F8C0Dc237E881 — StargateMultiRewarder
- [smart_contract] https://etherscan.io/address/0x6D5521F46b2cba9443feFC09cBaC3B15AE0F73eB — FeeLibV1mETH
- [smart_contract] https://etherscan.io/address/0x6Dd69717B1194B81A92105B7e0F94cb40f68A3e3 — FeeLibV1METIS
- [smart_contract] https://etherscan.io/address/0x6d6620eFa72948C5f68A3C8646d58C00d3f4A980 — TokenMessaging
- [smart_contract] https://etherscan.io/address/0x77b2043768d28E9C9aB44E1aBfC95944bcE57931 — StargatePoolNative
- [smart_contract] https://etherscan.io/address/0x933597a323Eb81cAe705C5bC29985172fd5A3973 — StargatePoolUSDT
- [smart_contract] https://etherscan.io/address/0xFF551fEDdbeDC0AeE764139cCD9Cb644Bb04A6BD — StargateStaking
- [smart_contract] https://etherscan.io/address/0xc026395860Db2d07ee33e05fE50ed7bD583189C7 — StargatePoolUSDC
- [smart_contract] https://etherscan.io/address/0xcDafB1b2dB43f366E48e6F614b8DCCBFeeFEEcD3 — StargatePoolMETIS
- [smart_contract] https://etherscan.io/address/0xe171AFcd1E0394b3312e68ca823D5BC87F3Db311 — FeeLibV1USDT
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (7)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$10,000,000, minReward=$100,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of __USD 10 000 000__. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of __USD 100 000__ is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

- For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

- High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 10 000 to USD 100 000 depending on the funds at risk, capped at the maximum high reward.  

- In the event of temporary freezing, the reward doubles from the full frozen value for every additional [24h] that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

__Reward Payment Terms__

Payouts are handled by the Stargate Foundation team directly, on behalf of the StargateDAO, and are denominated in __USD__. However, payments are done in __USDC__ on __Ethereum__.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
