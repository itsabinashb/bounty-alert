# Starknet Staking

- Page: https://immunefi.com/bug-bounty/starknet-staking/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - medium, smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (18)

- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/stake/PeriodMintLimit.sol — PeriodMintLimit.sol
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/upgrade/ProxySupportImpl.sol — Upgrade_ProxySupportImpl.sol
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/minting_curve/interface.cairo — minting_curve_interface,cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/minting_curve/minting_curve.cairo — minting_curve.cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/pool/interface.cairo — Pool_interface.cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/pool/pool.cairo — Pool.cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/reward_supplier/interface.cairo — reward_supplier_interface.cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/reward_supplier/reward_supplier.cairo — reward_supplier.cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/staking/interface.cairo — staking_interface.cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/staking/staking.cairo — staking.cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/blob/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/contracts/src/utils.cairo — utils.cairo
- [smart_contract] https://github.com/starkware-libs/starknet-staking/tree/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/components — L1 Solidity Components
- [smart_contract] https://github.com/starkware-libs/starknet-staking/tree/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/interfaces — L1 Solidity Interfaces
- [smart_contract] https://github.com/starkware-libs/starknet-staking/tree/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/libraries — L1 Solidity Libraries
- [smart_contract] https://github.com/starkware-libs/starknet-staking/tree/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/stake/MintManager.sol — MintManager.sol
- [smart_contract] https://github.com/starkware-libs/starknet-staking/tree/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/stake/RewardSupplier.sol — RewardSupplier.sol
- [smart_contract] https://github.com/starkware-libs/starknet-staking/tree/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/stake/RewardSupplierExternalInterfaces.sol — RewardSupplierExternalInterfaces.sol
- [smart_contract] https://github.com/starkware-libs/starknet-staking/tree/%40staking/contracts-v1.0.1-dev.854/workspace/apps/staking/L1/starkware/solidity/stake/RewardSupplierStorage.sol — RewardSupplierStorage.sol

## Asset notes

Starknet Staking’s codebase can be found at https://github.com/starkware-libs/starknet-staking. Documentation and further resources can be found on https://docs.starknet.io/staking/overview/. 

Submitting multiple vulnerabilities that can be resolved with one solution may result in reduced severity ratings or invalidation of the later submissions. 

Security Researchers are required to address all vulnerable points across contracts in one fix. Any missed issues later reported by the security researcher will be considered unique.

## Impacts in scope (9)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$15,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$1,500, rewardModel=range
- [smart_contract] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Payouts are handled by the StarkWare team directly and are denominated in USD. However, payments are done in USDC or STRK, at StarkWare’s discretion.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

- Impacts caused by attacks requiring access to privileged addresses (including, but not limited to: governance and strategist contracts) without additional modifications to the privileges attributed
- Vulnerabilities that can be reverted by upgrading the contract will have reduced severity.
- - Findings already reported through this or other bug bounty programs on Immunefi or any other BBP Platform.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
