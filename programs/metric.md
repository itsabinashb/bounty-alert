# Metric

- Page: https://immunefi.com/bug-bounty/metric/scope/
- Max bounty: $500,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (4)

- [smart_contract] https://github.com/Metricxyz/oracle-contracts — Oracle and Price Provider Contracts
- [smart_contract] https://github.com/Metricxyz/periphery-contracts — Periphery Contracts that facilitate the protocol
- [smart_contract] https://github.com/Metricxyz/pool-contracts — Pool Contracts
- [smart_contract] https://www.metric.xyz — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (22)

- [smart_contract] Critical: An oracle accepts a price update without a valid Pyth or Chainlink signature, or a compressed-feed push from an unauthorized pusher
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Bypassing the admin fee caps or the price-provider timelock.
- [smart_contract] High: Permanent freezing of funds
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Swap on a Metric anchored price provider pool executes outside the band or beyond its configured staleness limit
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] High: Unauthorized use of protocol roles: factory owner, oracle ADMIN_ROLE, propAMM adapter admin
- [smart_contract] Medium: A configured stop-loss check is bypassed.
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Fees reach the wrong destination: protocol or admin fees go somewhere other than the configured receiver.
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Successful swap on a paused pool
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Medium: bypassing the deposit or swap allowlist extensions.
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Malicious Price Provider implementation that can lead to significant losses of funds for LPs

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$500,000, minReward=$50,000, primacy=primacy_of_impact, rewardCalculationPercentage=20, rewardModel=range
- [smart_contract] High: maxReward=$50,000, minReward=$10,000, primacy=primacy_of_impact, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$2,500, primacy=primacy_of_impact, rewardModel=range
- [smart_contract] Low: fixedReward=$1,000, primacy=primacy_of_impact, rewardModel=fixed

## Reward notes

Rewards for High and Medium smart contract vulnerabilities are 20% of the funds directly affected. Each amount is capped at its tier’s maximum and floored at its tier’s minimum.

Permanent freezing of funds critical is capped at 200 000$.

Malicious price provider implementations are out of scope. We still encourage research in this area: the team may, at its discretion, award individual valid findings hence why we added it to the scope as low.

## Out of scope (program-specific)

Additional Out of Scope Information

The following are out of scope and not eligible for rewards:

1. Trusted roles and configuration
- Issues requiring a malicious, compromised or careless trusted role: Factory Owner, Oracle ADMIN_ROLE (blacklist, integrators, approved factories, registration fee, withdrawEth), and the PriceProvider / AnchoredProvider factory admins.
- Pool Admin actions within their allowed bounds (admin fees up to the cap, timelocked price-provider changes, pausing their own pool, bin and extension settings). Only bypassing the caps or an honestly configured timelock is in scope, and only at Medium severity or higher.
- Pools created or configured with unreasonable or malicious parameters. Users are expected to do their own due diligence; pool risk tiers (red, unverified curator, unverified price provider) are informational.

2. Oracles and off-chain components
- Incorrect, manipulated or stale prices from oracle providers (Chainlink, Pyth, compressed or pushed oracles) or from off-chain pushers and signers. Oracle data is assumed correct and fresh.
- Pools halting because a feed is stale or down (FeedStalled, staleness checks, Chainlink deviation or sequencer checks). This is intended behaviour, not denial of service.
- Off-chain infrastructure: price pushers, quote and maker services (including protected execution lanes and pamm-quote), keepers, indexers, the API (api.metric.xyz), SDK, app, admin dashboard and docs.

3. Tokens and third-party code
- Non-standard ERC-20 tokens: fee-on-transfer, rebasing, tokens with transfer hooks (ERC-777), tokens with fewer than 6 or more than 18 decimals, tokens that revert on zero transfers. USDC and USDT are in scope; the effect of their issuers blocklisting an address is not.
- Price providers, sources and extensions written and deployed by third parties, and anything that depends on them.
- External protocols and routers (aggregators, other DEXes, routes through externalSwap / ExternalSwapExecutor). Losses caused by external routers or integrators, including insufficient gas limits, are out of scope.

4. Market and execution risk
- Front-running, sandwiching and other MEV within the user's slippage or deadline settings; gas griefing; block stuffing; reorgs; sequencer or builder behaviour.
- Liquidity-provider losses from normal market risk: adverse selection, unfavourable price-provider or spread settings, impermanent loss.
- Rounding dust or precision loss below the Medium threshold (0.01% and $10), unless it can be repeated to reach Medium or higher.

5. Already known or not deployed
- Issues listed in previous audits or known-issue documents, and any report sharing a root cause with them. https://github.com/Metricxyz/Known_issues for all known issues.
- Contracts not listed as in-scope assets, superseded or deprecated deployments, test files, mocks, scripts, deployment tooling and testnet deployments.
- Issues in code that is not deployed, or already fixed in the deployed version.

6. General exclusions
- Gas optimisations, code style, missing events, informational or best-practice findings, and centralisation concerns about trusted roles.
- Attacks requiring stolen private keys, phishing, social engineering or physical access; denial-of-service on websites or APIs; rate-limit or spam issues on off-chain services.
- Bugs in the underlying blockchain, the EVM, compilers or standard libraries (e.g. OpenZeppelin), unless Metric's code uses them incorrectly.

7. Severity and feasibility rules

- Critical requires at least $10,000 of funds directly at risk; otherwise the report is assessed as High at most.
- Attacks that require a user to interact with a pool, extension or price provider created by the attacker are downgraded by one severity level.
- Immunefi’s standard feasibility limitations apply, including Attack Investment Amount: if the capital required exceeds the potential gain, severity may be downgraded.
- Reports must include a runnable proof of concept on a local fork. Testing against mainnet or testnet deployments is prohibited.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (2)

- Audit contest results include a lot of issues that are known as well (https://audits.sherlock.xyz/contests/1279?p=3d1041a8897184d70afd42ef032bc5f0c5b5f0fe4670aed8e94e945834476ef0)
- This document + all issues mentioned int any of the audit reports (https://github.com/Metricxyz/Known_issues/tree/main/other)
