# Celer

- Page: https://immunefi.com/bug-bounty/celer/scope/
- Max bounty: $200,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: websites_and_applications - critical, smart_contract - critical
- End date: (none)

## Assets in scope (16)

- [smart_contract] https://arbiscan.io/address/0x1619DE6B6B20eD217a58d00f37B9d47C7663feca — Arbitrum 42161
- [smart_contract] https://blockexplorer.boba.network/address/0x841ce48F9446C8E281D3F1444cB859b4A6D0738C — Boba 288
- [smart_contract] https://bscscan.com/address/0xdd90E5E87A2081Dcf0391920868eBc2FFB81a1aF — BSC 56
- [smart_contract] https://etherscan.io/address/0x5427FEFA711Eff984124bFBB1AB6fbf5E3DA1820 — Ethereum 1
- [smart_contract] https://etherscan.io/address/0x5803457E3074E727FA7F9aED60454bf2F127853b — Viewer
- [smart_contract] https://etherscan.io/address/0x61f85fF2a2f4289Be4bb9B72Fc7010B3142B5f41 — Farming Rewards
- [smart_contract] https://etherscan.io/address/0x8a4B4C2aCAdeAa7206Df96F00052e41d74a015CE — Staking
- [smart_contract] https://etherscan.io/address/0xCb4A7569a61300C50Cf80A2be16329AD9F5F8F9e — State Guardian Network
- [smart_contract] https://etherscan.io/address/0xb01fd7Bc0B3c433e313bf92daC09FF3942212b42 — Staking Rewards
- [smart_contract] https://etherscan.io/address/0xea129aE043C4cB73DcB241AAA074F9E667641BA0 — Governance
- [smart_contract] https://ftmscan.com/address/0x374B8a9f3eC5eB2D97ECA84Ea27aCa45aa1C57EF — Fantom 250
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [smart_contract] https://optimistic.etherscan.io/address/0x9D39Fc627A6d9d9F8C831c16995b209548cc3401 — Optimism 10
- [smart_contract] https://polygonscan.com/address/0x88DCDC47D2f83a99CF0000FDF667A468bB958a78 — Polygon 137
- [smart_contract] https://snowtrace.io/address/0xef3c714c9425a8F3697A9C969Dc1af30ba82e5d4 — Avalanche 43114
- [websites_and_applications] https://cbridge.celer.network/#/transfer — cBridge Web App

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program. For cBridge contracts (multiple instances on different chains), there will not be duplicated counting of bugs. One bug that exists in all contracts will be counted as a single bug.

## Impacts in scope (2)

- [smart_contract] Critical: Thefts and permanent freezing of any funds in liquidity pool smart contracts or staking contracts
- [websites_and_applications] Critical: The only web vulnerabilities in scope are those which lead directly and unequivocally to loss of user funds, a direct breach of data, and the deletion of site data

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$200,000, primacy=primacy_of_impact, rewardCalculationPercentage=10, rewardModel=up_to
- [websites_and_applications] Critical: fixedReward=$3,000, otherImpactMaxReward=$0, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit. 

There are some modifications from the above Severity Classification for this bug bounty program:

Critical Level Security - Modified: 
  - Thefts and permanent freezing of any funds in liquidity pool smart contracts or staking contracts (e.g. economic attacks, flash loans, reentrancy, MEV, logic errors, integer over-/under-flow)

Medium Level Security - Excluded: 
  - Griefing denial of service (i.e. attacker spends as much in gas as damage to the contract)
  - Gas griefing

All web/app bug reports must come with a PoC in order to be considered for a reward. All High and Critical Smart Contract bug reports require a PoC and a suggestion for a fix to be eligible for a reward. 

Critical Smart Contract and Blockchain bug reports are further capped at 10% of economic damage up to USD 200,000, which primarily takes into consideration the funds at risk but may include branding and PR aspects at the discretion of the team. However, they have a minimum reward of USD 15,000. No repeated attacks will be considered.

The following vulnerabilities are not eligible for a reward:

  - Previously known vulnerabilities (resolved or not) on the Ethereum network (and any other fork of these).
  - Previously known vulnerabilities in Tendermint and or/any other fork of these.
  - Previously known vulnerabilities in cosmos-sdk and or/any other fork of these.
  - Previously known vulnerable libraries without a working Proof of Concept.
  - Attacks requiring MITM or physical access to a user's device.
  - Public Zero-day vulnerabilities that have had an official patch for less than 1 month will be awarded on a case by case basis
  - Any griefing attacks on the system or smart contract trying to spend gas costs or liquidity lockup to incur gas costs and computational overhead  for the validators and operators of the network.
  - Liquidity value reduction or arbitraging incurred due to the pricing mechanisms of the system and LP’s own operations. 
  - Attacks involving getting access to privileged admin keys 
  - Delay of cross-chain transfer (fund security not compromised) due to network/rpc error from the blockchain endpoint being used by SGN validators
  - Security issues related to connected blockchains of cBridge is not in the scope
  - As to the current implementation, it is possible (with low probability) that a user triggered transaction (e.g., add liquidity, send fund, delegate stake) is not automatically synced to the sgn, or the sgn failed to automatically submit the fund relay transaction to the destination chain (e.g., due to chain rpc endpoint failure). Such cases do not introduce fund security, and can be recovered through manual CLI tools. Related improvements will be included in later releases.

Celer Network requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed is acquired through mutually agreed third-party KYC solutions. The collection of this information will be done by the Celer Network team.

Payouts are handled by the __Celer Network__ team directly and are denominated in USD. However, payouts are done in __ETH__, __CELR__, __or a stablecoin__, with the choice of the ratio at the discretion of the team.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

The following vulnerabilities are excluded from the rewards for this bug bounty program:

  - Attacks that the reporter has already exploited themselves, leading to damage
  - Attacks requiring access to leaked keys/credentials
  - Attacks requiring access to privileged addresses (governance, strategist)

__Smart Contracts and Blockchain__

  - Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
  - Basic economic governance attacks (e.g. 51% attack)
  - Lack of liquidity
  - Best practice critiques
  - Sybil attacks

__Websites and Apps__

  - Theoretical vulnerabilities without any proof or demonstration
  - Content spoofing / Text injection issues
  - Self-XSS
  - Captcha bypass using OCR
  - CSRF with no security impact (logout CSRF, change language, etc.)
  - Missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”)
  - Server-side information disclosure such as IPs, server names, and most stack traces
  - Vulnerabilities used to enumerate or confirm the existence of users or tenants
  - Vulnerabilities requiring unlikely user actions
  - URL Redirects (unless combined with another vulnerability to produce a more severe vulnerability)
  - Lack of SSL/TLS best practices
  - DDoS vulnerabilities
  - Attacks requiring privileged access from within the organization
  - Feature requests
  - Best practices

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
