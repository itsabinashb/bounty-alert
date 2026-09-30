# DeFi Saver

- Page: https://immunefi.com/bug-bounty/defisaver/scope/
- Max bounty: $350,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, websites_and_applications - critical
- End date: (none)

## Assets in scope (2)

- [smart_contract] https://github.com/defisaver/defisaver-v3-contracts/tree/main/contracts — Defi Saver V3 (excluding the 'mocks' and 'views' folders)
- [websites_and_applications] https://app.defisaver.com/

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

## Impacts in scope (25)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Miner-extractable value (MEV)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [websites_and_applications] Critical: Ability to execute system commands
- [websites_and_applications] Critical: Bypassing Authentication
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Extract Sensitive data/files from the server such as /etc/passwd
- [websites_and_applications] Critical: Redirection of user deposits and withdrawals
- [websites_and_applications] Critical: Signing transactions for other users
- [websites_and_applications] Critical: Stealing User Cookies
- [websites_and_applications] Critical: Subdomain takeover resulting in financial loss (applicable for subdomains with addresses published)
- [websites_and_applications] Critical: Submitting malicious transactions to an already-connected wallet
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Tampering with transactions submitted to the user’s wallet
- [websites_and_applications] Critical: Wallet interaction modification resulting in financial loss

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$350,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: fixedReward=$30,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$10,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$20,000, otherImpactMaxReward=$0, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

All web/app bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. All High and Critical Smart Contract bug reports require a PoC to be eligible for a reward. Explanations and statements are not accepted as PoC and code is required.

Critical smart contract vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk, but also PR and branding aspects, at the discretion of the team. However, there is a minimum reward of __USD 50 000__.

All vulnerabilities marked in the [security reviews](https://github.com/DecenterApps/defisaver-v3-contracts/tree/main/audits) are not eligible for a reward.

Payouts are handled by the __Defi Saver__ team directly and are denominated in USD. However, payouts are done in __DAI and USDC__, with the choice of the ratio at the discretion of the team.

## Out of scope (program-specific)

- Lack of SSL/TLS best practices
 - DDoS vulnerabilities
 - Attacks requiring privileged access from within the organization
 - Feature requests
 - Best practice critiques
 - Customer support pop-up (aka Helpcrunch integration)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
