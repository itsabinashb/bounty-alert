# Ava Labs

- Page: https://immunefi.com/bug-bounty/avalabs/scope/
- Max bounty: $10,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (18)

- [websites_and_applications] https://api.avax-test.network/
- [websites_and_applications] https://api.avax.network/
- [websites_and_applications] https://apps.apple.com/ng/app/core-crypto-wallet-nfts/id6443685999 — Core iOS App
- [websites_and_applications] https://avax.network/
- [websites_and_applications] https://backstage.avax-dev.network/
- [websites_and_applications] https://bridge.avax-test.network/
- [websites_and_applications] https://chrome.google.com/webstore/detail/core-crypto-wallet-nft-ex/agoakfejjabomempkjlepdflaleeobhb — Core Browser Extension
- [websites_and_applications] https://core.app/ — Core Web Wallet
- [websites_and_applications] https://explorer.avax.network/
- [websites_and_applications] https://faucet.avax-test.network/
- [websites_and_applications] https://github.com/ava-labs/Avalanche-Wallet-SDK — Avalanche-Wallet-SDK
- [websites_and_applications] https://github.com/ava-labs/AvalancheJS — AvalancheJS
- [websites_and_applications] https://notify.avax.network/
- [websites_and_applications] https://play.google.com/store/apps/details?id=com.avaxwallet — Core Android App
- [websites_and_applications] https://stats.avax.network/
- [websites_and_applications] https://subnets.avax.network/
- [websites_and_applications] https://www.avalabs.org/
- [websites_and_applications] https://www.avax.network/

## Asset notes

Ava Labs’s codebase can be found at [https://github.com/ava-labs](https://github.com/ava-labs). Documentation and further resources can be found on [https://docs.avax.network/](https://docs.avax.network/). For details on standing up a local test network, sees [https://docs.avax.network/tooling/network-runner](https://docs.avax.network/tooling/network-runner).

Whilst this program adheres to Primacy of Rules, the following assets are excluded and are considered out of scope for this program. 

  - chat.avax.network
  - docs.avax.network
  - chat.avalabs.org
  - buy.avax.network
  - *.snowtrace.io
  - community.avax.network
  - test*.avax.network
  - forum.avax.netowrk
  - avalanche-hub.com
  - academy.avax.network
  - support.avax.network
  - *.avacloud.io
  - Status.avax.network
  - [www.gamingonavax.com](https://www.gamingonavax.com/)
  - [www.artonavalanche.com](http://www.artonavalanche.com)
  - [www.avalanchesummit.com/](https://www.avalanchesummit.com/)
  - Broken links to third-parties from [http://www.avax.network/blog](http://www.avax.network/blog)
  - Broken links within third-party project content under [https://core.app/discover](https://core.app/discover)

## Impacts in scope (18)

- [websites_and_applications] Critical: Changing NFT metadata
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as: modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:  /etc/shadow database passwords blockchain keys (does not include non-sensitive environment variables, open source code, usernames), taking down the application/website, taking down the NFT URI
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:  changing registration information, commenting, voting, making trades, withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:  email, password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:  email address, phone number, physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:  HTML injection without JavaScript, replacing existing text with arbitrary text, arbitrary file uploads, etc
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: changing the name of user, enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as: reflected HTML injection, loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as: Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:  social media handles, etc
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as: locking up the victim from login, cookie bombing, etc

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$10,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$5,000, minReward=$2,500, rewardModel=range
- [websites_and_applications] Medium: maxReward=$2,500, minReward=$1,000, rewardModel=range
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Repeatable Attack Limitations__

  - If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attacks within the first hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

  - For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

  - High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are considered at the full amount of funds at risk, capped at the maximum high reward. This is to incentivize security researchers to uncover and responsibly disclose vulnerabilities that may have not have significant monetary value today, but could still be damaging to the project if it goes unaddressed.   

  - In the event of temporary freezing, the reward increases at a multiplier of two from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lenghents, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.    

For critical web/apps bug reports will be rewarded with USD $10,000, only if the impact leads to:

  - A loss of funds involving an attack that does not require any user action
  - Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of USD 5 000. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Reward Payment Terms__

Payouts are handled by the __Ava Labs__ team directly and are denominated in __USD__.

Please note: In cases where the size of the reward exceeds an equivalent of 10 000 USD, Ava Labs is entitled to make the payment in one-year locked AVAX at the rate calculated based on the VWAP of AVAX during 90 calendar days preceding the date of the respective validated report.

## Out of scope (program-specific)

- Dependency confusion attacks on NPM

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- APPSEC-330: Update address bar management (https://github.com/ava-labs/core-mobile/pull/3877)
