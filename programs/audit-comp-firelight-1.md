# Audit Comp | Firelight

- Page: https://immunefi.com/bug-bounty/audit-comp-firelight-1/scope/
- Max bounty: $20,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: 2026-08-25T10:00:00.000Z

## Assets in scope (14)

- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/CoverNFT.sol — Upgradeable ERC721 enumerable/pausable cover receipt NFT minted by the allocator.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/CoverOrderAllocator.sol — Cover order lifecycle, premium collection, off-chain matching Merkle commitments, settlement, CoverNFT minting, capacity configuration, market support, protocol concentration caps, and recommit/cancel controls.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/FirelightVault.sol — Upgradeable ERC4626-compatible vault with delayed withdrawals, deposits/mints, blocklist and rescue controls, pausing, historical checkpoints, incident gating, and payout execution. V2 upgrade implementation for the deployed legacy predeposit vault.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/FirelightVaultStorage.sol — V2 FirelightVault storage structs, role constants, and period configuration. Storage compatibility with the deployed legacy predeposit vault storage is part of the upgrade context.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/IncidentManager.sol — Incident creation, confirmation, assessment rounds, approval/rejection/cancel flows, FIFO incident ordering, payout waterfall, and payout receiver/oracle administration.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/VaultRewardDistributor.sol — Pulls vault assets from authorized distributors and forwards rewards/incentives to the vault with accounting events and vault checkpointing.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/interfaces/IAggregatorV3.sol — Chainlink AggregatorV3-style interface consumed by the FTSO adapter.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/interfaces/ICoverOrderAllocator.sol — Interface for the CoverOrderAllocator contract.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/interfaces/IFirelightVault.sol — Interface for the FirelightVault contract.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/interfaces/IIncidentManager.sol — Interface for the IncidentManager contract.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/lib/Checkpoints.sol — Local checkpoint lookup/push library used for historical vault accounting.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/lib/Decimals.sol — Decimal conversion helper.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/core/lib/PriceFeed.sol — Price feed freshness/positivity helper.
- [smart_contract] https://github.com/immunefi-team/audit-comp-firelight/blob/v1_audit_ready/contracts/oracle/FtsoChainlinkAdapter.sol — Flare FTSO v2 to Chainlink AggregatorV3-style adapter for live price reads.

## Asset notes

##Technical Walkthrough
https://drive.google.com/file/d/1b1AWKE-ZeML5VWdIzzNczY3s0Bd4MeJv/view

## Build, Test, and Run

Prerequisites: Node.js and npm.

Clone the repository and check out the audit branch:

```
git clone https://github.com/immunefi-team/audit-comp-firelight.git
cd audit-comp-firelight
git checkout v1_audit_ready
```

Install dependencies and run the tests:

```
npm install
npm test
```

No `.env` file is needed to run local tests; Hardhat uses its default accounts.

### Educational resources

- Official Firelight documentation: https://docs.firelight.finance/
- Phase 1 / Phase 2 overview: https://docs.firelight.finance/#phase-1-and-phase-2
- How Firelight works: https://docs.firelight.finance/introduction/how-firelight-works
- Vault architecture: https://docs.firelight.finance/core-concepts/vault-architecture
- Staking deposits and withdrawals: https://docs.firelight.finance/for-stakers/deployments-and-withdrawals
- Program-operator Cover Tokens: https://docs.firelight.finance/for-program-operators/cover-tokens
- Claims process: https://docs.firelight.finance/for-program-operators/claims-process
- Protocol architecture / on-chain components: https://docs.firelight.finance/protocol-architecture/on-chain-components
- Claims liquidation and payout waterfall: https://docs.firelight.finance/protocol-architecture/claims-liquidation

## Impacts in scope (23)

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
- [smart_contract] High: Temporary freezing of NFTs for at least 24 hours
- [smart_contract] High: Temporary freezing of funds for at least 24 hours
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of NFTs for at least 1 hour
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

## Program Assurances

### Asset Accuracy Assurance

Bugs found on assets incorrectly listed in scope are valid.

### Code Update Assurance

Duplicate submissions of bugs are valid until the relevant bug fix is public. Once a fix is public, the bug is out of scope and later submissions of it are invalid. Duplicate submissions of Insights are invalid.

The project commits to keeping all information about bug findings private until each fix is disclosed through the process described in the Bug Fix Policy. This includes bug findings found independently by the project or from concurrent private audits.

### Code Freeze Assurance

Code of the assets in scope is frozen while the program is live.

If a bug found during the competition requires an immediate fix, the bug will be considered a publicly known issue as soon as the fix is deployed. Submissions of the same bug after the fix is public are invalid, and a bypass of the fix is considered a new, valid bug.

Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.

The project commits to keeping private all information related to bug findings until this program is over. This means the project will not leak information about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

### Token standards

- ERC-20: the vault asset, premium tokens, and first-loss-buffer token are ERC-20 tokens.
- ERC-721: CoverNFT is an ERC-721 enumerable, pausable, upgradeable cover receipt NFT.

### Privileged actors

- Any bug report that requires a privileged role holder to act within the permissions explicitly granted to that role is out of scope, unless the report demonstrates that the role can exceed its intended permissions or bypass an intended protocol constraint.
- There are no actors whose involvement is out of scope when they exceed their attributed privileges. Reports where a privileged role, admin, or operator can exceed the privileges attributed to them remain in scope.

### Emergency actions and severity downgrades

Emergency actions may be used to fix or mitigate an issue, but they are not intended as an automatic reason to downgrade an otherwise valid report.

### Deployment

The Phase 1 vault proxy is deployed on Flare mainnet. The in-scope Phase 2 code is intended for deployment/upgrade on Flare mainnet.

Phase 1 vault proxy:
https://flare-explorer.flare.network/address/0x4C18Ff3C89632c3Dd62E796c0aFA5c07c4c1B2b3

### External dependencies

- An off-chain matching engine that reads pending cover orders, computes Merkle allocation commitments, submits allocation commitments, and settles matched cover orders.
- An off-chain premium conversion service that converts collected premiums into the vault asset and forwards rewards.
- Off-chain/manual payout distribution from the configured payout receiver in the MVP model.
- Flare FTSO v2, accessed via the Flare Contract Registry and read through `FtsoChainlinkAdapter`.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False

## Reward notes

Rewards are distributed among SRs according to [Immunefi's Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms), and include the All Star Pool and Podium Pool reserved for All Star Program participants. Rewards are denominated in USD and distributed in USDC on Ethereum.

- If any valid bug is found — even a single Low-severity bug — the full reward pool of **$20,000 USD** is unlocked and must be fully distributed among security researchers.
- If no security vulnerability is found (Insights do not count as bugs), the reward pool is **$3,000 USD**.

### Private Known Issues Reward Policy

Private known issues — known issues that were not publicly disclosed — are valid for a reward at their full severity and unlock the corresponding reward pool without any downgrade. Public known issues are invalid.

## Out of scope (program-specific)

### Public Disclosure of Known Issues

Bug reports for publicly disclosed bugs are not eligible for a reward. The following describe the intended, permissioned design of the Phase 2 MVP and are not eligible unless a report demonstrates a protocol-constraint bypass or unauthorized privilege escalation:

- Firelight Phase 2 is intentionally permissioned and operationally centralized for the MVP. Trusted operators and role holders create and settle cover orders, submit matching commitments, assess incidents, approve or reject assessments, configure risk parameters, operate the first-loss buffer, and execute or coordinate payouts. Reports requiring these trusted parties to act maliciously or incorrectly within their documented privileges are not eligible unless they demonstrate that the role can exceed its intended authority or bypass an intended protocol constraint.
- Cover purchasers (referred to as "Program Operators" in the official docs) do not author orders directly in the MVP. Cover orders are authored by the operator/curator, with the purchaser's on-chain consent limited to premium token approval.
- The first-loss-buffer token is treated as USD-pegged and valued through decimal conversion, without a token-specific on-chain price oracle. Reports based only on the first-loss buffer token depegging, without a protocol bug causing or mishandling that depeg, are not eligible.
- The first-loss buffer (address) is an external, unescrowed wallet. The protocol relies on that wallet remaining funded and having the required token approvals when approved claims are paid.
- If the underlying staked asset decreases in USD value, available capital and the Capital Adequacy Ratio decrease. Severe collateral drawdowns can reduce coverage capacity and may cause shortfalls or undercollateralization relative to outstanding cover obligations.
- Aggregate claims are not capped on-chain against total cover sold. The MVP relies on trusted incident/assessment roles and the approval process to prevent duplicate, excessive, or otherwise invalid claims.
- Incident assessment and payout execution are permissioned. Reports requiring trusted assessors, approvers, operators, or payout coordinators to make intentionally incorrect business decisions are not eligible unless they demonstrate a protocol-constraint bypass or unauthorized privilege escalation.
- Final distribution from the configured payout receiver to end beneficiaries may involve off-chain/manual operational processes in the MVP.

### Scope boundaries (out-of-scope code that may look in-scope)

- The legacy vault is not intended to be an in-scope asset. It is mentioned only as contextual upgrade reference for reviewing `FirelightVault.sol` and storage compatibility and new functionality.

The repository includes tests, local mocks, harness contracts, archived/reference contract copies, and third-party Flare/FAsset interfaces. Unless a file is explicitly listed in the Assets in Scope table, it is provided for context only and is not a competition target.

### Notes for researchers (unusual design points)

- Program operators do not author their own cover orders in the MVP. Orders are submitted by a permissioned Firelight operator role (named `curator` in the contracts) on the program operator's behalf. The program operator's only on-chain action is the premium token allowance.
- `FirelightVault` intentionally deviates from standard ERC4626 withdrawal semantics. Withdraw and redeem create delayed withdrawal requests; users later call `claimWithdraw`.
- Matching is off-chain, while settlement is verified on-chain through Merkle proofs.
- A settled cover order mints an ERC721 receipt NFT; the NFT is not itself the payout asset.
- Incident payouts are assessed/approved by permissioned roles and paid to a configured payout receiver; beneficiary distribution is off-chain/manual in the MVP.
- The first-loss buffer is an external wallet, not escrowed in the protocol.
- The first-loss buffer token is assumed to be USD-pegged and is valued by decimal conversion rather than a token-specific oracle.
- `CoverNFT` pausing affects settlement, because settlement mints NFTs.
- Deposits are blocked during active incidents for the relevant period.
- First-loss buffer payouts use the configured buffer balance first, up to the approved assessment loss. Insufficient allowance is treated as an operational misconfiguration and may cause payout execution to revert. The payout logic intentionally does not cap the first-loss buffer leg by allowance before calling `safeTransferFrom`; if the wallet is funded but allowance is insufficient, payout reverts as an operational misconfiguration rather than falling back to the vault.

## General Out of Scope and Rules

These impacts are out of scope for this program.

### All categories

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage.
- Impacts caused by attacks requiring access to leaked keys/credentials.
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist), except in cases where the contracts are intended to have no privileged access to functions that make the attack possible.
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code.
- Mentions of secrets, access tokens, API keys, private keys, etc. in GitHub will be considered out of scope without proof that they are in use in production.
- Best practice recommendations.
- Feature requests.
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program.

### Blockchain/DLT and smart contract specific

- Incorrect data supplied by third-party oracles (this does not exclude oracle manipulation / flash loan attacks).
- Impacts requiring basic economic and governance attacks (e.g., 51% attack).
- Lack of liquidity impacts.
- Impacts from Sybil attacks.
- Impacts involving centralization risks.

### Websites and apps

- Theoretical impacts without any proof or demonstration.
- Impacts involving attacks requiring physical access to the victim device.
- Impacts involving attacks requiring access to the local network of the victim.
- Reflected plain text injection (e.g., url parameters, path). This does not exclude reflected HTML injection with or without JavaScript, or persistent plain text injection.
- Any impacts involving self-XSS.
- Captcha bypass using OCR without impact demonstration.
- CSRF with no state-modifying security impact (e.g., logout CSRF).
- Impacts related to missing HTTP security headers (such as X-FRAME-OPTIONS) or cookie security flags (such as "httponly") without demonstration of impact.
- Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces.
- Impacts causing only the enumeration or confirmation of the existence of users or tenants.
- Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows.
- Lack of SSL/TLS best practices.
- Impacts that only require DDoS.
- UX and UI impacts that do not materially disrupt use of the platform.
- Impacts primarily caused by browser/plugin defects.
- Leakage of non-sensitive API keys (e.g., Etherscan, Infura, Alchemy).
- Any vulnerability exploit requiring browser bugs for exploitation (e.g., CSP bypass).
- SPF/DMARC misconfigured records.
- Missing HTTP headers without demonstrated impact.
- Automated scanner reports without demonstrated impact.
- UI/UX best practice recommendations.
- Non-future-proof NFT rendering.

### Prohibited activities

- Any testing on mainnet or public testnet deployed code; all testing should be done on local forks of either public testnet or mainnet.
- Any testing with pricing oracles or third-party smart contracts.
- Attempting phishing or other social engineering attacks against the project's employees and/or customers.
- Any testing with third-party systems and applications (e.g., browser extensions) as well as websites (e.g., SSO providers, advertising networks).
- Any denial-of-service attacks executed against project assets.
- Automated testing of services that generates significant amounts of traffic.
- Public disclosure of an unpatched vulnerability in an embargoed bounty.

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (3)

- Aggregate claims are not capped on-chain against total cover sold; the MVP relies on trusted incident/assessment roles and the approval process to prevent duplicate, excessive, or otherwise invalid claims. (https://immunefi.com/audit-competition/audit-comp-firelight-1/information/#:~:text=29%20July%202026-,Known%20Issues,-Reports%20covering%20previously)
- The first-loss buffer is an external, unescrowed wallet; the protocol relies on it remaining funded and holding the required token approvals when approved claims are paid. (https://immunefi.com/audit-competition/audit-comp-firelight-1/information/#:~:text=29%20July%202026-,Known%20Issues,-Reports%20covering%20previously)
- The first-loss-buffer token is treated as USD-pegged and valued through decimal conversion, without a token-specific on-chain price oracle. Depeg-only reports, absent a protocol bug causing or mishandling the depeg, are ineligible. (https://immunefi.com/audit-competition/audit-comp-firelight-1/information/#:~:text=29%20July%202026-,Known%20Issues,-Reports%20covering%20previously)
