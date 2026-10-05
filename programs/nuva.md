# NUVA

- Page: https://immunefi.com/bug-bounty/nuva/scope/
- Max bounty: $40,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (11)

- [smart_contract] https://etherscan.io/address/0x50AE1e4A612A4623b747aEeFb30aFBA82804e12c — ETH_NVPRIME_VAULT_ROUTER
- [smart_contract] https://etherscan.io/address/0xBB2f90A20AbC107161c0C66e2f7015bdb1D2c2f9 — ETH_WITHDRAWAL_USDC_NVYLDS
- [smart_contract] https://etherscan.io/address/0xC360e625F19A7ea47e47810B13E386221d5187D1 — ETH_NVPRIME_VAULT
- [smart_contract] https://etherscan.io/address/0xCB74517bfDe9Af6692C5C7D4A125b20bA7FA14D5 — ETH_DEPOSITOR_USDC_NVYLDS
- [smart_contract] https://etherscan.io/token/0x5965f8e28eC14B58E49569f382A50F4f0B238327 — ETH_NVYLDS_TOKEN
- [smart_contract] https://nuva.finance/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://zonescan.io/provenance/accounts/pb15y0f2zkc9a2cgyqkhpp3z9u6fmvtegf92s7ndx — nvYLDS Vault Address
- [smart_contract] https://zonescan.io/provenance/contracts/pb10yzuaqqjsf4pwv6wkp87dqka0scrcgf92k92j6qkz9msc6qyzt3qqgl7e4 — nvYLDS Vault Proxy SC Address
- [websites_and_applications] http://app.nuva.finance — App
- [websites_and_applications] http://nuva.finance — Website
- [websites_and_applications] https://nuva.finance/ — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (31)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
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
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:
- Locking up the victim from login
- Cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$40,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$3,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$2,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$20,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: fixedReward=$3,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$2,000, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of **USD 40 000**. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of **USD 5 000** is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

For critical web/apps bugs, reports will be rewarded with **USD 20 000**, only if the impact leads to:
- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of **USD 5 000**. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. 
- The amount of funds at risk will be calculated with the impact of the first attack being at **100%** and then a reduction of **25%** from the amount of the first attack for every **[300 blocks]** the attack needs for subsequent attacks from the first attack, rounded down.

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of **USD 2 000 to USD 5 000** with the reward calculated based on **100%** of the funds at risk, though capped at the maximum high reward. 
In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. 

__Reward Payment Terms__

Payouts are handled by the NUVA team directly and are denominated in USD. However, payments are done in USDC on Ethereum.
The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
