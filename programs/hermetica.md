# Hermetica

- Page: https://immunefi.com/bug-bounty/hermetica/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (13)

- [smart_contract] https://explorer.hiro.so/txid/0x0f1ad52bafc2099b9b75ecff15933546dc09a4c60ed93f902998c7eb570563e9?chain=mainnet — Blacklist
- [smart_contract] https://explorer.hiro.so/txid/0x49512dd2cf400a9b1ace64687d386b3d3d1ad40444de83f6dda1c29cebe01919?chain=mainnet — State
- [smart_contract] https://explorer.hiro.so/txid/0x570b90c20a3b63e431a387a50ee3c9f6a3a709527731a8cbde75b731e9c7369a?chain=mainnet — Zest Interface
- [smart_contract] https://explorer.hiro.so/txid/0x834662426960938e9d483ebfb7ecae90a6c5c0d4327e2cb4011700387d2167bf?chain=mainnet — HQ
- [smart_contract] https://explorer.hiro.so/txid/0x87f8c3bc9625579280050678cdddf46b00f678009be32aab76e5d9beca4e7056?chain=mainnet — Fee Collector
- [smart_contract] https://explorer.hiro.so/txid/0x8a6cfafb63b1fb9549d42789cf2b9a160bcf5859257f4c578451d77dafd0a2e0?chain=mainnet — Controller
- [smart_contract] https://explorer.hiro.so/txid/0x99e0e204634af511074897cae5d7b79602a808b1b4569a7f900fedb0ec2af245?chain=mainnet — Token
- [smart_contract] https://explorer.hiro.so/txid/0x9e2cd7bdd7cc29cf30750835155060a42ebd26943c1f35d2a83b8e6e81f90a35?chain=mainnet — Trading
- [smart_contract] https://explorer.hiro.so/txid/0xb8ce9c1fb139bc4338ae3b6d6c5fa4525fafb87ed9f9ce515b213a0cc0022449?chain=mainnet — Reserve
- [smart_contract] https://explorer.hiro.so/txid/0xb8e567a6f918e041e1fa5a9ca317fdf3048d14f57b0fefdd836cba9da14d3c6e?chain=mainnet — Vault
- [smart_contract] https://explorer.hiro.so/txid/0xc1c3face1d66819ce2cd6f28876b07577c252812c4c43b2145ac89af61819117?chain=mainnet — Hermetica Interface
- [smart_contract] https://explorer.hiro.so/txid/0xdd73e479841dbedba4fa6eee29be9dcef5d64e6093b905016ec1ba74dabba2ba?chain=mainnet — Reserve Fund
- [smart_contract] https://hermetica.fi/ — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (6)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$1,000, rewardModel=range

## Reward notes

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 20 000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

The rest of the severity levels are paid out according to the Impact in Scope table.  


__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward
- The amount of funds at risk will be calculated with the impact of the first attack being at **100%** and then a reduction of **25%** from the amount of the first attack for every **[300 blocks]** the attack needs for subsequent attacks from the first attack, rounded down.


__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of **USD 1 000 to USD 20 000** depending on the funds at risk, capped at the maximum high reward.  

In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.


__Reward Payment Terms__

Payouts are handled by the Hermetica team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
