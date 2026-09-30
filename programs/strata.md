# Strata

- Page: https://immunefi.com/bug-bounty/strata/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: (none)

## Assets in scope (11)

- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/governance/ — All current and future Solidity files in this directory are in scope
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/TrancheDepositor.sol — A  routing helper that converts any supported token into the right form before depositing it into a tranche vault
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/TwoStepConfigManager.sol — Manages exit-fee updates through a secure, two-step governance process
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/base/CDOComponent.sol — Abstract base contract for CDO components (Tranches, Accounting, Strategy)
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/base/cooldown/CooldownBase.sol — Base Cooldown contract
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/base/cooldown/ERC20Cooldown.sol — Locks ERC-20 tokens for a specified cooldown period before withdrawal finalization.
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/base/cooldown/UnstakeCooldown.sol — UnstakeCooldown Contract for strategy unstake redeem requests
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/utils/AccountingLib.sol — Splits a Senior redemption into Senior's base and Junior's loss coverage during a valuation loss.
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/utils/RoundingGuard.sol — Keeps the original value when a recomputed one differs by ≤1 wei, ignoring harmless rounding dust.
- [smart_contract] https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/utils/UD60x18Ext.sol — Extended PRB-Math's UD60x18 with a max(x, y) helper.
- [smart_contract] https://github.com/Strata-Markets/contracts/tree/tranches/contracts/tranches/oracles — All current and future Solidity files in this directory are in scope

## Asset notes

(none)

## Impacts in scope (9)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$250,000, minReward=$10,000, primacy=primacy_of_rules, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$5,000, primacy=primacy_of_rules, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, minReward=$1,000, primacy=primacy_of_rules, rewardModel=range
- [smart_contract] Low: fixedReward=$1,000, primacy=primacy_of_rules, rewardModel=fixed

## Reward notes

## PoC Requirements

To be considered valid, a PoC must reflect a realistic, deployable protocol state. In particular:  Tranche seeding. Each tranche (Junior and Senior) is seeded with at least 10 assets at deployment. PoCs must initialize both tranches with ≥ 10 assets each. Submissions that initialize a tranche at or near the protocol's 1-asset accounting floor (ONE_ASSET) do not represent a deployable state and will be considered out of scope.  Findings whose impact depends on a tranche's base NAV sitting at or near ONE_ASSET, or on initial conditions that would not occur under the seeding above, will be closed as invalid.


Rewards are distributed according to the impact of the vulnerability based on the Immunefi Vulnerability Severity Classification System V2.3.

**Reward Calculation for Critical Level Reports**

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD $250,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD $10,000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

**Repeatable Attack Limitations**

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk.

For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward.

**Reward Calculation for High Level Reports**

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within the specified range depending on the funds at risk, capped at the maximum high reward.

In the event of temporary freezing, the reward doubles from the full frozen value for every additional [48h] that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

**Reward Payment Terms**

Payouts are handled by the Strata team directly and are denominated in USD. However, payments are done in USDC on Mainnet.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

The following will not qualify for bounty:
 - UI and frontend bugs not causing financial loss
 - Minor issues such as typos, formatting problems, or “best practice” suggestions without security impact
 - Social engineering, phishing attempts, or external ecosystem vulnerabilities
 - Bugs in third-party dependencies not directly part of Strata’s deployed contracts
 - Incorrect data supplied by third party oracles
 - Lack of liquidity impacts
 - Centralization risk or attacks requiring access to privileged keys
 - Impact related to attacks that are already exploited and have damaged the protocol
 - Impacts involving centralization risks

## Out of scope and rules

s

## Prohibited activities (program-specific)

(none)

## Known issues (3)

- AprPairFeed::updateRoundData() accepts timestamo that can be 60 seconds in the future and if the UPDATER_FEED_ROLE passes such timestamp deposits  and withdrawals will be blocked for up to 60 sec. The updater feed role is trusted to not do this. Also if it occurs the issues is self-healing - after the time passes operations would be unfrozen (https://github.com/Strata-Markets/contracts-internal/blob/tranches/contracts/tranches/oracles/AprPairFeed.sol#L124)
- ChainlinkAprProviderLib returns base APRs down to -100% (BOUND_MIN = -1e12), but AprPairFeed.ensureValid only accepts down to -50% (APR_BOUNDARY_MIN = -0.5e12), so any APR in [-100%, -50%) passes the provider but reverts the feed. Since Accounting.fetchAprs() reads the feed on every deposit/withdraw with no try/catch, a sufficiently negative base APR (from an underlying pps decline) freezes all deposits and withdrawals until the APR recovers or a keeper pushes a valid round. (https://github.com/Strata-Markets/contracts-internal/blob/tranches/contracts/tranches/oracles/providers/ChainlinkAprProviderLib.sol#L36)
- In DiscreteAccounting.calculateNAVSplitProjected (the path taken when strategy NAV is flat between rewards), the live on-chain contract caps Senior's projected target gain by projected Junior NAV but debits it from real Junior (flooring real Junior to 0) and credits Senior the full amount, with no solvency check. If Senior's accrued target over a continuous rewardless stretch ever exceeds real Junior, the stored tranche NAVs sum to more than actual assets, and the next realized-yield update reverts InvalidNavSplit permanently — freezing all deposits and withdrawals. This is already fixed in the repo (commit 6aee201 caps by real Junior instead), but that fix was never deployed to the live MHyper/MM1USD impls. In practice the trigger is effectively unreachable — it requires Junior thinned to the ~5% floor and exactly-flat NAV (zero realized yield) continuously for ≥1 year — so it's a latent, deploy-the-fix issue rather than a live threat. (https://github.com/Strata-Markets/contracts/blob/tranches/contracts/tranches/DiscreteAccounting.sol#L470)
