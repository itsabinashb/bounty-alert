# Axelar Network

- Page: https://immunefi.com/bug-bounty/axelarnetwork/scope/
- Max bounty: $500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Smart Contract
- PoC required for: smart_contract - critical, blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (22)

- [blockchain_dlt] https://github.com/axelarnetwork/axelar-core — Infrastructure -  Axelar core protocol
- [blockchain_dlt] https://github.com/axelarnetwork/tofn/blob/main/src/ecdsa/mod.rs — Axelarcrypto library
- [blockchain_dlt] https://github.com/axelarnetwork/tofnd — Infrastructure -  Axelar signer
- [smart_contract] https://aurorascan.dev/address/0x304acf330bbE08d1e512eefaa92F6a57871fD895#code — Aurora Axelar Gateway contract address Proxy
- [smart_contract] https://bscscan.com/address/0x304acf330bbE08d1e512eefaa92F6a57871fD895 — Binance Axelar Gateway contract address Proxy
- [smart_contract] https://bscscan.com/address/0x4268B8F0B87b6Eae5d897996E6b845ddbD99Adf3 — Binance  axlUSDC token address
- [smart_contract] https://etherscan.io/address/0x4F4495243837681061C4743b74B3eEdf548D56A5 — Ethereum Axelar Gateway contract address Proxy
- [smart_contract] https://etherscan.io/address/0x83a93500d23Fbc3e82B410aD07A6a9F7A0670D66 — Interchain Token Factory contract address proxy (all chains)
- [smart_contract] https://etherscan.io/address/0xB5FB4BE02232B1bBA4dC8f81dc24C26980dE9e3C — Interchain Token Service contract address (all chains)
- [smart_contract] https://etherscan.io/token/0x467719aD09025FcC6cF6F8311755809d45a5E5f3 — AXL token address
- [smart_contract] https://ftmscan.com/address/0x1B6382DBDEa11d97f24495C9A90b7c88469134a4 — Fantom axlUSDC token address
- [smart_contract] https://ftmscan.com/address/0x5e3C572A97D898Fe359a2Cea31c7D46ba5386895 — Fantom Axelar Gateway contract address Proxy
- [smart_contract] https://github.com/axelarnetwork/axelar-cgp-solidity — Infrastructure - Axelar EVM Gateway
- [smart_contract] https://github.com/axelarnetwork/axelar-gmp-sdk-solidity — Infrastructure - GMP SDK
- [smart_contract] https://github.com/axelarnetwork/axelar-gmp-sdk-solidity/blob/main/contracts/governance/InterchainGovernance.sol — Interchain Governance Contract
- [smart_contract] https://github.com/axelarnetwork/interchain-token-service — Interchain Token Service
- [smart_contract] https://moonbeam.moonscan.io/address/0x4F4495243837681061C4743b74B3eEdf548D56A5#code — Moonbeam Axelar Gateway contract address Proxy
- [smart_contract] https://moonbeam.moonscan.io/address/0xCa01a1D0993565291051daFF390892518ACfAD3A — Moonbeam axlUSDC token address
- [smart_contract] https://polygonscan.com/address/0x6f015F16De9fC8791b234eF68D486d2bF203FBA8 — Polygon Axelar Gateway contract address Proxy
- [smart_contract] https://polygonscan.com/address/0x750e4C4984a9e0f12978eA6742Bc1c5D248f40ed — Polygon axlUSDC token address
- [smart_contract] https://snowtrace.io/address/0x5029C0EFf6C34351a0CEc334542cDb22c7928f78 — Avalanche Axelar Gateway contract address Proxy
- [smart_contract] https://snowtrace.io/address/0xfaB550568C688d5D8A52C7d794cb93Edc26eC0eC — Avalanche axlUSDC token address

## Asset notes

Only those contracts from the repos in the Assets in Scope table are considered as in-scope of the bug bounty program. In tofn, the only thing in scope is src/ecdsa/mod.rs and it’s project dependencies, excluding third-party dependencies. Only tofnd pieces relating to the mod.rs file in tofn is in scope. 

Impacts stemming from off-chain components, such as relayers and vald, are out of scope. We still encourage reporting these. They’ll be accepted at the discretion of the project.

Though only the proxy contracts are listed as in-scope, current implementation and any further updates to the implementation contracts are considered in scope. When reporting a bug, please make sure to select the relevant proxy smart contract as the target.

## Impacts in scope (27)

- [blockchain_dlt] Critical: Cryptographic vulnerabilities
- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] High: Freezing of funds (fix requires hardfork on Axelar)
- [blockchain_dlt] High: Network not being able to confirm new transactions (Total network shutdown)
- [blockchain_dlt] High: Non-determinism in the network and consensus failure
- [blockchain_dlt] High: Privilege escalation resulting in a severe impact
- [blockchain_dlt] High: Transient consensus failures
- [blockchain_dlt] High: Unintended permanent chain split requiring hard fork (Network partition requiring hard fork)
- [blockchain_dlt] Medium: Attacks against light clients
- [blockchain_dlt] Medium: DoS of greater than 30% of validator or miner nodes and does not shut down the network
- [blockchain_dlt] Medium: High compute consumption by validator nodes
- [blockchain_dlt] Medium: Privilege Escalation causing DoS
- [blockchain_dlt] Low: DoS of greater than 10% but less than 30% of validator nodes and does not shut down the network
- [blockchain_dlt] Low: Significant underpricing of transaction fees relative to computation time
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion
- [smart_contract] Critical: Insolvency
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Privilege escalation resulting in a severe impact
- [smart_contract] Critical: Unauthorized mint/burn/transfer of wrapped assets
- [smart_contract] High: Invalid command execution
- [smart_contract] High: Temporary freezing of funds for a minimum of 24 hours
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Smart contract fails to deliver promised returns, but doesn’t lose value

## Impact notes

(none)

## Rewards

- [blockchain_dlt] Critical: maxReward=$500,000, rewardCalculationPercentage=0, rewardModel=up_to
- [blockchain_dlt] High: maxReward=$25,000, minReward=$5,000, rewardModel=range
- [blockchain_dlt] Medium: fixedReward=$2,500, rewardModel=fixed
- [blockchain_dlt] Low: maxReward=$1,000, rewardModel=up_to
- [smart_contract] Critical: maxReward=$500,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: maxReward=$25,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$2,500, rewardModel=fixed
- [smart_contract] Low: maxReward=$1,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.

All Critical Blockchain/DLT and Smart Contract bug reports require a PoC to be eligible for a reward. Explanations and statements are not accepted as PoC and code is required.

In addition to Immunefi’s Vulnerability Severity Classification System, Axelar Network classifies the following vulnerabilities as follows. In case of discrepancy, the one below will be followed.

Critical
  - Loss of funds of over or equal to $500,000

High
  - Vulnerabilities that result in loss of funds of less than $500,000

Medium
  - Vulnerabilities that result in loss of funds of less than $50,000

Low
  - Vulnerabilities that result in loss of funds of less than $10,000

Any vulnerabilities discussed within the github issues below are considered vulnerabilities already known to Axelar, and will not be eligible for a reward:

  - [https://github.com/axelarnetwork/axelar-core/issues](https://github.com/axelarnetwork/axelar-core/issues) 
  - [https://github.com/axelarnetwork/axelar-cgp-solidity/issues 
](https://github.com/axelarnetwork/axelar-cgp-solidity/issues) 
  - [https://github.com/axelarnetwork/tofnd/issues](https://github.com/axelarnetwork/tofnd/issues)
  - [https://github.com/axelarnetwork/tofn/issues](https://github.com/axelarnetwork/tofn/issues)

Critical blockchain/ smart contract vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk, but also PR and branding aspects, at the discretion of the team. There is no minimum reward for Critical smart contract vulnerabilities.  

Bug reports that are classified as High will be rewarded USD 5 000 and up to USD 25 000 at the Axelar team’s discretion. High impact rewards for the project bug bounty program are scaled based on an internally established team criteria, taking into account the exploitability of the bug, the impact it causes, and the likelihood of the vulnerability presenting itself, which is especially factored in with bug reports requiring multiple conditions to be met that are currently not in-place. However, there is a minimum reward of USD 5 000 for High severity level, rewards will be provided at the determined fair value by the team depending on these conditions, assuming that the bug report is in-scope of the bug bounty program. Only impacts that cause a loss of funds of over or equal to $500K are considered as Critical 

Axelar Network requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. We use a service provider, Jumio, to collect this information and will send you a link to the KYC application if your report is deemed eligible for bounties. The information needed is

  - A piece of government issued photo ID such as passport or driver’s license
  - A live webcam facial recognition scan to match biometrics with submitted photo ID

The collection of this information will be done by the project team.

Payouts are handled by the __Axelar Network__ team directly and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

The following vulnerabilities are excluded from the rewards for this bug bounty program:

  - Third party dependencies, especially Cosmos SDK dependencies
  - In the tofn repository, the only thing in scope is src/ecdsa/mod.rs and it’s project dependencies, excluding third-party dependencies
  - In the tofnd repository, the only thing in scope is parts related to src/ecdsa/mod.rs in tofn repository
  - Off-chain components, such as relayer, and vald, are out of scope. Any reports related to these will only be accepted at the discretion of the project.
  - Vulnerabilities in forks of third-party dependencies are OUT OF SCOPE. Please report such vulnerabilities directly to the maintainers of the upstream repository

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
