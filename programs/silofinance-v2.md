# Silo Finance (v2 & v3)

- Page: https://immunefi.com/bug-bounty/silofinance-v2/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (29)

- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/Silo.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/SiloConfig.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/SiloFactory.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/hooks/SiloHookV1.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/hooks/SiloHookV2.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/hooks/SiloHookV3.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/incentives/SiloIncentivesControllerCompatible.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/incentives/SiloIncentivesControllerFactory.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/interestRateModel/kink/DynamicKinkModel.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/interestRateModel/kink/DynamicKinkModelConfig.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/interestRateModel/kink/DynamicKinkModelFactory.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/silo-router/SiloRouterV2.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/silo-router/SiloRouterV2Implementation.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/utils/ShareDebtToken.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-core/contracts/utils/ShareProtectedCollateralToken.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-vaults/contracts/IdleVault.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-vaults/contracts/IdleVaultsFactory.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-vaults/contracts/SiloVault.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-vaults/contracts/SiloVaultsFactory.sol
- [smart_contract] https://github.com/silo-finance/silo-contracts-v3/blob/master/silo-vaults/contracts/incentives/VaultIncentivesModule.sol
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://sonicscan.org/address/0x1D9289efd4424F50c9155cf8b591944B0fba0fD0 — SiloHookV1.sol - Silo Lending
- [smart_contract] https://sonicscan.org/address/0x1a36C81756d09950AcBd1aBDC522C0DD41363353 — ShareProtectedCollateralToken.sol - Silo Lending
- [smart_contract] https://sonicscan.org/address/0x435Ab368F5fCCcc71554f4A8ac5F5b922bC4Dc06 — Silo.sol - Silo Lending
- [smart_contract] https://sonicscan.org/address/0x4e125E605FDcf3B07BDE441DECf8EDAd423D5DC6 — SiloVaultsFactory.sol - Silo Vaults
- [smart_contract] https://sonicscan.org/address/0x4e9dE3a64c911A37f7EB2fCb06D1e68c3cBe9203 — SiloFactory.sol - Silo Lending
- [smart_contract] https://sonicscan.org/address/0xDED4aC8645619334186f28B8798e07ca354CFa0e — Example of SiloVault.sol - Silo Vaults
- [smart_contract] https://sonicscan.org/address/0xE83fDb15b5efeD3E3D3FD2a086219c33686b7231 — ShareDebtToken.sol - Silo Lending
- [smart_contract] https://sonicscan.org/address/0xff1d0359CAd3BC603584A63D852D884BF5b17A67 — SiloRouterV2.sol

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

## Impacts in scope (16)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Miner-extractable value (MEV)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3). 

All Critical/High severity smart contract bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

Rewards for critical smart contract vulnerabilities are further capped at 10% of economic damage, with the main consideration being the funds affected in addition to PR and brand considerations, at the discretion of the team. However, there is a minimum reward of __USD 20 000__ and a maximum of __USD 100 000__ for Critical smart contract bug reports.


__Repeatable Attack Limitations__
- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

- For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

- High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of 1,000 to 20,000 depending on the funds at risk, capped at the maximum high reward.  

- In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

Payouts are handled by the __Silo Finance__ team directly and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

- Best practice critiques
- Missing Heartbeat/Staleness Validation (ie. Chainlink) is out of scope for all oracles.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (2)

- All issues publicly disclosed by audits reports hosted in smart contracts repository are considered known issues. (https://github.com/silo-finance/silo-contracts-v3/tree/master/audits)
- For all known issues, read all audit reports before submitting a bounty report. (https://docs.silo.finance/docs/audits)
