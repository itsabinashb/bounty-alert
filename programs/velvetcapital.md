# Velvet Capital

- Page: https://immunefi.com/bug-bounty/velvetcapital/scope/
- Max bounty: $51,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (31)

- [smart_contract] https://bscscan.com/address/0x0Fb11066768e7775e1b9dAC3C6022F17D893853f — FeeLibrary
- [smart_contract] https://bscscan.com/address/0x1d2bA92e2227377fCD3c047CCdF1D4389c98f29B — OffChainRebalance
- [smart_contract] https://bscscan.com/address/0x2606ac7e68044245282643202A391d82D6650b3B — RebalanceLibrary
- [smart_contract] https://bscscan.com/address/0x26Ae500eDcE7c7a9F00007fCeF026062E10E9FE1 — PancakeSwapLPHandler
- [smart_contract] https://bscscan.com/address/0x3bD9A49283F059b3faa7DdBD7515e2E82dce02b1 — FeeModule
- [smart_contract] https://bscscan.com/address/0x433879587EC11845ACE71C9c4061DeDa7a6d17Be — AssetManagerConfig
- [smart_contract] https://bscscan.com/address/0x4DCdeBc14c8e3A1dc499976fe57a16162045eFBd — IndexSwapLibrary
- [smart_contract] https://bscscan.com/address/0x4Dc08588a95244DF46ADd6b274079d99Bf521d57 — ParaswapHandler
- [smart_contract] https://bscscan.com/address/0x577d56b755f5904184abE5792477a57f9CE37463 — OffChainIndexSwap
- [smart_contract] https://bscscan.com/address/0x5Dec110904701E1888ff740362231f735b4D0487 — BeefyLPHandler
- [smart_contract] https://bscscan.com/address/0x5c2Cd133c766ea78F7BEA635fcfFff3191bD5F56 — PancakeSwapHandler
- [smart_contract] https://bscscan.com/address/0x5d3405Db3A16Cd9C545DBac651ab5D9456C14B73 — ZeroExHandler
- [smart_contract] https://bscscan.com/address/0x74003BD2bDB88EE4D6b55F88FB88616686a6f214 — BaseHandler
- [smart_contract] https://bscscan.com/address/0x80EF871da875Bebe6D9F04aEb9eA883d00192636 — IndexSwap
- [smart_contract] https://bscscan.com/address/0x8133c0f5414950e3ecd3870732A38D4c3510BdeE — RebalanceAggregator
- [smart_contract] https://bscscan.com/address/0x87279059F6c600D894579A6EF6B87e8Df14E4779 — BeefyHandler
- [smart_contract] https://bscscan.com/address/0x8DF80904404010a5B8C767236f2d8671e1d5250D — ApeSwapLendingHandler
- [smart_contract] https://bscscan.com/address/0x9AFC0716beAEe8a7632df4bdbE14C27055145aC7 — VenusHandler
- [smart_contract] https://bscscan.com/address/0x9B85c8D03E082365AB48230761BFaD28D4e45B37 — BiSwapLPHandler
- [smart_contract] https://bscscan.com/address/0xA1c283f1C9C3A70378160434B37e79635aAB52Bf — Exchange
- [smart_contract] https://bscscan.com/address/0xB9669646EBb93A03dB67CC05f2894487C9923775 — ERC1967Proxy
- [smart_contract] https://bscscan.com/address/0xC2f2Bf0c228714d038c2495343224c0d9199cC82 — PriceOracle
- [smart_contract] https://bscscan.com/address/0xD9528E3Ca04A9dd0cC6515Af69B7958eB3b6E248 — WombatHandler
- [smart_contract] https://bscscan.com/address/0xE61472Ce45e559830ECF12F6a215Cd732F4D798B — ERC1967Proxy
- [smart_contract] https://bscscan.com/address/0xb0a7f3da89634F31E904a369F83241744B5c2a7d — ApeSwapLPHandler
- [smart_contract] https://bscscan.com/address/0xb0e7a890ae4351bd0bc8e3e6ebec4525f3edf171#code — New IndexSwap
- [smart_contract] https://bscscan.com/address/0xd21d51E9BB8aF5De3dbacc519dc73DCD95a7c036 — New OffChainRebalance
- [smart_contract] https://bscscan.com/address/0xdbA97FF0dc7ddDB8c42Dc50DCD151F2E95978ae6 — Rebalancing
- [smart_contract] https://bscscan.com/address/0xe776BAa635d7FA9D2a62371A180895F016eD4045 — OneInchHandler
- [smart_contract] https://bscscan.com/address/0xf68e38906DD101f0617A6fB4A0FA25694620C013 — VelvetSafeModule
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (11)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds for more than 24 hours
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$51,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$1,500, rewardModel=range
- [smart_contract] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the[ Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is __10%__ of the funds directly affected up to a maximum of __USD 51 000__. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of __USD 10 000__ is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attacks within the first hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are considered at the full amount of funds at risk, capped at the maximum high reward. This is to incentivize security researchers to uncover and responsibly disclose vulnerabilities that may have not have significant monetary value today, but could still be damaging to the project if it goes unaddressed.   

__Reward Payment Terms__

Payouts are handled by the __Velvet__ team directly and are denominated in __USD__. However, payments are done in __USDC__

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
