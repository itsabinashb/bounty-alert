# Audit Comp | Alchemix V3

- Page: https://immunefi.com/bug-bounty/alchemix-v3-audit-competition/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: 2025-11-04T14:00:00.000Z

## Assets in scope (28)

- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/AlchemistAllocator.sol — AlchemistAllocator
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/AlchemistCurator.sol — AlchemistCurator
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/AlchemistETHVault.sol — AlchemistETHVault
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/AlchemistStrategyClassifier.sol — AlchemistStrategyClassifier
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/AlchemistTokenVault.sol — AlchemistTokenVault
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/AlchemistV3.sol — AlchemistV3
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/AlchemistV3Position.sol — AlchemistV3Position
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/MYTStrategy.sol — MYTStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/Transmuter.sol — Transmuter
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/arbitrum/AaveV3ARBUSDCStrategy.sol — AaveV3ARBUSDCStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/arbitrum/AaveV3ARBWETHStrategy.sol — AaveV3ARBWETHStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/arbitrum/EulerARBUSDCStrategy.sol — EulerARBUSDCStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/arbitrum/EulerARBWETHStrategy.sol — EulerARBWETHStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/arbitrum/FluidARBUSDCStrategy.sol — FluidARBUSDCStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/mainnet/EulerUSDCStrategy.sol — EulerUSDCStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/mainnet/EulerWETHStrategy.sol — EulerWETHStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/mainnet/MorphoYearnOGWETH.sol — MorphoYearnOGWETH
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/mainnet/PeapodsETH.sol — PeapodsETH
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/mainnet/PeapodsUSDC.sol — PeapodsUSDC
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/mainnet/TokeAutoEth.sol — TokeAutoEth
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/mainnet/TokeAutoUSDStrategy.sol — TokeAutoUSDStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/optimism/AaveV3OPUSDCStrategy.sol — AaveV3OPUSDCStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/optimism/MoonwellUSDCStrategy.sol — MoonwellUSDCStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/optimism/MoonwellWETHStrategy.sol — MoonwellWETHStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/strategies/optimism/StargateEthPoolStrategy.sol — StargateEthPoolStrategy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/utils/PermissionedProxy.sol — PermissionedProxy
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/utils/Whitelist.sol — Whitelist
- [smart_contract] https://github.com/alchemix-finance/v3-poc/blob/immunefi_audit/src/utils/ZeroXSwapVerifier.sol — ZeroXSwapVerifier

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

## Impacts in scope (20)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs for at least 24 hour
- [smart_contract] High: Temporary freezing of funds for at least 24 hour
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of NFTs for at least 1 hour
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

**Proof of Concept (PoC) Requirements**

A **runnable PoC**, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

**Build Commands, Test Commands, and How to Run Them**

All tests for the Alchemists/Transmuters can be run at once if you specify the fork and block. Whitehats will need their own fork URL. The block number currently used for testing is: 

Examples: 
- AlchemistV3: FOUNDRY_PROFILE=default forge test --fork-url <URL> --match-path src/test/AlchemistV3.t.sol  -vvvv --evm-version cancun 
- Transmuter: FOUNDRY_PROFILE=default forge test --fork-url <URL> --match-path src/test/Transmuter.t.sol  -vvvv --evm-version cancun 
- All MYT strategies: FOUNDRY_PROFILE=default forge test --match-path "src/test/strategies/**/*.sol" -vvvv --evm-version cancun 

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope are valid.

**Code Freeze Assurance**

Code of the assets in scope is frozen while the program is live. 

Duplicate submissions of bugs are **valid**. Duplicate submissions of Insights are **invalid**.

The project commits to keeping private all info related to bug findings until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

**Previous Audits**

- Alchemix’s completed audit reports can be found at - https://cantina.xyz/portfolio/f638950d-a8ad-4df8-a6ec-8b067e416d7b or in the github repository. 
- Unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.
- All cantina audit items are resolved and all tests are passing, EXCEPT the below items. Reporting any of the below items are NOT IN SCOPE for this contest. All other bug findings in cantina would be valid reportings if still occurring:
    - 3.1.8 - Devs did fix the calculation here but disagree that people putting money into the transmuter is a bad thing. They are technically adding backing to the system
    - 3.2.2 - intended behavior 
    - 3.2.8 - UI handles this so intended behavior
    - 3.2.15 - Incorrect. A user wouldnt be able to deposit into a new position twice in one block since they wouldnt know what the ID they were assigned until after the block is written.
    - 3.2.21 - Intended behavior

**Public Disclosure of Known Issues**

Bug reports for publicly disclosed bugs are not eligible for a reward. 

- Technically an individual could open numerous small positions at max LTV, hoping that they become eligible for liquidation so they can liquidate themselves and get paid from the feeVault for a net profit. However, the feeVault ONLY pays out when the alchemist is globally undercollateralized, NOT for liquidate individually undercollateralized positions when global collateralization is otherwise acceptable. This is an acceptable risk and therefore not considered in scope. None currently known

**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

*Fundamental Oracles*

- We are pricing strategies based on the fundamental backing, rather than dex price, whenever possible. This means there may be scenarios where the fundamental backing has a queue to access (such as the exit queue for wstETH). In these scenarios, as an example, 1 alETH in the transmuter would return 1 ETH worth of MYT, but that 1 ETH of MYT would not be accessible until the withdrawal queue clears, OR the user could sell the 1 ETH of MYT for < 1 ETH. Thus, the MYT market price may be < 1 ETH, which may bring the price of the alAsset < 1 ETH. This is intended behavior, as should the withdrawal queue clear the 1 ETH of MYT value would once again be instantly accessible and thus the alAsset would be redeemable for 1 ETH. 

- IF the price of the MYT drops below the LTV (say 1 ETH of MYT has a market price of 0.85 ETH) due to withdrawal queues, then it would be expected that arbitragers mint alETH to sell at > 100% LTV. However, so long as the value of the MYT these arbitragers collateralize returns to 1:1, there is no bad debt created in the system. Only a situation that returns permanent bad debt, even after MYT recovery, would be in scope (or a situation where the MYT is prevented from recovering). 

*Morpho V2 Vaults*

The Meta Yield Token is a Morpho v2 Vault. The base Morpho v2 code is unchanged and not in scope. Only the implementation of the base code and associated wrappers/extensions are in scope. (Ie, only issues that propogate from the main v2 code and implementation into the in-scope contracts are in scope). 

*Interfaces, Unit Tests, Mock Tokens*

Interface Definitions, Unit Tests, and Mock Tokens are not in scope unless the issues propogate to the actual logic of the in-scope contracts. 

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

While some of the economic ideas of Alchemix V3 are closely tied to Alchemix v2, this is an entirely new codebase. The only carryover is that the alAssets that are currently minted by Alchemix v2 will be the same alAssets minted by Alchemix v3.

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

*Flash Loans*: Alchemix v2 does not allow smart contract interactions, which means flash loans could never interact with Alchemix v2. Alchemix v3 does not have this restriction, thus attention paid to potential attacks that take significant capital (ie, flashloans) is appreciated.

*Bad Debt and MYT Pricing*: Any attack vectors that would create permanent bad debt are very high priority, due to pricing exploits, pricing manipulation of internal oracles, or otherwise in the Meta Yield Tokens. The internal oracle especially should be a point of focus. 

*Liqudations*:  Liquidations are unique in that they need to interact with earmarking, as the system’s highest priority repayment is to fulfill transmuter obligations. This means if a position is eligible for liquidation, it will first have all earmarked debt cleared early, and then a liquidation will only occur if the redemption did not bring the user to a safe LTV. Thus, an invariant is that a liquidation shall never take priority over a redemption. The multistep liquidation system, with partial liquidations, is also somewhat custom and should be paid attention to.

*0x Matcha Swaps*: Our ZeroXSwapVerifier (part of the dual unwrap/wrapping approach that uses both fundamental contracts and dex aggregation) heavily relies on implicit calldata parsing. We would like explicit effort put into the review that such in-place verification matches the 0x protocol logic and a malicious swap event cannot make it trough the strategy with manipulated tokens, senders, amounts, receivers, slippages etc

*Earmarking*: Redemptions are discrete - when someone claims their transmuter position, their alAsset is burned and they recieve collateral directly from the Alchemist. Vault users will see both collateral and debt decrease. However, earmarking is continuous - essentially ensuring that building up to the time a transmuter position is claimed, enough collateral is being “reserved” in the system to ensure that users are unable to withdraw collateral that will be necessary to fulfill redemption obligations to the transmuter. This requires a continuous accounting weighting / earmarking system. Any inaccuracies in this system could be considered a valid bug. 


**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

ERC20 (throughout), ERC721 (transmuter, and enumerables used for alchemist NFT positions), ERC4626 (Meta Yield Token)

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

None (Ie, if trusted roles such as Alchemix DAO (Admin), 0xMatcha Aggregator, and Guardians are operating normally and a bug can occur, that would be in scope. Entering the wrong function inputs would NOT be in scope. Griefing would NOT be in scope.)

**What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?**

- Any Alchemix DAO multisig (Admin)
- 0xMatcha Aggregator
- Guardians

(These are all trusted roles, however if there was a valid exploit that could be executed for example only when the 0xMatcha Aggregator is down or has a temporary loss of service, that would be in scope. Loss of functionality of the contracts while the aggregator is down would NOT be in scope unless it could result in permanent loss of user funds or bad debt. The aggregator just “being down” is not in scope, there would need to be impact beyond temporarily reduced protocol functionality)

**Which chains and/or networks will the code in scope be deployed to?**
- Ethereum, Optimism, Arbitrum, Base

**What external dependencies are there?**
- Morpho v2 Vaults
- OpenZeppelin
- Permit2
- 0x Matcha Routing
- Twap Pricing Mechanism
- All yield strategies are dependent on the protocol they derive yield from

**Are there any unusual points about your protocol that may confuse Security Researchers?**

- The earmarking and redemption system is unique. The purpose of earmarking is to time-weight the communal redemptions in the system
- The liquidation system is unique, especially in how it interacts with earmarking.

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

- https://keenanlukeom.github.io/alchemix-v3-docs/
- https://keenanlukeom.github.io/alchemix-v3-docs/dev/alchemist/alchemist-contract

Resources related to: https://github.com/alchemix-finance/v3-poc/tree/immunefi_audit/src/strategies/mainnet
- https://app.tokemak.xyz/pools/autoETH?breakdown=pools
- https://app.euler.finance/vault/0xD8b27CF359b7D15710a5BE299AF6e7Bf904984C2?network=ethereum
- https://app.morpho.org/ethereum/vault/0xE89371eAaAC6D46d4C3ED23453241987916224FC/yearn-og-weth
- https://peapods.finance/lending/1/0x9a42e1bEA03154c758BeC4866ec5AD214D4F2191
- https://app.euler.finance/vault/0xe0a80d35bB6618CBA260120b279d357978c42BCE?network=ethereum
- https://peapods.finance/lending/1/0x3717e340140D30F3A077Dd21fAc39A86ACe873AA
- https://app.tokemak.xyz/pools/autoUSD

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of Reward Pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program participants](https://immunefi.com/allstars/). 

Rewards are denominated in USD and distributed in USDC on Optimism

The reward pool is **$100,000 USD** if any bug is found. That means that even if 1 Low severity bug is found, the whole reward pool is unlocked and has to be fully distributed between security researchers. 

If not a single bug is found (Insights do not count as bugs) the insight reward pool is $15,000 USD.

**Proof of Concept (PoC) Requirements**
A **runnable PoC**, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Technically an individual could open numerous small positions at max LTV, hoping that they become eligible for liquidation so they can liquidate themselves and get paid from the feeVault for a net profit. However, the feeVault ONLY pays out when the alchemist is globally undercollateralized, NOT for liquidate individually undercollateralized positions when global collateralization is otherwise acceptable. This is an acceptable risk and therefore not considered in scope. (https://github.com/alchemix-finance/v3-poc/tree/immunefi_audit)
