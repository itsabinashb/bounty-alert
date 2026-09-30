# Balancer Foundation

- Page: https://immunefi.com/bug-bounty/balancer/scope/
- Max bounty: $1,000,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (24)

- [smart_contract] https://etherscan.io/address/0x04d584195a96DFfc7F8B695aA3C9D3c1606b69d1#code — GyroECLPPoolFactory
- [smart_contract] https://etherscan.io/address/0x0E8B07657D719B86e06bF0806D6729e3D528C9A9 — V3 VaultExtension
- [smart_contract] https://etherscan.io/address/0x136f1EFcC3f8f88516B9E94110D56FDBfB1778d1 — BatchRouter
- [smart_contract] https://etherscan.io/address/0x187a05fb9e4234Dd310ae74215743560D1BAA6Ac#code — V3 StableSurgePoolFactory (V3)
- [smart_contract] https://etherscan.io/address/0x212F884252792ebaaA811FB0678444b21c7C2879#code — ProtocolFeeController (V2)
- [smart_contract] https://etherscan.io/address/0x301EDe5Fd4f9d7266B09c3A2E38F97776447154B#code — EclpLPOracleFactory
- [smart_contract] https://etherscan.io/address/0x332694Ef46D880DF6Ea9593e04CB8ABEE5F81D99#code — V3 WeightedPoolFactory (V2)
- [smart_contract] https://etherscan.io/address/0x35Cea9e57A393ac66Aaa7E25C391D52C74B5648f — BalancerRelayer (V6)
- [smart_contract] https://etherscan.io/address/0x35fFB749B273bEb20F40f35EdeB805012C539864 — V3 VaultAdmin
- [smart_contract] https://etherscan.io/address/0x3ccD78683efFffdDc1A16f5553C896ac6D3ab7FF#code — ReClammPoolFactory (V3)
- [smart_contract] https://etherscan.io/address/0x4b4b45Edf6Ca26ae894377Cf4FeD1FA9F82D85C6#code — WeightedLPOracleFactory (V2)
- [smart_contract] https://etherscan.io/address/0x4eFcd8bcE8AC9b94bd76648e2c85bEf6c40F3228#code — V3 StablePoolFactory (V3)
- [smart_contract] https://etherscan.io/address/0x6642863979e66d995717A2B836A121700595069A#code — V3 LBPoolFactory (V4)
- [smart_contract] https://etherscan.io/address/0x765ce16dbb3D7e89a9beBc834C5D6894e7fAA93c#code — StableLPOracleFactory (V2)
- [smart_contract] https://etherscan.io/address/0x8902F9C211f91c84Da2076f633873F8266dCECC6#code — Gyro2CLPPoolFactory
- [smart_contract] https://etherscan.io/address/0x8F42aDBbA1B16EaAE3BB5754915E0D06059aDd75#code — AuthorizerAdaptor
- [smart_contract] https://etherscan.io/address/0x9179C06629ef7f17Cb5759F501D89997FE0E7b45 — BufferRouter
- [smart_contract] https://etherscan.io/address/0xA331D84eC860Bf466b4CdCcFb4aC09a1B43F3aE6#code — Authorizer
- [smart_contract] https://etherscan.io/address/0xAE563E3f8219521950555F5962419C8919758Ea2#code — V3 Router (V2)
- [smart_contract] https://etherscan.io/address/0xBA12222222228d8Ba445958a75a0704d566BF2C8#code — V2 Vault
- [smart_contract] https://etherscan.io/address/0xb21A277466e7dB6934556a1Ce12eb3F032815c8A#code — CompositeLiquidityRouter (V2)
- [smart_contract] https://etherscan.io/address/0xbA1333333333a1BA1108E8412f11850A5C319bA9 — V3 Vault
- [smart_contract] https://etherscan.io/address/0xeA66501dF1A00261E3bB79D1E90444fc6A186B62 — BatchRelayerLibrary (V6)
- [smart_contract] https://etherscan.io/address/0xeb1aa94421aecfb1dc17ddb1068e4609c4be8758#code — FixedPriceLBPoolFactory

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

If a Critical impact can be caused to any other asset managed by Balancer that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project.

## Impacts in scope (7)

- [smart_contract] Critical: Permanent freezing of >1% of total funds in the Vault, affecting every pool type
- [smart_contract] Critical: Theft of >1% of total funds in the Vault, affecting every pool type
- [smart_contract] High: Permanent freezing of funds in excess of gas costs or swap fees, affecting a specific pool type
- [smart_contract] High: Theft of funds in excess of gas costs or swap fees, affecting a specific pool type
- [smart_contract] Medium: Permanent freezing of unclaimed yield
- [smart_contract] Medium: Temporary freezing of funds in excess of gas costs or swap fees
- [smart_contract] Medium: Theft of unclaimed yield

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$1,000,000, minReward=$100,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$75,000, minReward=$25,000, rewardModel=range
- [smart_contract] Medium: maxReward=$15,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All Critical/High severity bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

Critical smart contract vulnerabilities are further capped at __10%__ of economic damage, taking into account the funds at risk at the moment of the bug report submission. However, there is a minimum reward of __USD 100 000__. Additionally, the maximum reward is capped at __USD 1 000 000__, even if __10%__ of the damage in USD equivalent is greater than __USD 1 000 000__.

High severity smart contract vulnerabilities are also further capped at __10%__ of economic damage, taking into account the funds at risk at the moment of the bug report submission. However, there is a minimum reward of __25 000 USD__. Additionally, the maximum reward is capped at __USD 75 000__, even if __10%__ of the damage is greater than __USD 75 000__.

Vulnerabilities involving non-standard ERC20 tokens are considered out of scope, as it would be trivial to insert an exploit into a token for the sake of applying to this bug bounty. A standard, Balancer-compatible ERC20 token is one that conforms to all [EIP-20 interfaces](https://eips.ethereum.org/EIPS/eip-20) and exhibits expected behavior in implementation; i.e., transfers move exactly N tokens from sender to recipient, and balances do not change by any means other than transfers. Notably, tokens with transfer fees, rebasing supplies, streaming mechanics or multiple entrypoints are not compatible with Balancer, but that list is not exhaustive.

Following the same line, vulnerabilities that require the user to interact with explicitly malicious routers, pools, hooks or rate providers are out of scope. This is because introducing such vulnerabilities in a permissionless protocol is both trivial and impossible to prevent.

Known issues such as those previously highlighted in the following audit report are considered out of scope (list is not exhaustive): 
  - [https://github.com/balancer/balancer-v2-monorepo/tree/master/audits](https://github.com/balancer/balancer-v2-monorepo/tree/master/audits) 
  - [https://github.com/balancer/balancer-v3-monorepo/tree/master/audits](https://github.com/balancer/balancer-v3-monorepo/tree/master/audits)
  - [https://github.com/balancer/reclamm/tree/main/audits](https://github.com/balancer/reclamm/tree/main/audits)

Payouts are handled by the __Balancer__ team directly and are denominated in __USD__. However, payouts are done in __ETH__ or __USDC__, at the discretion of the team.

## Out of scope (program-specific)

Balancer is only compatible with standard ERC20 tokens that transfer the exact amount from sender to recipient, where balances do not change by any means other than transfers. Tokens with transfer fees, rebasing supplies, streaming mechanics, or multiple entry points are not compatible with Balancer; that list is not exhaustive. Impacts that depend on such tokens are out of scope.

Vulnerabilities that require the user to interact with explicitly malicious routers, pools, hooks, or rate providers are out of scope, because introducing such components in a permissionless protocol is trivial and impossible to prevent.

Best practice critiques are out of scope, as are known issues, such as those highlighted in the following audit reports, are out of scope (the list is not exhaustive):
https://github.com/balancer/balancer-v2-monorepo/tree/master/audits
https://github.com/balancer/balancer-v3-monorepo/tree/main/audits

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (4)

- Centeredness-preserving price-ratio updates in ReClamm pools can shift spot price in edge cases (issue 3.2.13). (https://github.com/balancer/reclamm/blob/reclamm-2.1/audits/cantina/2026-04-13.pdf)
- LBP swaps can leave a token's real Vault balance below the minimum trade amount, causing subsequent proportional exits to revert until Recovery Mode is enabled. FixedPriceLBPool does not enforce a minimum remaining balance after a swap. In seedless bidirectional LBPool configurations, the virtual reserve balance can satisfy the inherited minimum-balance check while the real reserve falls below the minimum. (https://github.com/balancer/balancer-v3-monorepo/pull/1673)
- The way the surge fees are computed in the stable surge hook is an approximation that keeps the computation simple. For big swaps and large max surge swap fee, the approximation breaks exact in / exact out equivalence. In other words:  swap_in(Ai) = Ao  swap_out(Ao) != Ai Since this happens only in extreme cases that are not relevant in practice, simplicity is preferred over accuracy in this case. By no means this constitutes a security issue: any error computing a dynamic swap fee above the static swap fee percentage cannot lead to theft of funds. (https://github.com/balancer/balancer-v3-monorepo/blob/main/audits/WONTFIX.md#stable-surge---exact-in--exact-out-equivalence)
- When the aggregate fees are split between protocol and pool creator, rounding effects can make the transaction revert under specific circumstances.  These typically happen when the pool creator fee is low, and low amount of fees are collected.  In this case, the cost of fixing an obscure edge case and migrating the fee controller is not justified by the potential impact. In practice:  Most pools do not use pool creator fees While the fee split to trigger the problem is technically valid, fee splits in practice tend to use larger numbers Fees are collected after they reach certain threshold, not right after each operation generates any amount of fees (https://github.com/balancer/balancer-v3-monorepo/blob/main/audits/WONTFIX.md#protocol-fee-controller---fee-split-rounding)
