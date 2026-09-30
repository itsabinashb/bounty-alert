# Flux Finance

- Page: https://immunefi.com/bug-bounty/fluxfinance/scope/
- Max bounty: $550,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (9)

- [smart_contract] https://etherscan.io/address/0x1C9A2d6b33B4826757273D47ebEe0e2DddcD978B — fFRAX
- [smart_contract] https://etherscan.io/address/0x1dD7950c266fB1be96180a8FDb0591F70200E018 — fOUSG
- [smart_contract] https://etherscan.io/address/0x2c5898da4DF1d45EAb2B7B192a361C3b9EB18d9c — Timelock
- [smart_contract] https://etherscan.io/address/0x336505EC1BcC1A020EeDe459f57581725D23465A — GovernorBravoDelegator
- [smart_contract] https://etherscan.io/address/0x465a5a630482f3abD6d3b84B39B29b07214d19e5 — fUSDC
- [smart_contract] https://etherscan.io/address/0x81994b9607e06ab3d5cF3AffF9a67374f05F27d7 — fUSDT
- [smart_contract] https://etherscan.io/address/0x95Af143a021DF745bc78e845b54591C53a8B3A51 — Unitroller
- [smart_contract] https://etherscan.io/address/0xba9b10f90b0ef26711373a0d8b6e7741866a7ef2 — OndoPriceOracle V2
- [smart_contract] https://etherscan.io/address/0xe2bA8693cE7474900A045757fe0efCa900F6530b — fDAI

## Asset notes

In some cases, only the proxy contracts are listed as in-scope; however, current implementation and any further updates to the implementation are considered in scope. When reporting a bug, please make sure to select the relevant proxy smart contract as the target. 

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program. 

If an impact can be caused to any other asset managed by Flux Finance that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project.

## Impacts in scope (14)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Miner-extractable value (MEV)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 24 hours
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Smart contract fails to deliver promised returns, but doesn't lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$550,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: fixedReward=$25,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$10,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the[  Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2/). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported. 

All bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. Bug reports are required to include a runnable PoC in order to prove impact. Exceptions may be made in cases where the vulnerability is objectively evident from simply mentioning the vulnerability and where it exists. However, the bug reporter may be required to provide a PoC at any point in time.

Rewards for critical smart contract vulnerabilities are further capped at 10% of economic damage, with the main consideration being the funds affected in addition to PR and brand considerations, at the discretion of the team. However, there is a minimum reward of USD 25 000 for Critical smart contract bug reports.

The following known issues are also considered out of scope of this program:
- Effects from blacklists (e.g. KYC revoked, USDC blacklist), if the effect only impacts the specific user.
- Impact of KYC or sanctions status changes on borrower liquidation
- Effects from using hypothetical use of tokens that do not follow the ERC-20 standard or include unusual behavior (e.g. transfer tax). If a token has certain functionality but that functionality is currently disabled, the effect will also be considered out of scope.
- Misuse of admin rights (e.g. malicious admin multi-sig)
- The protocol is forked from CompoundV2. The fToken contracts are forked from this [commit](https://github.com/compound-finance/compound-protocol/tree/a3214f67b73310d547e00fc578e8355911c9d376). All other contracts (Comptroller, CErc20Delegator, InterestRateModel, etc.) are forked from this [commit](https://github.com/compound-finance/compound-protocol/tree/3affca87636eecd901eb43f81a4813186393905d). Bug reports covering previously-discovered bugs are not eligible for the program. If a bug report covers a known issue, it may be rejected together with proof of the issue being known before escalation of the bug report. Previous audits of CompoundV2 can be found at: [https://docs.compound.finance/v2/security/#audits](https://docs.compound.finance/v2/security/#audits)
- Any known issues in CompoundV2 up to these commits are considered out of scope. This includes, but is not limited to:
   - First deposit bug when a market is initialized - example [video](https://youtu.be/_pO2jDgL0XE?t=157)
   - Discrepancy in borrow rate per block on-chain vs. displayed APY in the UI

Payouts are handled by the __Flux Finance__ team directly and are denominated in USD. However, payouts are done in __USDC__.  The payment will be made by Flux Finance (the entity).

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
