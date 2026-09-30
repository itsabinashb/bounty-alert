# Audit Comp | Belong

- Page: https://immunefi.com/bug-bounty/audit-comp-belong/scope/
- Max bounty: $30,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - medium, smart_contract - high, smart_contract - critical, smart_contract - low
- End date: 2025-10-29T15:00:00.000Z

## Assets in scope (25)

- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/nft/interface.cairo — interface.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/nft/nft.cairo — nft.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/nftfactory/interface.cairohttps://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/nftfactory/interface.cairo — interface.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/nftfactory/nftfactory.cairohttps://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/nftfactory/nftfactory.cairo — nftfactory.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/receiver/interface.cairo — interface.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/receiver/receiver.cairo — receiver.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/snip12/dynamic_price_hash.cairo — dynamic_price_hash.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/snip12/interfaces.cairo — interfaces.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/snip12/produce_hash.cairo — produce_hash.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/snip12/snip12.cairo — snip12.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/snip12/static_price_hash.cairo — static_price_hash.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/feat/cairo/src/snip12/u256_hash.cairo — u256_hash.cairo
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/Structures.sol — Structures.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/periphery/Escrow.sol — Escrow.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/periphery/RoyaltiesReceiverV2.sol — RoyaltiesReceiverV2.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/periphery/Staking.sol — Staking.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/periphery/VestingWalletExtended.sol — VestingWalletExtended.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/platform/BelongCheckIn.sol — BelongCheckIn.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/platform/Factory.sol — Factory.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/platform/extensions/ReferralSystemV2.sol — ReferralSystemV2.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/tokens/AccessToken.sol — AccessToken.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/tokens/CreditToken.sol — CreditToken.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/tokens/base/ERC1155Base.sol — ERC1155Base.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/utils/Helper.sol — Helper.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-belong/blob/main/contracts/v2/utils/SignatureVerifier.sol — SignatureVerifier.sol

## Asset notes

**Insight Reporting** 

Insight reports may be reported to this program and require a PoC. Insights are rewarded according to [Immunefi’s Standardized Competition Reward Terms.](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms)

**Dispute Resolution**

If there is any dispute over bug reports between projects and security researchers, Immunefi has final say on validity and severity based on the terms of this program.

**Responsible Publication Policy**

- Immunefi will publish bug reports, earnings, and a leaderboard for this Audit Competition.
- Security Researchers may publish their bug reports as well, but only after Immunefi has published the valid bug reports as part of the competition results.

**Eligibility Criteria**

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in an audit review of the code in scope (Such auditors may still participate in this program only if they receive project permission)

## Impacts in scope (21)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs for at least 24 hour
- [smart_contract] High: Temporary freezing of funds for at least 24 hour
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

**Build Commands, Test Commands, and How to Run Them**

https://github.com/belongnet/checkin-contracts/tree/main/docs/guides 

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope are valid.

**Code Freeze Assurance**

Code of the assets in scope is frozen while the program is live.

**Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.**

The project commits to keeping private all info related to bug findings until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

-----
**Previous Audits**

Belong’s completed audit reports can be found at https://hacken.io/audits/belong-net/. Unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

------

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

Smart contracts only from ./contracts/v2 should be audited. LONG.sol has been built by OZ Wizard.

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

Factory has been updated from the previous version, which stored token and royalties receiver codes within itself. Currently, Factory utilises a minimal proxy clone deployment.

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

- LONG.sol - ERC20
- CreditToken.sol - ERC1155
- AccessToken.sol - ERC721

**Which chains and/or networks will the code in scope be deployed to?**

BNB Smart Chain

**What external dependencies are there?**

- Solady library.
- Uniswap/Pancakeswap V3.

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

Documentation can be found in: ./docs/ folder.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program](https://immunefi.com/allstars/) participants. 

Rewards are denominated in USD and distributed in both USDC and $LONG token.

The reward pool is $30,000 USD if any bug is found. That means that even if 1 Low severity bug is found, the whole reward pool is unlocked and has to be fully distributed between security researchers. 

The reward pool consists of $7.5k USDC on ETH and $22.5k $LONG token. The latter will be distributed among the leaderboard winners post TGE on October 29th with a 1 month cliff.

If not a single bug is found (Insights do not count as bugs) the reward pool is $4,500 USD of Max SR Rewards.

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
