# Attackathon | VeChain Hayabusa Upgrade

- Page: https://immunefi.com/bug-bounty/vechain-hayabusa-upgrade-attackathon/scope/
- Max bounty: $160,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Smart Contract
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: 2025-10-26T14:00:00.000Z

## Assets in scope (2)

- [blockchain_dlt] https://github.com/vechain/thor/compare/v2.3.2...release/hayabusa — VeChain Hayabusa Release Branch - [8855 Go]
- [smart_contract] https://github.com/vechain/thor/blob/release/hayabusa/builtin/gen/staker.sol — builtin - [389 Sol]

## Asset notes

**Build Commands, Test Commands, and How to Run Them**

[https://github.com/vechain/thor-hayabusa](https://github.com/vechain/thor-hayabusa) provides some information in operating a public or validator node in the Hayabusa network and provides access to additional tools, faucet for funds, an explorer and inspector a tool that allows for easy interaction with deployed smart contracts.

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

The scope is limited to a particular release branch of code so the scope is very clear, see scope above.


**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

Yes, upgrading the consensus mechanism of VeChainThor from Proof of Authority (PoA) to Delegated Proof of Stake (DPoS). See the provided VIPs for details of the changes. 

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

The change in the consensus mechanism and the distribution of rewards

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

All of the above listed standards are implemented on chain but do not form part of the upgrade.

**What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?**

The fact that two traditional audits are taking place in parallel with this Attackathon.

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

There is the executor address and stargate address which have privileged roles in the network and their actions so long as they operate within the privileges attributed to them are expected.

**What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?**

Both the executor and stargate address are essentially out of scope as they are known addresses and operated by trusted third parties.

**Which chains and/or networks is and will the code in scope be deployed to?**

VeChainThor

**What external dependencies are there?**

There are no new dependencies. All of the old dependencies are out of scope. 

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

For more information about the VeChain Hayabusa upgrade refer to, please visit the following resources:
- https://docs.vechain.org/ 
- VeChainThor Hayabusa Upgrade Release Branch
    - https://github.com/vechain/thor/tree/release/hayabusa 
- VeChain Hayabusa E2E Tests Repo
    - https://github.com/vechain/hayabusa-e2e 
- VeChain Hayabusa Upgrade VIPs
    - https://github.com/vechain/VIPs/blob/master/vips/VIP-253.md
    - https://github.com/vechain/VIPs/blob/master/vips/VIP-254.md

## Impacts in scope (28)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] Critical: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Causing network processing nodes to process transactions from the mempool beyond set parameters
- [blockchain_dlt] High: RPC API crash affecting programs with greater than or equal to 25% of the market capitalization on top of the respective layer
- [blockchain_dlt] High: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments
- [blockchain_dlt] High: Unintended chain split (network partition)
- [blockchain_dlt] Medium: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hours
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

**Proof of Concept (PoC) Requirements** 

A runnable PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules?utm_source=immunefi).

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope are valid.

**Previous Audits**

VeChain’s completed audit reports can be found:

- [https://github.com/slowmist/Knowledge-Base/blob/master/open-report/VeChainThorNodeToken-Smart-Contract-Security-Audit-Report.md](https://github.com/slowmist/Knowledge-Base/blob/master/open-report/VeChainThorNodeToken-Smart-Contract-Security-Audit-Report.md)
- [https://www.nccgroup.com/media/f05ojmp4/ncc_group_vechainfoundationsanmarinosrl_e0237_.pdf](https://www.nccgroup.com/media/f05ojmp4/ncc_group_vechainfoundationsanmarinosrl_e0237_.pdf)
- [https://www.coinspect.com/doc/Coinspect%20-%20Source%20Code%20Audit%20-%20VeChainThor%20Galactica%20V250512.pdf](https://www.coinspect.com/doc/Coinspect%20-%20Source%20Code%20Audit%20-%20VeChainThor%20Galactica%20V250512.pdf)

Unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

**Public Disclosure of Known Issues**

Bug reports for publicly disclosed bugs are not eligible for a reward. 
- Underflow enables contract drain, [https://github.com/vechain/thor/pull/1348](https://github.com/vechain/thor/pull/1348).
- No delegations allowed in Exiting Validator, [https://github.com/vechain/thor/pull/1384](https://github.com/vechain/thor/pull/1384)

**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

**Mainnet AC (Audit Competition) Bug Fix Policy**

The project may make bug fixes during the competition.
- Fixed bugs immediately become out of scope once the fix is public.
- Duplicate submissions of a bug are only valid if they’re submitted before the fix is public.	

All project made bug fixes immediately become in scope for the mitigation competition once the fix is public, including fixes to bugs found independently of SRs.

Read our full [mainnet AC rules](https://immunefisupport.zendesk.com/hc/en-us/articles/33256328266769-Mainnet-Audit-Competition-Rules) for more info.

**Insight Reporting**

Insight reports may be reported to this program and do not require a PoC. Insights are rewarded according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

Rewards are denominated in USD and distributed in USDT on Ethereum.

The reward pool is determined by the greatest severity bug found.

- A Critical is found 	- **$160,000 USD**
- A High is found 	- **$100,000 USD**
- A Medium is found 	- **$70,000 USD**
- A Low is found 	- **$40,000 USD**

If none of the above conditions apply then the reward pool is - **$24,000 USD**

Private known issues, meaning known issues that were not publicly disclosed, are valid and unlock the corresponding reward pool.

__Mitigation Competition Rewards__

The maximum reward pool for the mitigation competition is **$40,000 USD**.

If any bug in scope is fixed during the mainnet AC then a mitigation competition will begin immediately, run simultaneously, and end 5 days after the mainnet AC has ended.

The mitigation competition’s reward pool is based on how many bugs are fixed while the competitions are live relative to how many bugs are found in the mainnet AC. So if projects make more bug fixes mid-competition then the size of the mitigation competition reward pool increases up to the maximum.

The full mitigation competition reward terms can be [read here](https://immunefisupport.zendesk.com/hc/en-us/articles/33256328266769-Mainnet-Audit-Competition-Rules).

__Code Updates Log__
- Fix hayabusa solo mode for executor actions - https://github.com/vechain/thor/commit/6d29c7513818d515f4ad9f8f18d92d79e03d145c
- remove redundant gas consumption call - https://github.com/vechain/thor/commit/f08442278f1eb45bae74f1fe922955c8e2f1d367
- Authority isEndorsed now accounts for Staker Transition - https://github.com/vechain/thor/commit/c3a28e55c3bc5a6c2ae96178c9a8124178bff5ca
- Improve customnet for Hayabusa - https://github.com/vechain/thor/commit/cdc9c606c4e1c8fc9bad23472198d6e6dcb4e434
- chore: removed TODOs - https://github.com/vechain/thor/commit/4084a8e3d7301b33e7fde8fda9c0db5640a310e1
- fix: test - https://github.com/vechain/thor/commit/aaad156e7cecf54c289e96134513f6d74b632882
- chore: add comment - https://github.com/vechain/thor/commit/b58d9efd4ed35eb397dad40b7493d437e59b76bd
- fix: delegation withdrawal while validator pending - https://github.com/vechain/thor/commit/038e406d4eb247e44675933b2d3ed3809b3943d8
- fix: delegation withdrawal while validator pending - https://github.com/vechain/thor/commit/12d7e1b252756ea4ebb14f2c7ab9519e75f3bcec
- fix: delegation withdrawal while validator pending - https://github.com/vechain/thor/commit/a28869da0aed1b102c2a9b3a80523bd5a05e7519
- chore(staker): reduce housekeepnig logs" - https://github.com/vechain/thor/commit/8a12e30656c7626f3ccb94f10dfa63b6b1ae7d9b
- fix stater - https://github.com/vechain/thor/commit/3ad5e1805c778a070e27d0d0293f335a256c235e
- Resolved merge conflicts - https://github.com/vechain/thor/commit/8ff104a3fb1ee5f39c6be5e54cb262bf10100063
- Merge master - https://github.com/vechain/thor/commit/d087893b1f1c93e9fcf29e60928ffe73c95909be
- chore(energy): cap validator rewards to 100% - https://github.com/vechain/thor/commit/91597ce1daf3064e2298a0606798030d43a90c1c
- chore(test): verify issued - https://github.com/vechain/thor/commit/4bfef54f7013b89943f8de86d9b02db828b7a715
- Error handling - https://github.com/vechain/thor/commit/2595b990a842662cd476007ea838c9ac10d1d956
- TP set to 7 days - https://github.com/vechain/thor/commit/f040eed7f30d8256c959a7c7ee2d2a97816f45e7
- Increase and Decrease are only on active validators - https://github.com/vechain/thor/commit/016c22992e5939e7ed12a93edd2e87c2ceafdb2b
- chore: set testnet/ mainnet hayabusa block - https://github.com/vechain/thor/commit/b4c914fe573ed6141daa159fa293e9193a96d74f
- chore(staker): make all methods external to reduce gas costs - https://github.com/vechain/thor/commit/b42b73f58d93c677a0e8085ba1f901ef7aaf2682
- chore(energy): Add an inline comment to clarify that totalSupply does - https://github.com/vechain/thor/commit/6387d5ef68f834000088325ddb00fa884dd8c8ff
- move ascii art out of post-block handler - https://github.com/vechain/thor/commit/b3634c2c16d5988101aae5447ab9a3700f2e59c5
- chore: squash commits - https://github.com/vechain/thor/commit/13b241e9129233135d63edcf381de9d7e6bf990d
- Custom encoding for Energy Stop Growth Time - https://github.com/vechain/thor/commit/ce5c407c4cfddd92ec89c065915f9f05d3624faf
- Merge aikido updates - https://github.com/vechain/thor/commit/706bee9e6693244a6ddac17f883c7b09c6c63852
- Charge extra sload -https://github.com/vechain/thor/commit/c1a18885ef673dfd9bfff48ff89dc15e30bb833f
- fix(authority): charge gas if fetching validation - https://github.com/vechain/thor/commit/7391a7dd97b8840827b59d4aaf802f7732713953
- custom genesis: error when external executor and builtin executor are - https://github.com/vechain/thor/commit/55dfff0c869801d9c02f50780b15f9b153953970

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
