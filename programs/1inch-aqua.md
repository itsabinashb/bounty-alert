# 1inch - Aqua

- Page: https://immunefi.com/bug-bounty/1inch-aqua/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (33)

- [smart_contract] https://github.com/1inch/aqua/blob/v1.0.0/src/Aqua.sol — Aqua - src/Aqua.sol - new
- [smart_contract] https://github.com/1inch/aqua/blob/v1.0.0/src/AquaRouter.sol — Aqua - src/AquaRouter.sol - new
- [smart_contract] https://github.com/1inch/aqua/blob/v1.0.0/src/libs/Balance.sol — Aqua - src/libs/Balances.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/6.9.16/contracts/libraries/Calldata.sol — Utils - contracts/libraries/Calldata.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/libraries/CalldataPtr.sol — Utils - contracts/libraries/CalldataPtr.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/libraries/ECDSA.sol — Utils - contracts/libraries/ECDSA.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/libraries/RevertReasonForwarder.sol — Utils - contracts/libraries/RevertReasonForwarder.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/libraries/SafeERC20.sol — Utils - contracts/libraries/SafeERC20.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/libraries/StringUtil.sol — Utils - contracts/libraries/StringUtil.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/libraries/Transient.sol — Utils - contracts/libraries/Transient.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/libraries/TransientLock.sol — Utils - contracts/libraries/TransientLock.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/libraries/UniERC20.sol — Utils - contracts/libraries/UniERC20.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/mixins/EthReceiver.sol — Utils - contracts/mixins/EthReceiver.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/mixins/Multicall.sol — Utils - contracts/mixins/Multicall.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/mixins/OnlyWethReceiver.sol — Utils - contracts/mixins/OnlyWethReceiver.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/mixins/Rescuable.sol — Utils - contracts/mixins/Rescuable.sol - new
- [smart_contract] https://github.com/1inch/solidity-utils/blob/7.0.0/contracts/mixins/Simulator.sol — Utils - contracts/mixins/Simulator.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/main/src/routers/AquaSwapVMRouter.sol — Swap VM - src/routers/AquaSwapVMRouter.sol
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/SwapVM.sol — Swap VM - src/SwapVM.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/instructions/Balances.sol — Swap VM - src/instructions/Balances.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/instructions/Controls.sol — Swap VM - src/instructions/Controls.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/instructions/Decay.sol — Swap VM - src/instructions/Decay.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/instructions/Extruction.sol — Swap VM - src/instructions/Extruction.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/instructions/Fee.sol — Swap VM - src/instructions/Fee.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/instructions/PeggedSwap.sol — Swap VM - src/instructions/PeggedSwap.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/instructions/XYCConcentrate.sol — Swap VM - src/instructions/XYCConcentrate.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/instructions/XYCSwap.sol — Swap VM - src/instructions/XYCSwap.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/libs/MakerTraits.sol — Swap VM - src/libs/MakerTraits.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/libs/PeggedSwapMath.sol — Swap VM - src/libs/PeggedSwapMath.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/libs/TakerTraits.sol — Swap VM - src/libs/TakerTraits.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/libs/VM.sol — Swap VM - src/libs/VM.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/opcodes/AquaOpcodes.sol — Swap VM - src/opcodes/AquaOpcodes.sol - new
- [smart_contract] https://github.com/1inch/swap-vm/blob/v1.0.2/src/routers/AquaSwapVMRouter.sol — Swap VM - src/routers/AquaSwapVMRouter.sol - new

## Asset notes

(none)

## Impacts in scope (10)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of coins or tokens (e.g gas) in a smart contract intended for transaction fees
- [smart_contract] Low: Impacts caused by griefing with no economic damage other than transaction fees where fix requires a change or a pause of a smart contract
- [smart_contract] Low: Smart contract fails to deliver promised token amounts but the remaining token amounts is not stolen or lost and can still be claimed

## Impact notes

***Note: The program applies only to the latest tag/releases.***

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$20,000, rewardCalculationPercentage=0, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, minReward=$2,000, rewardModel=range
- [smart_contract] Low: maxReward=$2,000, minReward=$100, rewardModel=range

## Reward notes

## Reward Calculation for All Reports

***Note: The program applies only to the latest tag/releases.***

As Aqua is not yet deployed on mainnet with actual user funds, all severity levels have a base reward amount. At its discretion, 1inch may decide to provide a reward up to the maximum of each respective severity level. However, any amount higher than the base reward amount is not guaranteed and 1inch retains full rights in determining whether or not a report justifies a reward greater than the base reward amount. By default, only the base reward amount is provided and is what security researchers should expect. 

Once Aqua is deployed to mainnet with live user funds, this section will be reviewed and updated to reflect production reward amounts. Reports submitted prior to mainnet deployment will be evaluated against the rules in effect at the time of submission. 1inch reserves the right to update reward amounts for new submissions after mainnet deployment.

## Other Limitations and Requirements

https://github.com/1inch/sdks asset are out-of-scope.

Within the https://github.com/1inch/swap-vm asset, the file src/strategies/AquaAMM.sol is explicitly out of scope. Vulnerabilities or improvements affecting this file are not eligible for rewards.

## Research License

Participants are granted a limited, non-exclusive, non-transferable license to compile, deploy, and test the Aqua codebase listed in the Assets in Scope table solely for the purpose of identifying vulnerabilities under this bug bounty program. This license:

- Is limited to local development environments, local forks, and testnets — production deployments and live mainnet usage are prohibited
- Does not permit redistribution, sublicensing, or commercial use of the code
- Does not transfer any intellectual property rights
- Provides safe harbor against claims under applicable computer fraud and copyright statutes (including but not limited to ARSL, EULA, DMCA, and CFAA) for actions taken in good faith and in compliance with the rules of this program
- Auto-terminates upon any breach of program rules, after which the safe harbor no longer applies and 1inch reserves all rights

This license applies only to the assets explicitly listed in scope and does not extend to any other 1inch property or third-party dependencies.


Publishing or distributing modified versions of Aqua source code, binaries, or compiled artifacts in any form is prohibited, both during and after the embargoed period. After coordinated disclosure, only minimal technical details necessary to describe the vulnerability or fix may be shared, and only with prior written approval from 1inch consistent with the Responsible Publication policy above.

## Reward Payment Terms

Payouts are handled by the 1inch team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability. 

*Reports and payout details may be checked against OFAC, EU, and UK sanctions lists prior to payment. Payment may be withheld, delayed, or refused entirely if prohibited by applicable law, sanctions regimes, or 1inch's compliance obligations. Researchers are responsible for ensuring their participation does not violate the laws of their jurisdiction.*

## Out of scope (program-specific)

These impacts are out of scope for this bug bounty program. 

**All Categories:**

* Impacts requiring attacks that the reporter has already exploited themselves, leading to damage  
* Impacts caused by attacks requiring access to leaked keys/credentials  
* Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible  
* Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code  
* Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production  
* Best practice recommendations  
* Feature requests  
* Impacts on test files and configuration files unless stated otherwise in the bug bounty program  
* Impacts requiring phishing or other social engineering attacks against project's employees and/or customers
* Redundant code
* Old compiler version
* Code style guide violations
* The compiler version is not locked
* Theoretical or purely speculative exploits without demonstrated business impact


**Blockchain/DLT & Smart Contract Specific:**

* Incorrect data supplied by third party oracles  
  * Not to exclude oracle manipulation/flash loan attacks  
* Impacts requiring basic economic and governance attacks (e.g. 51% attack)  
* Lack of liquidity impacts  
* Impacts from Sybil attacks  
* Impacts involving centralization risks  
* Vulnerabilities in imported contracts or third-party libraries, except where 1inch-specific configuration or initialization causes the issue  
* Lack of support for Fee-on-Transfer (FoT) tokens  
* Known issues in third-party dependencies, except where they materialize through 1inch-specific misconfiguration
* TWAP-related issues

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


## Additional Out of Scope terms:

- https://github.com/1inch/sdks asset are out-of-scope.

- Within the https://github.com/1inch/swap-vm asset, the file src/strategies/AquaAMM.sol is explicitly out of scope. Vulnerabilities or improvements affecting this file are not eligible for rewards.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
