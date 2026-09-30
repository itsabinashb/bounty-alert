# Variational

- Page: https://immunefi.com/bug-bounty/variational/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (6)

- [smart_contract] https://arbiscan.io/address/0x0F820B9afC270d658a9fD7D16B1Bdc45b70f074C — Settlement Pool Factory Contract
- [smart_contract] https://arbiscan.io/address/0x5e91b40467fb8902c46a7b6cb90482363188d645 — Variational Protocol Treasury
- [smart_contract] https://arbiscan.io/address/0x74bbbb0e7f0bad6938509dd4b556a39a4db1f2cd — Core OLP Vault
- [smart_contract] https://www.variational.io/ — Primacy of Impact Critical (primacy of impact)
- [websites_and_applications] https://omni.variational.io/
- [websites_and_applications] https://www.variational.io/ — Primacy of Impact Critical (primacy of impact)

## Asset notes

(none)

## Impacts in scope (29)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hours
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
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

- [smart_contract] Critical: maxReward=$100,000, minReward=$10,000, primacy=primacy_of_impact, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$25,000, minReward=$3,500, rewardModel=range
- [smart_contract] Medium: fixedReward=$3,500, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$50,000, minReward=$10,000, primacy=primacy_of_impact, rewardModel=range
- [websites_and_applications] High: fixedReward=$10,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$2,000, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

#### Reward Calculation for Critical Level Reports

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 10,000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

For critical web/apps bugs, reports will be rewarded with USD 50,000, only if the impact leads to:

* A loss of funds involving an attack that does not require any user action  
* Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of USD 10,000.

#### Repeatable Attack Limitations

* If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. 

* The amount of funds at risk will be calculated with the impact of the first attack being at **100%** and then a reduction of **25%** from the amount of the first attack for every \[**300 blocks\]** the attack needs for subsequent attacks from the first attack, rounded down.

#### 

#### Reward Calculation for High Level Reports

High impact concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 3,500 - USD 25,000 with the reward calculated based on **100%** of the funds at risk, though capped at the maximum high reward. 

In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. 

#### **Reward Payment Terms**

Payouts are handled by the Variational team directly and are denominated in USD. However, payments are done in USDC on Arbitrum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

**Websites and Apps**

* Theoretical impacts without any proof or demonstration  
* Impacts involving attacks requiring physical access to the victim device  
* Impacts involving attacks requiring access to the local network of the victim  
* Reflected plain text injection (e.g. url parameters, path, etc.)  
* This does not exclude reflected HTML injection with or without JavaScript  
* This does not exclude persistent plain text injection  
* Any impacts involving self-XSS  
* Captcha bypass using OCR without impact demonstration  
* CSRF with no state modifying security impact (e.g. logout CSRF)  
* Impacts related to missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”) without demonstration of impact  
* Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces  
* Impacts causing only the enumeration or confirmation of the existence of users or tenants  
* Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows  
* Lack of SSL/TLS best practices  
* Impacts that only require DDoS  
* UX and UI impacts that do not materially disrupt use of the platform  
* Impacts primarily caused by browser/plugin defects  
* Leakage of non sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)  
* Any vulnerability exploit requiring browser bugs for exploitation (e.g. CSP bypass)  
* SPF/DMARC misconfigured records)  
* Missing HTTP Headers without demonstrated impact  
* Automated scanner reports without demonstrated impact  
* UI/UX best practice recommendations  
* Non-future-proof NFT rendering

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
