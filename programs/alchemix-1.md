# Alchemix

- Page: https://immunefi.com/bug-bounty/alchemix-1/scope/
- Max bounty: $150,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (2)

- [smart_contract] https://alchemix.fi/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://github.com/alchemix-finance/v3/tree/master/src — V3 Contracts

## Asset notes

(none)

## Impacts in scope (14)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary Freezing of Funds at 0 cost or profit to attacker for greater than 1 day
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing at minimal no to cost to attacker
- [smart_contract] Medium: Miner Extractable Value in excess of 0.75%
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Unbounded gas consumption with no additional sever related bugs

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$150,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$3,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

__Reward Calculation for Critical Level Reports__
For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to the maximum listed. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward.

__Reward Calculation for High Level Reports__
High impacts concerning theft/permanent freezing of unclaimed yield/royalties are rewarded with a range of 5,000 to 35,000 with the reward calculated based on 100% of the funds at risk, though capped at the maximum high reward.

In the event of temporary freezing, the reward doubles from the full frozen vallue for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward.

## Out of scope (program-specific)

**Yield Strategies**
Only yield strategies that are deployed and hooked up to the MYT on at least one chain are in scope. 

**Trusted Admin**
Admin, Curator, Allocator, and Sentinel are all trusted roles. This will change in the future with onchain governance, but for now are assumed trusted. As an example, strategies recieve a high/med/low risk rating, which dictates maximum relative caps. However, these relative caps are not yet enforced onchain and instead are enforced by trusted curators/allocators.

**Perpetual Gauge** Unused and out of scope, related to "Trusted Admin" above.

**OraclePricedSwapStrategy** is currently in audit and out of scope.

**Known AI Audit Report Issues**
The items located at https://github.com/alchemix-finance/v3/blob/scoopy-ai-scan-findings/REJECTED.md are AI-assisted audit reports that were reviewed internally and deemed invalid. The list can be cross referenced with the findings here: https://github.com/alchemix-finance/v3/blob/scoopy-ai-scan-findings/FINDINGS-INDEX.md

**Bad Debt** The transmuter has a calculator to distribute bad debt more fairly when detected (claim value in the transmuter is reduced when bad debt is detected). This mechanism is not meant to be perfect - once bad debt happens, there is not really a perfect mechanism. It is simply meant to be *more* fair than a simple race to the exit scenario. There are scenarios where there may be some bad debt where the bad debt mechanism may not trigger - that is OK. Thus, any report akin to "bad debt distribution isn't totally fair" is not in scope.

**How transmuter returns are viewed**
When a user deposits to the transmuter, they deposit alAsset and expect to get MYT back after a fixed period of time. We view the alAsset to MYT conversion as "promised returns", NOT "user funds". Ie, the user does not own MYT until the conversion. They own the alAsset. If they are unable to claim the MYT, then their position is still alAsset denominated and they have not recieved the promised returns.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (5)

- All curators and allocators are trusted (ie, low/med/high risk strategy cap maximums are not enforced on chain, assumed done by curators/allocators/admin) (https://docs.alchemix.fi/user)
- IF the price of the MYT drops below the LTV (say 1 ETH of MYT has a market price of 0.85 ETH) due to withdrawal queues, then it would be expected that arbitragers mint alETH to sell at > 100% LTV. However, so long as the value of the MYT these arbitragers collateralize returns to 1:1, there is no bad debt created in the system. Only a situation that returns permanent bad debt, even after MYT recovery, would be in scope (or a situation where the MYT is prevented from recovering). (https://immunefi.com/audit-competition/alchemix-v3-audit-competition/scope/#top)
- Technically an individual could open numerous small positions at max LTV, hoping that they become eligible for liquidation so they can liquidate themselves and get paid from the feeVault for a net profit. However, the feeVault ONLY pays out when the alchemist is globally undercollateralized, NOT for liquidate individually undercollateralized positions when global collateralization is otherwise acceptable. This is an acceptable risk and therefore not considered in scope. (https://github.com/alchemix-finance/v3-poc/tree/immunefi_audit)
- The DAO Multisig on each chain, which takes on an admin role in the system, is trusted. (https://alchemix-stats.com/)
- We are pricing strategies based on the fundamental backing, rather than dex price, whenever possible. This means there may be scenarios where the fundamental backing has a queue to access (such as the exit queue for wstETH). In these scenarios, as an example, 1 alETH in the transmuter would return 1 ETH worth of MYT, but that 1 ETH of MYT would not be accessible until the withdrawal queue clears, OR the user could sell the 1 ETH of MYT for < 1 ETH. Thus, the MYT market price may be < 1 ETH, which may bring the price of the alAsset < 1 ETH. This is intended behavior, as should the withdrawal queue clear the 1 ETH of MYT value would once again be instantly accessible and thus the alAsset would be redeemable for 1 ETH. (https://immunefi.com/audit-competition/alchemix-v3-audit-competition/scope/#top)
