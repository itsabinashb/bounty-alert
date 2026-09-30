# Horizen

- Page: https://immunefi.com/bug-bounty/horizen/scope/
- Max bounty: $10,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: smart_contract - high, websites_and_applications - critical, websites_and_applications - high, smart_contract - critical
- End date: (none)

## Assets in scope (9)

- [smart_contract] https://github.com/HorizenOfficial/staker/blob/ab92502e9da98784dfe3bd3ef933d4e9345ff628/src/RewardAccumulator.sol — RewardAccumulator source at the staker main testnet merge commit (ab92502).
- [smart_contract] https://github.com/HorizenOfficial/staker/blob/ab92502e9da98784dfe3bd3ef933d4e9345ff628/src/ZenStaker.sol — ZenStaker source at the staker main testnet merge commit (ab92502).
- [smart_contract] https://horizen-testnet.explorer.caldera.xyz/address/0x06f5555fee73EDdc385b6d76FE00DB2D96ccDaE8 — RewardAccumulator (Horizen Testnet). Buffers ZEN rewards from multiple sources and forwards to the Staker on a fixed schedule.
- [smart_contract] https://horizen-testnet.explorer.caldera.xyz/address/0x6BF7CF29a8bcE11Aa62Cf593d165C244fA4d3E31 — ZenStaker - ZEN staking contract (Horizen Testnet, chain ID 2651420). Primary asset; severity assessed as if deployed on mainnet.
- [smart_contract] https://horizen.io — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://github.com/HorizenOfficial/staker-services — Staking dApp source (frontend/). Testnet merge commit a404746a693adca207c8c31f3e21fc3762fbb7b8.
- [websites_and_applications] https://github.com/HorizenOfficial/staker/tree/ab92502e9da98784dfe3bd3ef933d4e9345ff628/subgraphs — ZenStaker subgraph mapping code (indexed data rendered by the dApp). Subgraph hosting infrastructure (Goldsky) is out of scope.
- [websites_and_applications] https://horizen.io — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://staking-testnet.horizen.io/ — Official ZEN staking dApp, testnet deployment. Fully client-side static app (no backend); reads chain + Goldsky subgraph, writes are user-signed transactions.

## Asset notes

During Phase A (from 2026-07-21) the in-scope deployment is on Horizen Testnet (chain ID 2651420); severity is assessed as if the same code were on mainnet. 

The same code deploys to mainnet on 2026-07-27, when the mainnet contracts and the production site (staking.horizen.io) become the severity-defining assets and are added to scope. Contract source is pinned to staker commit ab92502e9da98784dfe3bd3ef933d4e9345ff628; the pin will be updated if contracts are redeployed. 

Testnet entries remain listed as the sanctioned environment for reading state and local forking. Upstream, unmodified ScopeLift/Tally Staker code paths already covered by the published audits (base Staker.sol, extensions, calculators, notifiers) are out of scope except where Horizen's ZenStaker / RewardAccumulator integration introduces a new issue.

## Impacts in scope (10)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.

## Impact notes

NFT-related and governance-voting impacts are not applicable to this program in Phase 1: there are no NFTs, and delegation surrogates are non-voting (ZenDelegationSurrogate), so governance-manipulation impacts cannot arise. Server-side web impacts do not apply to the staking frontend, which is a static export with no server runtime.

## Rewards

- [smart_contract] Critical: fixedReward=$10,000, maxReward=$10,000, minReward=$5,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: fixedReward=$3,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$3,000, otherImpactMaxReward=$0, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$1,000, rewardModel=fixed

## Reward notes

### Phase A (testnet, 2026-07-21 to 2026-07-27)

**Flat rewards $5000 for criticals**; funds-at-risk is meaningless on testnet, so severity is judged by the mainnet impact of the same code. 

### Phase B (mainnet, from 2026-07-27)

Smart-contract Critical is priced by funds at risk. Principal-affecting criticals (funds at risk = staked principal) pay 10% of funds directly affected, capped at $10,000, measured at submission time. A minimum reward of $5,000 is offered for criticals.

Reward-buffer-limited criticals (funds at risk bounded by the RewardAccumulator balance, at most about one 30-day window) pay a flat $3,000; a pure percentage would understate the severity of a bug in the accumulator, which never holds principal and is flushed on a fixed schedule. 

Non-critical tiers remain fixed as configured. 

KYC is required before payout: valid reporters must complete identity verification before a bounty is paid.

## Out of scope (program-specific)

RULES OF ENGAGEMENT - PoC EXECUTION ENVIRONMENT (local-only): All proof-of-concept code must be executed exclusively against a local environment - an Anvil/Foundry/Hardhat node, or a local fork of testnet or mainnet state. Broadcasting exploit or attack transactions to ANY public network (mainnet or testnet) is strictly prohibited: a public transaction is public disclosure of the exploit and can be replayed by anyone. Violating this voids reward eligibility and breaches the rules of engagement. Public networks may be read (state inspection, forking) but never written to with exploit payloads. For frontend findings, do not broadcast transactions to a public chain; run the dApp locally against a local chain (see the repo README) or limit the demonstration to client-side behavior with no on-chain writes. A vulnerability whose exploit has already been broadcast to any public network (by the reporter or anyone else) is treated as publicly disclosed and handled under the public-disclosure rules, not as a confidential submission.

REPORT QUALITY / ANTI-SPAM: Reports must demonstrate impact against the exact in-scope code (pinned commit) or deployed contracts. Reports are closed as invalid without further review if they: (a) describe code paths, functions, or behaviors that do not exist in the in-scope code; (b) re-report findings from the published audit reports or the documented known issues; (c) report generic framework CVEs without a working PoC against the deployed asset - note the staking frontend is a static export with NO server runtime, so server-side Next.js issues (middleware bypass, SSRF, RSC issues, image-optimization DoS) do not apply; or (d) are LLM-generated boilerplate without evidence the reporter executed the PoC. Tool-assisted research is welcome; the burden of demonstrating a real, reproducible impact is on the reporter.

GENERAL OUT OF SCOPE: The completed ZEN migration (ZENDBackupVault, EONBackupVault, migration tooling), finished 2025-07-23. Test code, deployment scripts, e2e tests, CI configuration. Vela and all vela-* repositories (in development, not production). Third-party infrastructure: Base, Caldera rollup infra (sequencer, bridge hub), LayerZero OFT contracts, Goldsky subgraph hosting, Cloudflare Pages, Stork oracle, CoinGecko API. Chain-level Horizen L3 / rollup issues (this is a staking-only program). The ZEN ERC-20 / OFT token contracts themselves (staking-only scope; may be added in a later revision). Subgraph hosting/infrastructure (Goldsky) and subgraph data-staleness or unavailability (the dApp shows a health banner by design; write paths never depend on the subgraph). Best-practice/informational findings without demonstrated impact; automated scanner output without validation. Attacks requiring compromised admin keys / trusted multisigs. Malicious clone/phishing sites are in scope TO REPORT (we want to know) and rewarded at our discretion, but not severity-rated as program vulnerabilities.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (8)

- Phase 1 configuration: bumping disabled (maxBumpTip=0), claim fees 0 and immutable (MAX_CLAIM_FEE=0), identity earning power (earning power = staked balance), non-voting delegation surrogates, and governance delegation not surfaced. Reports that assume a non-Phase-1 configuration are invalid. (https://github.com/HorizenOfficial/staker/blob/bc369be9acf7c76906cc837e4eabc9eada44be4d/src/ZenStaker.sol)
- RewardAccumulator open mode (whitelistEnabled = false). Anyone may contribute rewards and anyone may call sendRewardsToStaker() once the window elapses. The following consequences of this permissionless design are ACCEPTED and OUT OF SCOPE regardless of the impact a report selects (incl. "temporary freezing of funds", "permanent freezing", "reward DoS", "griefing", "bricking", "theft"): (a) Empty / zero-reward flush advancing the schedule — calling sendRewardsToStaker() while accumulatedRewards == 0 transfers nothing but still advances lastRewardTime by whole windows, so rewards funded later that window are delivered at the next boundary (<= one timeWindow = 30 days). Timing only: full delivery, principal unaffected, self-healing. (b) Sub-REWARD_DURATION ("dust") contribution reverting the flush — a total below REWARD_DURATION (2,592,000 wei) makes the inherited, audited Staker.notifyRewardAmount round the rate to zero and revert with Staker__InvalidRewardRate. NOT permanent and NOT theft: the revert is atomic (lastRewardTime does not advance), accumulatedRewards is monotonic, anyone can top the balance over the threshold and the next flush then distributes everything. Tokens only flow contributor -> accumulator -> staker -> stakers. In production both (a) and (b) are moreover unreachable by operational design: the next window's reward tranche is funded into the accumulator early in the current window and an off-chain keeper flushes the moment the window gate opens, so the accumulator always holds a full legitimate tranche at each boundary — never empty, and far above the dust threshold. Still IN scope (any whitelist setting): loss or incorrect attribution of principal or rewards, permanent denial of distribution via a DIFFERENT mechanism, over-extraction, or theft. (https://github.com/HorizenOfficial/staker/blob/main/src/RewardAccumulator.sol)
- Staking and claiming in the same block yields zero rewards by design (flash-stake prevention). A second claim in the same block or multicall returns zero instead of reverting. Both are intended behavior. (https://github.com/HorizenOfficial/staker/blob/bc369be9acf7c76906cc837e4eabc9eada44be4d/src/ZenStaker.sol)
- The audited base Staker.sol is unmodified in logic, storage, and write paths, except that the owner parameter of the StakeDeposited and StakeWithdrawn events is now indexed (see AUDIT_DELTA.md in the repo). This changes EVM log topic layout only; reports that the base 'differs from the audited upstream' based solely on this delta are invalid. (https://github.com/HorizenOfficial/staker/blob/bc369be9acf7c76906cc837e4eabc9eada44be4d/src/Staker.sol)
- While total earning power is zero, the reward-per-token accumulator does not advance; rewards attributable to such intervals are not distributed to any staker, are not rolled into subsequent reward periods, and remain undistributed in the contract balance. This is inherited, documented behavior of the audited Staker framework, made practically unreachable by the RewardAccumulator's scheduled release into a funded pool. (https://github.com/HorizenOfficial/staker/blob/bc369be9acf7c76906cc837e4eabc9eada44be4d/src/Staker.sol)
- ZenStaker admin and RewardAccumulator owner are Horizen Safe multisigs. Findings that require a malicious or compromised admin/owner are out of scope (standard trusted-role assumption). (https://github.com/HorizenOfficial/staker/blob/bc369be9acf7c76906cc837e4eabc9eada44be4d/src/ZenStaker.sol)
- alterDelegatee updates the deposit's delegatee and its surrogate assignment, but Phase 1 surrogates are non-voting (ZenDelegationSurrogate), so no governance power is conferred or movable. Reports that delegation does nothing, or that it enables governance manipulation, are invalid for Phase 1. (https://github.com/HorizenOfficial/staker/blob/bc369be9acf7c76906cc837e4eabc9eada44be4d/src/ZenStaker.sol)
- permitAndStake / permitAndStakeMore wrap the EIP-2612 permit call in try/catch. Production ZEN has no permit, so a failed permit does not itself revert: with no allowance the later transferFrom reverts (the gasless single-tx path is simply unavailable on a non-permit token); with a prior normal zen.approve allowance, staking succeeds even with dummy signature args. Both outcomes are expected. Reports that 'permit is ignored / silently swallowed' describe this documented, audited try/catch design. (https://github.com/HorizenOfficial/staker/blob/bc369be9acf7c76906cc837e4eabc9eada44be4d/src/ZenStaker.sol)
