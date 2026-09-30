# Ref Finance

- Page: https://immunefi.com/bug-bounty/reffinance/scope/
- Max bounty: $250,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: (none)
- End date: (none)

## Assets in scope (38)

- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/actions_of_farmer_reward.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/actions_of_farmer_seed.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/actions_of_seed.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/big_decimal.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/booster.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/errors.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/events.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/farmer.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/farmer_seed.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/legacy.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/lib.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/management.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/owner.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/seed.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/seed_farm.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/storage_impl.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/token_receiver.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/utils.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/boost-farming/src/view.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/mock-ft/src/lib.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/mock-mft/src/lib.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/boost-farm/blob/main/contracts/mock-mft/src/mft.rs — Boosted Farming (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/account_deposit.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/action.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/admin_fee.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/errors.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/legacy.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/lib.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/multi_fungible_token.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/owner.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/pool.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/simple_pool.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/stable_swap/math.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/stable_swap/mod.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/storage_impl.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/token_receiver.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/utils.rs — Exchange (Github)
- [smart_contract] https://github.com/ref-finance/ref-contracts/blob/main/ref-exchange/src/views.rs — Exchange (Github)

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

## Impacts in scope (14)

- [smart_contract] Critical: Direct theft of any user funds (with value > $250,000), whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Miner-extractable value (MEV)
- [smart_contract] Critical: Permanent freezing of user funds (with value > $250,000)
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Direct theft of any user funds (with value > $5,000 and < $250,000), whether at-rest or in-motion
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds (including unclaimed yield) for any amount of time
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Low: Smart contract fails to work correctly, but doesn’t lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$250,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: fixedReward=$30,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All web/app bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. In addition, all bug reports must come with a suggestion for a fix in order to be considered for a reward. 

Rewards for critical smart contract vulnerabilities are further capped at 10% of economic damage, with the main consideration being the funds affected in addition to PR and brand considerations, at the discretion of the team. However, there is a minimum reward of __USD 50 000__ for Critical smart contract bug reports. 

Issues previously highlighted in the following audit report are considered as out of scope: 
  - [https://422665050-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MhIB0bSr6nOBfTiANqT-2910905616%2Fuploads%2Fh8mipVuJTakoLC6XmzfU%2FRef%20Finance%20Security%20Audit-1.pdf?alt=media&token=cf0398d1-97d5-4367-9776-07bc8e4c67ea](https://422665050-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MhIB0bSr6nOBfTiANqT-2910905616%2Fuploads%2Fh8mipVuJTakoLC6XmzfU%2FRef%20Finance%20Security%20Audit-1.pdf?alt=media&token=cf0398d1-97d5-4367-9776-07bc8e4c67ea)

Payouts are handled by the __Ref Finance__ team directly and are denominated in USD. However, payouts are done in __USDT__, __USDC__, __NEAR__, __wNEAR__ or __REF__, at the discretion of the team.

## Out of scope (program-specific)

- Best practice critiques
  - Issues related to the frontend without concrete impact and PoC
  - Best practices issues without concrete impact and PoC

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
