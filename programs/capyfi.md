# CapyFi

- Page: https://immunefi.com/bug-bounty/capyfi/scope/
- Max bounty: $1,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, websites_and_applications - critical, websites_and_applications - high
- End date: (none)

## Assets in scope (12)

- [smart_contract] https://app.capyfi.com — Primacy of Impact (primacy of impact)
- [smart_contract] https://etherscan.io/address/0x00dc4965916e03A734190fA382633657c71f867E — Comptroller
- [smart_contract] https://etherscan.io/address/0x0568F6cb5A0E84FACa107D02f81ddEB1803f3B50 — caLAC
- [smart_contract] https://etherscan.io/address/0x0b9af1fd73885aD52680A1aeAa7A3f17AC702afA — Unitroller
- [smart_contract] https://etherscan.io/address/0x0f864A3e50D1070adDE5100fd848446C0567362B — caUSDT
- [smart_contract] https://etherscan.io/address/0x37DE57183491Fa9745d8Fa5DCd950f0c3a4645c9 — caETH
- [smart_contract] https://etherscan.io/address/0xDa5928d59ECE82808Af2cbBE4f2872FeA8E12CD6 — caWBTC
- [smart_contract] https://etherscan.io/address/0xF61159B4a0EE5b1615c9Afb3dA38111043344c32 — caRPC
- [smart_contract] https://etherscan.io/address/0xc3aD34De18B59A24BD0877e454Fb924181F09C8f — caUSDC
- [smart_contract] https://etherscan.io/address/0xf80eeec09f417Fa7FCc4A848Ef03af9dF2658d7B — caWARS
- [websites_and_applications] https://app.capyfi.com — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://app.capyfi.com/ — Capyfi App

## Asset notes

(none)

## Impacts in scope (21)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
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
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$1,000,000, minReward=$50,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$50,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$5,001, rewardModel=range
- [smart_contract] Low: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Critical: fixedReward=$8,000, otherImpactMaxReward=$0, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$3,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,500, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD $1M. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD $50,000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

For critical web/apps bugs, reports will be rewarded with up to USD $10,000, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded within a range of USD $4,001 to USD $10,000 depending on the impact. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. 

- The amount of funds at risk will be calculated with the impact of the first attack being at 100% and then a reduction of 25% from the amount of the first attack for every [300 blocks] the attack needs for subsequent attacks from the first attack, rounded down

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD $10,000 to USD $50,000  with the reward calculated based on 100% of the funds at risk, though capped at the maximum high reward. 
In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. 

__Reward Payment Terms__

Payouts are handled by the CapyFi team directly and are denominated in **USD**. However, payments are done in **USDC** on **ETH**.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
