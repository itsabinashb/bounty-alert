# Mitigation Audit | Flare | FAssets

- Page: https://immunefi.com/bug-bounty/flare-fassets--mitigation-audit/scope/
- Max bounty: $25,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-09-25T10:00:00.000Z

## Assets in scope (9)

- [smart_contract] https://github.com/flare-foundation/fassets/commit/01190b0e4386714d4c2b968597fce5f35cf58047 — Fix of Report - 46265
- [smart_contract] https://github.com/flare-foundation/fassets/commit/03304ecf8110fd32f94620f111e2593f6969d573 — Fix of Report - 45514
- [smart_contract] https://github.com/flare-foundation/fassets/commit/29d4370abb61ca0e2df4d741245537a15cdf2e2e — Fix of Report - 45897
- [smart_contract] https://github.com/flare-foundation/fassets/commit/2abc918d3dec2ea6c4f34ca972a6eeb89b4ecafc — Fix of Report - 45478
- [smart_contract] https://github.com/flare-foundation/fassets/commit/59373cee12e6d2a9fa0a9cc8735bb486faa51b36 — Fix of Report - 45439
- [smart_contract] https://github.com/flare-foundation/fassets/commit/5f82ac58e9c74f58a927c66a0df50df25b67e60b — Fix of Report - 45904
- [smart_contract] https://github.com/flare-foundation/fassets/commit/7aa02b62285cd5313032103710c2e083b166bf60 — Fix of Report - 45533
- [smart_contract] https://github.com/flare-foundation/fassets/commit/7dd1ddd574989c44b3057ce426ff188bc69743d1 — Fix of Report - 46520
- [smart_contract] https://github.com/flare-foundation/fassets/commit/92e1e2bdc6e8f75f61cfd9f10ddb05df4a7c8c6b — Fix of Report - 45893

## Asset notes

**Proof of Concept (PoC) Requirements**: A runnable PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

__Asset Accuracy Assurance__

- Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

- Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Primacy of Impact vs Primacy of Rules__

- Flare adheres to the Primacy of Rules, which means that the whole Audit Competition & Mitigation Audit program is run strictly under the terms and conditions stated within this page.

__KYC Requirement__

- No KYC is required for the Flare FAssets Audit Competition & Mitigation Audit

__Eligibility Criteria__

- Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
   - On OFACs SDN list 
   - Official contributor, both past or present
   - Employees and/or individuals closely associated with the project 
   - Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

- Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
   - Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

- Immunefi may publish bug reports submitted to this Audit Competition and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

- When there is uncertainty about how feasible an attack is Immunefi will use our feasibility limitation standards to determine the severity of the report.

__Immunefi Standard Badge__

- By adhering to Immunefi’s best practice recommendations, Flare Network has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (17)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Temporary freezing of funds for at least 24 hour
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

**Build Commands, Test Commands, and How to Run Them**
- Instructions on how to start the project: https://github.com/flare-foundation/fassets?tab=readme-ov-file#getting-started
- The easiest way is to add code in unit tests because the functionality on which the project relates is mocked.
- You can look at https://github.com/flare-foundation/fassets/blob/main/test/integration/fasset-simulation/AttackScenarios.ts where researchers have submitted their reports.
- Information and some guides you can also find on Flare Dev Hub: https://dev.flare.network/fassets/overview

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

The FAssets system is able to support wrapped tokens for XRP, BTC and DOGE. However, the initial v1.1 deployment will only have XRP (FXRP) enabled and that will be the sole scope of this audit competition. Any attacks related to FBTC, FDOGE, or UTXO-based logic in general, are out of scope.

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

As a result of the Main Audit Competition, here are the changes: 

- Removed trailing fees
- Removed handshake
- Removed collateral pool topup functionality
- Simplified enter/exit logic in collateral pool, so that FAsset fees are transfered separately by payFAssetFeeDebt and withdrawPoolFees
- Each main operation in collateral pool now emits own event
- Removed special support for WNat as vault collateral
- All NAT transfers from asset manager (e.g. paying executor) are WNat deposits to avoid reenetrancy and DOS issues (the exception is returning overpaid fee to msg.sender, but that is strictly done at the end of methods)
- Removed token tracking in agent vault; instead tokens can be withdrawn from agent vault after destroy
- Bulk of the external code has been moved to the facets (previously the facets just delegated to the library methods). The libraries now only contain internal reusable code.
- Removed FTSOv1 support.
- Removed minUnderlyingBackingBIPS, now the backing must always be 100%.
- Removed waiting time for underlying withdrawal confirmation (it was supposed to solve an issue that was better solved with withdrawal id randomization)
- Instead of deleting storage structures at the end of lifetime, just mark them as deleted (for agents, collateral reservations, redemption requests)
- Removed EOA ownership proofs - they were obsoleted by EIP-7702 and we officially don't support smart contract chains now.
- Removed terminate and agent buyback functionality - replaced by allowing agents to transfer all their backing to the core vault when the FAsset is winding down.
- Refactored Agents library into several libraries.
- To keep the storage compatible with the deployed contracts on Songbird (to enable upgrade by diamond cut), the variables not needed anymore have remained, but we have prefixed them with __.
- ##Code organization
- Use custom errors in reverts instead of error strings.
- Major contracts grouped with related files in their own directories.
- No more '*' imports.

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

Those interacting with new Core Vault features.

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

We use only ERC20 for our FAsset implementation

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

governance, core vault multisig

**What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?**

governance (hard to exceed the privileges, as they can update the contracts)

**Which chains and/or networks will the code in scope be deployed to?**

Coston (testnet), Coston2 (testnet), Songbird, Flare

**What external dependencies are there?**

FDC (Flare Data Connector), FTSO-V2 (Flare Time Series Oracle)

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

- For concept-level understanding, visit the Flare Developer Hub https://dev.flare.network/fassets/overview 
- For technical details:
    - Refer to the inline code documentation directly in the repository.
    - As an example, you can explore the Redemption function implementation in RedemptionRequestsFacet.sol https://github.com/flare-labs-ltd/fassets/blob/main/contracts/assetManager/facets/RedemptionRequestsFacet.sol#L33

**Previous Audits**
- Flare Network’s completed audit reports can be found at https://dev.flare.network/support/audits/. Unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.
- Flare FAssets Mainnet Audit Competition Reports are available at https://reports.immunefi.com/flare-fassets

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of Reward Pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

Rewards are denominated in USD and distributed in **USDC** on **Ethereum**.

### Flat Rewards

**Mitigation Audit Rewards**: The reward pool is **$25,000 USD** if any bug is found.

If not a single bug is found (Insights do not count as bugs) the reward pool is **$3,750 USD**

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (4)

- Array of escrows always grows: the number of escrows created will be low (if it is more than one or two, we will increase the daily escrow amount). So the total number of escrows will not be huge, perhaps a few hundred. (https://reports.immunefi.com/flare-fassets/)
- Escrows finalized close to expiry time decouple the Core Vault internal accountancy: before escrows are released, the triggering bots will be shut down, and they will only be enabled after setEscrowsFinished is called. So there will be no instructions triggered between escrow finalization and the corresponding update on the core vault manager. (https://reports.immunefi.com/flare-fassets/)
- Triggering instructions might run out of gas: the size of the allowed destination addresses will be low (5-10). (https://reports.immunefi.com/flare-fassets/)
- Users are unprotected against missing or malformed vault redemption payments: in that case, we assume the core vault has full trust, and its redemptions don't have a time limit. Also, core-vault redeemers are special entities. (https://reports.immunefi.com/flare-fassets/)
