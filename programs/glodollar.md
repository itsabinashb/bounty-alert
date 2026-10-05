# Glo Dollar

- Page: https://immunefi.com/bug-bounty/glodollar/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (4)

- [smart_contract] https://etherscan.io/address/0x4F604735c1cF31399C6E711D5962b2B3E0225AD3 — ERC1967Proxy for USDGLO on Ethereum
- [smart_contract] https://etherscan.io/address/0xf8dbe4f52b7d4fe90cd360aa4f49b7a66783c56f — current implementation contract of USDGLO on Ethereum
- [smart_contract] https://polygonscan.com/address/0x4F604735c1cF31399C6E711D5962b2B3E0225AD3 — ERC1967Proxy for USDGLO on Polygon
- [smart_contract] https://polygonscan.com/address/0xf8dbe4f52b7d4fe90cd360aa4f49b7a66783c56f — current implementation contract of USDGLO on Polygon

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

If an impact can be caused to any other asset managed by Global Income Coin that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project. This only applies to Critical impacts.

## Impacts in scope (12)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Miner-extractable value (MEV)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Smart contract fails to deliver promised returns, but doesn’t lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$50,000, rewardCalculationPercentage=0, rewardModel=fixed
- [smart_contract] High: fixedReward=$2,500, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$1,250, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All High and Critical Smart Contract bug  reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

Glo requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed are name, address, date and full amount you claim, clearly stated on an invoice. The collection of this information will be done by the project team.

Payouts are handled by the __Glo__ team directly and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
