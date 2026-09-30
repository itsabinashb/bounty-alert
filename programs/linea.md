# Linea

- Page: https://immunefi.com/bug-bounty/linea/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (10)

- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/a83412e247b7d352b905c906271138e97c1ee5a4/contracts/contracts/LineaRollup.sol — Rollup LineaRollup.sol
- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/a83412e247b7d352b905c906271138e97c1ee5a4/contracts/contracts/ZkEvmV2.sol — Rollup ZkEVMv2.sol
- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/a83412e247b7d352b905c906271138e97c1ee5a4/contracts/contracts/messageService/l2/L2MessageService.sol — L2MessageService.sol
- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/a83412e247b7d352b905c906271138e97c1ee5a4/contracts/contracts/tokenBridge/TokenBridge.sol — TokenBridge.sol
- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/a9a43aafe9004c043b61063373264e2c9217a978/contracts-tge/src/L1/LineaToken.sol — L1 LineaToken
- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/a9a43aafe9004c043b61063373264e2c9217a978/contracts-tge/src/L2/L2LineaToken.sol — L2 LineaToken
- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/main/contracts/src/yield/LidoStVaultYieldProvider.sol — Contract to handle native yield operations with Lido Staking Vault
- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/main/contracts/src/yield/LidoStVaultYieldProviderFactory.sol — Deploys LidoStVaultYieldProvider contract
- [smart_contract] https://github.com/Consensys/linea-monorepo/blob/main/contracts/src/yield/YieldManager.sol — Contract to handle native yield operations
- [smart_contract] https://immunefi.com/bug-bounty/linea/scope/#top (primacy of impact)

## Asset notes

(none)

## Impacts in scope (5)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$100,000, rewardCalculationPercentage=0, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below.

__Repeatable Attack Limitations__

In cases of repeatable attacks or attacks stemming from the same root cause, for smart contract bugs, only the first attack will be counted, regardless of whether the smart contract is upgradable, pausable, or killable.

__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Smart Contract - Critical
- Smart Contract - Medium
- Smart Contract - Low

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules) Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

Payouts are handled by the Consensys team directly and are denominated in USDC.

## Out of scope (program-specific)

- Impacts caused by incorrectly provided user data (e.g. wrong fees, values or addresses etc.)
- External 3rd party systems not maintained by Linea
- Typographical errors
- Gas optimizations

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Linea prioritizes withdrawal availability over yield efficiency. (https://diligence.security/audits/2025/12/linea-yield-manager/#inconsistent--_pausestakingifnotalready-conditions-in-withdrawal-functions)
