# Katana

- Page: https://immunefi.com/bug-bounty/katana/scope/
- Max bounty: $80,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (23)

- [smart_contract] https://basescan.org/address/0xD5390300c5DB71F80d46f0fA9983Fc72D4d1e3da — KAT OFT
- [smart_contract] https://etherscan.io/address/0x100d3ca4f97776a40a7d93db4abf0fea34230666 — Aggchain FEP
- [smart_contract] https://etherscan.io/address/0x250D30c523104bf0a06825e7eAdE4Dc46EdfE40E — OptimismPortal
- [smart_contract] https://etherscan.io/address/0x8F051Ca72a3440d83B18E71C3E59676203aB8f91 — KAT OFT
- [smart_contract] https://immunefi.com/bug-bounty/katana/information/ — Primacy of Impact
- [smart_contract] https://katana.network/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://katanascan.com/address/0x053FA9b934b83E1E0ffc7e98a41aAdc3640bB462 — NativeConverter vbUSDT
- [smart_contract] https://katanascan.com/address/0x0913DA6Da4b42f538B445599b46Bb4622342Cf52 — WBTC (aka vbWBTC)
- [smart_contract] https://katanascan.com/address/0x106F7D67Ea25Cb9eFf5064CF604ebf6259Ff296d — vKAT
- [smart_contract] https://katanascan.com/address/0x203A662b0BD271A6ed5a60EdFbd04bFce608FD36 — USDC (aka vbUSDC)
- [smart_contract] https://katanascan.com/address/0x2DCa96907fde857dd3D816880A0df407eeB2D2F2 — USDT (aka vbUSDT)
- [smart_contract] https://katanascan.com/address/0x2a3DD3EB832aF982ec71669E178424b10Dca2EDe — Agglayer Bridge
- [smart_contract] https://katanascan.com/address/0x4d6fC15Ca6258b168225D283262743C623c13Ead — vKAT escrow
- [smart_contract] https://katanascan.com/address/0x62D6A123E8D19d06d68cf0d2294F9A3A0362c6b3 — USDS (aka vbUSDS)
- [smart_contract] https://katanascan.com/address/0x639f13D5f30B47c792b6851238c05D0b623C77DE — NativeConverter
- [smart_contract] https://katanascan.com/address/0x6C16E26013f2431e8B2e1Ba7067ECCcad0Db6C52 — Jitosol OFT
- [smart_contract] https://katanascan.com/address/0x7231dbaCdFc968E07656D12389AB20De82FbfCeB — avKAT
- [smart_contract] https://katanascan.com/address/0x7f1f4b4b29f5058fa32cc7a97141b8d7e5abdc2d — KAT
- [smart_contract] https://katanascan.com/address/0x8f051ca72a3440d83b18e71c3e59676203ab8f91 — KAT OFT Adapter
- [smart_contract] https://katanascan.com/address/0x97a3500083348A147F419b8a65717909762c389f — NativeConverter vbUSDC
- [smart_contract] https://katanascan.com/address/0xEE7D8BCFb72bC1880D0Cf19822eB0A2e6577aB62 — WETH (aka vbETH)
- [smart_contract] https://katanascan.com/address/0xa6b0db1293144ebe9478b6a84f75dd651e45914a — NativeConverter vbETH
- [smart_contract] https://katanascan.com/address/0xb00aa68b87256E2F22058fB2Ba3246EEc54A44fc — NativeConverter vbWBTC

## Asset notes

(none)

## Impacts in scope (12)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Low: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Low: Theft of gas
- [smart_contract] Low: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$80,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$15,000, minReward=$3,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$2,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of **USD 80 000**. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of **USD 20 000** is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. 
- The amount of funds at risk will be calculated with the impact of the first attack being at **100%** and then a reduction of **25%** from the amount of the first attack for every **[300 blocks]** the attack needs for subsequent attacks from the first attack, rounded down. 

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of **USD 3 000 to USD 15 000** with the reward calculated based on **100%** of the funds at risk, though capped at the maximum high reward
In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. 

__Reward Payment Terms__

Payouts are handled by the Katana team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

- Any vulnerability originating in the AggLayer bridge contracts is out of scope unless it results in direct, irreversible loss of funds from the Vault Bridge contracts.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (2)

- Issue that talks about Destination Address = address(0) AggLayer bridge exploit path relying on where the destinationAddress is set to zero , this is considered OOS. (https://github.com/agglayer/lxly-bridge-and-call/tree/3826c37ea7be36eaeba8decae8ef1479203f71e7/src)
- JumpPoint Behavior: Issues that occur within the bridge-and-call logic that lead to funds being "stuck" at a JumpPoint contract only. (https://github.com/agglayer/lxly-bridge-and-call/tree/3826c37ea7be36eaeba8decae8ef1479203f71e7/src)
