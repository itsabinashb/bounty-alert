# 1inch - Aqua Improvement

- Page: https://immunefi.com/bug-bounty/1inch-aqua-improvement/scope/
- Max bounty: $25,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low
- End date: (none)

## Assets in scope (32)

- [smart_contract] https://github.com/1inch/aqua/blob/main/src/Aqua.sol — Aqua - src/Aqua.sol
- [smart_contract] https://github.com/1inch/aqua/blob/main/src/AquaRouter.sol — Aqua - src/AquaRouter.sol
- [smart_contract] https://github.com/1inch/aqua/blob/main/src/libs/Balance.sol — Aqua - src/libs/Balances.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/Calldata.sol — Utils - contracts/libraries/Calldata.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/CalldataPtr.sol — Utils - contracts/libraries/CalldataPtr.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/ECDSA.sol — Utils - contracts/libraries/ECDSA.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/RevertReasonForwarder.sol — Utils - contracts/libraries/RevertReasonForwarder.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/SafeERC20.sol — Utils - contracts/libraries/SafeERC20.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/StringUtil.sol — Utils - contracts/libraries/StringUtil.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/Transient.sol — Utils - contracts/libraries/Transient.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/TransientLock.sol — Utils - contracts/libraries/TransientLock.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/libraries/UniERC20.sol — Utils - contracts/libraries/UniERC20.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/mixins/EthReceiver.sol — Utils - contracts/mixins/EthReceiver.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/mixins/Multicall.sol — Utils - contracts/mixins/Multicall.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/mixins/OnlyWethReceiver.sol — Utils - contracts/mixins/OnlyWethReceiver.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/mixins/Rescuable.sol — Utils - contracts/mixins/Rescuable.sol
- [smart_contract] https://github.com/1inch/solidity-utils/blob/master/contracts/mixins/Simulator.sol — Utils - contracts/mixins/Simulator.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/SwapVM.sol — Swap VM - src/SwapVM.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/instructions/Balances.sol — Swap VM - src/instructions/Balances.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/instructions/Controls.sol — Swap VM - src/instructions/Controls.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/instructions/Decay.sol — Swap VM - src/instructions/Decay.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/instructions/Extruction.sol — Swap VM - src/instructions/Extruction.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/instructions/Fee.sol — Swap VM - src/instructions/Fee.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/instructions/PeggedSwap.sol — Swap VM - src/instructions/PeggedSwap.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/instructions/XYCConcentrate.sol — Swap VM - src/instructions/XYCConcentrate.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/instructions/XYCSwap.sol — Swap VM - src/instructions/XYCSwap.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/libs/MakerTraits.sol — Swap VM - src/libs/MakerTraits.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/libs/PeggedSwapMath.sol — Swap VM - src/libs/PeggedSwapMath.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/libs/TakerTraits.sol — Swap VM - src/libs/TakerTraits.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/libs/VM.sol — Swap VM - src/libs/VM.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/opcodes/AquaOpcodes.sol — Swap VM - src/opcodes/AquaOpcodes.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/routers/AquaSwapVMRouter.sol — Swap VM - src/routers/AquaSwapVMRouter.sol

## Asset notes

(none)

## Impacts in scope (6)

- [smart_contract] Low: Accounting/invariant correctness (liquidity shares, fees/rewards, rounding/precision)
- [smart_contract] Low: Enhancements to existing protocol mechanics that materially improve user value, safety, or capital efficiency without introducing fundamentally new functionality
- [smart_contract] Low: Integration fixes where 1inch-specific configuration/initialization of third-party libraries creates risk
- [smart_contract] Low: MEV/price-manipulation resistance (oracle usage, slippage/deadline handling, sandwich protection, excluding TWAP)
- [smart_contract] Low: Security hardening of existing contracts (tighter authorization/roles, reentrancy mitigations, invariant enforcement)
- [smart_contract] Low: Substantial gas efficiency improvements (≥1k gas net savings per typical user transaction on hot paths)

## Impact notes

***Note: The program applies only to the latest tag/releases.***

## Rewards

- [smart_contract] Low: maxReward=$25,000, minReward=$100, rewardModel=range

## Reward notes

***Note: The program applies only to the latest tag/releases.***

#### Proof of Concept (PoC) Requirements

A PoC is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules). 

A demonstration of the proposal's value is required for this program. Depending on the type of improvement, this may take the form of:

* Before/after benchmarks (for gas optimizations or performance improvements)  
* Test cases demonstrating accounting/invariant correctness  
* A minimal reproducible example showing the integration issue or hardening gap

A brief implementation outline demonstrating how the change would be applied

#### Previous Audits

1inch’s completed audit reports can be found at https://github.com/1inch/1inch-audits. Any improvement suggestions mentioned in these reports are not eligible for a reward.

#### 

### Rewards by Threat Level

Rewards are distributed according to the Impacts in Scope table. 

#### Reward Calculation for All Reports

Reports under this program follow a goodwill payout process. There is no guaranteed minimum reward — 1inch retains full discretion on whether to provide a reward for any submitted improvement suggestion, and on the exact amount within the range of USD 100 to USD 25000 based on the demonstrated value of the proposal. Submission of a proposal does not entitle the proposer to a reward.

#### Other Limitations and Requirements

[https://github.com/1inch/sdks](https://github.com/1inch/sdks) asset is out-of-scope.

Within the https://github.com/1inch/swap-vm asset, the file src/strategies/AquaAMM.sol is explicitly out of scope. Vulnerabilities or improvements affecting this file are not eligible for rewards.  
This license applies only to the assets explicitly listed in scope and does not extend to any other 1inch property or third-party dependencies.

Publishing or distributing modified versions of Aqua source code, binaries, or compiled artifacts in any form is prohibited, both during and after the embargoed period. After coordinated disclosure, only minimal technical details necessary to describe the vulnerability or fix may be shared, and only with prior written approval from 1inch consistent with the Responsible Publication policy above.

Each proposal should describe the rationale and expected impact, identify affected contracts or components, outline minimal tests and benchmarks, and, if relevant, note any migration considerations. A good PoC typically includes clear before/after evidence, a minimal reproducible example, and a brief implementation outline demonstrating how the change would be applied.

Immunefi Mediations are not possible with this bug bounty program as it only covers improvement suggestions. Any request for mediation will be closed. 

#### Research License

Participants are granted a limited, non-exclusive, non-transferable license to compile, deploy, and test the Aqua codebase listed in the Assets in Scope table solely for the purpose of identifying vulnerabilities under this bug bounty program. This license:

* Is limited to local development environments, local forks, and testnets — production deployments and live mainnet usage are prohibited  
* Does not permit redistribution, sublicensing, or commercial use of the code  
* Does not transfer any intellectual property rights  
* Provides safe harbor against claims under applicable computer fraud and copyright statutes (including but not limited to ARSL, EULA, DMCA, and CFAA) for actions taken in good faith and in compliance with the rules of this program  
* Auto-terminates upon any breach of program rules, after which the safe harbor no longer applies and 1inch reserves all rights

This license applies only to the assets explicitly listed in scope and does not extend to any other 1inch property or third-party dependencies.

Publishing or distributing modified versions of Aqua source code, binaries, or compiled artifacts in any form is prohibited, both during and after the embargoed period. After coordinated disclosure, only minimal technical details necessary to describe the vulnerability or fix may be shared, and only with prior written approval from 1inch consistent with the Responsible Publication policy above.

#### Reward Payment Terms

Payouts are handled by the 1inch team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability. 

Reports and payout details may be checked against OFAC, EU, and UK sanctions lists prior to payment. Payment may be withheld, delayed, or refused entirely if prohibited by applicable law, sanctions regimes, or 1inch's compliance obligations. Researchers are responsible for ensuring their participation does not violate the laws of their jurisdiction.

## Out of scope (program-specific)

These impacts are out of scope for this bug bounty program. 

**All Categories:**

* Proposals previously submitted by another researcher (first-proposer policy applies)  
* Proposals already documented in publicly available audit reports listed in the Previous Audits section  
* Proposals that overlap with publicly known roadmap items, unless providing substantial new insight or a materially better implementation  
* Proposals submitted as AI-generated content without meaningful researcher analysis or original contribution  
* Proposals lacking the demonstrations described in the PoC Requirements section
* Redundant code
* Old compiler version
* Code style guide violations
* The compiler version is not locked
* Theoretical or purely speculative exploits without demonstrated business impact


**Blockchain/DLT & Smart Contract Specific:**

* Changes that weaken security/correctness or materially increase complexity risk  
* Pure refactors (style/naming/comments) without measurable security or cost impact  
* Compiler/pragma/lint/config changes that do not demonstrably improve safety or efficiency  
* New features or protocol mechanics (feature requests) rather than improvements to existing contracts  
* Duplicates of known issues/roadmap items, unless providing substantial new insight or a materially better solution  
* Micro gas optimizations (\< 1k gas net savings per typical user transaction on hot paths) or changes that merely shift costs between paths without net benefit  
* Proposals dependent on third-party code we do not control, or targeting imported libraries, except where 1inch-specific integration/initialization causes the issue  
* Off-chain only suggestions (UI, backend, indexers, docs) unless they directly and materially improve on-chain security

**Prohibited Activities:**

* Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet  
* Any testing with pricing oracles or third-party smart contracts (Testing the integration logic on local forks is permitted)  
* Attempting phishing or other social engineering attacks against our employees and/or customers  
* Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)  
* Any denial of service attacks that are executed against project assets  
* Automated testing of services that generates significant amounts of traffic  
* Public disclosure of an unpatched vulnerability in an embargoed bounty  
* Accessing or modifying data belonging to other users  
* Submitting AI-generated reports  
* Spamming forms or account creation flows (even with low volume)  
* Any testing of proposals on mainnet or public testnet deployments — testing should be done on local forks only  
* Submitting AI-generated proposals without substantive original analysis or contribution  
* Submitting low-quality or spam proposals (multiple repetitive proposals with minimal substantive difference will be treated as spam)  
* Attempting phishing or social engineering against 1inch employees or contractors

Public disclosure of any proposal details prior to receiving 1inch's explicit written approval, in accordance with the Responsible Publication policy

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
