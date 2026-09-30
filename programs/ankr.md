# Ankr

- Page: https://immunefi.com/bug-bounty/ankr/scope/
- Max bounty: $500,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium
- End date: (none)

## Assets in scope (7)

- [smart_contract] https://bscscan.com/address/0x52F24a5e03aee338Da5fd9Df68D2b6FAe1178827 — ankrBNB
- [smart_contract] https://bscscan.com/address/0x9e347Af362059bf2E55839002c699F7A5BaFE86E — BNB Pool
- [smart_contract] https://bscscan.com/token/0x67428dE0680494E448F1A19d33C2022a51719348 — BNBStakingConfig
- [smart_contract] https://etherscan.io/address/0x84db6eE82b7Cf3b47E8F19270abdE5718B936670 — ETH Pool
- [smart_contract] https://etherscan.io/token/0xE95A203B1a91a908F9B9CE46459d101078c2c3cb#code — aETHc
- [smart_contract] https://etherscan.io/token/0xd01ef7c0a5d8c432fc2d1a85c66cf2327362e5c6#code — aETHb
- [websites_and_applications] https://www.ankr.com/staking/* — Main Web App

## Asset notes

Only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

Though only the proxy contracts are listed as in-scope, current implementation and any further updates to the implementation contracts are considered in scope. When reporting a bug, please make sure to select the relevant proxy smart contract as the target. 

If an impact can be caused to any other asset managed by Ankr that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project. This only applies to Critical impacts.

## Impacts in scope (27)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Miner-extractable value (MEV)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 30 days
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as /etc/shadow, database passwords, and blockchain keys(this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as, changing registration information, commenting, voting, making trades, withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as email or password of the victim, etc.
- [websites_and_applications] High: Improperly disclosing confidential user information such as email address, phone number, physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc.
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the first/last name of user, or en/disabling notification
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as reflected HTML injection or loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$500,000, rewardCalculationPercentage=0, rewardModel=up_to
- [smart_contract] High: maxReward=$50,000, rewardModel=up_to
- [smart_contract] Medium: maxReward=$5,000, rewardModel=up_to
- [smart_contract] Low: maxReward=$1,000, rewardModel=up_to
- [websites_and_applications] Critical: maxReward=$10,000, otherImpactMaxReward=$0, rewardModel=up_to
- [websites_and_applications] High: maxReward=$5,000, rewardModel=up_to
- [websites_and_applications] Medium: maxReward=$2,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the  [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All web/app bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

Critical smart contract vulnerabilities are capped at 5% of economic damage, primarily taking into consideration funds at risk. However, there is a minimum reward of __USD 10 000__. 

All other rewards for the Ankr bug bounty program are scaled based on an internally established team criteria, taking into account the exploitability of the bug, the impact it causes, and the likelihood of the vulnerability presenting itself, which is especially factored in with bug reports requiring multiple conditions to be met that are currently not in-place. However, there is a minimum reward of __USD 1 000__ for each severity level, rewards will be provided at the determined fair value by the team depending on these conditions, assuming that the bug report is in-scope of the bug bounty program.

The following vulnerabilities marked in [https://www.ankr.com/docs/staking/extra/audit-reports/](https://www.ankr.com/docs/staking/extra/audit-reports/) are not eligible for a reward.

Payouts are handled by the Ankr team directly and are denominated in USD. However, payouts are done in __ANKR, USDT and USDC__, with the choice of the ratio at the discretion of the team.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
