# Sei

- Page: https://immunefi.com/bug-bounty/sei/scope/
- Max bounty: $500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low
- End date: (none)

## Assets in scope (4)

- [blockchain_dlt] https://github.com/sei-protocol/go-ethereum
- [blockchain_dlt] https://github.com/sei-protocol/sei-chain — Sei Chain
- [blockchain_dlt] https://github.com/sei-protocol/sei-js
- [blockchain_dlt] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

All code of Sei Foundation can be found at https://github.com/sei-protocol. Documentation for the assets provided in the table can be found at [https://github.com/sei-protocol/sei-chain/blob/main/whitepaper/Sei_Whitepaper.pdf](https://github.com/sei-protocol/sei-chain/blob/main/whitepaper/Sei_Whitepaper.pdf)

## Impacts in scope (15)

- [blockchain_dlt] Critical: Direct loss of funds of USD $5,000 or more (including but not limited to unauthorized transfers, token minting, or token burning)
- [blockchain_dlt] Critical: Permanent freezing of funds of USD $5,000 or more with no on-chain remediation path, excluding general network unavailability (fix requires hard fork)
- [blockchain_dlt] High: Crash of RPC nodes running default configuration without assuming direct network access (e.g. via malicious block/transaction payloads propagated through the network)
- [blockchain_dlt] High: Crash or halt of ≥1/3 of validators (assuming no direct network access to validator nodes), resulting in loss of network liveness
- [blockchain_dlt] High: Unintended permanent chain split requiring hard fork to resolve (network partition with no automatic recovery)
- [blockchain_dlt] Medium: Block production delay exceeding 2.5 seconds on realistic validator hardware, caused by crafted transactions or messages (excluding malicious proposers)
- [blockchain_dlt] Medium: Bug in layer 0/1/2 network code that causes deterministic unintended smart contract execution, with no funds directly at risk
- [blockchain_dlt] Medium: Crash of RPC nodes running default configuration via direct unauthenticated network access to the EVM JSON-RPC endpoints (HTTP and WebSocket)
- [blockchain_dlt] Medium: Crash or halt of ≥10% but <1/3 of validators (assuming no direct network access to validator nodes) via crafted (non-brute-force) messages, where the network retains liveness
- [blockchain_dlt] Medium: Direct loss of funds of less than USD $5,000 (including but not limited to unauthorized transfers, token minting, or token burning)
- [blockchain_dlt] Medium: Malicious proposer block freeze: delay of ≥10 minutes caused by a single proposer beyond simply skipping their own proposal slot(s)
- [blockchain_dlt] Medium: Permanent freezing of funds of less than USD $5,000 with no on-chain remediation path, excluding general network unavailability (fix requires hard fork)
- [blockchain_dlt] Low: Causing network processing nodes to include or order mempool transactions outside of protocol-defined selection and priority rules
- [blockchain_dlt] Low: Crash or halt of <10% of validators (assuming no direct network access to validator nodes) via crafted (non-brute-force) messages, where the network retains liveness
- [blockchain_dlt] Low: Manipulation of transaction fee calculation resulting in fees outside protocol-defined bounds

## Impact notes

__Giga-Related Functionality__

With the exception of the **Giga executor** and **FlatKV**, all functionality related to **Giga** is currently **out of scope** for this bug bounty program.

**The Giga executor is in scope.** The Giga executor is **enabled by default**. The following are in scope:

- The `giga/executor` Go package (and its subpackages)
- The `[giga_executor]` configuration section, including both the `enabled` and `occ_enabled` options

The following are **out of scope** even though they relate to the Giga executor, and are **not eligible for rewards**:

- **EVMone**: any functionality related to the evmone-based execution backend, including the `evmone` VM integration and any code paths specific to it. EVMone is not used in production and has not been extensively tested.
- **Transaction result differences (including `LastResultsHash` divergence) between the Giga and V2 executors**: the two execution implementations are not guaranteed to produce identical transaction results or an identical `LastResultsHash`. This is a known difference.
- **Block delay impacts that rely on the current fallback from Giga to V2 execution**: the current fallback from Giga to V2 execution can increase EVM transaction execution time, and block delay impacts that depend on this fallback are not in scope.

**All other Giga functionality is out of scope.** Every Giga feature other than the executor and FlatKV remains **disabled by default** in all supported environments. Specifically, the following are excluded from scope:

- The **Autobahn** multi-proposer consensus protocol
- **Giga storage**, other than **FlatKV**, which is in scope (see the Giga-only FlatKV exclusion below)
- Any code paths that require setting a `GIGA_*` configuration flag to `true`, other than enabling the Giga executor
- Any configuration options under `giga`-prefixed sections other than `[giga_executor]`
- Any code contained within `giga` packages other than `giga/executor`

As a result:
- Vulnerabilities that are only exploitable when Giga functionality other than the executor and FlatKV is enabled
- Vulnerabilities that exist exclusively within `giga` packages other than `giga/executor`
- Vulnerabilities reachable solely through execution paths gated by non-executor Giga configuration

are **not eligible for rewards** under this bug bounty program.

---

__Excluded Giga-Only FlatKV Functionality__

**FlatKV is in scope** as the EVM state store of a default seid node. Some FlatKV code, however, exists only to serve Giga functionality that is out of scope and is not live on mainnet. It is not isolated into `giga` packages and can share code paths with the in-scope FlatKV store.

Specifically, the following are excluded from scope and are **not eligible for rewards**:

- **BUD (Block Update Digest) hashes, BUD proofs and BUD state proofs**, including the `giga/apphash` packages and the hash the StateWAL reports to the Giga app hash builder. That hash is currently a placeholder, not a BUD hash.
- The **Giga storage manager** (`sei-db/bootstrap`) and the FlatKV, StateWAL and app hash wiring it sets up for Autobahn and the EVM-only application
- The lack of **state proofs for FlatKV-backed stores**: queries with `prove=true` against a FlatKV-backed store (such as `evm`) return an error until BUD proofs are implemented. This is a known limitation.
- Vulnerabilities that are only exploitable with Autobahn or Giga storage enabled, even when the affected code is in a FlatKV package.

---

__Excluded StateSync Peer Functionality__

Any functionality related to **StateSync Peers** is currently **out of scope** for this bug bounty program.

A StateSync Peer is a trusted node that provides state synchronization data to other nodes during initial sync. These are nodes explicitly configured as RPC servers and persistent peers for the purpose of state sync. They serve trust height, trust hash, and block/state data that the syncing node consumes directly.

Specifically, the following are excluded from scope:

- Any vulnerabilities that require a **malicious or compromised StateSync Peer** to be exploited
- Any attack vectors that depend on a StateSync Peer returning **tampered block data, trust hashes, or state snapshots**
- Any vulnerabilities that rely on **poisoning the persistent peers list** with attacker-controlled node IDs obtained through compromised StateSync Peer RPC responses
- Any vulnerabilities related to **P2P-mode state sync**, where any connected P2P peer can serve as a state provider. P2P-mode state sync is **disabled by default** and is not used in Sei's supported state sync workflow

StateSync Peers are considered trusted infrastructure within the Sei network's threat model. As a result:
- Vulnerabilities that assume a StateSync Peer is acting maliciously or has been compromised
- Vulnerabilities that are only exploitable by controlling or impersonating a StateSync Peer endpoint
- Vulnerabilities reachable solely through tampered RPC responses from a trusted StateSync Peer
- Vulnerabilities that exist exclusively within P2P-mode state sync code paths

are **not eligible for rewards** under this bug bounty program.

---

__Excluded Non-EVM RPC Endpoints__

Of the RPC/API endpoints a node exposes, only the **EVM JSON-RPC** endpoints (HTTP and WebSocket) are in scope for direct-access attacks.

Specifically, the following are excluded from scope and are **not eligible for rewards**:

- Crashes, halts, or resource exhaustion (CPU, memory, file descriptors, goroutines, disk) of a node caused by sending requests directly to the **CometBFT/Tendermint RPC** endpoint (HTTP and WebSocket, port `26657` by default)
- The same impacts caused by sending requests directly to the Cosmos **REST/LCD API** (`1317`) endpoint
- The same impacts caused by sending requests directly to the Cosmos **gRPC** (`9090`) or **gRPC-Web** (`9091`) endpoints, on any node that still serves them. These servers are being removed from `seid` ([sei-chain#4570](https://github.com/sei-protocol/sei-chain/pull/4570))
- The same impacts caused through any other node RPC/API endpoint other than EVM JSON-RPC

This exclusion covers only availability impacts reached by connecting to these endpoints. It does not exclude:

- Crashes caused by malicious blocks, transactions, or messages propagated through the network, which remain in scope under the impacts that assume no direct network access
- CometBFT/Tendermint consensus, mempool, and P2P code
- Loss or freezing of funds, or any other in-scope impact, regardless of which endpoint the transaction or request was submitted through

Reports whose impact is a node crash or resource exhaustion via direct requests to these endpoints are **not eligible for rewards**.

---

__Excluded Governance-Dependent Issues__

Issues which require a **governance proposal to pass** are **out of scope** for this bug bounty program and are **not eligible for rewards**. This includes vulnerabilities that are only exploitable after a parameter change, software upgrade, or any other proposal has been approved through on-chain governance.

Vulnerabilities that allow a proposal to pass, or to take effect, without the required votes remain in scope.

## Rewards

- [blockchain_dlt] Critical: maxReward=$500,000, minReward=$50,000, rewardCalculationPercentage=0, rewardModel=range
- [blockchain_dlt] High: fixedReward=$25,000, rewardModel=fixed
- [blockchain_dlt] Medium: fixedReward=$5,000, primacy=primacy_of_rules, rewardModel=fixed
- [blockchain_dlt] Low: fixedReward=$1,000, primacy=primacy_of_rules, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below.

__Reward Calculation for Critical Level Reports__

For Critical Blockchain/DLT vulnerabilities, rewards are determined based on the ratio between the total funds at risk—including all affected projects built on the Sei blockchain—and the Sei market capitalization, calculated as the average market cap reported by CoinMarketCap and CoinGecko at the time the report is submitted.

A minimum reward of **USD $50,000** is guaranteed for all valid Critical reports in order to incentivize timely and responsible disclosure.

This ratio is referred to as the **risk ratio**, defined as:

Risk Ratio = Funds at Risk / Sei Market Capitalization

Rewards scale linearly from a 0:1 to a 1:1 risk ratio, where a 1:1 ratio corresponds to a maximum reward of **USD $500,000**.  
If the funds at risk exceed the market capitalization, the reward remains capped at **USD $500,000**.

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs acknowledged below are not eligible for any reward through the bug bounty program.
- Project operation risk in tokenfactory module

__Previous Audits__

Sei Foundation has provided these completed audit review reports for reference. Any unfixed vulnerability mentioned in these reports are not eligible for a reward.
- [https://github.com/oak-security/audit-reports/blob/master/Sei/2023-05-15%20Audit%20Report%20-%20Sei%20Cosmos%20v1.0.pdf](https://github.com/oak-security/audit-reports/blob/master/Sei/2023-05-15%20Audit%20Report%20-%20Sei%20Cosmos%20v1.0.pdf)
- [https://github.com/oak-security/audit-reports/blob/master/Sei/2023-05-15%20Audit%20Report%20-%20Sei%20Tendermint%20v1.0.pdf](https://github.com/oak-security/audit-reports/blob/master/Sei/2023-05-15%20Audit%20Report%20-%20Sei%20Tendermint%20v1.0.pdf)
- [https://github.com/oak-security/audit-reports/blob/master/Sei/2023-05-19%20Audit%20Report%20-%20Sei%20Chain%20and%20CosmWasm%20v1.0.pdf](https://github.com/oak-security/audit-reports/blob/master/Sei/2023-05-19%20Audit%20Report%20-%20Sei%20Chain%20and%20CosmWasm%20v1.0.pdf)


__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Blockchain/DLT: Critical
- Blockchain/DLT: High
- Blockchain/DLT: Medium
- Blockchain/DLT: Low

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules) Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

For Medium, High and Critical reports, we ask that whitehats provide a PoC using a local 4-node cluster. You can follow these steps to provide this PoC:

1. Spin up the local testnet with `make docker-cluster-start`
2. Connect to node0 with `docker exec -it sei-node-0 /bin/bash`
3. Carry out attack

PoCs for the direct network access RPC crash impact must target the EVM JSON-RPC endpoints. PoCs that crash a node via direct requests to the CometBFT/Tendermint RPC, gRPC, gRPC-Web, or REST/LCD endpoints are **out of scope**.

Note that any PoC submitted against testnet **must not** enable any Giga functionality other than the Giga executor. In particular, a PoC **must not**:
- Set any `GIGA_*` flag to `true`, other than the flags that enable the Giga executor (`[giga_executor]`)
- Explicitly enable any configuration under sections prefixed with `giga`, other than the `[giga_executor]` section

The Giga executor is enabled by default and is in scope. PoCs that rely on out-of-scope Giga functionality — for example, Autobahn consensus, Giga storage other than FlatKV, Giga-only FlatKV functionality such as BUD hashes and proofs, or the EVMone execution backend — will be considered **out of scope** and will not be eligible for a bounty. See [scope](https://immunefi.com/bug-bounty/sei/scope/#top) for further information.


__Reward Payment Terms__

Rewards are denominated in USD and paid by the Sei Foundation team.

Payouts are made in **SEI** or **USDT/C**, at the Foundation’s discretion. For additional details on payout mechanics and reward amounts, please refer to the **Rewards by Threat Level** section below.

__Malicious Proposer Rule__ 

If an attack requires the attacker to be a block proposer (or equivalent privileged validator role), its severity is reduced by one level (e.g. Critical → High, Low → Informational/Out of Scope). 

**Note, direct loss of funds of USD $5,000 or more remains Critical regardless of attacker role.**

## Out of scope (program-specific)

(none)

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
