# OpenZeppelin

- Page: https://immunefi.com/bug-bounty/openzeppelin/scope/
- Max bounty: $25,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (6)

- [smart_contract] https://github.com/OpenZeppelin/openzeppelin-community-contracts/blob/master/contracts/crosschain/ERC7786OpenBridge.sol — ERC7786OpenBridge (only commit 0361935dc5edd233adbb9fbae5871ccbb8c739d8 in scope)
- [smart_contract] https://github.com/OpenZeppelin/openzeppelin-community-contracts/blob/master/contracts/crosschain/axelar/AxelarGatewayAdapter.sol — Axelar Gateway Adapter (only commit 0361935dc5edd233adbb9fbae5871ccbb8c739d8 in scope)
- [smart_contract] https://github.com/OpenZeppelin/openzeppelin-confidential-contracts/releases/tag/v0.5.3 — OpenZeppelin Confidential Contracts (only the latest release v.0.5.3 (4a4f6c71f58b75e391899b57e42e3b73d288dfe3) is in-scope, mocks and examples are also out-of-scope)
- [smart_contract] https://github.com/OpenZeppelin/openzeppelin-contracts — Smart Contract
- [smart_contract] https://github.com/OpenZeppelin/openzeppelin-contracts-upgradeable — Smart Contract
- [smart_contract] https://github.com/OpenZeppelin/uniswap-hooks

## Asset notes

All smart contracts in the “contracts” directory are included in the bug bounty, except those under “contracts/mocks”, which are testing artifacts, and those under “contracts/vendor”.

## Impacts in scope (14)

- [smart_contract] Critical: Access control is bypassed, including privilege escalation
- [smart_contract] Critical: Direct theft of user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] High: Governance voting result manipulation
- [smart_contract] High: Permanent denial of service (smart contract is made unable to operate)
- [smart_contract] High: Permanent freezing of funds
- [smart_contract] High: Temporary freezing of funds - Impact severity depends on funds at risk
- [smart_contract] High: Theft of unclaimed yield / Permanent freezing of unclaimed yield - Impact severity is determined by potential yield lost
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Invalid events are emitted, potentially confusing indexers (internal storage is unaffected)
- [smart_contract] Low: Temporary denial of service (smart contract is made unable to operate for one block, functionality is restored in the next block)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$25,000, minReward=$5,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$5,000, minReward=$2,500, rewardModel=range
- [smart_contract] Medium: fixedReward=$2,500, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit. 

The rewards stated here are additive to any existing bug bounty programs hosted by projects that are currently using OpenZeppelin contracts. 

Bounty rewards are given according to an impact/likelihood [matrix for assessing threat levels.](https://raw.githubusercontent.com/OpenZeppelin/immunefi-assets/main/impact-likelihood-matrix.png) Each issue is assessed considering the likelihood of the vulnerability being successfully exploited and the expected impact in scope to a single instance of the affected smart contract. Note that, as can be seen in the matrix, if the impact is Critical then the threat is always Critical, for other impacts the maximum reduction is one level only if the likelihood is low, and if the likelihood is high then the threat is increased one level above the impact. 

__Proof of Concept (PoC) Requirements__

A PoC compliant with [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules) is required for the following severity levels:
- Smart Contract: Critical
- Smart Contract: High

Bugs introduced by a release candidate version and reported during the review period, the dates for which will be declared by OpenZeppelin on each release, will receive a 50% bonus.

Payouts are handled by the __OpenZeppelin__ team directly and are denominated in USD. However, payouts are done in __ETH__ or __USDC__.

## Out of scope (program-specific)

- Best practice critiques
- ERC mandated behaviors

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (8)

- Final cancel clears accounting while the hook still holds accrued fee claims (https://github.com/OpenZeppelin/uniswap-hooks/issues/127)
- In `_beforeSwap`, the hook iterates over all ticks between last tick and current tick. Developers must be aware that for large price changes in pools with small tick spacing, the `for` loop will iterate over a large number of ticks, which could lead to `MemoryOOG` error. (https://github.com/OpenZeppelin/uniswap-hooks/blob/2c39623ce5a5103bd314f1380df0443df2523149/src/general/AntiSandwichHook.sol#L44)
- RLP's `decodeBool`, `decodeUint256`, `decodeBytes32`, `decodeBytes`, and `decodeString` accept trailing bytes (https://github.com/OpenZeppelin/openzeppelin-contracts/issues/6515)
- Swaps without JIT liquidity allow seeded assets to be exchanged at a poisoned price

Root Cause: _beforeSwap lets a swap continue when no JIT liquidity is available, allowing the pool price to move without any token exchange before assets are seeded.

Toy example:

A tick-spacing-60 pool is initialized without liquidity.
An attacker uses a zero-liquidity swap to move slot0 above the hook's upper tick without paying assets.
An LP seeds 100e18 units of each token.
The attacker reverses the price and receives approximately 91.99e18 token1 for six wei of token0, including the pool fee.
Location: ReHypothecationHook._beforeSwap

The ReHypothecationHook._beforeSwap function temporarily provides liquidity from the hook's yield sources before each swap. When _getLiquidityToUse returns zero, _beforeSwap skips _modifyLiquidity but unconditionally allows the swap to continue. This state necessarily exists between pool initialization and the permissionless seedLiquidity call.

In Uniswap v4, a nonzero swap with zero active liquidity can advance the price to the caller's valid price limit while producing zero input, output, and fee amounts. For tick spacing 60, valid prices exist above the hook's getTickUpper boundary. An attacker can therefore move slot0 above the JIT range without paying assets and wait for seedLiquidity, which deposits the supplied assets but neither validates nor resets slot0. At the poisoned price, _getLiquidityToUse converts the balanced seed into one-sided JIT liquidity. The attacker can then reverse the swap, cross into that liquidity, and extract most of the seeded asset at the extreme price. With a 0.3% pool fee and 100e18 units of each token seeded, the reverse swap can receive approximately 91.990778322506861783e18 token1 for five wei of token0 plus one wei of fee.

Consider reverting in _beforeSwap whenever the computed JIT liquidity is zero. Also consider enforcing atomic initialization and seeding, or requiring slot0 to remain inside the active range and the seed ratio to match the current price. (https://audits.openzeppelin.com/openzeppelin-solidity/project/uniswap-hooks/2da25c3b-6073-4085-a42f-0e33736a166a/issue/swaps-without-jit-liquidity-allow-seeded-assets-to-be-exchanged-at-a-poisoned-price)
- The Anti-sandwich mechanism only protects swaps in the zeroForOne swap direction. Swaps in the !zeroForOne direction are not protected by this hook design. (https://github.com/OpenZeppelin/uniswap-hooks/blob/26dc8e53f812a1ca390d470342adb6cd8c3286ad/src/general/AntiSandwichHook.sol#L38)
- The RehypothecadedHook relies on the PoolManager singleton token reserves for flash accounting debts and credits during swaps. During `afterSwap`, the hook briefly generates token debts to the PoolManager even before users transfer their swap tokens. As a consequence, the PoolManager singleton may lack sufficient reserves for illiquid tokens in the instants between the swap executed and the posterior payment from the user, preventing swaps from being executed until the PoolManager accumulates enough tokens. Altrough it is very unlikely to happen, it can be mitigated by maintaining some permanent pool liquidity alongside rehypothecated liquidity. (https://github.com/OpenZeppelin/uniswap-hooks/blob/638c56d9bf1ebd0f3b192b9d0392a70d525a37fa/src/general/ReHypothecationHook.sol#L55)
- Withdrawal accounting can underflow after earlier withdrawals, permanently blocking some participants (https://github.com/OpenZeppelin/uniswap-hooks/issues/129)
- https://github.com/OpenZeppelin/uniswap-hooks/issues/140 (https://github.com/OpenZeppelin/uniswap-hooks/issues/140)
