# Audit Comp | Firelight

- Page: https://immunefi.com/bug-bounty/audit-comp-firelight/scope/
- Max bounty: $15,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: 2025-11-17T10:00:00.000Z

## Assets in scope (2)

- [smart_contract] https://github.com/firelight-protocol/firelight-core/blob/main/contracts/FirelightVault.sol — FirelightVault.sol - Upgradeable ERC4626-compatible vault -  [500]
- [smart_contract] https://github.com/firelight-protocol/firelight-core/blob/main/contracts/FirelightVaultStorage.sol — FirelightVaultStorage.sol - Storage layout for FirelightVault- [28]

## Asset notes

**Insight Reporting** 

Insight reports may be reported to this program and require a PoC. Insights are rewarded in accordance with [Immunefi’s Standardized Competition Reward Terms.](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms)

**Dispute Resolution**

If there is any dispute over bug reports between projects and security researchers, Immunefi has the final say on validity and severity based on the terms of this program.

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

**Build Commands, Test Commands, and How to Run Them**

Installation:
git clone https://github.com/firelight-protocol/firelight-core.git
cd firelight-core
npm install
Create your .env file using .env.sample as a reference.

Run tests:
npx hardhat test

Optional:
For faster test execution, comment out the forking configuration on line 29 of hardhat.config.js.

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope are valid.

**Code Freeze Assurance**

Code of the assets in scope is frozen while the program is live.

Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.

The project commits to keeping all info related to bug findings private until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

------------------

**Previous Audits**

Firelight’s completed audit reports can be found at https://firelight.finance/audit.pdf. Unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

**Public Disclosure of Known Issues**

Bug reports for publicly disclosed bugs are not eligible for a reward. 

Inflation attack: This is a known issue with ERC-4626 described at https://docs.openzeppelin.com/contracts/5.x/erc4626#security-concern-inflation-attack We'll take care of this at the time of deployment.

**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

-----------------------

**Where might Security Researchers confuse out-of-scope code to be in-scope?**
There should be no confusion. Only one smart contract and its storage contract are in scope.

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

No, this is not an upgrade of an existing system and will be a first-time deployment.

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

Overall security and correctness are especially important.


**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

The vault is ERC-4626 compliant and holds/transfers ERC-20 tokens. No ERC-721, ERC-777, or ERC-1155 tokens are supported.

**What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?**

None.
We do not use emergency actions as a basis to downgrade severity.

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

The role-based administrative addresses are considered trusted.These roles are intentionally authorized to modify configurations or perform emergency actions. Their intended permissions are not considered vulnerabilities.
This includes: DEPOSIT_LIMIT_UPDATE_ROLE, RESCUER_ROLE, BLOCKLIST_ROLE, PAUSE_ROLE,  PERIOD_CONFIGURATION_UPDATE_ROLE


**What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?**
None. 

**Which chains and/or networks will the code in scope be deployed to?**

Flare Network. https://flare-explorer.flare.network/

**What external dependencies are there?**
There are no external dependencies. The system does not rely on oracles, price feeds, or external protocol integrations.

**Are there any unusual points about your protocol that may confuse Security Researchers?**

We do not think so. The time-based period configuration may be slightly unusual, but the implementation is straightforward and self-explanatory in the code.

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

https://github.com/firelight-protocol/firelight-core/blob/main/README.md

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to Immunefi’s Standardized Competition Reward Terms and includes All Star Pool and Podium Pool reserved for All Star Program participants. 

Rewards are denominated in USD and distributed in USDC on Ethereum.

The reward pool is $15,000 for any bug found. That means that even if 1lLow severity bug is found, the whole reward pool is unlocked and has to be fully distributed between security researchers. 

If not a single bug is found (Insights do not count as bugs) the reward pool is $2,250 of Max SR Rewards.

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
