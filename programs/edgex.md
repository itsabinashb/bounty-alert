# edgeX

- Page: https://immunefi.com/bug-bounty/edgex/scope/
- Max bounty: $10,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: (none)
- End date: (none)

## Assets in scope (4)

- [websites_and_applications] https://pro.edgex.exchange/ — Primary domain for edgeX mainnet site and perp trading APIs
- [websites_and_applications] https://quote.edgex.exchange/ — API and websocket endpoints for perp quoting
- [websites_and_applications] https://spot-quote.edgex.exchange/ — API and websocket endpoints for spot quoting
- [websites_and_applications] https://spot.edgex.exchange/ — Primary domain for our spot trading APIs.

## Asset notes

(none)

## Impacts in scope (15)

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
- [websites_and_applications] Critical: Taking down the application/website
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
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$10,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] High: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

#### Reward Calculation for Critical Level Reports

For critical web/apps bugs, reports will be rewarded with $10,000, only if the impact leads to:

* A loss of funds involving an attack that does not require any user action  
* Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of $5,000. The rest of the severity levels are paid out according to the Impact in Scope table.  

#### 

#### Reward Payment Terms

Payouts are handled by the edgeX team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
