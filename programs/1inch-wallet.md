# 1inch - Wallet

- Page: https://immunefi.com/bug-bounty/1inch-wallet/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (2)

- [websites_and_applications] http://apps.apple.com/us/app/1inch-crypto-defi-wallet/id1546049391 — Apple Wallet
- [websites_and_applications] http://play.google.com/store/apps/details?id=io.oneinch.android — Play (Android) Wallet

## Asset notes

(none)

## Impacts in scope (31)

- [websites_and_applications] Critical: Bypass of wallet authentication (PIN/passlock, biometric, or equivalent) allowing transaction signing or seed phrase access without legitimate user authorization
- [websites_and_applications] Critical: Compromise of the wallet's integrated dApp browser (WebView) leading to extraction of keys, signing of unauthorized transactions, or full wallet hijack
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Disruption of the entire application without requiring the user to open a malicious URL via an in-app browser.
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Extraction of user's seed phrase, private keys, or other key material from the device by another app, remote attacker, or via insecure storage
- [websites_and_applications] Critical: Malicious deep link, URL scheme, or IPC handling that triggers transaction signing or fund movement without explicit user consent matching the displayed action
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Remote code execution within the wallet application context on the user's device
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Substitution or modification of transaction parameters (recipient address, amount, contract calldata) between user confirmation and signing, such that funds are sent to attacker-controlled destination without the user's awareness
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] High: Bypass of authentication in non-fund-affecting flows (e.g., access to non-sensitive settings or transaction history without auth)
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Cryptographic weaknesses in key derivation, transaction signing, or random number generation that reduce security guarantees without immediately enabling key extraction
- [websites_and_applications] High: Disclosure of confidential user information (transaction history, wallet addresses, PII) to other apps via insecure IPC, content providers, or shared storage
- [websites_and_applications] High: Disclosure of seed phrase, private keys, or sensitive wallet data to system logs, screenshots, backup mechanisms, or other unintended channels (must demonstrate retrieval by an attacker, not just presence)
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
- [websites_and_applications] Medium: Information disclosure of non-public but non-key data to unauthorized parties
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Persistent local storage of sensitive but non-key data without proper protection (e.g., addresses, transaction details accessible to non-rooted attacker apps)
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Medium: Wallet operates in a degraded security mode without informing the user (e.g., silently failing certificate validation)
- [websites_and_applications] Low: Bypass of in-app passlock leading only to access to non-sensitive UI or settings (no transaction signing, no seed phrase access, no sensitive data disclosure)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Minor information leaks via verbose logging or debug output not exploitable for fund theft
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:  Locking up the victim from login Cookie bombing, etc.
- [websites_and_applications] Low: UI confusion or misrepresentation that could mislead the user but with limited financial impact and requires significant user action

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$100,000, minReward=$30,000, rewardModel=range
- [websites_and_applications] High: maxReward=$30,000, minReward=$10,000, rewardModel=range
- [websites_and_applications] Medium: maxReward=$10,000, minReward=$2,000, rewardModel=range
- [websites_and_applications] Low: maxReward=$2,000, minReward=$100, rewardModel=range

## Reward notes

### Rewards by Threat Level

Rewards are distributed according to the impact of the vulnerability based on the Impacts in Scope table. 

#### Reward Calculation for Critical Level Reports

For critical web/apps bugs, reports will be rewarded with 100000, only if the impact leads to:

* A loss of funds involving an attack that does not require any user action  
* Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts for assets with those designations that would be classified as Critical would be rewarded a flat amount of 30000\. 

#### Reward Calculation for Other Levels

High, Medium, and Low reports are rewarded at a flat rate of USD 10 000, USD 2 000, and USD 100, respectively. At the discretion of 1inch, it may decide to increase the reward paid out to security researchers for exceptional cases. However, it makes no commitment to rewarding above these amounts. The maximum reward listed on the table provided is only as guidance for the maximum that could ever be expected in even the most exceptional cases within those severity levels. 

#### Other Restrictions and Limitations

The listed app store URLs reference the official 1inch Wallet applications. Testing should be performed against the latest production version of the wallet downloaded from the listed app stores. Beta, staging, or modified builds (including but not limited to APKs from third-party sources, side-loaded variants, or self-built versions) are not considered as production assets and fall under the non-production severity cap above.

#### Additional Terms

Any vulnerability discovered must be reported no later than 24 hours after the initial discovery. Reports submitted after this window may be considered at 1inch's discretion but are not guaranteed eligibility for a reward.

In cases where the same vulnerability is reported through multiple platforms, priority will be determined by the earlier submission timestamp, regardless of the platform used.

#### Reward Payment Terms

Payouts are handled by the 1inch team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability. 

Reports and payout details may be checked against OFAC, EU, and UK sanctions lists prior to payment. Payment may be withheld, delayed, or refused entirely if prohibited by applicable law, sanctions regimes, or 1inch's compliance obligations. Researchers are responsible for ensuring their participation does not violate the laws of their jurisdiction.

## Out of scope (program-specific)

These impacts are out of scope for this bug bounty program. 

**All Categories:**

* Impacts requiring attacks that the reporter has already exploited themselves, leading to damage  
* Impacts caused by attacks requiring access to leaked keys/credentials  
* Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
* Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code  
* Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production  
* Best practice recommendations  
* Feature requests  
* Impacts on test files and configuration files unless stated otherwise in the bug bounty program  
* Impacts requiring phishing or other social engineering attacks against project's employees and/or customers

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
* Impacts that only require DDoS  
* UX and UI impacts that do not materially disrupt use of the platform  
* Leakage of non sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)  
* Automated scanner reports without demonstrated impact  
* UI/UX best practice recommendations  
* Vulnerabilities requiring a rooted or jailbroken device, unless the impact occurs on a non-rooted device through the rooted attacker's actions  
* Lack of binary obfuscation, code protection, or anti-tampering controls  
* Lack of root or jailbreak detection  
* Bypass of certificate pinning on rooted or jailbroken devices  
* Lack of exploit mitigations in the binary (e.g., PIE, ARC, stack canaries)  
* Path disclosure within the app binary  
* Sensitive data in URLs or request bodies when transmitted over TLS  
* OAuth secrets or app secrets hard-coded in the IPA/APK without demonstrated critical impact  
* Sensitive information retained as plaintext in device memory without demonstrated extraction by an unprivileged attacker  
* Crashes caused by malformed URL schemes, intents, or messages sent to exported activities/services/broadcast receivers without further impact  
* Sensitive data stored in the app's private directory accessible only to the app itself  
* Runtime hacking exploits (Frida, Appmon, etc.) requiring a jailbroken or rooted environment  
* Shared content leaked through the system clipboard  
* Reports based purely on static analysis of the binary without a runnable PoC demonstrating business logic impact
* Exposure of non-sensitive data on the device

**Prohibited Activities:**

* Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet  
* Any testing with pricing oracles or third-party smart contracts  
* Attempting phishing or other social engineering attacks against our employees and/or customers  
* Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)  
* Any denial of service attacks that are executed against project assets  
* Automated testing of services that generates significant amounts of traffic  
* Public disclosure of an unpatched vulnerability in an embargoed bounty  
* Accessing or modifying data belonging to other users  
* Submitting AI-generated reports  
* Spamming forms or account creation flows (even with low volume)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
