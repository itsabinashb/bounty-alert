# Felix

- Page: https://immunefi.com/bug-bounty/felix/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Smart Contract
- PoC required for: (none)
- End date: (none)

## Assets in scope (28)

- [smart_contract] https://hyperevmscan.io/address/0x02c6a2fa58cc01a18b8d9e00ea48d65e4df26c70 — feUSD
- [smart_contract] https://hyperevmscan.io/address/0x12a1868b89789900e413a6241ca9032dd1873a51 — Price Feed
- [smart_contract] https://hyperevmscan.io/address/0x3100f4e7bda2ed2452d9a57eb30260ab071bbe62 — Trove Manager
- [smart_contract] https://hyperevmscan.io/address/0x36b7bd65276eda7cdc5f730da5cdb7ee7736672e — Borrower Operations
- [smart_contract] https://hyperevmscan.io/address/0x39ebba742b6917d49d4a9ac7cf5c70f84d34cc9e — Active Pool
- [smart_contract] https://hyperevmscan.io/address/0x50743a84c68a9d14d93364ed31afa4012183df1c — Default Pool
- [smart_contract] https://hyperevmscan.io/address/0x5555555555555555555555555555555555555555 — WHYPE
- [smart_contract] https://hyperevmscan.io/address/0x576c9c501473e01ae23748de28415a74425efd6b — Stability Pool
- [smart_contract] https://hyperevmscan.io/address/0x5ad1512e7006fdbd0f3ebb8aa35c5e9234a03aa7 — Trove NFT
- [smart_contract] https://hyperevmscan.io/address/0x5b271dc20ba7beb8eee276eb4f1644b6a217f0a3 — Borrower Operations
- [smart_contract] https://hyperevmscan.io/address/0x642d979341eaac9c10623f5a58283aa72f6e2fa9 — Sorted Troves
- [smart_contract] https://hyperevmscan.io/address/0x7201fb5c3ba06f10a858819f62221ae2f473815d — Address Registry
- [smart_contract] https://hyperevmscan.io/address/0x7560059081ede2ff6c6b980fd1ee9a53df4e9935 — Gas Pool
- [smart_contract] https://hyperevmscan.io/address/0x8b71c92edf02dff693042e4e808d0568ccf0a137 — Gas Pool
- [smart_contract] https://hyperevmscan.io/address/0x8d99575ebbbda038a626ca769561c16fdd7a5939 — Active Pool
- [smart_contract] https://hyperevmscan.io/address/0x9182e36bd7cceb71812c766c4464208ad9c122ca — Collateral Surplus Pool
- [smart_contract] https://hyperevmscan.io/address/0x9de1e57049c475736289cb006212f3e1dce4711b — Collateral Registry
- [smart_contract] https://hyperevmscan.io/address/0xa1e95e74d07fec324a82cd2ef19ebcb33907c605 — Default Pool
- [smart_contract] https://hyperevmscan.io/address/0xa32e89c658f7fdcc0bdb2717f253bacd99f864d4 — Hint Helpers
- [smart_contract] https://hyperevmscan.io/address/0xabf0369530205ae56dd4c49629474c65d1168924 — Stability Pool
- [smart_contract] https://hyperevmscan.io/address/0xad8a43ac8da98990efa4d5ec7b91135965d5846b — Trove NFT
- [smart_contract] https://hyperevmscan.io/address/0xb9bE1AeD5Ba289510cDfeF80700d22d4f25459A8 — Price Feed
- [smart_contract] https://hyperevmscan.io/address/0xbbe5f227275f24b64bd290a91f55723a00214885 — Trove Manager
- [smart_contract] https://hyperevmscan.io/address/0xd1caa4218808eb94d36e1df7247f7406f43f2ef6 — Sorted Troves
- [smart_contract] https://hyperevmscan.io/address/0xe7aba857f8e2c95462e69b93c7ea78ac19aafe38 — Collateral Surplus Pool
- [smart_contract] https://hyperevmscan.io/address/0xefbd9cfe88235f0e648aefb52c8e8dc152a9ad6f — feUBTC (Felix UBTC Wrapper for Decimals)
- [smart_contract] https://hyperevmscan.io/address/0xfc4e20bd9f0e4f8782bea92a7bd8002367882407 — Address Registry
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (21)

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

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$20,000, primacy=primacy_of_impact, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$4,000, primacy=primacy_of_impact, rewardModel=range
- [smart_contract] Medium: fixedReward=$2,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 20 000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

- For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward.

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 4 000 to USD 10 000 depending on the funds at risk, capped at the maximum high reward.  

In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

__Reward Payment Terms__

Payouts are handled by the Felix Protocol team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
