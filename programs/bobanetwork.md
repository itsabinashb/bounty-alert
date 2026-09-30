# Boba Network

- Page: https://immunefi.com/bug-bounty/bobanetwork/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (8)

- [smart_contract] https://arbiscan.io/address/0x2dE73Bd1660Fbf4D521a52Ec2a91CCc106113801 — Proxy__LightBridge (Arb)
- [smart_contract] https://bobascan.com/address/0x0dfFd3Efe9c3237Ad7bf94252296272c96237FF5 — Proxy__LightBridge
- [smart_contract] https://bobascan.com/address/0x670b130112C6f03E17192e63c67866e67D77c3ee — Proxy__LightBridge
- [smart_contract] https://etherscan.io/address/0x2dE73Bd1660Fbf4D521a52Ec2a91CCc106113801 — Proxy_LightBridge
- [smart_contract] https://optimistic.etherscan.io/address/0x2dE73Bd1660Fbf4D521a52Ec2a91CCc106113801 — Proxy__LightBridge (Op)
- [websites_and_applications] https://gateway.boba.network — Gateway
- [websites_and_applications] https://mainnet.boba.network — Mainnet RPC
- [websites_and_applications] wss://ws.mainnet.boba.network/ — Websocket

## Asset notes

All smart contracts of Boba Network can be found at https://github.com/bobanetwork/boba Boba-Eth - Core Rollup contracts (https://github.com/bobanetwork/boba)
However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

Though only the proxy contracts are listed as in-scope, current implementation and any further updates to the implementation contracts are considered in scope. When reporting a bug, please make sure to select the relevant proxy smart contract as the target. 

If an impact can be caused to any other asset managed by Boba Network that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project. This only applies to Critical and High impacts.

## Impacts in scope (41)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Direct theft of user NFTs originally developed by Boba Network, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Permanent freezing of NFTs originally developed by Boba Network
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs originally developed by Boba Network
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content) for NFTs originally developed by Boba Network
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs originally developed by Boba Network for any amount of time
- [smart_contract] High: Temporary freezing of funds for any amount of time
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Protocol failure caused by block stuffing
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Smart contract fails to deliver promised returns, but doesn’t lose value
- [websites_and_applications] Critical: Changing the NFT metadata for NFTs originally developed by Boba Network
- [websites_and_applications] Critical: Direct theft of user NFTs for NFTs originally developed by Boba Network
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as /etc/shadow, database passwords, and blockchain keys(this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the NFT URI for NFTs originally developed by Boba Network
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as, changing registration information, commenting, voting, making trades, withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as email or password of the victim, etc.
- [websites_and_applications] High: Improperly disclosing confidential user information such as email address, phone number, physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the first/last name of user, or en/disabling notification
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as reflected HTML injection or loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Any impact involving a publicly released CVE without a working PoC
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction such as iframing leading to modifying the backend/browser state (demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links such as social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as locking up the victim from login, cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$3,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$3,000, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$2,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,500, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the  [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). 

All web/app bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. All High and Critical Blockchain/DLT/Smart Contract bug reports require a PoC to be eligible for a reward. Explanations and statements are not accepted as PoC and code is required.

Critical blockchain vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk, but also PR and branding aspects, at the discretion of the team. However, there is a minimum reward of __USD 10 000__. 

Critical smart contract vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk, but also PR and branding aspects, at the discretion of the team. However, there is a minimum reward of __USD 10 000__. 

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100 000. However, a minimum reward of __USD 10 000__ is to be rewarded in order to incentivize security researchers against withholding on a bug report.

For web/app bugs, reports will be rewarded within a range of __USD 1 000 - 3 000__ depending on severity levels and will be rewarded according to the Impact in Scope table.  


The following vulnerabilities are not eligible for a reward:

- Contracts are upgradable. 
- The fact that fraud proofs are not yet running. 
- A bug in Lib_MerkleTrie.sol which will prevent withdrawals from succeeding in some cases. There is a workaround for this, by modifying the proof to add an extra element. 
- A bug in Lib_ResolvedDelegateProxy.sol which could result in a storage slot key collision overwriting the address of the implementation. This bug is dependent on the layout of the implementation contract, and Boba is not affected. 
- The user cannot commit to a L1 gas price, the OVM_GasPriceOracle is owned by a key controlled by Boba and is responsible for setting the L1 gas price.
- There appears to be an obvious bug which would allow an attacker to withdraw a fake ERC20 token from L2 in exchange for a real ERC20 (such as WBTC) token on L1. There is no check in the L2StandardBridge, however the withdrawal is prevented from finalizing by a check in the L1StandardBridge. Naturally if you do find a way to circumvent Boba Network’s protections, then you would be rewarded.
- All vulnerabilities mentioned in https://github.com/bobanetwork/boba_legacy/tree/develop/boba_audits 

Boba Network requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward for critical and high threat levels. The information needed is proof of your identity. The collection of this information will be done by the Boba Foundation.

Payouts are handled by the __Boba Foundation__ and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

- Best practice critiques
- All content on the Ecosystem pages of website (community driven) [https://boba.network/dapps/](https://boba.network/dapps/)
- Failed-disbursement bookkeeping collisions or overwrites that only impact privileged retry or manual recovery flows, without enabling unauthorized fund access or permanent loss of funds.

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
