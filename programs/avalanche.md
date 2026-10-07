# Ava Labs Avalanche

- Page: https://immunefi.com/bug-bounty/avalanche/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (28)

- [blockchain_dlt] https://github.com/ava-labs/avalanchego — AvalancheGo
- [blockchain_dlt] https://github.com/ava-labs/libevm — libevm
- [smart_contract] https://github.com/ava-labs/icm-services/tree/main/icm-contracts — ICM Contracts
- [smart_contract] https://snowtrace.io/address/0x02d980a0d7af3fb7cf7df8cb35d9edbcf355f665 — SHIB.e
- [smart_contract] https://snowtrace.io/address/0x152b9d0fdc40c096757f570a51e494bd4b943e50 — BTC.b
- [smart_contract] https://snowtrace.io/address/0x19860ccb0a68fd4213ab9d8266f7bbf05a8dde98 — BUSD.e
- [smart_contract] https://snowtrace.io/address/0x2147efff675e4a4ee1c2f918d181cdbd7a8e208f — ALPHA.e
- [smart_contract] https://snowtrace.io/address/0x249848beca43ac405b8102ec90dd5f22ca513c06 — CRV.e
- [smart_contract] https://snowtrace.io/address/0x37b608519f91f70f2eeb0e5ed9af4061722e4f76 — SUSHI.e
- [smart_contract] https://snowtrace.io/address/0x3bd2b1c7ed8d396dbb98ded3aebb41350a5b2339 — UMA.e
- [smart_contract] https://snowtrace.io/address/0x49d5c2bdffac6ce2bfdb6640f4f80f226bc10bab — WETH.e
- [smart_contract] https://snowtrace.io/address/0x50b7545627a5162f82a992c33b87adc75187b218 — WBTC.e
- [smart_contract] https://snowtrace.io/address/0x5947bb275c521040051d82396192181b413227a3 — LINK.e
- [smart_contract] https://snowtrace.io/address/0x596fa47043f99a4e0f122243b841e55375cde0d2 — ZRX.e
- [smart_contract] https://snowtrace.io/address/0x63a72806098bd3d9520cc43356dd78afe5d386d9
- [smart_contract] https://snowtrace.io/address/0x88128fd4b259552a9a1d457f435a6527aab72d42 — MKR.e
- [smart_contract] https://snowtrace.io/address/0x8a0cac13c7da965a312f08ea4229c37869e85cb9 — GRT.e
- [smart_contract] https://snowtrace.io/address/0x8ebaf22b6f053dffeaf46f4dd9efa95d89ba8580 — UNI.e
- [smart_contract] https://snowtrace.io/address/0x98443b96ea4b0858fdf3219cd13e98c7a4690588 — BAT.e
- [smart_contract] https://snowtrace.io/address/0x9eaac1b23d935365bd7b542fe22ceee2922f52dc — YFI.e
- [smart_contract] https://snowtrace.io/address/0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664 — USDC.e
- [smart_contract] https://snowtrace.io/address/0xabc9547b534519ff73921b1fba6e672b5f58d083 — WOO.e
- [smart_contract] https://snowtrace.io/address/0xbec243c995409e6520d7c41e404da5deba4b209b — SNX.e
- [smart_contract] https://snowtrace.io/address/0xc3048e19e76cb9a3aa9d77d8c03c29fc906e2437 — COMP.e
- [smart_contract] https://snowtrace.io/address/0xc7198437980c041c805a1edcba50c1ce5db95118 — USDT.e
- [smart_contract] https://snowtrace.io/address/0xc7b5d72c836e718cda8888eaf03707faef675079 — SWAP.e
- [smart_contract] https://snowtrace.io/address/0xd501281565bf7789224523144fe5d98e8b28f267 — 1inch.e
- [smart_contract] https://snowtrace.io/address/0xd586e7f844cea2f87f50152665bcbc2c279d8d70 — DAI.e

## Asset notes

Ava Labs’s codebase can be found at [https://github.com/ava-labs](https://github.com/ava-labs). Documentation and further resources can be found on [https://docs.avax.network/](https://docs.avax.network/). For details on standing up a local test network, sees [https://docs.avax.network/tooling/network-runner](https://docs.avax.network/tooling/network-runner).

**libevm and avalanchego/graft**
- If a bug is publicly disclosed in [ethereum/go-ethereum](https://github.com/ethereum/go-ethereum), that bug is considered out-of-scope in this program.
- The following issues are considered out of scope:
    - Network-level Denial-of-Service (TCP/IP/P2P)
    - Misconfigurations of AvalancheGo nodes currently running on the Avalanche Network
    - Denial-of-Service, OOM, or panic on any API exposed by AvalancheGo
    - Any usage of the node's HTTP API through intended mediums. Intended mediums include usage:
        - requiring direct machine access
        - through explicitly opened RPC ports
        - This includes the ability to send HTTP requests that cause node panics, OOMs, increased disk usage, or causing the node to become unhealthy.
    - Consensus liveness failure requiring network control.
    - Ex: BGP hijacking attacks
    - Preventing a node from properly connecting to the P2P network due to brute force networking DoS vectors.
    - Ex: Syn attacking a specific node with a botnet.
    - Unintended node behavior caused by local disk failures.
    - Unintended node behavior caused by unusual node configuration deviating from best practices for node configurations
    - Compile time or runtime errors due to using unsupported hardware or operating systems.
    - Inability to automatically perform NAT-hole punching on specific router hardware.

Even if a bug is considered out-of-scope but you feel it should be disclosed privately, we appreciate any and all informational disclosures through this portal. Thanks for your responsible disclosure! 

Blockchain/DLT - ICM Services: Excluding tests

## Impacts in scope (19)

- [blockchain_dlt] Critical: Ability to exfiltrate a node's staking keys (TLS or BLS) without direct machine access
- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] Critical: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Ability to produce a disproportionate number of blocks compared to the amount of controlled stake (High) Assuming the blockchain is using the Snowman++ congestion control mechanism.
- [blockchain_dlt] High: Causing network processing nodes to process transactions from the mempool beyond set parameters
- [blockchain_dlt] High: Unintended chain split (network partition)
- [blockchain_dlt] Medium: A bug in the respective layer 1 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Medium: Ability to display arbitrary logs to users
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

**Expected resource-intensive operations including but not limited to:**
- Node synchronization after being offline or behind on block height
- Initial blockchain sync or historical data loading
- Large database migrations or reindexing operations
- Batch processing of accumulated transactions or events

**Valid DoS vulnerabilities must demonstrate:**
- An exploitable vulnerability beyond normal resource consumption
- Malicious input or actions that cause disproportionate resource usage
- A realistic attack scenario that differs from standard operational load
- Impact that prevents legitimate users from accessing the service beyond expected operational delays
- Disproportionate resource consumption relative to the cost paid (e.g., spending $1 in gas to cause $1000 in computational cost)

## Rewards

- [blockchain_dlt] Critical: maxReward=$100,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: maxReward=$10,000, minReward=$5,000, rewardModel=range
- [blockchain_dlt] Medium: fixedReward=$5,000, rewardModel=fixed
- [blockchain_dlt] Low: fixedReward=$1,000, rewardModel=fixed
- [smart_contract] Critical: maxReward=$100,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

For critical Blockchain/DLT bugs, the reward amount is 10% of the funds directly affected, capped at the maximum critical reward USD $100,000.
For critical Blockchain/DLT bugs with a non-funds-at risk impact, the reward will be paid out as follows: 

  - Network not being able to confirm new transactions (total network shutdown)
USD $100,000
  - Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
USD $100,000
  - Permanent freezing of funds (fix requires hardfork)
USD $100,000

For high Blockchain/DLT non-funds-at risk impacts, the reward will be paid out as follows: 

  - Causing network processing nodes to process transactions from the mempool beyond set parameters
USD $5,000

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 10 000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

NOTE: Smart contracts deployed by third-parties on Avalanche are EXPLICITLY OUT OF SCOPE. This bug bounty ONLY includes the smart contracts listed as in scope below.

__Repeatable Attack Limitations__

  - If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attacks within the first hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

  - For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

  - High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are considered at the full amount of funds at risk, capped at the maximum high reward. This is to incentivize security researchers to uncover and responsibly disclose vulnerabilities that may have not have significant monetary value today, but could still be damaging to the project if it goes unaddressed.   

  - In the event of temporary freezing, the reward increases at a multiplier of two from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lenghents, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.    

__Reward Payment Terms__

Payouts are handled by the __Ava Labs__ team directly and are denominated in __USD__.

Please note: In cases where the size of the reward exceeds an equivalent of 10 000 USD, Ava Labs is entitled to make the payment in one-year locked AVAX at the rate calculated based on the VWAP of AVAX during 90 calendar days preceding the date of the respective validated report.

## Out of scope (program-specific)

- If a bug is publicly disclosed (in the repo of an "asset in scope" or otherwise), that bug is considered out-of-scope in this program.
  - If a bug is publicly disclosed in a dependency of any of the "assets in scope", that bug is considered out-of-scope in this program.

__Coreth/Subnet-EVM__

- If a bug is publicly disclosed in https://github.com/ethereum/go-ethereum, that bug is considered out-of-scope in this program.
- If a bug is publicly disclosed in https://github.com/ava-labs/subnet-evm that affects https://github.com/ava-labs/coreth (or vice-versa), that bug is considered out-of-scope in this program.

  - Network-level Denial-of-Service (TCP/IP/P2P)
  - Misconfigurations of AvalancheGo nodes currently running on the Avalanche Network
  - Denial-of-Service, OOM, or panic on any API exposed by AvalancheGo
  - Any usage of the node's HTTP API through intended mediums. Intended mediums include usage:
    - requiring direct machine access
    - through explicitly opened RPC ports
    - This includes the ability to send HTTP requests that cause node panics, OOMs, increased disk usage, or causing the node to become unhealthy.
  - Consensus liveness failure requiring network control.
  - Ex: BGP hijacking attacks
  - Preventing a node from properly connecting to the P2P network due to brute force networking DoS vectors.
    - Ex: Syn attacking a specific node with a botnet.
  - Unintended node behavior caused by local disk failures.
  - Unintended node behavior caused by unusual node configuration deviating from best practices for node configurations
  - Compile time or runtime errors due to using unsupported hardware or operating systems.
  - Inability to automatically perform NAT-hole punching on specific router hardware.

Even if a bug is considered out-of-scope but you feel it should be disclosed privately, we appreciate any and all informational disclosures through this portal. Thanks for your responsible disclosure!

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- The Diff.Apply Ordering issue is known from #71513 we have a PR for the fix of this in the works since April 1st (https://github.com/ava-labs/avalanchego-internal/pull/2964)
