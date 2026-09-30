# Berachain (Web/Apps)

- Page: https://immunefi.com/bug-bounty/berachain-webapps/scope/
- Max bounty: $10,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (12)

- [websites_and_applications] https://api.berachain.com/
- [websites_and_applications] https://berachain.com
- [websites_and_applications] https://bridge.berachain.com
- [websites_and_applications] https://buildabera.xyz
- [websites_and_applications] https://ecosystem.berachain.com
- [websites_and_applications] https://honey.berachain.com
- [websites_and_applications] https://honeypaper.berachain.com
- [websites_and_applications] https://hub.berachain.com
- [websites_and_applications] https://nftbridge.berachain.com
- [websites_and_applications] https://rfb.berachain.com
- [websites_and_applications] https://rpc.berachain.com
- [websites_and_applications] https://safe.berachain.com

## Asset notes

(none)

## Impacts in scope (20)

- [websites_and_applications] Critical: Changing NFT metadata
- [websites_and_applications] Critical: Direct theft of user NFTs
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] Critical: Taking down the NFT URI
- [websites_and_applications] Critical: Taking down the application/website - Causing the application/website to enter an unrecoverable failure state, rendering it permanently unresponsive until explicitly restarted.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:
- Email address
- Phone number
- Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:
- Locking up the victim from login
- Cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$10,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: fixedReward=$5,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

***STOP!*** **Is your report `Blockchain/DLT` or `Smart Contracts` related?**

**If yes, please visit:** https://immunefi.com/bug-bounty/berachain/information/

___

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).  

__Reward Calculation for High-Level Reports__
 
For critical web/apps bug reports will be rewarded with USD 10 000, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of USD 5 000. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Reward Payment Terms__

Payouts are handled by the Berachain team directly and are denominated in USD. However, payments are made in BERA on Berachain.

The net amount rewarded is calculated based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

- DoS attacks due to a lack of rate limits and improper handling of large HTTP request data or queries are not eligible for the reward.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
