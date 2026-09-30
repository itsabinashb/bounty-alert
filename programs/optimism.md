# Optimism

- Page: https://immunefi.com/bug-bounty/optimism/scope/
- Max bounty: $2,000,042
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications, Blockchain/DLT
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, blockchain_dlt - high, blockchain_dlt - critical, websites_and_applications - critical
- End date: (none)

## Assets in scope (36)

- [blockchain_dlt] https://github.com/ethereum-optimism/optimism/tree/develop/op-dispute-mon — op-dispute-mon (in scope for impacts listed in the smart contracts section)
- [blockchain_dlt] https://github.com/ethereum-optimism/optimism/tree/develop/op-node — op-node
- [blockchain_dlt] https://github.com/ethereum-optimism/optimism/tree/develop/rust/op-reth — op-reth
- [blockchain_dlt] https://immunefi.com — Primacy of Impact (primacy of impact)
- [smart_contract] https://etherscan.io/address/0x0f8EdFbDdD3c0256A80AD8C0F2560B1807873C9c — MIPS
- [smart_contract] https://etherscan.io/address/0x18DAc71c228D1C32c99489B7323d441E1175e443 — AnchorStateRegistry
- [smart_contract] https://etherscan.io/address/0x229047fed2591dbec1eF1118d64F7aF3dB9EB290 — SystemConfig
- [smart_contract] https://etherscan.io/address/0x25ace71c97B33Cc4729CF772ae268934F7ab5fA1 — L1CrossDomainMessenger
- [smart_contract] https://etherscan.io/address/0x4146DF64D83acB0DcB0c1a4884a16f090165e122 — FaultDisputeGame
- [smart_contract] https://etherscan.io/address/0x543bA4AADBAb8f9025686Bd03993043599c6fB04 — ProxyAdmin
- [smart_contract] https://etherscan.io/address/0x5a7749f83b81B301cAb5f48EB8516B986DAef23D — L1ERC721Bridge
- [smart_contract] https://etherscan.io/address/0x75505a97BD334E7BD3C476893285569C4136Fa0F — OptimismMintableERC20Factory
- [smart_contract] https://etherscan.io/address/0x99C9fc46f92E8a1c0deC1b1747d010903E884bE1 — L1StandardBridge
- [smart_contract] https://etherscan.io/address/0xD326E10B8186e90F4E2adc5c13a2d0C137ee8b34 — PreimageOracle
- [smart_contract] https://etherscan.io/address/0xE497B094d6DbB3D5E4CaAc9a14696D7572588d14 — DelayedWETH
- [smart_contract] https://etherscan.io/address/0xE9daD167EF4DE8812C1abD013Ac9570C616599A0 — PermissionedDisputeGame
- [smart_contract] https://etherscan.io/address/0xbEb5Fc579115071764c7423A4f12eDde41f106Ed — OptimismPortal
- [smart_contract] https://etherscan.io/address/0xdE1FCfB0851916CA5101820A69b13a4E276bd81F — AddressManager
- [smart_contract] https://etherscan.io/address/0xdfe97868233d1aa22e815a266982f2cf17685a27 — L2OutputOracle
- [smart_contract] https://etherscan.io/address/0xe2F826324b2faf99E513D16D266c3F80aE87832B — OptimismPortal Implementation
- [smart_contract] https://etherscan.io/address/0xe5965Ab5962eDc7477C8520243A95517CD252fA9 — DisputeGameFactory
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [smart_contract] https://optimistic.etherscan.io/address/0xb5CB7a05DD1311195982A26DFC8222477f9D8179 — PolicyEngineStaking
- [websites_and_applications] http://gateway.optimism.io/ — Optimism's Gateway
- [websites_and_applications] http://jobs.optimism.io/ — Optimism's Careers page
- [websites_and_applications] https://app.optimism.io/ — Optimism's App
- [websites_and_applications] https://blog.oplabs.co/ — Main OP Labs blog
- [websites_and_applications] https://community.optimism.io/ — Optimism's Community page
- [websites_and_applications] https://console.optimism.io/ — Optimism's Console
- [websites_and_applications] https://dapp-console-api.optimism.io — Optimism's Console API
- [websites_and_applications] https://docs.optimism.io/ — Optimism's Docs
- [websites_and_applications] https://enterprise.optimism.io/ — OP Enterprise Dashboard
- [websites_and_applications] https://ope-dashboard-api.optimism.io/ — OP Enterprise Dashboard API
- [websites_and_applications] https://specs.optimism.io/ — Optimism's Specs
- [websites_and_applications] https://www.oplabs.co/ — Main OP Labs website
- [websites_and_applications] https://www.optimism.io/ — Main Optimism website

## Asset notes

**Whenever the asset is a smart contract proxy, its implementation is also in scope.**

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

## Impacts in scope (29)

- [blockchain_dlt] Critical: Direct loss of funds, not including proposer/challenger bonds or fee vaults
- [blockchain_dlt] High: Freezing of funds (fix requires L2 hardfork)
- [blockchain_dlt] High: Network not being able to confirm any new transactions, including deposits (Total network shutdown)
- [blockchain_dlt] Medium: Direct theft or permanent loss of fee vault funds (excluding missed revenue, unrealized yield, or failure to collect fees from pending transactions)
- [blockchain_dlt] Medium: Network not being able to confirm new transactions on L2, while forced-inclusion via L1 is still possible
- [smart_contract] Critical: Loss of user funds by direct theft, not including proposer/challenger bonds or fee vaults
- [smart_contract] Critical: Permanent freezing of funds, not including proposer/challenger bonds or fee vaults
- [smart_contract] Critical: Protocol insolvency, not including proposer/challenger bonds or fee vaults
- [smart_contract] High: Incorrectly proven withdrawal other than by incorrectly resolved dispute game, mitigated by a delay
- [smart_contract] High: Incorrectly resolved dispute game, not detected by op-dispute-mon, allows proving invalid withdrawal
- [smart_contract] High: Temporary freezing of funds, not including proposer/challenger bonds or fee vaults (e.g. recoverable via an upgrade)
- [smart_contract] Medium: Direct theft or permanent loss of fee vault funds (excluding missed revenue, unrealized yield, or failure to collect fees from pending transactions)
- [smart_contract] Medium: Incorrectly initiated dispute game bond withdrawal other than by incorrectly resolved dispute game, mitigated by a delay
- [smart_contract] Medium: Incorrectly resolved dispute game, detected by op-dispute-mon, excluding bugs in off-chain components
- [smart_contract] Medium: Incorrectly resolved dispute game, not detected by op-dispute-mon, does not allow proving invalid withdrawal
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as server configuration, credentials, or source code (excluding production user or tenant data)
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking or modifying authenticated actions on behalf of other users, where the action results in direct theft of funds or execution of an unauthorized onchain transaction
- [websites_and_applications] Critical: Unauthorized access to, modification of, or destruction of production user or tenant data, where a single exploitation affects multiple users or tenants, as distinct from an attack that must be repeated for each additional victim
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] High: Taking down the application/website
- [websites_and_applications] Medium: Taking or modifying authenticated actions on behalf of other users, where the action does not result in any impact listed at critical severity
- [websites_and_applications] Medium: Unauthorized access to, modification of, or destruction of production user or tenant data, where a single exploitation affects one user or tenant

## Impact notes

(none)

## Rewards

- [blockchain_dlt] Critical: maxReward=$2,000,042, rewardCalculationPercentage=10, rewardModel=up_to
- [blockchain_dlt] High: maxReward=$50,000, minReward=$15,000, rewardModel=range
- [blockchain_dlt] Medium: maxReward=$15,000, minReward=$1,000, rewardModel=range
- [smart_contract] Critical: maxReward=$2,000,042, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: maxReward=$50,000, minReward=$15,000, rewardModel=range
- [smart_contract] Medium: maxReward=$15,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Critical: maxReward=$50,000, minReward=$5,000, otherImpactMaxReward=$0, primacy=primacy_of_rules, rewardModel=range
- [websites_and_applications] High: maxReward=$5,000, minReward=$500, primacy=primacy_of_rules, rewardModel=range
- [websites_and_applications] Medium: maxReward=$500, minReward=$50, primacy=primacy_of_rules, rewardModel=range

## Reward notes

__Rewards by Threat Level__:

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

For KYC, OptimismPBC will request a W-9 if you reside in the US or a W-8 if you reside outside the US.

Critical vulnerabilities are further capped at 10% of economic damage, with the main consideration being the funds affected in addition to PR and brand considerations, at the discretion of the team.

For web application reports, the sensitivity of the data involved determines the position within the reward range. Disclosure of personal information or confidential customer organization data is awarded towards the top of the range.

For testing any exploits involving cross-domain transactions, we recommend working with our [dockerized services](https://github.com/ethereum-optimism/optimism/blob/6f8e432506a5f4ba094f091b22a0bb6acc53fdac/ops/README.md) and modifying our [integration tests](https://github.com/ethereum-optimism/optimism/blob/6f8e432506a5f4ba094f091b22a0bb6acc53fdac/integration-tests/test/bridged-tokens.spec.ts)

__Governance Proposals:__

In addition to the above assets listed, the calldata and code for the latest Protocol Upgrade Proposals (not for Governor Upgrade proposals, or proposal previews) is also in scope. This must be an official governance proposal, meaning it has either (1) moved to onchain vote appearing on vote.optimism.io, or (2) has been posted by someone from OP Labs or the Optimism Foundation, or (3) a comment has been left by someone from OP Labs or the Optimism Foundation indicating it's eligible for the bounty. The latest in-flight governance proposal can be found at https://gov.optimism.io/c/88-category/technical-proposals/47.

## Out of scope (program-specific)

__Chains__:
* When assessing impact for a bug, it will be primarily assessed against the impact it has on the following live chains: OP, Ink, Soneium, and Unichain. Each chain is identified by their entries in the superchain-registry (https://github.com/ethereum-optimism/superchain-registry/).
* A feature actively in use on at least one of these chains, or planned to be in use according to a governance proposal, is eligible for the highest tier impacts. A feature not actively in use on these chains will have its impact downgraded by one level.

The following are considered out-of-scope for the bug bounty:

__Blockchain / DLT__:
- Vulnerabilities requiring the user to have publicly exposed an API, such as JSON-RPC or the Beacon API
- Vulnerabilities requiring the chain operator to violate recommended best practices as described on our docs website, for example around network topology, proxy configuration and so on. See here https://docs.optimism.io/chain-operators/reference/architecture#network-design-example
- The Alt-DA feature of op-node and op-batcher.
- All execution layer clients which have reached end-of-service (e.g. op-geth).
- op-reth depends on several crates sourced from https://github.com/paradigmxyz/reth/. Issues which are responsibly disclosed to the upstream reth team or the Ethereum Foundation Bug Bounty Program (https://bbp-form.ethereum.org/) cannot be "replayed" against Optimism’s bug bounty program if the vulnerability has already been made public. If the vulnerability is disclosed to Optimism at the same time as upstream, the vulnerability is eligible for the bug bounty program.
 - All currently known issues with devp2p here: [https://github.com/ethereum/devp2p/blob/master/rlpx.md#known-issues-in-the-current-version](https://github.com/ethereum/devp2p/blob/master/rlpx.md#known-issues-in-the-current-version)
- There are scenarios where, if an attacker can predict an L1 reorg, they could exploit it to reorder dispute game transactions in a way that causes the honest challenger to respond incorrectly and therefore lose its bond — although the dispute game itself will still resolve correctly.

__Smart Contracts__:
- Vulnerabilities in the implementation of ‘custom token bridges’ which are written by third parties for bridging tokens to their network
- Bugs in op-challenger or other off-chain components that result in "Incorrectly resolved dispute game, detected by op-dispute-mon".
- Proof of whale based attacks on Fault Proofs.
- There appears to be an obvious bug which would allow an attacker to withdraw a fake ERC20 token from L2 in exchange for a real ERC20 (such as WBTC) token on L1. There is no check in the L2StandardBridge, however the withdrawal is prevented from finalizing by a check in the L1StandardBridge. Naturally if you do find a way to circumvent our protections, then we would reward you.
- A bug in ResolvedDelegateProxy.sol which could result in a storage slot key collision overwriting the address of the implementation. This bug is dependent on the layout of the implementation contract, and Optimism is not affected.
- There is an edge case in which ETH deposited to the OptimismPortal by a contract can be irrecoverably stranded:
  - When a deposit transaction fails to execute, the sender’s account balance is still credited with the mint value. However, if the deposit’s L1 sender is a contract, the tx.origin on L2 will be aliased, and this aliased address will receive the minted on L2. In general the contract on L1 will not be able to recover these funds. We have documented this risk and encourage users to take advantage of our CrossDomainMessenger contracts which provide additional safety measures.
- Sending cross-chain messages with very large amounts of data, or very specific amounts of gas can open up griefing attacks causing the sender’s funds to be stuck and requiring an upgrade to release them.
- Deposit transactions can be griefed at a cost to the attacker, by filling up the MAX_RESOURCE_LIMIT. This issue is mitigated by PR 5064, which does not completely resolve the issue but does increase the cost of a sustained griefing attack. A more complete fix will require architectural changes.
- There are various ‘foot guns’ in the bridge which may arise from misconfiguration of a token. To minimize complexity our bridge design does not try to prevent all forms of developer and user error. Examples of such foot guns include:
  - Having both (or neither of) the local and remote tokens be OptimismMintable.
  - Tokens which dynamically alter the amount of a token held by an account, such as fee-on-transfer and rebasing tokens.

__Web & App__:
- explorer.optimism.io
- testnet-explorer.optimism.io
- retrofunding.optimism.io
- public-grafana.optimism.io
- discord.optimism.io
- kyc.optimism.io
- kyb.optimism.io
- raas.optimism.io
- contribute.optimism.io
- superfest.optimism.io
- welovetheart.optimism.io
- support.enterprise.optimism.io
- login.enterprise.optimism.io, the Auth0-hosted login page for enterprise.optimism.io. The page itself is operated by Auth0 and is out of scope. Optimism's own Auth0 tenant configuration remains in scope, including allowed callback URLs, allowed web origins, connection settings, actions and rules, and any custom login page template, as does any vulnerability that results in unauthorized access to enterprise.optimism.io.
- Abuse of testnet faucet allocations on console.optimism.io, including bypassing or spoofing drip eligibility criteria. Testnet funds have no market value, so this is not treated as theft of user funds. Genuine authentication flaws in the faucet's identity flow remain in scope at the applicable severity.


- Additionally, any other asset belonging to Optimism but not under Optimism’s control will also be out of scope.

__The following domains, operated by Agora__:
- vote.optimism.io
- atlas.optimism.io

*Security researchers who discover vulnerabilities on these domains are encouraged to report them directly to Agora at security@voteagora.com. However, if a vulnerability on these domains leads to a direct financial impact on the OP Stack or the Optimism protocol itself, the impact remains in scope under the Primacy of Impact and should be submitted through this bug bounty program.*

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (10)

- A bug in ResolvedDelegateProxy.sol that could cause a storage-slot key collision overwriting the implementation address. The bug depends on the implementation contract's storage layout; Optimism is not affected. (https://immunefi.com/bug-bounty/optimism/scope/#top:~:text=The%20following%20are%20considered%20out%2Dof%2Dscope%20for%20the%20bug%20bounty%3A)
- All currently known issues with devp2p, as documented in the upstream list are considered known and ineligible for a reward. (https://github.com/ethereum/devp2p/blob/master/rlpx.md#known-issues-in-the-current-version)
- Bugs in op-challenger that result in an "Incorrectly resolved dispute game, detected by op-dispute-mon" — these are considered known due to the existing ability to detect and resolve them via op-dispute-mon. (https://immunefi.com/bug-bounty/optimism/scope/#top:~:text=The%20following%20are%20considered%20out%2Dof%2Dscope%20for%20the%20bug%20bounty%3A)
- Deposit transactions can be griefed at a cost to the attacker by filling up the MAX_RESOURCE_LIMIT. Mitigated (but not fully resolved) by PR 5064, which increases the cost of a sustained griefing attack; a complete fix requires architectural changes. (https://immunefi.com/bug-bounty/optimism/scope/#top:~:text=The%20following%20are%20considered%20out%2Dof%2Dscope%20for%20the%20bug%20bounty%3A)
- Edge case where ETH deposited to the OptimismPortal by a contract can be irrecoverably stranded — a failed deposit transaction still credits the sender's account with the mint value, but if the L1 sender is a contract, the L2 tx.origin is aliased and the minted ETH is sent to the aliased address, which generally cannot recover it. Documented; users are encouraged to use the CrossDomainMessenger contracts. (https://immunefi.com/bug-bounty/optimism/scope/#top:~:text=The%20following%20are%20considered%20out%2Dof%2Dscope%20for%20the%20bug%20bounty%3A)
- Fake ERC-20 withdrawal via L2StandardBridge — there is no check in L2StandardBridge preventing an attacker from withdrawing a fake ERC-20 token from L2 in exchange for a real ERC-20 (e.g. WBTC) on L1; the withdrawal is currently blocked from finalizing by a check in L1StandardBridge. (Circumventing the L1 protection would be eligible for a reward.) (https://immunefi.com/bug-bounty/optimism/scope/#top:~:text=The%20following%20are%20considered%20out%2Dof%2Dscope%20for%20the%20bug%20bounty%3A)
- Missing zlib error/header validation in kona's channel decompressor leads to cross-client fault-proof divergence (https://bugs.immunefi.com/magnus/855/projects/355/reports/84201)
- Sending cross-chain messages with very large amounts of data, or very specific amounts of gas, can open griefing attacks that cause the sender's funds to be stuck and require an upgrade to release them. (https://immunefi.com/bug-bounty/optimism/scope/#top:~:text=The%20following%20are%20considered%20out%2Dof%2Dscope%20for%20the%20bug%20bounty%3A)
- There are scenarios where, if an attacker can predict an L1 reorg, they could exploit it to reorder dispute game transactions in a way that causes the honest challenger to respond incorrectly and therefore lose its bond — although the dispute game itself will still resolve correctly. (https://immunefi.com/bug-bounty/optimism/scope/#top:~:text=The%20following%20are%20considered%20out%2Dof%2Dscope%20for%20the%20bug%20bounty%3A)
- Various bridge "foot guns" arising from token misconfiguration, which the bridge intentionally does not try to prevent — for example: having both (or neither) of the local and remote tokens be OptimismMintable; or tokens that dynamically alter balances, such as fee-on-transfer and rebasing tokens. (https://immunefi.com/bug-bounty/optimism/scope/#top:~:text=The%20following%20are%20considered%20out%2Dof%2Dscope%20for%20the%20bug%20bounty%3A)
