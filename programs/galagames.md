# Gala Games

- Page: https://immunefi.com/bug-bounty/galagames/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium
- End date: (none)

## Assets in scope (11)

- [smart_contract] https://etherscan.io/token/0xb045f7f363fe4949954811b113bd56d208c67b23#code — SILK
- [smart_contract] https://etherscan.io/token/0xcd17fa52528f37facb3028688e62ec82d9417581#code — MTRM
- [smart_contract] https://etherscan.io/token/0xd1d2eb1b1e90b638588728b4130137d262c87cae#code — GALA
- [websites_and_applications] https://app.gala.games/ — Game domain & APIs
- [websites_and_applications] https://app.gala.games/games — Desktop launcher
- [websites_and_applications] https://app.gala.games/nodes — Node network
- [websites_and_applications] https://film.gala.com/ — Film domain & APIs
- [websites_and_applications] https://gala.com/ — Main domain & APIs
- [websites_and_applications] https://music.gala.com/ — Music domain & APIs
- [websites_and_applications] https://node.gala.games/ — Node dashboard
- [websites_and_applications] https://walletsrv.gala.games/ — Wallet server

## Asset notes

(none)

## Impacts in scope (36)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing NFTs (>24 hours)
- [smart_contract] High: Temporary freezing of funds (>24 hours)
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [websites_and_applications] Critical: Changing the NFT metadata
- [websites_and_applications] Critical: Direct theft of user NFTs
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through NFT metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as: Modifying transaction arguments or parameters, Substituting contract addresses, Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as: /etc/shadow, database passwords, blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking down the NFT URI
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as: Changing registration information, Commenting, Voting, Making trades, Withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: Email or password of the victim, etc.
- [websites_and_applications] High: Improperly disclosing confidential user information such as: Email address, Phone number, Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as: HTML injection without Javascript, Replacing existing text with arbitrary text, Arbitrary file uploads, etc.
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: Changing the name of user, Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as: Reflected HTML injection, Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$50,000, rewardCalculationPercentage=10, rewardModel=fixed
- [smart_contract] High: fixedReward=$20,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$7,500, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$5,000, otherImpactMaxReward=$0, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$2,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Restrictions on Security Researcher Eligibility__

Security researchers who fall under any of the following are ineligible for a reward:
- KYC blocked security researchers - Gala Games cannot pay bounties to individuals that take part in criminal or illegal activities. Therefore, Gala Games must perform KYC and wallet verification due to rules & regulations.
- KYT blocked wallets - the identity of the individual must be verified as well as the legitimacy of the wallet on which they would like to receive their bounty payment due to rules & regulations.

__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Smart contract, Critical severity
- Smart contract, High severity
- Smart contract, Medium severity
- Websites & applications, Critical severity
- Websites & applications, High severity
- Websites & applications, Medium severity

All PoCs submitted must comply with the [Immunefi-wide PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules). Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

Payouts are handled by the __Gala Games__ team directly and are denominated in USD. However, payments are done in __$GALA__. 

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability. For avoidance of doubt, if the reward amount is USD 5 000 and the average price is USD 1.75 per token, then the reward will be 2857.142857 units of that token.

## Out of scope (program-specific)

Physical or social engineering attempts (including phishing attacks)
- Ability to take over external tools or social media accounts
- Vulnerabilities that have already been reported or are already known at Gala
- Vulnerabilities caused by a lack of encryption or by using weak encryption methods
- Subdomain takeover

- CSV injection
- Protocol mismatch
- Rate limiting
- Exposed login panels
- Dangling IPs
- Reports that affect only outdated user agents or app versions
- Stack traces
- Path disclosure
- Directory listings
- Breach of our privacy statement

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
