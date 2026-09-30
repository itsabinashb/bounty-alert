# Avail

- Page: https://immunefi.com/bug-bounty/avail/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (2)

- [smart_contract] https://github.com/availproject/contracts — Avail Bridge Smart Contracts
- [websites_and_applications] https://bridge.availproject.org — Bridge UI

## Asset notes

Fusion contracts (Fusion.sol,...) are out of scope as they are not in production.

## Impacts in scope (25)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Unbounded gas consumption
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:  Modifying transaction arguments or parameters Substituting contract addresses Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:   /etc/shadow, database passwords, blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:   Changing registration information, Commenting, Voting, Making trades, Withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:  Email, Password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:  Email address, Phone number, Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:  HTML injection without JavaScript, Replacing existing text with arbitrary text, Arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users(including modifying browser local storage)without already-connected wallet interaction & with up to one click of user interaction, such as: Changing the first/last name of user, Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:  Reflected HTML injection, Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction & with significant user interaction, such as: Iframing leading to modifying the backend/browser state(must demonstrate impact with POC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:  Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:  Locking up the victim from login Cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$250,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$40,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$4,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$20,000, minReward=$6,000, rewardModel=range
- [websites_and_applications] High: fixedReward=$5,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical Blockchain/DLT bugs, the reward amount is 10% of the funds directly affected, capped at the maximum critical reward USD 250,000. However, a minimum reward of USD 25,000 is to be rewarded in order to incentivize security researchers against withholding on a bug report. Note that critical Blockchain/DLT bugs need to be able to exploit the runtime layer of the blockchain, as the critical chain logic is strictly part of the runtime.

For critical Blockchain/DLT bugs with a non-funds-at risk impact, the reward will be paid out as follows: 

- Network not being able to confirm new transactions (total network shutdown) - USD 30,000
- Unintended permanent chain split requiring hard fork (network partition requiring hard fork) - USD 30,000
- Permanent freezing of funds (fix requires hardfork) - USD 30,000

For high Blockchain/DLT non-funds-at risk impacts, the reward will be paid out as follows: 

- Unintended chain split (network partition) - USD 20,000
- Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments - USD 20,000
- Causing network processing nodes to process transactions from the mempool beyond set parameters - USD 20,000
- RPC API crash affecting projects with greater than or equal to 25% of the market capitalization on top of the respective layer - USD 20,000

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 250,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 25,000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 5,000 to USD 20,000 depending on the funds at risk, capped at the maximum high reward.  

In the event of temporary freezing, the reward doubles from the full frozen value for every additional [24h] that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

For critical web/apps bug reports will be rewarded with USD 20,000, only if the impact leads to:
A loss of funds involving an attack that does not require any user action
Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of USD 6,000. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Reward Payment Terms__

Payouts are handled by the Avail team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
