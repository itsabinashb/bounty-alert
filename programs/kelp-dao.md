# Kelp DAO

- Page: https://immunefi.com/bug-bounty/kelp-dao/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (11)

- [smart_contract] https://etherscan.io/address/0x036676389e48133B63a802f8635AD39E752D375D — LRT Deposit Pool
- [smart_contract] https://etherscan.io/address/0x07b96cf1183c9bff2e43acf0e547a8c4e4429473 — NodeDelegator
- [smart_contract] https://etherscan.io/address/0x349A73444b1a310BAe67ef67973022020d70020d — LRT Oracle
- [smart_contract] https://etherscan.io/address/0x3D08ccb47ccCde84755924ED6B0642F9aB30dFd2 — EthXPriceOracle
- [smart_contract] https://etherscan.io/address/0x598dbcb99711e5577ff76ef4577417197b939dfa — LRTConverter
- [smart_contract] https://etherscan.io/address/0x62De59c08eB5dAE4b7E6F7a8cAd3006d6965ec16 — LRTWithdrawalManager
- [smart_contract] https://etherscan.io/address/0x947Cb49334e6571ccBFEF1f1f1178d8469D65ec7 — LRT Config
- [smart_contract] https://etherscan.io/address/0xA1290d69c65A6Fe4DF752f95823fae25cB99e5A7 — rsETH
- [smart_contract] https://etherscan.io/address/0xc66830e2667bc740c0bed9a71f18b14b8c8184ba — LRTUnstakingVault
- [smart_contract] https://etherscan.io/address/0xdbc3363de051550d122d9c623cbaff441afb477c — FeeReceiver
- [websites_and_applications] https://kelpdao.xyz/restake — Restaking

## Asset notes

(none)

## Impacts in scope (28)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Permanent freezing of unclaimed yield
- [smart_contract] Medium: Temporary freezing of funds
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Block stuffing
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [websites_and_applications] Critical: Changing NFT metadata
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:  Modifying transaction arguments or parameters Substituting contract addresses Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:   /etc/shadow database passwords blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:   Changing registration information Commenting Voting Making trades Withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:  Email Password of the victim etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:  HTML injection without JavaScript Replacing existing text with arbitrary text Arbitrary file uploads, etc
- [websites_and_applications] High: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] High: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Improperly disclosing confidential user information, such as:  Email address Phone number Physical address, etc.
- [websites_and_applications] Medium: Taking down the application/website
- [websites_and_applications] Low: Changing details of users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:  Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Changing non-sensitive details of users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: Changing the first/last name of user Enabling/disabling notifications
- [websites_and_applications] Low: Injecting/modifying the static content on the target application without JavaScript (reflected), such as: Reflected HTML injection Loading external site data
- [websites_and_applications] Low: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:  Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:  Locking up the victim from login Cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$250,000, minReward=$100,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$50,000, rewardModel=range
- [smart_contract] Medium: maxReward=$50,000, minReward=$11,000, rewardModel=range
- [smart_contract] Low: fixedReward=$10,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$25,000, minReward=$10,000, otherImpactMaxReward=$20,000, rewardModel=range
- [websites_and_applications] High: fixedReward=$5,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 250 000. 

The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. 

However, a minimum reward of USD 100 000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. 

This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 


For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. 

This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 50 000 to USD 100 000  depending on the funds at risk, capped at the maximum high reward.  

__Reward Calculation for Medium Level Reports__

Medium vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 11 000 to USD 50 000   depending on the funds at risk, capped at the maximum medium reward.  

In the event of temporary freezing, the reward doubles from the full frozen value for every additional [24h] that the funds are temporarily frozen, up until a max cap of the high reward. 

This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

For critical web/apps bug reports will be rewarded with USD 100 000, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of USD 20 000. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Reward Payment Terms__

Payouts are handled by the Kelp DAO team directly and are denominated in USD. However, payments are done in USDC on Ethereum

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
