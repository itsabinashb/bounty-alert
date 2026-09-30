# Exactly

- Page: https://immunefi.com/bug-bounty/exactly/scope/
- Max bounty: $25,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (23)

- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://optimistic.etherscan.io/address/0x22ab31Cd55130435b5efBf9224b6a9d5EC36533F — MarketWstETH
- [smart_contract] https://optimistic.etherscan.io/address/0x29bAbFF3eBA7B517a75109EA8fd6D1eAb4A10258 — MarketETHRouter
- [smart_contract] https://optimistic.etherscan.io/address/0x3179265d20d13cE507157b8087dE48759eb21006 — InterestRateModelWETH
- [smart_contract] https://optimistic.etherscan.io/address/0x3d73D0fb9e63c49ba8e9cd738964D5E08C047f3e — ExaPlugin
- [smart_contract] https://optimistic.etherscan.io/address/0x59a644e490e48235adf8ba9b814a4f666c4feb3a — IssuerChecker
- [smart_contract] https://optimistic.etherscan.io/address/0x60D92e570D096f8E5C99A600bD130d71295AaF38 — InterestRateModelWstETH
- [smart_contract] https://optimistic.etherscan.io/address/0x6817974ca2c354f2fa40d8349b725b5bf81c8338 — ProposalManager
- [smart_contract] https://optimistic.etherscan.io/address/0x6926B434CCe9b5b7966aE1BfEef6D0A7DCF3A8bb — MarketUSDC
- [smart_contract] https://optimistic.etherscan.io/address/0x6E1Bb47F2895E84160f61df922e7fF0B656f3Cff — InstallmentsRouter
- [smart_contract] https://optimistic.etherscan.io/address/0x6f748FD65d7c71949BA6641B3248C4C191F3b322 — MarketWBTC
- [smart_contract] https://optimistic.etherscan.io/address/0x81C9A7B55A4df39A9B7B5F781ec0e53539694873 — MarketUSDC.e
- [smart_contract] https://optimistic.etherscan.io/address/0x8C2F35c8076bCb5D4b696bAE11AcA0ac0Dd873e4 — InterestRateModelUSDC
- [smart_contract] https://optimistic.etherscan.io/address/0x8f498c8240E621f8050249D1C2F5f2AAeE484ca0 — WebAuthnOwnerPlugin
- [smart_contract] https://optimistic.etherscan.io/address/0x92024C4bDa9DA602b711B9AbB610d072018eb58b — TimelockController
- [smart_contract] https://optimistic.etherscan.io/address/0xBd1ba78A3976cAB420A9203E6ef14D18C2B2E031 — RewardsController
- [smart_contract] https://optimistic.etherscan.io/address/0xCEed2bFE740F02dB6094eBE89FF93b1031be752b — StakedEXA
- [smart_contract] https://optimistic.etherscan.io/address/0xa430A427bd00210506589906a71B54d6C256CEdb — MarketOP
- [smart_contract] https://optimistic.etherscan.io/address/0xaEb62e6F27BC103702E7BC879AE98bceA56f027E — Auditor
- [smart_contract] https://optimistic.etherscan.io/address/0xb27113B72135942065E0Fa09984FE2Bf008d5f3c — DebtManager
- [smart_contract] https://optimistic.etherscan.io/address/0xbea586A167853ADddEF12818f264f1F9823fBc18 — EscrowedEXA
- [smart_contract] https://optimistic.etherscan.io/address/0xc4d4500326981eacD020e20A81b1c479c161c7EF — MarketWETH
- [smart_contract] https://optimistic.etherscan.io/address/0xd5f8c9d87b7691449dec453d041d9054e0fdd228 — Refunder

## Asset notes

Only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

Though only the proxy contracts are listed as in-scope, current implementation and any further updates to the implementation contracts are considered in scope. When reporting a bug, please make sure to select the relevant proxy smart contract as the target. 

If an impact can be caused to any other asset managed by Exactly that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for consideration by the project. This only applies to Critical and High impacts.

Periphery Contracts have a reward cap equal to “High” (USD 25 000). This means that regardless of the complexity, impact, or exploitability of a potential vulnerability discovered within these contracts, the bounty paid out will not exceed that limit.

## Impacts in scope (12)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Miner-extractable value (MEV)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Substantial generation of bad debt on the protocol
- [smart_contract] High: Temporary freezing of funds for at least 4 hours
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield

## Impact notes

Only the following impacts are accepted within this bug bounty program. All other impacts are not considered in-scope, even if they affect something in the assets in the scope table.

## Rewards

- [smart_contract] Critical: maxReward=$25,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$5,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

Audit Discoveries and Known Issues

Bug reports covering previously-discovered bugs are not eligible for any reward through the bug bounty program. If a bug report covers a known issue (e.g., the use of deprecated Chainlink API was reported in [EXA-36](https://github.com/exactly/audits/blob/main/Coinspect%204th%20audit%20(Oct-22).pdf)), it may be rejected together with proof of the issue being known before escalation of the bug report via Immunefi.

Previous audits and known issues can be found at: [https://docs.exact.ly/security/audits](https://docs.exact.ly/security/audits).

All High and Critical Smart Contract bug reports require a PoC to be eligible for a reward. Explanations and statements are not accepted as PoC and code is required.

Critical smart contract vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk, but also PR and branding aspects, at the discretion of the team. However, there is a minimum reward of __USD 20 000__. 

KYC is required for this bug bounty program. Government identification, legal name, and country of residence will need to be supplied.

Payouts are handled by the __Exactly__ team directly and are denominated in USD. However, payouts are done in __USDC and DAI__, with the choice of the ratio at the team's discretion.

## Out of scope (program-specific)

- Griefing
  - Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
