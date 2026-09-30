# Vesper

- Page: https://immunefi.com/bug-bounty/vesper/scope/
- Max bounty: $50,000
- KYC required: no
- Paused: yes
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium
- End date: (none)

## Assets in scope (18)

- [smart_contract] https://basescan.org/address/0x1e41238aCd3A9fF90b0DCB9ea96Cf45F104e09Ef — Base USDC
- [smart_contract] https://basescan.org/address/0x3899a6090c5C178dB8A1800DA39daD0D06EeEFBE — Base cbETH
- [smart_contract] https://basescan.org/address/0x46fb68Eb2b1Fc43654AbaE5691D39D18D933E4b4 — Base wstETH
- [smart_contract] https://basescan.org/address/0x82562507429876486B60AF4F32390ef0947b3d13 — Base ETH
- [smart_contract] https://etherscan.io/address/0x01e1d41C1159b745298724c5Fd3eAfF3da1C6efD — vaWBTC
- [smart_contract] https://etherscan.io/address/0x0538C8bAc84E95A9dF8aC10Aad17DbE81b9E36ee — vaDAI
- [smart_contract] https://etherscan.io/address/0x4Dbe3f01aBe271D3E65432c74851625a8c30Aa7B — vastETH
- [smart_contract] https://etherscan.io/address/0x650CD45DEdb19c33160Acc522aD1a82D9701036a — vacbETH
- [smart_contract] https://etherscan.io/address/0xDD9F61a85fFE73E41eF889817972f0B0AaE6D6Dd — varETH
- [smart_contract] https://etherscan.io/address/0xa8b607Aa09B6A2E306F93e74c282Fb13f6A80452 — vaUSDC
- [smart_contract] https://etherscan.io/address/0xc14900dFB1Aa54e7674e1eCf9ce02b3b35157ba5 — vaFrax
- [smart_contract] https://etherscan.io/address/0xd1C117319B3595fbc39b471AB1fd485629eb05F2 — vaETH
- [smart_contract] https://etherscan.io/address/0xef4F4604106de23CDadfEAE08fcC34602cB475C1 — vaLINK
- [smart_contract] https://optimistic.etherscan.io/address/0x19382707d5a47E74f60053b652Ab34b6e30Febad — Optimism OP
- [smart_contract] https://optimistic.etherscan.io/address/0x539505Dde2B9771dEBE0898a84441c5E7fDF6BC0 — Optimism USDC
- [smart_contract] https://optimistic.etherscan.io/address/0xCcF3d1AcF799bAe67F6e354d685295557cf64761 — Optimism ETH
- [smart_contract] https://optimistic.etherscan.io/address/0xdd63ae655b388Cd782681b7821Be37fdB6d0E78d — Optimism wSTETH
- [websites_and_applications] http://App.vesper.finance — vaMUSD Pool

## Asset notes

All smart contracts of Vesper can be found at [https://github.com/vesperfi/vesper-pools/tree/main/contracts](https://github.com/vesperfi/vesper-pools/tree/main/contracts). However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

If an impact can be caused to any other asset managed by Vesper that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project. If a bug is submitted in an underlying Vesper strategy that results in the loss of user funds (not listed as a Smart Contract above),it may be considered as ‘In Scope’.

## Impacts in scope (25)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds that cannot be fixed by an upgrade
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds that cannot be fixed by an upgrade
- [smart_contract] High: Theft of unclaimed yield
- [websites_and_applications] Critical: Changing the NFT metadata
- [websites_and_applications] Critical: Direct theft of user NFTs
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through NFT metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as /etc/shadow, database passwords, and blockchain keys(this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the NFT URI
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as, changing registration information, commenting, voting, making trades, withdrawals, etc
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as email or password of the victim, etc
- [websites_and_applications] High: Improperly disclosing confidential user information such as email address, phone number, physical address, etc
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the first/last name of user, or en/disabling notification
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as reflected HTML injection or loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$50,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] Critical: maxReward=$10,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit. 

Bounty payouts will be dependent on actual risk to the platform.  Total bounty will either be the minimum of the range, or 5% of the total funds that could be lost in the exploit (up to the maximum cap based on the tier severity) - whichever amount is greater.

All Critical severity bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. 

All web/app bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

Known issues highlighted in the following audit reports are considered out of scope: 
  - [https://github.com/vesperfi/doc/tree/main/audit/v3%2B](https://github.com/vesperfi/doc/tree/main/audit/v3%2B)

Payouts are handled by the __Vesper__ team directly and are denominated in USD. However, payouts are done in __USDC__, __DAI__, or __VSP__.

## Out of scope (program-specific)

(none)

## Out of scope and rules

The following vulnerabilities are excluded from the rewards for this bug bounty program:

  - Attacks that the reporter has already exploited themselves, leading to damage
  - Attacks requiring access to leaked keys/credentials
  - Attacks requiring access to privileged addresses (governance, strategist)

__Smart Contracts__
  - Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
  - Basic economic governance attacks (e.g. 51% attack)
  - Lack of liquidity
  - Best practice critiques
  - Sybil attacks
  - Centralization risks

__Websites and Apps__
  - Theoretical vulnerabilities without any proof or demonstration
  - Attacks requiring physical access to the victim device
  - Attacks requiring access to the local network of the victim
  - Reflected plain text injection ex: url parameters, path, etc.
    - This does not exclude reflected HTML injection with or without javascript
    - This does not exclude persistent plain text injection
  - Self-XSS
  - Captcha bypass using OCR without impact demonstration
  - CSRF with no state modifying security impact (ex: logout CSRF)
  - Missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”) without demonstration of impact
  - Server-side non-confidential information disclosure such as IPs, server names, and most stack traces
  - Vulnerabilities used only to enumerate or confirm the existence of users or tenants
  - Vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows
  - Lack of SSL/TLS best practices
  - DDoS vulnerabilities
  - Feature requests
  - Issues related to the frontend without concrete impact and PoC
  - Best practices issues without concrete impact and PoC
  - Vulnerabilities primarily caused by browser/plugin defects
  - Leakage of non sensitive api keys ex: etherscan, Infura, Alchemy, etc.
  - Any vulnerability exploit requiring browser bugs for exploitation. ex: CSP bypass

The following activities are prohibited by this bug bounty program:

  - Any testing with mainnet or public testnet contracts; all testing should be done on private testnets
  - Any testing with pricing oracles or third party smart contracts
  - Attempting phishing or other social engineering attacks against our employees and/or customers
  - Any testing with third party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
  - Any denial of service attacks
  - Automated testing of services that generates significant amounts of traffic
  - Public disclosure of an unpatched vulnerability in an embargoed bounty

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
