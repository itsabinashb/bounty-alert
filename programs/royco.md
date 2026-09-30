# Royco

- Page: https://immunefi.com/bug-bounty/royco/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, websites_and_applications - critical
- End date: (none)

## Assets in scope (10)

- [smart_contract] https://arbiscan.io/address/0x7cC6fB28eC7b5e7afC3cB3986141797ffc27253C — Royco Factory (ARB) that deploys all markets. All markets and their constituent components are in scope.
- [smart_contract] https://etherscan.io/address/0x170ff06326eBb64BF609a848Fc143143994AF6c8 — Multisig Safe
- [smart_contract] https://etherscan.io/address/0x7cC6fB28eC7b5e7afC3cB3986141797ffc27253C — Royco Factory (ETH) that deploys all markets. All markets and their constituent components are in scope.
- [smart_contract] https://etherscan.io/address/0xc5FeF644d59415cec65049e0653CA10eD9Cba778 — Royco Vault Makina Strategy. Our vaults are only configured with asynchronous strategy flows, so those are the only ones in scope.
- [smart_contract] https://etherscan.io/address/0xcD9f5907F92818bC06c9Ad70217f089E190d2a32 — Senior Royco USDC (srRoyUSDC)
- [smart_contract] https://etherscan.io/address/0xd3F8Edff57570c4F9B11CC95eA65117e2D7A6C2D — Multisig Strategy
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [smart_contract] https://snowscan.xyz/address/0x7cC6fB28eC7b5e7afC3cB3986141797ffc27253C — Royco Factory (AVAX) that deploys all markets. All markets and their constituent components are in scope.
- [websites_and_applications] https://dawn.royco.org/ — Royco Dawn & related subpages
- [websites_and_applications] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (3)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [websites_and_applications] Critical: Direct theft of user funds

## Impact notes

__Whitelisting & Fund Recovery Context__

Royco operates with a whitelisted architecture where certain trusted addresses and parties have privileged access to protocol functions. These whitelisted parties are assumed to act in good faith, and funds sent to whitelisted addresses (or addresses explicitly specified by whitelisted parties) are considered recoverable through administrative action or protocol upgrades.

__In-Scope Impacts for Direct Theft Rewards:__

For a vulnerability to qualify as a Direct Theft finding eligible for reward, it must demonstrate: 

Permanent loss of (non-dust) user funds that cannot be remediated through a protocol upgrade or administrative action — Either through theft to non-whitelisted addresses (or addresses not intended by whitelisted parties), or through funds being permanently locked. This includes abuse of privileged roles beyond their intended permissions.

## Rewards

- [smart_contract] Critical: maxReward=$250,000, minReward=$50,000, rewardCalculationPercentage=10, rewardModel=range
- [websites_and_applications] Critical: maxReward=$10,000, minReward=$2,000, otherImpactMaxReward=$0, rewardModel=range

## Reward notes

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of **USD 250 000**. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of **USD 50 000** is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

For critical web/apps bugs, reports will be rewarded with **USD 10 000**, only if the impact leads to:
- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of **USD 2 000**. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward.
- The amount of funds at risk will be calculated with the impact of the first attack being at **100%** and then a reduction of **25%** from the amount of the first attack for every **[300 blocks]** the attack needs for subsequent attacks from the first attack, rounded down.

__Reward Payment Terms__

Payouts are handled by the Royco Dawn team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

__Subdomain Scope & Web Application Restrictions:__
- **ONLY `dawn.royco.org` is in-scope** for web/app vulnerability reports.
- **ALL other subdomains are strictly OUT OF SCOPE**, including but not limited to:
  - `app.royco.org`
  - `terminal.royco.org`
  - Any non-explicitly listed `*.royco.org` subdomain or wildcard.
- Submissions targeting out-of-scope subdomains will be closed as **Ineligible / Out of Scope** without reward.

__Blockchain/DLT & Smart Contract Specific:__

- Incorrect data supplied by third party oracles
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts involving centralization risks
- Whitelisted/admin parties behaving maliciously (assumed trusted and funds recoverable)
- Incorrect amounts sent to whitelisted parties or their specified recipients (reversible)
- External protocol bugs
- Centralization risks
- MEV, gas griefing, frontrunning
- Frontend or off-chain components
- Synchronous Redemption Flows in vault strategy contracts (never used)

__Websites and Apps__

- Theoretical impacts without any proof or demonstration
- Impacts involving attacks requiring physical access to the victim device
- Impacts involving attacks requiring access to the local network of the victim
- Reflected plain text injection (e.g. url parameters, path, etc.)
- This does not exclude reflected HTML injection with or without JavaScript
- This does not exclude persistent plain text injection
- Any impacts involving self-XSS
- Captcha bypass using OCR without impact demonstration
- CSRF with no state modifying security impact (e.g. logout CSRF)
- Impacts related to missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”) without demonstration of impact
- Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces
- Impacts causing only the enumeration or confirmation of the existence of users or tenants
- Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows
- Lack of SSL/TLS best practices
- Impacts that only require DDoS
- UX and UI impacts that do not materially disrupt use of the platform
- Impacts primarily caused by browser/plugin defects
- Leakage of non sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)
- Any vulnerability exploit requiring browser bugs for exploitation (e.g. CSP bypass)
- SPF/DMARC misconfigured records
- Missing HTTP Headers without demonstrated impact
- Automated scanner reports without demonstrated impact
- UI/UX best practice recommendations
- Non-future-proof NFT rendering

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
