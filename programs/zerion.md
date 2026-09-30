# Zerion

- Page: https://immunefi.com/bug-bounty/zerion/scope/
- Max bounty: $25,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (20)

- [smart_contract] https://arbiscan.io/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_ARBITRUM
- [smart_contract] https://basescan.org/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_BASE
- [smart_contract] https://bscscan.com/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_BSC
- [smart_contract] https://celoscan.io/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_CELO
- [smart_contract] https://etherscan.io/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_ETHEREUM
- [smart_contract] https://explorer.mainnet.aurora.dev/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_AURORA
- [smart_contract] https://explorer.zero.network/address/0x4667fFb6a24017f977c93Da1BD630CF1801343b6 — Zerion Paymaster
- [smart_contract] https://explorer.zksync.io/address/0xa71B5eCb48669580ea46bEffB74E6CA0Ec9EefA3 — PREMIUM_PURCHASER_CONTRACT_ZKSYNC
- [smart_contract] https://explorer.zora.energy/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_ZORA
- [smart_contract] https://gnosisscan.io/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_XDAI
- [smart_contract] https://lineascan.build/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_LINEA
- [smart_contract] https://optimistic.etherscan.io/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_OPTIMISM
- [smart_contract] https://polygonscan.com/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_POLYGON
- [smart_contract] https://scrollscan.com/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_SCROLL
- [smart_contract] https://snowtrace.io/address/0x1AB3747DA0F88E883895DE58c105Fd25C21491ce — PREMIUM_PURCHASER_CONTRACT_AVALANCHE
- [smart_contract] https://www.oklink.com/fantom/address/0x1ab3747da0f88e883895de58c105fd25c21491ce — PREMIUM_PURCHASER_CONTRACT_FANTOM
- [websites_and_applications] https://app.zerion.io/ — Zerion Web App
- [websites_and_applications] https://apps.apple.com/us/app/zerion-crypto-defi-wallet/id1456732565 — Zerion Apple App
- [websites_and_applications] https://chromewebstore.google.com/detail/zerion-wallet-for-web3-nf/klghhnkeealcohjjanjjdaeeggmfmlpl — Zerion Extension
- [websites_and_applications] https://play.google.com/store/apps/details?id=io.zerion.android&hl=en_US&gl=US — Zerion Android App

## Asset notes

Only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

## Impacts in scope (17)

- [smart_contract] Critical: Any logic manipulation
- [smart_contract] Critical: Theft and/or permanent freezing of assets
- [smart_contract] High: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unable to call smart contract
- [smart_contract] Medium: Unbounded gas consumption
- [websites_and_applications] Critical: Accessing sensitive pages without authorization
- [websites_and_applications] Critical: Deletion of user data
- [websites_and_applications] Critical: Leak of user data
- [websites_and_applications] Critical: Open redirects and modifying user’s vital information
- [websites_and_applications] Critical: Redirected funds by address modification
- [websites_and_applications] Critical: Site goes down
- [websites_and_applications] Critical: Users spoofing other users
- [websites_and_applications] High: Injection of text
- [websites_and_applications] Medium: Changing details of other users without direct financial impact (CSRF)
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Medium: Third-Party API keys leakage that demonstrates loss of funds or modification on the website

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$25,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: fixedReward=$7,500, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$15,000, minReward=$7,500, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: fixedReward=$7,500, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All web/app bug reports and Critical/High/Medium smart contract bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. In addition, all Critical/High/Medium bug reports must come with a suggestion for a fix in order to be considered for a reward. 

The following known issues are considered to be out of scope of this bounty program: 
  - All issues highlighted previously in the following audit report: 
    - Peckshield Audit for DeFi SDK (August, 2020): [https://drive.google.com/file/d/158GG-J681xAc4d8pMibpP_SFJikX4HPM/view?usp=sharing](https://drive.google.com/file/d/158GG-J681xAc4d8pMibpP_SFJikX4HPM/view?usp=sharing)
    - Audit: [https://github.com/zeriontech/defi-sdk/blob/interactive/audits/Zerion%20DeFi%20SDK%20Trail%20of%20Bits%20Audit%20Report.pdf](https://github.com/zeriontech/defi-sdk/blob/interactive/audits/Zerion%20DeFi%20SDK%20Trail%20of%20Bits%20Audit%20Report.pdf)
  - External apps having integrations with Zerion

Rewards for critical smart contract vulnerabilities are further capped at 10% of economic damage, with the main consideration being the funds affected in addition to PR and brand considerations, at the discretion of the team. However, there is a minimum reward of __USD 10 000__ for Critical bug reports. 

Critical website and application bug reports will be rewarded with the full __USD 15 000__ only if the impact leads to a direct loss in funds or a manipulation of the votes or the voting result, as well as the modification of its display leading to a misrepresentation of the result or vote. All other impacts that would be classified as Critical would be rewarded no more than __USD 10 000__.

Critical website and application vulnerabilities are also evaluated based on practical exploitability, persistence, recovery complexity, and impact on end users. Availability-only attacks (e.g. cache poisoning, CDN/cache-layer disruptions, temporary denial-of-service) that are operational in nature, reversible within a short period of time, require constrained exploitation conditions, and do not expose or endanger user funds, authentication, or account integrity will generally fall on the lower end of the Critical reward range.

Zerion requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed is email address, full name, and country of residence.

Payouts are handled by the __Zerion__ team directly and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

- Attacks requiring physical access to a user's device, social engineering, phishing, physical, or other fraud activities 
 - Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
