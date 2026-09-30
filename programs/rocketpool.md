# Rocket Pool

- Page: https://immunefi.com/bug-bounty/rocketpool/scope/
- Max bounty: $150,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (77)

- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/RocketBase.sol — Base settings / modifiers for each contract in Rocket Pool
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/RocketStorage.sol — The primary persistent storage for Rocket Pool
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/RocketVault.sol — The RocketVault contract must not be upgraded
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/auction/RocketAuctionManager.sol — Facilitates RPL liquidation auctions
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/RocketDAOProposal.sol — A DAO proposal
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/RocketDAONodeTrusted.sol — The Trusted Node DAO
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/RocketDAONodeTrustedActions.sol — The Trusted Node DAO Actions
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/RocketDAONodeTrustedProposals.sol — The Trusted Node DAO Proposals
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/RocketDAONodeTrustedUpgrade.sol — Handles network contract upgrades
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/settings/RocketDAONodeTrustedSettings.sol — Trusted node settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/settings/RocketDAONodeTrustedSettingsMembers.sol — The Trusted Node DAO Members
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/settings/RocketDAONodeTrustedSettingsMinipool.sol — The Trusted Node DAO Minipool settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/settings/RocketDAONodeTrustedSettingsProposals.sol — The Trusted Node DAO Members
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/node/settings/RocketDAONodeTrustedSettingsRewards.sol — The Trusted Node DAO Rewards settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/RocketDAOProtocol.sol — The Rocket Pool Protocol DAO (pDAO)
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/RocketDAOProtocolActions.sol — The Rocket Pool Network DAO Actions
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/RocketDAOProtocolProposal.sol — Manages protocol DAO proposals
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/RocketDAOProtocolProposals.sol — Manages protocol DAO proposals
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/RocketDAOProtocolVerifier.sol — Implements the protocol DAO optimistic fraud proof proposal system
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettings.sol — Protocol DAO settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsAuction.sol — Network auction settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsDeposit.sol — Network deposit settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsInflation.sol — RPL Inflation settings in RP
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsMegapool.sol — Network megapool settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsMinipool.sol — Network minipool settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsNetwork.sol — Network auction settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsNode.sol — Network auction settings
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsProposals.sol — Settings related to proposals in the protocol DAO
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsRewards.sol — Settings relating to RPL reward intervals
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/protocol/settings/RocketDAOProtocolSettingsSecurity.sol — Protocol parameters relating to the security council
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/security/RocketDAOSecurity.sol — The Rocket Pool Security Council DAO
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/security/RocketDAOSecurityActions.sol — Executes proposals which affect security council members
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/security/RocketDAOSecurityProposals.sol — Proposal contract for the security council
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/dao/security/RocketDAOSecurityUpgrade.sol — Proposal contract for the security council upgrade veto powers
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/deposit/RocketDepositPool.sol — Accepts user deposits and mints rETH; handles assignment of deposited ETH to megapools
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/megapool/RocketMegapoolDelegate.sol — This contract manages multiple validators belonging to an individual node operator.
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/megapool/RocketMegapoolDelegateBase.sol — All megapool delegate contracts must extend this base to include the expected deprecation functionality
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/megapool/RocketMegapoolFactory.sol — Performs deterministic deployment of megapool delegate contracts and handles deprecation of old ones
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/megapool/RocketMegapoolManager.sol — Handles protocol-level megapool functionality
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/megapool/RocketMegapoolPenalties.sol — Applies penalties to megapools for MEV theft
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/megapool/RocketMegapoolProxy.sol — Contains the initialisation and delegate upgrade logic for megapools.
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/megapool/RocketMegapoolStorageLayout.sol — The RocketMegapool contract storage layout
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/minipool/RocketMinipoolBase.sol — Contains the initialisation and delegate upgrade logic for minipools
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/minipool/RocketMinipoolBondReducer.sol — Handles bond reduction window and trusted node cancellation
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/minipool/RocketMinipoolDelegate.sol — Minipools exclusively DELEGATECALL into this contract it is never called directly
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/minipool/RocketMinipoolFactory.sol — Performs CREATE2 deployment of minipool contracts
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/minipool/RocketMinipoolManager.sol — Minipool creation
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/minipool/RocketMinipoolPenalty.sol — Non-upgradable contract which gives guardian control over maximum penalty rates
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/minipool/RocketMinipoolQueue.sol — Minipool queueing for deposit assignment
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/minipool/RocketMinipoolStorageLayout.sol — The RocketMinipool contract storage layout, shared by RocketMinipoolDelegate
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/network/RocketNetworkBalances.sol — Oracle contract for network balance data
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/network/RocketNetworkFees.sol — Network node demand and commission rate
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/network/RocketNetworkPenalties.sol — Applies penalties to minipools for MEV theft
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/network/RocketNetworkPrices.sol — Oracle contract for network token price data
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/network/RocketNetworkRevenues.sol — Handles the calculations of revenue splits for the protocol's Universal Adjustable Revenue Split
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/network/RocketNetworkSnapshots.sol — Accounting for snapshotting of values based on block numbers
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/network/RocketNetworkSnapshotsTime.sol — Accounting for snapshotting of values based on block timestamps
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/network/RocketNetworkVoting.sol — Accounting for snapshotting of governance related values based on block numbers
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/node/RocketNodeDeposit.sol — Entry point for node operators to perform deposits for the creation of new validators on the network
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/node/RocketNodeDistributor.sol — Execution layer reward fee recipient for non-smoothing pool minipool operators
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/node/RocketNodeDistributorDelegate.sol — Contains the logic for RocketNodeDistributors
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/node/RocketNodeDistributorFactory.sol — RocketNodeDistributor Create2 factory
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/node/RocketNodeDistributorStorageLayout.sol — RocketNodeDistributor storage layout
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/node/RocketNodeManager.sol — Node registration and management
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/node/RocketNodeStaking.sol — Handles staking of RPL by node operators
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/rewards/RocketClaimDAO.sol — Recipient of pDAO RPL from inflation. Performs treasury spends and handles recurring payments.
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/rewards/RocketMerkleDistributorMainnet.sol — Mainnet merkle reward claim distributor
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/rewards/RocketRewardsPool.sol — Holds RPL and ETH generated by the network for distribution each reward cycle
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/rewards/RocketSmoothingPool.sol — Receives priority fees and MEV via fee_recipient
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/token/RocketTokenRETH.sol — rETH liquid staking token contract
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/token/RocketTokenRPL.sol — RPL token contract
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/util/AddressQueueStorage.sol — Address queue storage helper for RocketStorage data
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/util/AddressSetStorage.sol — Address set storage helper for RocketStorage data
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/util/BeaconStateVerifier.sol — Verifier for beacon state proofs
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/util/LinkedListStorage.sol — A linked list storage helper for the deposit requests queue data
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/util/LinkedListStorageHelper.sol — A linked list storage helper to test internal functions
- [smart_contract] https://github.com/rocket-pool/rocketpool/blob/v1.4/contracts/contract/util/SSZ.sol — Set of utilities for working with SSZ serialisation and merklelisation

## Asset notes

The Rocket Pool explainer series provides information about how Rocket Pool works; purpose, general concepts, actors, and interactions:

__Part 1 - Overview and users of the protocol__
[https://medium.com/rocket-pool/rocket-pool-staking-protocol-part-1-8be4859e5fbd](https://medium.com/rocket-pool/rocket-pool-staking-protocol-part-1-8be4859e5fbd)

__Part 2 - The Protocol and Oracle Node DAO's__
[https://medium.com/rocket-pool/rocket-pool-staking-protocol-part-2-e0d346911fe1](https://medium.com/rocket-pool/rocket-pool-staking-protocol-part-2-e0d346911fe1)

 __Part 3 - RPL & Tokenomics__
[ https://medium.com/rocket-pool/rocket-pool-staking-protocol-part-3-3029afb57d4c](https://medium.com/rocket-pool/rocket-pool-staking-protocol-part-3-3029afb57d4c)

Rocket Pool also has quick-start guides for:

__Stakers__ [(https://medium.com/rocket-pool/rocket-pool-stakers-guide-2c5c324b1749)](https://medium.com/rocket-pool/rocket-pool-stakers-guide-2c5c324b1749) 

__Node Operators__ [(https://medium.com/rocket-pool/rocket-pool-node-quickstart-guide-d40bc3d0de6d)](https://medium.com/rocket-pool/rocket-pool-node-quickstart-guide-d40bc3d0de6d) 

Comprehensive documentation can be found here: [https://docs.rocketpool.net/guides/](https://docs.rocketpool.net/guides/) 

For additional reference, please view their GitHub here - [https://github.com/rocket-pool/rocketpool/tree/master.](https://github.com/rocket-pool/rocketpool/tree/master)

## Impacts in scope (10)

- [smart_contract] Critical: Direct theft of principal user funds exceeding $150,000 (excluding unclaimed yield), whether at-rest or in-motion
- [smart_contract] Critical: Permanent freezing of funds (cannot be rescued)
- [smart_contract] High: Direct theft of principal user funds with value > $50,000 and <$150,000 (excluding unclaimed yield), whether at-rest or in-motion
- [smart_contract] High: Direct theft of unclaimed yield, whether at-rest or in-motion
- [smart_contract] High: Manipulation of governance voting result deviating from voted outcome with cost impact
- [smart_contract] Medium: Direct theft of principal user funds with value < $50,000 (excluding unclaimed yield), whether at-rest or in-motion
- [smart_contract] Medium: Manipulation of governance voting result deviating from voted outcome
- [smart_contract] Medium: Temporary freezing of funds
- [smart_contract] Low: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Low: Manipulation to gain unfair yield or commission advantage

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$150,000, minReward=$15,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$15,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, rewardModel=up_to
- [smart_contract] Low: maxReward=$1,000, rewardModel=up_to

## Reward notes

Payouts are handled by the __Rocket Pool__ team directly and are denominated in USD. However, payouts are done in __RPL__.

#### Reward Calculation for Critical Level Reports

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of **USD $150,000**. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of **USD $15,000** is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

#### Repeatable Attack Limitations

* If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward.   
* The amount of funds at risk will be calculated with the impact of the first attack being at **100%** and then a reduction of **25%** from the amount of the first attack for every \[**300 blocks\]** the attack needs for subsequent attacks from the first attack, rounded down.

#### Reward Calculation for High Level Reports

High impacts concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of **$5,000** to **$15,000**.  with the reward calculated based on **100%** of the funds at risk, though capped at the maximum high reward.

## Out of scope (program-specific)

Any submissions that match our known issues (https://rocketpool.net/protocol/security#known-issues) will be marked as spam.

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Known Issues (https://rocketpool.net/protocol/security#known-issues)
