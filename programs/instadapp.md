# Instadapp

- Page: https://immunefi.com/bug-bounty/instadapp/scope/
- Max bounty: $500,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - high, smart_contract - critical, websites_and_applications - critical, websites_and_applications - high
- End date: (none)

## Assets in scope (6)

- [smart_contract] https://github.com/Instadapp/avocado-contracts-public — Avocado (excluding the helper folder within avo-contracts)
- [smart_contract] https://github.com/Instadapp/dsa-contracts — Instadapp Pro
- [smart_contract] https://github.com/Instadapp/fluid-contracts-public — Fluid Liquidity Layer, Fluid Lending protocol, Fluid Vault protocol. Fluid Contracts (excluding periphery folder)
- [smart_contract] https://github.com/Instadapp/inst-governance — Governance
- [websites_and_applications] https://avocado.instadapp.io — Avocado
- [websites_and_applications] https://fluid.instadapp.io/ — Fluid

## Asset notes

Only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

All folders and files labeled with the words “test”, “mock/mocks”, or “dummy” are out-of-scope of the bug bounty program.

## Impacts in scope (22)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield (Connectors are out of scope from this)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Miner-extractable value (MEV)
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds (more than 10 Days)
- [smart_contract] High: Theft of unclaimed yield
- [websites_and_applications] Critical: Ability to execute system commands
- [websites_and_applications] Critical: Bypassing Authentication
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Extract Sensitive data/files from the server such as /etc/password
- [websites_and_applications] Critical: Redirection of user deposits and withdrawals
- [websites_and_applications] Critical: Signing transactions for other users
- [websites_and_applications] Critical: Subdomain takeover resulting in financial loss (applicable for subdomains with addresses published)
- [websites_and_applications] Critical: Submitting malicious transactions to an already-connected wallet
- [websites_and_applications] Critical: Tampering with transactions submitted to the user’s wallet
- [websites_and_applications] Critical: Wallet interaction modification resulting in financial loss
- [websites_and_applications] High: Privilege escalation to access unauthorized functionalities
- [websites_and_applications] High: Spoofing content on the target application (Persistent)
- [websites_and_applications] High: Third-Party API keys leakage that demonstrates loss of funds or modification on the website
- [websites_and_applications] High: Users Confidential information disclosure such as Email

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$500,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] Critical: maxReward=$50,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$10,000, minReward=$5,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

__Reward Calculation for Critical Level Reports__

For critical smart contract vulnerabilities, the reward is 10% of the directly affected funds, up to a maximum of USD 500,000. The calculation considers the funds at risk based on the bug report submission date and time. There is a minimum guaranteed reward of USD 25,000 to encourage reporting even for smaller valued critical bugs.


__Reward Calculation for High Level Reports__

For high smart contract impacts, the reward is capped at $100,000 and is based on 50% of the value of the affected funds. The calculation considers the funds at risk based on the bug report submission date and time. There is a minimum guaranteed reward of USD 5,000 to encourage reporting even for smaller valued high severity bugs.

__Secondary/Market Attack on Fluid__

Fluid as a lending protocol utilizes different aspects of the blockchain which may indirectly affect the protocol. The following outline conditions for particular secondary attacks that are not directly on the Fluid contracts, but that have secondary or associated effects to the Fluid contracts may be considered for a reward:

- The attack must directly impact Fluid i.e an attack which affects the broader market such as price manipulation but is not targeting Fluid would not qualify.

Examples of secondary attacks would be:

- Manipulation of a DEX or on Chain price oracle from a secondary source, which results in the immediate and total loss of funds of the Fluid protocol, where the attack is specifically targeting Fluid protocol.
- Flash Loan based attack that would cause immediate and irreversible financial loss to Fluid protocol; where the attack is specifically targeting the Fluid protocol, this would exclude attacks which manipulate the price of a single token used on Fluid.

__Repeatable Attacks on Pausable Contracts__

Fluid contracts can be paused by the protocol guardians. Where the vulnerable contract can be paused or upgraded, only the initial attack is considered for the reward, as Fluid can mitigate further exploitation by pausing or upgrading the affected component; repeated or looped extraction after the first attack is not compounded into severity or reward. For contracts that cannot be paused or upgraded, the Repeatable Attack Limitations configured for this program apply (25% reduction per additional attack, 1-hour interval).

__Audits__

Prior published audits are here for review, any noted vulnerability or bugs in previously completed audits are not eligible for a reward.

Defi Smart Accounts (DSA)/Instadapp PRO
- [Peckshield - Mar 16, 2021](https://github.com/Instadapp/dsa-contracts/blob/master/audits/v2_PeckShield_Mar_2021.pdf)
- [Peckshield - Mar 18, 2020](https://github.com/Instadapp/dsa-contracts/blob/master/audits/v1_PeckShield_Mar_2020.pdf)
- [Samczun Audit - Mar 2020](https://github.com/Instadapp/dsa-contracts/blob/master/audits/v1_samczsun_Mar_2020.md)

Avocado
- [Statemind - Sept 28, 2023](https://github.com/Instadapp/avocado-audits/blob/main/Statemind-Audit-Report-Avocado-v3.pdf)
- [Peckshield - June 12, 2023](https://github.com/Instadapp/avocado-audits/blob/main/PeckShield-Audit-Report-Avocado-v3.pdf)

Fluid
- [Statemind - Dec 29th, 2023](https://github.com/statemindio/public-audits/blob/main/Instadapp/2023-12-29_Instadapp_Fluid.pdf)

__Proof of Concept (PoC) Requirements__

A Proof of Concept is required for all severity levels (Critical, High, Medium and Low), for every asset type in scope.

When calculating the USD value of total value locked (TVL) to determine funds at risk, outstanding borrows are excluded.

To be eligible for a reward, the vulnerability must exist in the deployed smart contract.

Bugs resulting in temporary freezing of funds for under 10 days are not eligible for a reward. Temporary freezing of funds for more than 10 days is assessed under the in-scope High impact.

Payouts are handled by the Instadapp team directly. Payouts are made in USDC, USDT or DAI on Ethereum, denominated in USD.

__Scope Clarifications__

- Issues affecting the first or last user of a pool or vault that arise from dust amounts, in any protocol other than DexV2, are classified at most as Low, since the standard production setup includes seeding a dust position that serves as the first and last user.

- A vulnerability present in both the EVM and Solana codebases is treated as a single finding and rewarded once, not as two separate reports.

- Deployed contract addresses are listed in [deployments.md](https://github.com/Instadapp/fluid-contracts-public/blob/main/deployments/deployments.md) in the public repository; funds at risk is assessed against the deployed contracts referenced there.

## Out of scope (program-specific)

- Best practice critiques
  - Griefing involving gas fees alone
  - DexLite Protocol: https://github.com/Instadapp/fluid-contracts-public/tree/main/contracts/protocols/dexLite
- Chainlink oracle feed `updatedAt` staleness check on Oracles V1
- Chainlink oracle feed reporting a negative price on Oracles V1
- Avocado: input asymmetry between `signMessage` and `removeSignedMessage`
- Avocado: additional information in the signing screens are new features, not security bugs

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
