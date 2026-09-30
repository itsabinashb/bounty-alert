# MUX

- Page: https://immunefi.com/bug-bounty/mux/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: yes
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, smart_contract - critical
- End date: (none)

## Assets in scope (15)

- [smart_contract] https://github.com/mux-world/mux-aggregator-protocol
- [smart_contract] https://github.com/mux-world/mux-aggregator-protocol/tree/main/contracts/aggregators/gmxV2
- [smart_contract] https://github.com/mux-world/mux-aggregator-protocol/tree/main/contracts/proxyFactory
- [smart_contract] https://github.com/mux-world/mux-degen-protocol
- [smart_contract] https://github.com/mux-world/mux-protocol/tree/main/contracts/components
- [smart_contract] https://github.com/mux-world/mux-protocol/tree/main/contracts/core
- [smart_contract] https://github.com/mux-world/mux-protocol/tree/main/contracts/governance
- [smart_contract] https://github.com/mux-world/mux-protocol/tree/main/contracts/libraries
- [smart_contract] https://github.com/mux-world/mux-protocol/tree/main/contracts/orderbook
- [smart_contract] https://github.com/mux-world/mux-staking
- [smart_contract] https://github.com/mux-world/mux3-protocol/
- [websites_and_applications] https://app.mux.network/#/liquidity
- [websites_and_applications] https://app.mux.network/#/redeem
- [websites_and_applications] https://app.mux.network/#/stake
- [websites_and_applications] https://app.mux.network/#/trade?chainId=42161

## Asset notes

Only web/app vulnerabilities that __directly__ affect the web/app assets listed in this table and their subfolders are accepted within the bug bounty program. All others are out-of-scope.

Under the Github link, only mainnet smart contract vulnerabilities are considered in-scope for the bug bounty program. Smart contracts labeled as testnet are out-of-scope. Additionally, __all smart contracts in the test, oracle, and reader folders are out-of-scope__. 

Vulnerabilities surfaced in the audits provided by [ConsenSys](https://diligence.consensys.net/audits/private/nxaosool-mcdexio-mai-protocol-v2), [OpenZeppelin](https://blog.openzeppelin.com/mcdex-mai-protocol-audit/) and [Quantstamp](https://certificate.quantstamp.com/full/mcdex) are not considered in scope of the bug bounty program even if they affect the assets listed in this table.

## Impacts in scope (24)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of >1% of user funds, other than unclaimed yield, in excess of gas costs or swap fees
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of >1% of total funds in excess of gas costs or swap fees
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Theft of >1% of total unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Permanent freezing of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds
- [websites_and_applications] Critical: Direct theft of >1% of total user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as /etc/shadow, database passwords, and blockchain keys(this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as, changing registration information, commenting, voting, making trades, withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as email or password of the victim, etc.
- [websites_and_applications] High: Improperly disclosing confidential user information such as email address, phone number, physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the name of user, or enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as reflected HTML injection or loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, minReward=$2,000, rewardModel=range
- [websites_and_applications] Critical: maxReward=$15,000, minReward=$7,500, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$5,000, rewardModel=up_to
- [websites_and_applications] Medium: maxReward=$1,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

All web and app bugs must come with a Proof of Concept (PoC) in order to be accepted. All web and app bug reports without a PoC will be rejected with a request for a PoC. Critical web and app bugs can only be paid the full USD 15 000 if there is a vulnerability directly leading to a loss in user funds that don’t require social engineering or extensive non-normal user actions. 

Rewards for smart contract vulnerabilities are variable based on their exploitability, and other factors deemed relevant by the MUX team. For critical vulnerabilities, the payout is capped at 10% of economic damage and is the main determinant of the reward amount. Bug reports for critical vulnerabilities also require PoC. If no PoC is submitted but the bug is still validated and addressed, only USD 20 000 will be rewarded regardless of economic damage. 

Recommendations for fixes are required for a reward. Though bug reports without recommendations for fixes may be considered, the resulting reward cannot be the maximum amount. 

The final decision for all rewards are at the discretion of MUX Protocol. 

Payouts are handled by the __MUX Protocol__ team directly and are denominated in USD. Payouts are done in __USDC__. However, for payouts USD 1 000 and lower, the reward can be paid in __ETH__.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
