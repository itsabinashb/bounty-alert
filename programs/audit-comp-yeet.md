# Audit Comp | Yeet

- Page: https://immunefi.com/bug-bounty/audit-comp-yeet/scope/
- Max bounty: $30,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - low, smart_contract - medium
- End date: 2025-03-25T14:00:00.000Z

## Assets in scope (10)

- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/INFTContract.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/Reward.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/RewardSettings.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/StakeV2.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/Yeet.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/YeetGameSettings.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/YeetToken.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/Yeetback.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/contracts/MoneyBrinter.sol
- [smart_contract] https://github.com/immunefi-team/audit-comp-yeet/blob/main/src/contracts/Zapper.sol

## Asset notes

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

No

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

ERC4626, ERC-20

**What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?**

If there are configurations that we can change that would mitigate affected areas. Pausing the game or changing game settings for example.

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

Any addresses controlled by the team—whether an EOA with elevated access or a multisig—would not typically be considered in scope for a bug report, as long as the team retains control over them.

**What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?**

Any addresses controlled by the team—whether an EOA with elevated access or a multisig—would not typically be considered in scope for a bug report, as long as the team retains control over them.

**Which chains and/or networks will the code in scope be deployed to?**

Berachain

**What external dependencies are there?**

docs.oogabooga.io, 
docs.pyth.network/entropy, 
https://www.beradrome.com/ 
https://kodiak.finance/

**Are there any unusual points about your protocol that may confuse Security Researchers?**

No

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

docs.yeetit.xyz

## Impacts in scope (15)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hours
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

forge build, forge test.

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope are valid.

**Code Freeze Assurance**

Code of the assets in scope is frozen while the program is live.

- Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.

- The project commits to keeping private all info related to bug findings until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the reward pool, pocRequired=True

## Reward notes

**Reward pool:**

If bugs are found → USD $30k (see [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms))

If not a single bug is found (Insights do not count as bugs) the reward pool is (15% of the max Reward Pool) → $4.5k.

Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.

Private known issues, meaning known issues that were not publicly disclosed, are valid and unlock the corresponding reward pool.

Yeet rewards are denominated in USD and distributed in USDC on Ethereum

**Proof of Concept (PoC) Requirements**

For this program, runnable PoC code is not required. Whitehats are instead required to write a step-by-step explanation of the PoC and impact
This explanation needs to be entered in the PoC section of the submission wizard to prevent the submission from being excluded by our OOS filter.

## Out of scope (program-specific)

- **The contract `NFTVesting.sol` is not included in the scope of this Audit Competition.**
- **Griefing via block stuffing on berachain to prevent users from Yeeting, forcing the game to end by blocking new transactions.**

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Pre-Audit Analysis (https://drive.google.com/file/d/1JK91TgoE_t62RI7lu66V_N517P3AkA9c/view)
