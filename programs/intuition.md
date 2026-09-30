# Intuition

- Page: https://immunefi.com/bug-bounty/intuition/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: (none)

## Assets in scope (16)

- [smart_contract] https://basescan.org/address/0x6cd905dF2Ed214b22e0d48FF17CD4200C1C6d8A3 — Trust (TRUST token) - Base Mainnet
- [smart_contract] https://basescan.org/address/0x7745bDEe668501E5eeF7e9605C746f9cDfb60667 — BaseEmissionsController - Base Mainnet
- [smart_contract] https://basescan.org/address/0xE485D9a5Dc39774b7A80864B625969Cf9d93E5D7 — TrustSwapAndBridgeRouter - Base Mainnet
- [smart_contract] https://basescan.org/address/0xb1ce9Ac324B5C3928736Ec33b5Fd741cb04a2F2d — EmissionsAutomationAdapter - Base Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0x23afF95153aa88D28B9B97Ba97629E05D5fD335d — OffsetProgressiveCurve (proxy) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0x33827373a7D1c7C78a01094071C2f6CE74253B9B — AtomWalletFactory (proxy) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0x635bBD1367B66E7B16a21D6E5A63C812fFC00617 — TrustBonding (proxy) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0x6E35cF57A41fA15eA0EaE9C33e751b01A784Fe7e — MultiVault (proxy) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0x73B8819f9b157BE42172E3866fB0Ba0d5fA0A5c6 — SatelliteEmissionsController (proxy) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0x81cFb09cb44f7184Ad934C09F82000701A4bF672 — WrappedTrust (WTRUST) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0x98C9BCecf318d0D1409Bf81Ea3551b629fAEC165 — AtomWarden (proxy) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0xC23cD55CF924b3FE4b97deAA0EAF222a5082A1FF — AtomWalletBeacon - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0xbCb1526A8de4a155e4dE003361b122eDe2f22908 — AtomWallet implementation (logic behind AtomWalletBeacon) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0xc3eFD5471dc63d74639725f381f9686e3F264366 — LinearCurve (proxy) - Intuition Mainnet
- [smart_contract] https://explorer.intuition.systems/address/0xd0E488Fb32130232527eedEB72f8cE2BFC0F9930 — BondingCurveRegistry (proxy) - Intuition Mainnet
- [smart_contract] https://intuition.systems — Primacy of Impact (primacy of impact)

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

- [smart_contract] Critical: maxReward=$100,000, minReward=$5,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$5,000, minReward=$2,500, rewardModel=range
- [smart_contract] Medium: maxReward=$2,500, minReward=$1,000, rewardModel=range
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are processed via USDC on the Ethereum network.

## Out of scope (program-specific)

The following are out of scope for this program.

**Accepted protocol design & privileged roles**

- Actions taken by trusted roles within their documented powers: contract upgrades and parameter changes executed through the Upgrades / Parameters TimelockControllers and the governing multisig — pausing, upgrading, changing fees within configured caps, registering bonding curves, and setting the AtomWarden.
- Protocol fees accruing to the configured FeeProxy recipient by design.
- Bonding-curve rounding that favors the protocol and yields only dust-level differences with no profitable, repeatable extraction.
- First-depositor or share-inflation scenarios that do not overcome the protocol's initial-share-price and minimum-deposit mitigations.
- Reports premised on non-standard behavior of the TRUST token itself (fee-on-transfer, rebasing); TRUST is a standard ERC-20.

**Execution environment — single-sequencer networks**

- Both Base Mainnet and the Intuition Network are operated by a single centralized sequencer with no public mempool: pending transactions are not publicly gossiped and reach the sequencer only via RPC, and are ordered first-come-first-served without exposure to third-party reordering. Any finding whose exploitation depends on public-mempool access, transaction reordering, or MEV extraction — front-running, back-running, or sandwiching by other users or searchers — is out of scope on both networks, because that adversarial environment does not exist under the current sequencing model. User-configurable slippage bounds (min-shares / min-assets) remain the supported protection, and only defeating those bounds qualifies.

**Cross-chain & infrastructure**

- Cross-chain message latency, sequencer downtime, and reorg behavior inherent to the Intuition Network, the Caldera MetaLayer / Hyperlane bridge, and the Base settlement layer; only Intuition's own dispatcher and controller accounting logic is in scope.
- ERC-4337 EntryPoint, bundler, and paymaster behavior; only the AtomWallet / AtomWalletFactory / AtomWarden validation logic is in scope.
- Behavior of external systems the periphery integrates with — Aerodrome / Uniswap v3 routers, MetaLayer / Hyperlane, and Chainlink Automation — except where Intuition's own integration logic is at fault.
- Governance, admin, and proxy infrastructure: the TimelockControllers, all ProxyAdmin contracts, and the multisig signers.
- Shared third-party infrastructure deployed alongside the protocol: Multicall3, the ERC-4337 EntryPoint, and the SafeSingletonFactory.

**Excluded assets**

- Contracts not deployed to mainnet or not listed as in-scope assets.
- All testnet deployments (Base Sepolia, Intuition Sepolia).

**Known issues & prior audits**

- Any vulnerability already reported, publicly known, or already fixed in an unreleased branch.
- Findings from the protocol's public security audits, including the September 2025 audits by Consensys Diligence and the Code4rena April 2026 competitive audit.

**Standard exclusions**

- Attacks requiring leaked/compromised privileged keys, or control of a trusted role or governance majority.
- Generic economic or governance attacks (e.g. 51% attacks).
- Best-practice, informational, gas-optimization, missing-event, and NatSpec findings without a demonstrated impact.
- Automated scanner output without a working proof of concept.
- Sybil attacks, spam, and volumetric / DDoS attacks.
- Issues requiring social engineering, phishing, or physical attacks, or targeting Intuition employees, infrastructure, or off-chain services.
- Testing against public mainnet or testnet (use a local fork).
- Frontend, website, or UX issues with no contract-level fund or accounting impact.

*The assessment of the extent of any potential indirect economic damage, defined as damage other than that evidenced by a PoC that showcases the direct exploitation of the vulnerability leading to impact, is at the full discretion of the project.*

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
