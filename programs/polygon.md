# Polygon

- Page: https://immunefi.com/bug-bounty/polygon/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Smart Contract
- PoC required for: smart_contract - high, blockchain_dlt - high, smart_contract - medium, blockchain_dlt - critical, smart_contract - critical
- End date: (none)

## Assets in scope (13)

- [blockchain_dlt] https://github.com/0xPolygon/bor/releases/latest — Polygon POS - Bor
- [blockchain_dlt] https://github.com/0xPolygon/cometbft/releases/latest — Polygon POS - Commet BFT
- [blockchain_dlt] https://github.com/0xPolygon/cosmos-sdk/releases/latest — Polygon POS - Cosmos SDK
- [blockchain_dlt] https://github.com/0xPolygon/heimdall-v2/releases/latest — Polygon POS - Heimdall
- [blockchain_dlt] https://immunefi.com/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://etherscan.io/address/0x046Bb8bb98Db4ceCbB2929542686B74b516274b3 — LXLY AggLayer Gateway
- [smart_contract] https://etherscan.io/address/0x2a3DD3EB832aF982ec71669E178424b10Dca2EDe — LXLY AggLayer PolygonBridgeV2
- [smart_contract] https://etherscan.io/address/0x5132A183E9F3CB7C848b0AAC5Ae0c4f0491B7aB2 — LXLY Agglayer PolygonRollupManager
- [smart_contract] https://etherscan.io/address/0x580bda1e7a0cfae92fa7f6c20a3794f169ce3cfb — LXLY Agglayer PolygonGlobalExitRoot
- [smart_contract] https://github.com/0xPolygon/security/blob/main/scope-pol-token.md — POL Token
- [smart_contract] https://github.com/0xPolygon/security/blob/main/scope-pos-contracts.md — POS Bridge & Staking
- [smart_contract] https://github.com/0xPolygon/security/blob/main/scope-spol-contracts.md — POL LST: sPOL
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

Impacts only apply to assets in active use by the project like contracts on mainnet or web/app assets used in production. 

**For GitHub repositories please ensure you are reviewing the latest published releases and not the default branch**

Any impact that applies to assets not in active use, like test or mock files, are out-of-scope of the bug bounty program unless explicitly mentioned as in-scope. In the case of Smart Contracts, please always make sure the code has been deployed and present in scope md files.

__Blockchain/DLT__

  - __Blockchain/DLT - PoC__, Blockchain/DLT bug reports are to include a runnable Proof of Concept (PoC) in order to prove impact.  
  - For more information on PoCs please visit: [Proof of Concept (PoC) Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

  - __Smart Contracts - PoC__, Smart Contract bug reports are to include a runnable Proof of Concept (PoC) in order to prove impact.  
  - For more information on PoCs please visit: [Proof of Concept (PoC) Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

__Dev Environment and Documentation__ 

Polygon Labs has included dev documentation and/or instructions to help in reviewing code and looking for bugs:

| __Dev or Staging Environment Links__     |
| ---------- |
| https://docs.polygon.technology/](https://docs.polygon.technology/)        |

## Impacts in scope (12)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] High: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] High: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] High: Transient consensus failures
- [blockchain_dlt] Medium: Denial of service attacks
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Loss of bridge or staking funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of user fees
- [smart_contract] Medium: Denial of service attacks
- [smart_contract] Medium: Temporary freezing of funds for less than 1 week

## Impact notes

__Important notes:__
- You must be able to prove the real exploitability/severity of a report without doubt or assumptions, and based on the current state of the blockchain at the time of the report.
- Reports are classified by Impact and Likelihood/Probability and using common frameworks such as CVSS. The combination determines the severity and are determined at Polygon’s sole discretion.
- Actual reward amounts are determined at Polygon’s sole discretion. Factors influencing payout include report quality, completeness, and severity/exploitability.

__Severity Table__

Reports are classified using two dimensions: Impact and Probability (Likelihood) and classified using the following table

|                    | Low Impact | Medium Impact | High Impact |
|--------------------|------------|----------------|--------------|
| **High Probability**   | MEDIUM     | HIGH           | CRITICAL     |
| **Medium Probability** | LOW        | MEDIUM         | HIGH         |
| **Low Probability**    | LOW        | LOW            | MEDIUM       |

__Understanding Probability__

Reports are classified using two dimensions: Impact and Probability (Likelihood). Probability reflects how permissionless and reliably the issue can be exploited against the current production deployment. Critical severity requires both High Impact and High Probability (i.e., a permissionless exploit that can be executed at will).

High Probability
- Permissionless: no privileged role/allowlist or compromised keys required.
- Exploitable at will on production (reliable/repeatable under normal conditions).

Medium Probability
- Exploitable, but requires realistic preconditions (e.g., specific state/timing, meaningful capital/positioning, or common MEV/order-dependence).
- May not succeed every attempt; depends on conditions outside the attacker's full control.

Low Probability

- Requires rare edge conditions or strong assumptions (e.g., very narrow timing, unlikely state/user behavior).
- Hard to reproduce reliably / low success rate in practice.

__Impacts to other assets__ 

Hackers are encouraged to submit issues outside of those outlined Impacts and Assets in Scope. 

If Whitehats can demonstrate a critical impact of code in production for an asset not in scope, Polygon Labs encourages you to submit your bug report using the “primacy of impact exception” asset as outlined below.

## Rewards

- [blockchain_dlt] Critical: maxReward=$250,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: fixedReward=$10,000, rewardModel=fixed
- [blockchain_dlt] Medium: fixedReward=$2,000, rewardModel=fixed
- [smart_contract] Critical: maxReward=$250,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: fixedReward=$10,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$2,000, rewardModel=fixed

## Reward notes

__Reward Distribution__

Payouts over the lower bound reward are directly related to the direct funds at risk. If no funds are at risk, the Critical or High payouts are limited to the minimum, unless decided otherwise by Polygon Labs.

For the purposes of clarification, funds at risk refer to the proof of loss of funds.

Rewards for critical Blockchain/DLT and smart contract bug reports will be further capped at 10% of direct funds at risk if the bug discovered is exploited. However, there is a minimum reward of __USD 50 000__.

__Payouts and Payout Requirements__

Payouts are handled by the Polygon Labs team directly and are denominated in USD. Payouts are done in USDC or POL at the Polygon Labs teams' discretion. Polygon Labs commits to honoring payouts according to the terms set out in this program at the time of report submission, and to treat this program as the agreement and source of truth concerning bug reports and responsible disclosures. 

POL Payouts will be determined using TWAP 5 day price calculated from payment date.

Polygon Labs requires an invoice to be received for each payout. An invoice template can be provided by Polygon Labs.

This bug bounty program is only open to individuals who reside outside of the countries that are restricted by OFAC and by UNSC resolutions. If the individual is a US person, tax information may be required in order to properly issue a 1099.

Polygon Labs requires an invoice to be received for each payout. An invoice template can be provided by Polygon Labs.

__KYC Requirements__

Polygon Labs does have a Know Your Customer (KYC) requirement for bug bounty payouts. 

| __KYC Info Required__     |
| ---------- |
| Wallet Address       |
| Passport |
| Place of residence |

KYC information is only required on confirmation of the validity of a bug report which Polygon Labs determines in its sole discretion.

## Out of scope (program-specific)

- Vulnerabilities in unmodified upstream dependencies (e.g., go-ethereum, Cosmos SDK, CometBFT, Tendermint) that are not introduced by Polygon Labs modifications.
  - Broken link hijacking is out of scope
  - Loss of funds held by third parties
  - Best practice critiques
  - Attacks using vulnerable, old or deprecated libraries, that are not exploitable

__Smart Contracts and Blockchain/DLT__

- Previously known vulnerabilities (resolved or not) on the Ethereum network (and any other fork of these).
- Previously known vulnerabilities in Tendermint and or/any other fork of these.
- Previously known vulnerabilities in cosmos-sdk and or/any other fork of these.
- Basic economic governance attacks (e.g. 51% attack)
- Lack of liquidity
- Best practice critiques
- Sybil attacks
- Centralization risks
- Attacks using vulnerable, old or deprecated libraries, that are not exploitable

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (3)

- Any external tokens are expected to correctly follow their standards. Tokens are expected not to have non-standard functionalities such as fees on transfer, blacklists, etc. Rebasing tokens specifically are not supported (https://www.chainsecurity.com/reports/Polygon/ChainSecurity_Polygon_PoSPortal_Audit.pdf)
- CS-POLYGON-SPOL-006 "Bridge Liquidity on L1" (https://github.com/0xPolygon/sPOL-contracts/blob/main/audits/1.0.0/ChainSecurity_Polygon_SPOL_Audit.pdf)
- CS-POLYGON-SPOL-024 Migration Completion Can Be Front-Run (https://github.com/0xPolygon/sPOL-contracts/blob/main/audits/1.0.0/ChainSecurity_Polygon_SPOL_Audit.pdf)
