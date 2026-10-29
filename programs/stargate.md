# Stargate

- Page: https://immunefi.com/bug-bounty/stargate/scope/
- Max bounty: $3,500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - medium
- End date: (none)

## Assets in scope (5)

- [smart_contract] https://etherscan.io/address/0x72fAEbF58A62e33C044c37D8D973a961633ea294#code — TransferDelegate (EVM)
- [smart_contract] https://etherscan.io/address/0xAcdDAC6C77318B615f7F6fB9bb67c6833e9c05f1 — lzMultiCall (EVM)
- [smart_contract] https://explorer.solana.com/address/BRoueHsu3h2SfEse9ohXipm1R9uRGRSe3zPYsAT8RySr — lzMultiCall (Solana)
- [smart_contract] https://github.com/stargate-protocol/stargate-v2/tree/main/packages/stg-evm-v2/deployments — StargateV2 Deployments
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (4)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$3,500,000, minReward=$100,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$1, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

All bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. Bug reports are required to include a runnable PoC in order to prove impact. Exceptions may be made in cases where the vulnerability is objectively evident from simply mentioning the vulnerability and where it exists. However, the bug reporter may be required to provide a PoC at any point in time.

All non-critical rewards for the project bug bounty program are scaled based on an internally established team criteria, taking into account the exploitability of the bug, the impact it causes, and the likelihood of the vulnerability presenting itself, which is especially factored in with bug reports requiring multiple conditions to be met that are currently not in-place. Rewards will be provided at the determined fair value by the team depending on these conditions, assuming that the bug report is in-scope of the bug bounty program.

LayerZero requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed are: 
- Invoice is required with Name, Address, and Payment Instructions
- Proof of address (either a redacted bank statement with your address or a recent utility bill with your name, address, and issuer of the bill)
- Copy of your passport or other Government ID will be required

The collection of this information will be done by the project team.

Payouts are handled by LayerZero directly and are denominated in USD. However, payouts are done in Fiat USD via wire transfer, USDC, or USDT, with the choice of ratio at the discretion of the team.

## Out of scope (program-specific)

- LayerZero Offchain Infrastructure
- Sybil Attacks
- Impacts to assets as a result of their own misconfiguration
- Impacts as a result of a chain-level issue
- Reports regarding bugs that LayerZero was previously aware of are not eligible for a reward
- Dependencies & Third Party Code
- Temporary impacts resulting from configuration adjustment race-conditions

__Previous Audits__

Stargate’s completed audit reports can be found at [https://stargateprotocol.gitbook.io/stargate/v2-developer-docs/security/audit](https://stargateprotocol.gitbook.io/stargate/v2-developer-docs/security/audit). Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
