# Velvet Capital V2

- Page: https://immunefi.com/bug-bounty/velvet-capital-v2/scope/
- Max bounty: $10,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: (none)

## Assets in scope (14)

- [smart_contract] https://basescan.org/address/0x0490A477e4fc96392bDf1e2846E3230A1263a5D2 — ProtocolConfig
- [smart_contract] https://basescan.org/address/0x0827cf431c2f2a4f12584fddb6f01ab0e26ccbe0 — BaseRebalancingAddress
- [smart_contract] https://basescan.org/address/0x17e14a8bc2380096f9e9eafea47fe1015502a09d — BaseAssetManagementConfigAddress
- [smart_contract] https://basescan.org/address/0x3475dd4b852baf51279a463f0e5f38e5aed2e784 — BasePortfolioAddress
- [smart_contract] https://basescan.org/address/0x4f69982392ba29e98c62b07482be190301d12ca7 — BaseTokenExclusionManagerAddress
- [smart_contract] https://basescan.org/address/0x608e93ad410f3e3288dfc1a60446925a0fcf967e — PriceOracle
- [smart_contract] https://basescan.org/address/0x6e3e0fe13dae2c42cca7ae2e849b0976e2e63e05 — DepositBatch
- [smart_contract] https://basescan.org/address/0x6ec2a3a88a72943d2e87ed05cdf25914983ab7f6 — EnsoHandler
- [smart_contract] https://basescan.org/address/0xa9452eaf5aa440790e6ca90e38c10b40fb611e59 — WithdrawManager
- [smart_contract] https://basescan.org/address/0xaead7d9202f3efb73657ca031f645c6b46cfe177 — WithdrawBatch
- [smart_contract] https://basescan.org/address/0xc05d2e4bbe442172c649faa1fdc503e627062bd3 — FeeModuleImplementationAddress
- [smart_contract] https://basescan.org/address/0xe4e23120a38c4348d7e22ab23976fa0c4bf6e2ed — DepositManager
- [smart_contract] https://basescan.org/address/0xf93659fb357899e092813bc3a2959ceDb3282a7f — PortfolioFactory
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
- [smart_contract] Medium: Theft Gas

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$10,000, minReward=$7,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$5,000, minReward=$3,000, rewardModel=range
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
