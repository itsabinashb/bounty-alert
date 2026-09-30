# Audit Comp | Vechain | Stargate Hayabusa

- Page: https://immunefi.com/bug-bounty/audit-comp-vechain-stargate-hayabusa/scope/
- Max bounty: $40,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-11-24T10:00:00.000Z

## Assets in scope (11)

- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/Stargate.sol — Stargate.sol - Entrypoint to the protocol - 640 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/StargateNFT.sol — StargateNFT/StargateNFT.sol - ERC721 with extra functionality - 373 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/libraries/Clock.sol — StargateNFT/libraries/Clock.sol - Library for handling time - 22 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/libraries/DataTypes.sol — StargateNFT/libraries/DataTypes.sol - Types used across the project - 79 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/libraries/Errors.sol — StargateNFT/libraries/Errors.sol - Errors used in StargateNFT - 37 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/libraries/Levels.sol — StargateNFT/libraries/Levels.sol - Library that handles NFT levels - 237 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/libraries/MintingLogic.sol — StargateNFT/libraries/MintingLogic.sol - Library that takes care of minting, burning and migrating NFTs - 177 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/libraries/Settings.sol — StargateNFT/libraries/Settings.sol - NFT settings - 13 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/libraries/Token.sol — StargateNFT/libraries/Token.sol - Handles token maturity and getters - 141 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateNFT/libraries/TokenManager.sol — StargateNFT/libraries/TokenManager.sol - Library for handling Token Managers - 190 lines
- [smart_contract] https://github.com/immunefi-team/audit-comp-vechain-stargate-hayabusa/tree/main/packages/contracts/contracts/StargateProxy.sol — StargateProxy - Proxy for upgradeability - 11 lines

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

## Impacts in scope (16)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
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

**VeChain is running an audit in parallel. However, submitted reports depicting the same issues raised in the audit will be confirmed.**

------------------

**Build Commands, Test Commands, and How to Run Them**

The repo is a monorepo. Every command is in the readme. The most relevant ones:
- Build Contracts: yarn contracts:compile
- Unit Tests: yarn contracts:test:unit
- Integration Tests: yarn contracts:test:integration
- Coverage: yarn contracts:test:unit:coverage
- Deploy locally: yarn:contracts:deploy
- Deploy on other networks: yarn:contracts:deploy:{network}
- Spin a solo network locally: make solo-up

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope are valid.

**Code Freeze Assurance**

Code of the assets in scope is frozen while the program is live.

Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.

The project commits to keeping private all info related to bug findings until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

--------------------

**Previous Audits**

VeChain’s completed audit reports can be found at [https://docs.stargate.vechain.org/hayabusa/for-developers/contracts](https://docs.stargate.vechain.org/hayabusa/for-developers/contracts). Unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

**Public Disclosure of Known Issues**

Bug reports for publicly disclosed bugs are not eligible for a reward. 

- There are some functions that can run out of gas due to excessive looping, most of them are getters so we are not really worried about them. In the cases there are not getters we implemented mechanisms to avoid running out of gas like in the claimRewards function.
- There is a style choice in the _burnCallback and _safeMintCallback to precede the functions with an underscore even though they are external. This functions can only be called by the own StargateNFT contract and we want to discourage the usage of them from external developers.
We are not checking address zero when granting or revoking roles
- The boostOnBehalfOf function uses an arbitrary _sender parameter instead of msg.sender, which deviates from standard patterns but is intentional. The Stargate contract calls this function during stakeAndDelegate flows. Since msg.sender would be the Stargate contract (no VTHO), _sender specifies which user's VTHO to use. This is protected by the onlyStargate modifier ensuring only the Stargate contract can set an arbitrary _sender
- There can be breaks of the check-effects pattern in some functions but they are using the nonReentrant modifier
- We can assume the IProtocolStaker interface is correct

**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

-------------------------

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

Only Solidity is in-scope, external tools like the scripts written in Typescript are out of scope.
Also the project contains a `deprecated` folder with the previous versions of the contracts, those contracts can be useful to understand some of the decisions taken in the new contracts but they are out-of-scope.
Only the specified contracts are in-scope


**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

This is the second part of Vechain dPoS strategy.

In the first phase was a bootstrapping phase where we allowed users to stake their VET and get VTHO rewards from a pool allocated by Vechain. This was done so users are familiar with the language and the flows before the second phase.

The  3 main contracts from this bootstrapping phase are

- StargateNFT
- StargateDelegation
- NodeManagementV3

Both NodeManagement and StargateDelegation will be deprecated and paused for this second phase.

NodeManagement functionality now will live in the TokenManager.sol library. StargateDelegation was totally deprecated since it simulated the delegation and rewards that now will be handled by Stargate.sol and the thor protocol.

StargateNFT is upgraded so it can interact with Stargate, this means that all the NFTs minted and migrated in the bootstrapping phase should be compatible with this new phase.

Also in this new phase the funds are moved to Stargate rather than StargateNFT, so we can have a single entrypoint to the protocol.

So as a summary

Bootstrapping Phase:

- StargateNFT
- NodeManagement
- StargateDelegation

Second phase (hayabusa):

- StargateNFT
- Stargate

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

In the bootstrapping phase we had a bug related to rewards calculation that we had to fix and took us some time to reimburse all the affected users.

So calculating the rewards given to users is a key operation, since for example giving less rewards can be fixable giving extra rewards can cause a mismatch with what the protocol gives stargate and run the contract out of VTHO. Check that rewards calculations are correctly handled after rewards are claimed, and if rewards are not claimed.

Also minting, burning and migrating tokens since they have a fixed VET amount linked to them an unexpected mint of a token without paying the correct amount can have critical results in the protocol.

Other key operations are moving the VET from StargateNFT to Stargate, and ensuring those funds are secure.

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

StargateNFT contract is an extension of the ERC721 standard

**What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?**

Pause Stargate or StargateNFT

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

Any requiring an address with the DEFAULT_ADMIN_ROLE or any other role, we can assume that the addresses that have this roles are secure

**What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?**

The ProtocolStaker is a third party address that we trust for our operations of delegating, staking... we can assume the ProtocolStaker contract is not malicious and will perform as intended

**Which chains and/or networks will the code in scope be deployed to?**

VeChain Testnet, VeChain Mainnet

**What external dependencies are there?**

@openzeppelin/contracts
@openzeppelin/contracts-upgradeable

**Are there any unusual points about your protocol that may confuse Security Researchers?**

This is going to be deployed in the vechain network.

The vechain network is an EVM-like network with some extra features like multiclause. 

The major difference with other EVM networks is that it does not have a traditional JSON-RPC API instead it uses an HTTPS API, this is relevant because most of the tooling developed for Ethereum is not directly compatible with vechain.

We use Hardhat with an adapter that intercepts the RPC calls and translates them to HTTPS so we can perform integration tests against the vechain network but this is not available for other frameworks like foundry.

Performing integration tests against the vechain network should be easy because we have a beforeEach hook that sets up an environment with docker and deploys the contract on each test.

For unit tests we use the hardhat chain but we mock the interaction with the protocol (setting delegations, giving rewards, adding validators...)

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

- Bootstrapping phase: https://docs.stargate.vechain.org
- Hayabusa phase: https://docs.stargate.vechain.org/hayabusa 
- VeChain Docs: https://docs.vechain.org/

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program ](https://immunefi.com/allstars/) participants. 

Rewards are denominated in USD and distributed in USDT on Ethereum.

The reward pool is $40,000 USD if any bug is found. That means that even if 1 Low severity bug is found, the whole reward pool is unlocked and has to be fully distributed between security researchers. 

If not a single bug is found (Insights do not count as bugs) the reward pool is $6,000 USD.

KYC Requirement

VeChain requires KYC information to pay for bug submissions. The following information will be required:
Full name 
Date of birth
Proof of address (either a redacted bank statement with address or a recent utility bill)
Copy of Passport or other Government issued ID
Security researchers are required to submit KYC within 14 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (6)

- The boostOnBehalfOf function uses an arbitrary _sender parameter instead of msg.sender, which deviates from standard patterns but is intentional. The Stargate contract calls this function during stakeAndDelegate flows. Since msg.sender would be the Stargate contract (no VTHO), _sender specifies which user's VTHO to use. This is protected by the onlyStargate modifier ensuring only the Stargate contract can set an arbitrary _sender (https://vechain.org/)
- There are some functions that can run out of gas due to excessive looping, most of them are getters so we are not really worried about them. In the cases there are not getters we implemented mechanisms to avoid running out of gas like in the claimRewards function. (https://vechain.org/)
- There can be breaks of the check-effects pattern in some functions but they are using the nonReentrant modifier (https://vechain.org/)
- There is a style choice in the _burnCallback and _safeMintCallback to precede the functions with an underscore even though they are external. This functions can only be called by the own StargateNFT contract and we want to discourage the usage of them from external developers. (https://vechain.org/)
- We are not checking address zero when granting or revoking roles (https://vechain.org/)
- We can assume the IProtocolStaker interface is correct (https://vechain.org/)
