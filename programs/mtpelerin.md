# Mt Pelerin

- Page: https://immunefi.com/bug-bounty/mtpelerin/scope/
- Max bounty: $5,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: websites_and_applications - critical, websites_and_applications - high, smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (33)

- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/access/Operator.sol — Operator.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/access/Roles.sol — Roles.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/operating/ComplianceRegistry.sol — ComplianceRegistry.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/operating/PriceOracle.sol — PriceOracle.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/operating/Processor.sol — Processor.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/operating/RuleEngine.sol — RuleEngine.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/AddressThresholdLockRule.sol — AddressThresholdLockRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/GlobalFreezeRule.sol — GlobalFreezeRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/HardTransferLimitRule.sol — HardTransferLimitRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/MaxTransferRule.sol — MaxTransferRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/MinTransferRule.sol — MinTransferRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/SoftTransferLimitRule.sol — SoftTransferLimitRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/UserAttributeValidToRule.sol — UserAttributeValidToRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/UserFreezeRule.sol — UserFreezeRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/UserKycThresholdBothRule.sol — UserKycThresholdBothRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/UserKycThresholdFromRule.sol — UserKycThresholdFromRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/UserKycThresholdToRule.sol — UserKycThresholdToRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/UserValidRule.sol — UserValidRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/YesNoRule.sol — YesNoRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/rules/YesNoUpdateRule.sol — YesNoUpdateRule.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/sale/TokenSale.sol — TokenSale.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/token/BondBridgeToken.sol — BondBridgeToken.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/token/BridgeToken.sol — BridgeToken.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/token/CoinBridgeToken.sol — CoinBridgeToken.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/token/ShareBridgeToken.sol — ShareBridgeToken.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/token/abstract/BridgeERC20.sol — BridgeERC20.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/token/abstract/SeizableBridgeERC20.sol — SeizableBridgeERC20.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/utils/TokenDispenserQueue.sol — TokenDispenserQueue.sol
- [smart_contract] https://github.com/MtPelerin/bridge-v2/blob/master/contracts/voting/ShareholderMeeting.sol — ShareholderMeeting.sol
- [websites_and_applications] https://app.mtpelerin.com — Web application, onramp/offramp/swap widget
- [websites_and_applications] https://apps.apple.com/us/app/bridge-wallet/id1481859680 — Non custodial wallet app on iOS
- [websites_and_applications] https://play.google.com/store/apps/details?id=com.mtpelerin.bridge — Non custodial wallet app on Android
- [websites_and_applications] https://www.mtpelerin.com

## Asset notes

(none)

## Impacts in scope (6)

- [smart_contract] Critical: Loss of user funds staked (principal) by freezing or theft
- [smart_contract] High: Freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for any amount of time
- [smart_contract] High: Theft of unclaimed yield
- [websites_and_applications] Critical: Data theft
- [websites_and_applications] High: Data deletion

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$5,000, rewardCalculationPercentage=10, rewardModel=fixed
- [smart_contract] High: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$5,000, otherImpactMaxReward=$0, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

Additionally, all bug reports without proof of concept exploits with
demonstrated impact, as well as recommendations for new features, are not
accepted.

Payouts are handled by **Mt Pelerin** directly and are estimated in
**USD**. However, payouts are done in **ETH, BTC, USDT, USDC, or DAI**.

## Out of scope (program-specific)

- Best practice critiques
- Attacks requiring privileged access from within the organization
- Bugs without proof-of-concept exploits showing impact

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
