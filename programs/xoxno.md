# XOXNO

- Page: https://immunefi.com/bug-bounty/xoxno/scope/
- Max bounty: $20,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (2)

- [smart_contract] https://github.com/XOXNO/rs-lending-xlm — XOXNO Lending monorepo on Stellar Soroban: controller, pool, governance, position NFT, price aggregator and shared math
- [smart_contract] https://xoxno.com — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (7)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$20,000, minReward=$5,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$5,000, minReward=$3,500, rewardModel=range
- [smart_contract] Medium: maxReward=$3,500, minReward=$2,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 20 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 2 500 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. 
- The amount of funds at risk will be calculated with the impact of the first attack being at 100% and then a reduction of 25% from the amount of the first attack for every [300 blocks] the attack needs for subsequent attacks from the first attack, rounded down.

__Reward Calculation for High Level Reports__

- High impacts concerning theft/permanent freezing of unclaimed yield are rewarded within a range of USD 1 250 to USD 2 500 with the reward calculated based on 100% of the funds at risk, though capped at the maximum high reward. 
- In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. 

__Reward Payment Terms__

Payouts are handled by the XOXNO team directly and are denominated in USD. However, payments are done in USDC on ETH.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

This program covers the XOXNO Lending smart contracts on Stellar Soroban mainnet. A valid report shows a concrete deviation from a protocol invariant, an authorization boundary, an accounting rule, a price guarantee or a liveness property. A report that restates a documented design choice is closed without a reward.

__Out of scope__

- Bugs in the Stellar network, the Soroban host, the Rust toolchain, upstream crates, or third-party providers (Reflector, RedStone, DeFindex, Blend, swap venues, listed token contracts). Report those to their maintainers. How XOXNO Lending validates a response from one of them is in scope.
- Any scenario that requires a compromised governance key, role key, oracle signer key or keeper key, unless the report shows that the protocol makes the consequences of that compromise materially worse.
- Impact reachable only through the documented administration path: typed proposals, the configured execution delay, guardian pause, oracle sanity-band tightening or hot-role revocation.
- Loss caused by the behaviour of a listed token itself, including sender surcharges, fee-on-transfer, rebases, false balances, clawbacks, freezes, admin mint or post-listing upgrades. Admitting a token is a governance decision.
- Swap route quality, slippage, price impact, MEV and router fee outcomes. The controller checks positive measured output and final account health, not route optimality.
- Oracle prices that pass the configured sanity bands, source count and staleness limits. Manipulation of an external feed within those bands is a trust assumption of that provider.
- An operation that fails closed, or that is blocked by global pause, a listing flag, a cash shortage, storage archival or TTL expiry, or a Soroban CPU, memory or footprint budget.
- Deployments other than Stellar mainnet, and repository paths that are not deployable contracts: mock/, tests/, certora/, vendor/, scripts/, services/ and docs/. An issue there qualifies only when it reaches a production build.
- Web and application surfaces: the xoxno.com frontend, the REST API, the TypeScript SDK, the keeper and exporter services, and hosting, DNS, email or cloud infrastructure. This program is smart contract only.
- Governance parameter values as such, including listings, loan-to-value weights, liquidation thresholds, bonuses, caps, fees and feed selection. Logic that lets a parameter violate an invariant is in scope.
- Centralisation observations with no exploitable path. An owner or address gate is a source boundary, not a claim of multisig custody or a timelock.
- Scanner output, lint findings, missing events, fee optimisation, code style and documentation defects with no security consequence.

__Known design choices. Do not report these__

The behaviours below are deliberate, documented and covered by tests. Each one is recorded as a decision record in docs/explanation/decisions.md. A report that describes one of them as a vulnerability is closed as a non-issue unless it demonstrates a concrete invariant violation that the record does not already accept.

- Directed rounding (ADR-0003). Supply mints floor shares, withdrawal burns ceiling shares, borrowing mints ceiling debt and partial repayment burns floor debt. Single-unit rounding always favours the protocol. Only accumulated drift that breaks a stated accounting invariant is a finding.
- Supplier-index loss allocation (ADR-0012). Eligible bad debt is written down by reducing the affected market's supply index above a nonzero floor, so suppliers in that market bear the loss. A supplier who exits before the write-down avoids it, and a displayed claim is not a guarantee that the amount can be withdrawn.
- Gross-debt cleanup accounting (ADR-0021). Cleanup converts remaining account supply to protocol revenue and then socializes gross debt, without first netting supply against debt in the same market.
- Immutable spoke binding (ADR-0009). An account keeps its spoke for its whole lifetime. Governance can change listings and refresh applicable stored risk values, but cannot rebind an account to another risk regime.
- Central custody with separate market books (ADR-0002). One pool holds every token. The same token listed in several hubs keeps separate books while sharing one physical balance and one set of token risks.
- Credit measured receipts (ADR-0013). Credited amounts are the amounts actually received, not the amounts requested, and under-delivered liquidation repayment reduces the associated seizure. Direct donations do not rewrite market books.
- Fail-closed valuation (ADR-0005) and dual-source agreement (ADR-0004). A required price that is missing, stale, out of band or in disagreement aborts the operation. Where two sources are configured, one usable source never substitutes for a failed source.
- Liquidation share credit (ADR-0019). Liquidation may credit an authorized receiver in the same spoke instead of paying collateral out. The supply entry gate is deliberately bypassed for credited positions because value is moved rather than created, and the protocol fee is reclassified rather than minted.
- Zero-fee flash position (ADR-0020). flash_position creates debt with no origination fee, unlike multiply. It is an authorized borrowing strategy, not a free flash round trip, and returned debt is never automatically repaid.
- Literal asset-unit caps (ADR-0015). Caps are asset units converted at the applicable index. Exits do not release headroom, and same-spoke liquidation credit does not require new supply-cap headroom.
- Millisecond rates and chunked accrual (ADR-0016). Rates are RAY per millisecond and accrual is divided into bounded chunks, each using the preceding chunk's market state. Cadence dependence and bounded rounding error are expected consequences.
- Independent halt flags (ADR-0008) and the emergency ratchet (ADR-0007). Global pause preserves designated exit and recovery entrypoints, listing flags separately control entry, exit and seizure, and a sanity band may only be tightened.
- is_collateralizable is an entry gate only. Clearing the flag blocks new supply of that asset but deliberately does not strip collateral value from existing or credited positions, which is a soft wind-down. To remove borrowing power, governance sets the loan-to-value weight to zero.
- Account authority is the position NFT. The account id equals the NFT token id and the NFT owner controls the whole account. A registered delegate has complete economic control, including borrowing and withdrawing to an arbitrary address. This is the documented authority model.
- Full-close liquidation fallback. Once collateral is worth less than debt, no liquidation can raise the health factor, so the protocol falls back to a full close at the base bonus. The absence of a post-liquidation health-factor improvement guard is deliberate: such a guard would block liquidation of unrecoverable positions and let debt compound.
- Solvency and liquidity are separate. A healthy account that cannot borrow or withdraw because its market holds no available cash is behaving as designed.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
