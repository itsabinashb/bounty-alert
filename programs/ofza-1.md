# OFZA

- Page: https://immunefi.com/bug-bounty/ofza-1/scope/
- Max bounty: $10,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium
- End date: (none)

## Assets in scope (1)

- [websites_and_applications] https://ofza.com/ — Crypto currency exchange Regulated  by VARA

## Asset notes

(none)

## Impacts in scope (8)

- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$10,000, minReward=$3,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$3,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Medium: maxReward=$1,000, minReward=$500, rewardModel=range

## Reward notes

__Rewards by Threat Level__

For critical web/apps bug reports will be rewarded with USD $10,000 only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of **USD $3,000**. The rest of the severity levels are paid out according to the Impact in Scope table.

__Reward Payment Terms__

Payouts are handled by the **OFZA** team directly and are denominated in **USD**. However, payments are done in **USDT** on **Tron**.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Email Address Enumeration (https://ofza.com)
