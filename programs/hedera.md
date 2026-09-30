# Hedera

- Page: https://immunefi.com/bug-bounty/hedera/scope/
- Max bounty: $30,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium
- End date: (none)

## Assets in scope (8)

- [blockchain_dlt] https://github.com/hiero-ledger/hiero-consensus-node — Hedera Services Codebase
- [blockchain_dlt] https://github.com/hiero-ledger/hiero-cryptography — Hedera Cryptography Codebase
- [blockchain_dlt] https://github.com/hiero-ledger/hiero-json-rpc-relay — JSON RPC Relay
- [blockchain_dlt] https://github.com/hiero-ledger/hiero-mirror-node — Hedera Mirror Node Codebase
- [websites_and_applications] https://github.com/has...edera-transaction-tool
- [websites_and_applications] https://github.com/hiero-ledger/hiero-sdk-go
- [websites_and_applications] https://github.com/hiero-ledger/hiero-sdk-java
- [websites_and_applications] https://github.com/hiero-ledger/hiero-sdk-js

## Asset notes

(none)

## Impacts in scope (16)

- [blockchain_dlt] Critical: Any material impact caused by Tampering/Manipulating Hashgraph history
- [blockchain_dlt] Critical: Direct theft of funds
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Network partition caused outside of design parameters
- [blockchain_dlt] Critical: Unintended permanent freezing of funds
- [blockchain_dlt] High: Authorizing transactions without approval from signers/owners
- [blockchain_dlt] High: Preventing gossip of a transaction or multiple transactions
- [blockchain_dlt] High: Reorganizing transaction history without direct theft of funds
- [blockchain_dlt] High: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments
- [blockchain_dlt] Medium: Incorrect or missing records exported to mirror nodes
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Permanently crashing a mirror node with records from a consensus node without the ability to automatically restart
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Medium: Theft of unpaid staking rewards
- [websites_and_applications] Low: Application-wide DoS via (component)
- [websites_and_applications] Low: Private key or private key generation leakage leading to unauthorized access to user funds  Added

## Impact notes

*If a bug is exploitable on mainnet but a feature flag is in place that nullifies it from being exploitable, it may be downgraded by at least one severity level, or considered out of scope, at Hedera's discretion.*


The Critical Blockchian/DLT impact “Network not being able to confirm new transactions (total network shutdown)” is only able to be considered at Critical if the fix requires a manual rollback. Otherwise, the severity level may be downgraded by at least one severity level.

Any impact requiring an attack vector that involves a privileged account, defined as one that is of the Hedera team or one that is required to receive approval from the Hedera team, directly or indirectly, may be downgraded by at least one severity level or be considered as out of scope entirely due to certain permissioned aspects of the Hedera network. This includes attack vectors requiring a roster-admitted consensus node peer or an authenticated gossip connection. Additionally, any bug report with no attacker-induced action is considered as out of scope for this bug bounty program.

For the Medium Blockchain/DLT impact “Incorrect or missing records exported to mirror nodes”, this is limited to consensus-critical or financially significant records, including, but not limited to account balances, token balances, or other authoritative ledger state. All others, such as incorrect or missing records that are non-authoritative, derived, informational, or statistical in nature, may be considered as out of scope.

The following list is the max we pay for a specific impact. It can only be less, not more. In addition to the standard Feasibility Limitations applied to this bug bounty program, the following terms also apply:
 
__Network Impact Proof__
Bug reports with demonstrated impact on only a single node, including nodes in a reconnecting or transitional state, rather than network-wide behavior, are considered as out-of-scope.

__Functionality Not Active in Production__
Severity is assessed against the exploitability of the impact in the current mainnet production environment at the time of submission. Where a bug report demonstrates a valid impact that cannot presently be reached in production, such as where the affected functionality is gated behind a feature flag, is not yet enabled, or depends on a future release, the severity may be downgraded by at least one severity level at the discretion of the Hedera team. Bug reports of this nature remain in scope and are encouraged, as identifying issues in functionality that is not yet active in production is valuable and will be assessed on its merits. Any downgrade under this clause reflects only the current exploitability of the impact in production and not the validity of the bug report itself.

__Economic Viability of an Attack__
Severity is calibrated to the economic viability and financial impact of an attack rather than solely to its technical possibility. Where the investment required to execute an attack, whether in capital, resources, or fees, is disproportionate to the value an attacker could realistically extract or the damage they could realistically inflict, such that the attack yields no meaningful net gain or a net loss to a rational attacker, the severity may be downgraded by at least one severity level or may be considered as out of scope entirely at the discretion of the Hedera team. The same applies where the funds or value realistically at risk, or the financial loss the attack could realistically cause, is negligible in absolute terms, including where the impact is limited to low-value amounts such as transaction fees. This assessment is made against the realistic cost and realizable impact of the attack at the time of submission.


__Suggestions for places to start__

- Ability to execute system commands
- Signing transactions for other users
- Redirection of user deposits and withdrawals
- Tamper/manipulate Hashgraph history to invalidate transactions
- Tampering with submitted transactions
- Authorizing transactions without approval from the required signers/owners
- Preventing network from reaching consensus on transactions that are submitted
- Preventing gossip of a transaction or multiple transactions
- Bugs that cause the in-scope service to crash (e.g., Non-network-based DoS)
- Remote code execution vulnerabilities
- Attacks that cause a probabilistic consensus failure; or a deterministic consensus failure in reconnected nodes
- Effective non-network-bandwidth-flooding DDoS attacks (e.g., transaction hammering)
- Malicious capabilities of Hedera Token Service functions exposed via System contracts (e.g. transferring assets out of an account without permissions).
- System Smart contract modifiers not respected
- Bugs in the economic system to defraud other participants (e.g. avoid transaction fees to full nodes)
- Prevent node from accessing the network
- Incorrect or missing records exported to mirror nodes
- Correct transaction fees not being applied
- Unauthorized Hedera Token Service (HTS) activity
- Overpayment or underpayment of staking rewards
- Theft of unpaid staking rewards
- Sensitive information leakage (e.g., private keys, wallets credentials etc). Public keys are excluded from this scope

## Rewards

- [blockchain_dlt] Critical: maxReward=$30,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: maxReward=$10,000, minReward=$3,000, rewardModel=range
- [blockchain_dlt] Medium: fixedReward=$3,000, rewardModel=fixed
- [websites_and_applications] Low: maxReward=$100, minReward=$50, rewardModel=range

## Reward notes

__Reward Calculation for Critical Level Reports__

For critical Blockchain/DLT bug reports with the impact “Direct theft of funds” and “Unintended permanent freezing of fund", the reward amount is 10% of the funds directly affected, capped at the maximum critical reward [$30,000]. However, a minimum reward of USD [$10,000] is to be rewarded in order to incentivize security researchers against withholding on a bug report. All other reports that demonstrate a critical impact are rewarded within the range of USD [$10,000] to USD [$30,000] at the discretion of the Hedera team.

## Out of scope (program-specific)

__Blockchain/DLT__
- Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 2/3 attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks
- Impacts requiring a malicious or compromised node.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
