# Cosmos

- Page: https://immunefi.com/bug-bounty/cosmos/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT
- PoC required for: blockchain_dlt - high, blockchain_dlt - critical, blockchain_dlt - medium, blockchain_dlt - low
- End date: (none)

## Assets in scope (23)

- [blockchain_dlt] https://crates.io/crates/ibc-chain-registry — Blockchain/DLT - Hermes Relayer (ibc-chain-registry)
- [blockchain_dlt] https://crates.io/crates/ibc-relayer — Blockchain/DLT -  Hermes Relayer (ibc-relayer)
- [blockchain_dlt] https://crates.io/crates/ibc-relayer-cli — Blockchain/DLT - Hermes Relayer (ibc-relayer-cli)
- [blockchain_dlt] https://crates.io/crates/ibc-relayer-rest — Blockchain/DLT - Hermes Relayer (ibc-relayer-rest)
- [blockchain_dlt] https://crates.io/crates/ibc-telemetry — Blockchain/DLT - Hermes Relayer (ibc-telemetry)
- [blockchain_dlt] https://github.com/CosmWasm/cosmwasm — CosmWasm - WebAssembly Smart Contracts for the Cosmos SDK
- [blockchain_dlt] https://github.com/CosmWasm/cw-storage-plus — Blockchain/DLT - CosmWasm (cw-storage-plus)
- [blockchain_dlt] https://github.com/CosmWasm/cw-utils — Blockchain/DLT - CosmWasm (cw-utils)
- [blockchain_dlt] https://github.com/CosmWasm/rust-optimizer — Blockchain/DLT - CosmWasm (rust-optimizer)
- [blockchain_dlt] https://github.com/CosmWasm/serde-json-wasm — Blockchain/DLT - CosmWasm (serde-json-wasm)
- [blockchain_dlt] https://github.com/CosmWasm/wasmd — Blockchain/DLT - CosmWasm (wasmd). Note: Only the wasmd/x/wasm path is in scope. We are only interested in vulnerabilities related to the x/wasm module. Vulnerabilities related to the example wasmd application that also lives in this repo are not in scope.
- [blockchain_dlt] https://github.com/CosmWasm/wasmvm — Blockchain/DLT - CosmWasm (wasmvm)
- [blockchain_dlt] https://github.com/cometbft/cometbft — CometBFT - A distributed, Byzantine fault-tolerant, deterministic state machine replication engine. A fork and successor to Tendermint Core.
- [blockchain_dlt] https://github.com/cosmos/cosmos-sdk — Cosmos SDK - Framework for building performant, customizable blockchains with native interoperability.
- [blockchain_dlt] https://github.com/cosmos/evm — Cosmos EVM - An EVM compatible framework for blockchain development with the Cosmos SDK.",         "isPrimacyOfImpact
- [blockchain_dlt] https://github.com/cosmos/gaia — Gaia - Cosmos Hub
- [blockchain_dlt] https://github.com/cosmos/iavl — IAVL - Merkleized IAVL+ Tree implementation in Go.
- [blockchain_dlt] https://github.com/cosmos/ibc-go — IBC Go enables cross-blockchain communication. The protocol achieves interoperability by specifying data structures, abstractions, and semantics implementable by any distributed ledger that satisfies a small set of requirements.
- [blockchain_dlt] https://github.com/cosmos/ics23 — ICS23 - A generic merkle proof format for IBC
- [blockchain_dlt] https://github.com/cosmos/ledger-cosmos — Blockchain/DLT - Ledger Cosmos app
- [blockchain_dlt] https://github.com/cosmos/ledger-cosmos — Ledger Cosmos - The Cosmos app for Ledger Nano S+, X, Stax, Flex and Apex P.
- [blockchain_dlt] https://github.com/cosmos/solidity-ibc-eureka — Solidity IBC Eureka - IBC v2 is a simplified version of the IBC protocol that is encoding agnostic. This enables a trust-minimized IBC connection between Ethereum and a Cosmos SDK chain.
- [blockchain_dlt] https://github.com/informalsystems/hermes — Hermes - IBC relayer in Rust

## Asset notes

Other helpful links include:

- IBC documentation - https://ibc.cosmos.network/main/ibc/overview
- Hermes documentation, including an installation guide and tutorials for local test environments - https://hermes.informal.systems/
- CosmWasm documentation - https://www.cosmwasm.com/build
- Cosmos SDK module specifications - https://github.com/cosmos/cosmos-sdk/blob/main/docs/building-modules/README.md
- Cosmos Release Family Policy - https://docs.cosmos.network/sdk/latest/release-family#upgrades-and-support

## Impacts in scope (16)

- [blockchain_dlt] Critical: Unauthorized minting or burning of user funds
- [blockchain_dlt] High: Chain halt / liveness failure
- [blockchain_dlt] High: Loss of cryptoeconomic security
- [blockchain_dlt] High: Non-determinism / consensus fork / AppHash divergence
- [blockchain_dlt] High: Permanent locking / freezing of funds or clients
- [blockchain_dlt] High: Relayer / off-chain service key and wallet compromise
- [blockchain_dlt] High: Theft / unauthorized extraction of funds
- [blockchain_dlt] Medium: Privilege escalation / authorization bypass / unauthorized state mutation
- [blockchain_dlt] Medium: Relayer / off-chain service fund exhaustion (economic griefing)
- [blockchain_dlt] Medium: Relayer / off-chain service liveness failure (delivery DoS)
- [blockchain_dlt] Medium: Signing-display tamper / blind signing
- [blockchain_dlt] Medium: Single-node crash / resource-exhaustion DoS
- [blockchain_dlt] Medium: Supply inflation / accounting corruption
- [blockchain_dlt] Medium: Supply-chain / CI-CD / RCE / account takeover
- [blockchain_dlt] Medium: Transaction censorship / mempool manipulation
- [blockchain_dlt] Low: Information disclosure

## Impact notes

**For the ibc-go asset, the following components are in-scope:**

- IBC Core - 02-client, 03-connection, 04-channel, 05-port, 23-commitment, 24-host
- Application Modules - transfer, 27-interchain-accounts
- Light Clients - 06-solomachine, 07-tendermint, 08-wasm, 09-localhost
- Middleware Modules - 29-fee, callbacks

For the Cosmos SDK asset, the core packages baseapp, crypto, types, and store, as well as the modules x/auth, x/bank, x/staking, x/slashing, x/evidence, x/distribution, and x/mint, are the components most likely to contain significant vulnerabilities. Bug reports on other maintained modules are also accepted, subject to the module exclusions listed under Other Terms and Information.

# **Impact Definitions and Severity Downgrade Conditions**

The impacts listed in the Impacts in Scope table further below are defined as follows, together with the conditions under which a bug report covering that impact may be downgraded. Where more than one downgrade condition applies, the severity level is only downgraded once under this subsection.

**How the oracles apply**

Each oracle is the bar a report must meet to be assessed at that impact's listed severity, or at the tier named on the oracle. A report that demonstrates the impact but falls short of an oracle's threshold is not rejected outright; it is assessed at the severity of the downgrade condition that describes the shortfall, and if no downgrade condition or tier oracle covers it, it is Informational. The exception is a rule that states a report is out of scope below a threshold (for example, the memory-consumption rule for OOM reports): those are hard eligibility gates and take precedence.

**Blockchain/DLT**

For the Critical impact **"Unauthorized minting / burning of user funds"**, it is defined as direct, unauthorized creation or destruction of value tied to user balances which are tokens minted from nothing, or a user's tokens burned or destroyed, without authorization, changing what holders actually own.

Bug reports covering this impact may be downgraded to High severity where any of the following conditions applies:

- The impact is limited to a single, one-time mint or burn.
- The impact is limited to a limited amount of funds being minted or burned.
- The issue is reachable only when an optional or non-default module is enabled (ICA, PFM, IBC-hooks, vote extensions, x/poa, etc).
- Unauthorized burning of funds is reversible via governance (note that this is not a rollback).

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain (cosmos-sdk, cosmos/evm, wasmd/wasmvm, ibc-go, etc) or library/contract deployed on chain (ibc-contracts)
  - condition: value created or destroyed with no authorization
  - threshold: the net change in the denom's spendable balances, summed across every account the block touches, differs by ≥ 1 base unit from the authorized mints and burns in the block.
  - measurement: query spendable balances of the legitimate asset (native, token-factory, contract-issued, or IBC voucher denom) for every account the block touches before and after, sum the authorized mints (including vouchers for relayed packets) and burns, and confirm any created balance is transferable by the attacker.

For the High impact **"Theft / unauthorized extraction of funds"**, which is defined as where an attacker moves or withdraws value they do not own, bug reports covering this impact may be downgraded to High severity where any of the following conditions applies:

- The attack requires an optional or non-default module, or an attacker-deployed contract (TipDecorator chain, x/accounts lockup, CosmWasm + IBC-hooks, etc.).
- The attack requires being the account owner or withdrawer, or a contrived trigger (a forced timeout plus reentrant submessages, a victim contract relying on staticcall safety, etc.).
- The impact is single-victim and isolated per transaction.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain (cosmos-sdk, cosmos/evm, wasmd, ibc-go, etc)
  - condition: a victim's funds move without their authorization
  - threshold: the victim's balance (or escrow held for them) falls by ≥ 1 base unit more than the transfers and fees the victim authorized, while the net change in spendable balances across all touched accounts is 0.
  - measurement: query the victim and every recipient (attacker, module, fee collector, or third party) before and after, inspect the block's messages, signatures, and relayed packets, and for EVM or nested-message routes (ICA/authz/precompile) run a differential (`eth_call` or control account) in which the same path debits no victim without the flaw.

For the High impact **"Chain halt / liveness failure"**, it is defined as where the whole chain stops producing or finalizing blocks, so no transactions can land until operators ship a coordinated fix. This happens when a single attacker-reachable input drives every validator into the same fatal error or unbounded work while applying a block, so the network stalls on one height all at once.

Bug reports covering this impact may be downgraded to Medium severity where any of the following conditions applies:

- The issue is reachable only when an optional or non-default module is enabled (ICA, PFM, IBC-hooks, vote extensions, x/poa, etc.).
- The attack requires a contrived trigger, such as a multi-step setup, an oversized multi-MB payload, a version split, or a probabilistic GC/heap race.
- The halt is recoverable and clears once the offending transaction clears or on restart (a block delay, not a permanent stop).

Bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- The halt is difficult or nearly impossible in practice. I.e. a contrived trigger which is also unlikely to achieve in practice, or financially punishing to the attacker, or has no exploitable chains in production.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain (cometbft consensus under cosmos-sdk, cosmos/evm, wasmd, ibc-go, etc)
  - condition: the network produces no new block
  - threshold: no new block is committed on the network for ≥ 120s after the input, and block production does not resume without a node restart or software fix.
  - measurement: poll each node's /status latest block height and time before and after the input, counting an unreachable node as committing nothing, and when every node is down read the last committed height from the node logs or block store instead; tie the stall to the input by the exit, panic, or OOM line logged at the same height by > 1/3 of voting power (at block application, proposal/vote handling, mempool ingress, or replay on restart), or by block-execution time for the input against an equal-gas, equal-size benign control.
- For any chain (cometbft consensus under cosmos-sdk, cosmos/evm, wasmd, ibc-go, etc), medium tier, halt is recoverable
  - condition: the network keeps producing blocks, but the input stalls heights
  - threshold: no new block is committed on the network for ≥ 30s after the input, reproducible on each submission of the input, while an equal-gas, equal-size benign control submitted to the same network commits without a stall; the network must run CometBFT's default consensus timeouts or the target chain's production values.
  - measurement: poll each node's `/status` latest block height and time before and after the input and the control, record the commit round of each affected height (`/block`, `last_commit.round`), and state the consensus timeouts (`timeout_propose`, `timeout_commit`, etc.) the network ran with.

For the High impact **"Non-determinism / consensus fork / AppHash divergence"**, it is defined as where validators compute different results from the same block, so they can no longer agree on the chain state, splitting the network or halting it because no single result reaches the required supermajority. This arises whenever part of state processing depends on something that is not identical across all nodes.

Bug reports covering this impact may be downgraded to Medium severity where any of the following conditions applies:

- The issue is confined to an optional module or configuration (29-fee, PFM, ICA-host Proto3JSON, wasmd safe-queries, gov precompile, etc.).
- The issue requires validators running mismatched versions or configurations, or node-local configuration divergence.
- The attack requires a contrived trigger, such as a boundary-straddling transaction, repeated crafted messages, a corrupted snapshot, or attacker-controlled forwarding chains.
- The issue is configuration-dependent and recoverable via governance.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain or library (cometbft, cosmos-sdk, cosmos/evm, wasmd/wasmvm, ibc-go, ics23, etc)
  - condition: two nodes that should agree disagree on the same input
  - threshold: ≥ 1 compared value differs between the two nodes for the same height or input.
  - measurement: submit the input to the network with its nodes differing only in the property under test (none for honest-node divergence, toolchain or CPU-architecture build, the library implementation they consume, or one node restored from a snapshot that passed the trusted AppHash/light-client check), and compare `app_hash`, `last_results_hash`, `GasUsed`, persisted BlockIDs that pass `ValidatorSet.VerifyCommit`, verdicts/decodes, served values, or ICS-23 proofs.

For the High impact **"Permanent locking / freezing of funds or clients"**, which is defined as where user funds, an account, or a non-malicious cross-chain connection become permanently unusable with no automatic recovery, where typically only a chain upgrade or a governance intervention can release them, bug reports covering this impact may be downgraded to Medium severity where any of the following conditions applies:

- The issue requires an optional or non-default module (ICA host, x/accounts lockup, x/rate-limiting, ICS02 precompile, transfer-v2 forwarding, erc20 middleware, etc.).
- The issue requires a self-inflicted or contrived configuration or trigger (genesis export/import, forwarded-hop timeout, client-ID collision, knowing an account address before it is created, etc.).
- The scope of the impact is limited to a single account, client, or path and is recoverable via governance or a chain upgrade.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain (cosmos-sdk, cosmos/evm, wasmd, ibc-go, etc)
  - condition: an account, client, or channel stays unusable after recovery
  - threshold: the operation still fails after the trigger clears and all nodes restart, while the same operation succeeds on the control.
  - measurement: after a full restart, attempt the `x/bank` spend, `x/staking` withdrawal, module-account function, `MsgUpdateClient`, channel handshake, or packet ack/refund against the affected account/client/channel and a control, and query balances, client status (`Frozen`/`Expired`), and escrow.

For the High impact **"Loss of cryptoeconomic security"**, it is defined as where a misbehaving validator escapes the penalties (slashing) or breaks the signature guarantees that secure the chain economically, without crashing anything, weakening the deterrents that keep validators honest.

Bug reports covering this impact may be downgraded to Medium severity where any of the following conditions applies:

- The issue is a narrow, conditional slashing evasion, such as dodging a single slash in the re-delegation flow.
- The benefit accrues only to a Byzantine validator or double-signer, and the attack requires operating as a validator.
- The attack requires an optional module (LSM, or a non-default BLS build tag) or a contrived multi-step timing (tokenize/transfer/redeem/redelegate, conceal-past-expiry, etc.).

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain with staking/slashing or IBC light clients (cosmos-sdk, cosmos/evm, wasmd, ibc-go, etc)
  - condition: a provable offense draws no penalty
  - threshold: once the evidence/downtime window has elapsed, the offending validator's slashed amount is below `slash_fraction` × its stake at the offense height or it is not jailed where jailing is expected, or an IBC light client given valid misbehaviour evidence is not frozen.
  - measurement: query `x/staking` bonded tokens and `x/slashing` jailed and missed-block state before and after the offense (including offenses routed through the cosmos/evm staking precompile or wasmd staking messages), or submit the misbehaviour and query the client status.
- For any validator signature or evidence verifier (cometbft, cosmos-sdk `x/evidence, etc`)
  - condition: an invalid signature or evidence is accepted
  - threshold: ≥ 1 evidence item or signature that an independent reference verification rejects is accepted on-chain: committed as evidence, triggering a slash or jail, or counted toward a commit.
  - measurement: submit the crafted `DuplicateVoteEvidence`/`LightClientAttackEvidence` via `MsgSubmitEvidence` or evidence gossip, or the crafted vote over P2P (including against a non-default BLS build), query the committed evidence, validator slashing state, and commit signatures, and verify the input with an independent reference to show it is invalid.

For the Medium impact **"Supply inflation / accounting corruption"**, it is defined as where the chain's books or aggregate token supply drift from reality without directly creating or destroying a specific user's funds. Internal accounting (escrow, FeePool, reward or staking pools) becomes inconsistent, or total supply inflates through systemic miscalculation.

Bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- The issue is reachable only under an optional or non-default module or configuration (protocolpool, a custom InputOutputCoins caller, 29-fee, PFM, NonrefundableKey middleware, etc.).
- The attack requires validator or proposer privilege to land the transaction (e.g. a Byzantine proposer), meaning only a validator, and not an unprivileged user, can trigger it.
- The attack requires a contrived multi-step or asymmetric setup, or a forced forwarded-hop timeout or ordering race.
- The issue is recoverable via governance.
- The internal accounting mismatch produces no real-world impact.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain (cosmos-sdk, cosmos/evm, wasmd, ibc-go, etc)
  - condition: a tracked total no longer matches what it tracks
  - threshold: the gap between the two sides of a named invariant grows by ≥ 1 base unit across the tx.
  - measurement: compute both sides of the invariant before and after the tx, e.g. `x/bank` total supply vs sum of balances, `x/distribution` FeePool vs outstanding rewards, staking-pool total vs bonded tokens, IBC escrow vs counterparty voucher supply or its tracked aggregate, EVM `StateDB` balance vs `x/bank` balance, or a rate-limit flow counter vs completed transfers.

For the Medium impact **"Single-node crash / resource-exhaustion DoS"**, it is defined as where a single attacker-reachable input crashes an individual node, or exhausts its CPU, memory, or disk until it stops serving, without stopping the chain, but because the same input works against any node, it can knock out the public RPC and infrastructure that users and services depend on.

Bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- The crash is confined to a single node and is recoverable on restart.
- The crash requires access to publicly available RPC methods.
- The issue is reachable only via an optional module, a non-default configuration (state sync, vote extensions, PostHandler, wasm), or only on RPC, simulation, or build-tooling paths.

The following scenario is not in-scope for this impact:

- Use of the CometBFT tx_search and block_search RPC endpoints for DoS. This is a known issue and it is publicly documented that these endpoints should not be exposed publicly.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any node (cosmos-sdk, cometbft, cosmos/evm, wasmd, ibc-go, etc)
  - condition: one node stops working while the network advances
  - threshold: the target node commits no new height and answers no request for ≥ 120s after the input, while the network keeps committing new blocks. A node that keeps answering does not meet this threshold. Where the stop is caused by memory exhaustion, the node's memory consumption must also exceed 16 GB before it stops.
  - measurement: deliver the input over the reachable surface (tx, P2P, CometBFT or EVM JSON-RPC, etc) to a running node, poll its `/status` and the targeted RPC alongside a surviving node's `/status`, and record the exit, panic, OOM, or hang behind it.

For the Medium impact **"Privilege escalation / authorization bypass / unauthorized state mutation"**, it is defined as where an actor performs an action a control was meant to forbid, mutating state or evading a restriction they should not be able to. Bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- Some authorization is bypassed but leads to no impact for the attacker or the system that was bypassed.
- The attack requires an optional module to be enabled (authz, circuit, distribution, IBC, vesting, or capability-gated chains).
- The attack requires a governance-granted starting permission, a victim's loose authz grant, or a non-default mode (EIP-7702, Exchange swap).
- The attack requires a contrived trigger (address collision, re-entrant 7702 callback, etc.) and is single-account and isolated per transaction.

The following scenarios are not in-scope for this impact:

- Intentionally permissionless-by-design paths (permissionless evidence submission, UpdateClient, the ICA active-channel swap) where the missing control is cryptographic proof, not authorization.
- Nested authz MsgExec authorizations (a message wrapped, possibly several levels deep, inside MsgExec). Executing through a validly held authz grant is authorized behavior by design, so it is not an authorization bypass and is excluded from this impact.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain (cosmos-sdk, cosmos/evm, wasmd, ibc-go, etc)
  - condition: a forbidden state change is persisted
  - threshold: the attack path changes ≥ 1 field of shared/protocol state that the control, run with the same actor and input, leaves unchanged.
  - measurement: read the target state before and after both paths; the control is the guarded path (authz/gov/permission check or required proof) or, where no guard exists, a read-only simulation (`eth_call`) of the same call.

For the Medium impact **"Transaction censorship / mempool manipulation"**, which is defined as where an attacker prevents, delays, or unfairly reorders other users' transactions, or starves them of block space, without necessarily halting the chain, bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- The impact is a transaction ordering skew only.
- The fee-market censorship requires a paid premium plus a fee-enabled channel and a profit-optimizing relayer.
- The censorship is per-packet or isolated to a single transaction.
- The attack requires spamming transactions that impose significant financial penalties on the attacker.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any chain (cometbft, cosmos-sdk, cosmos/evm, ibc-go, etc)
  - condition: targeted transactions are left out of blocks they qualify for
  - threshold: the targeted transaction is left out of ≥ 10 blocks proposed by honest validators, each of which had the transaction in its mempool at proposal time, had room for it, and included a control transaction paying ≤ its fee.
  - measurement: submit the targeted and control transactions together, record each proposer's mempool contents at proposal time (`/unconfirmed_txs`), and read each block's proposer, gas/bytes used against the limit, and included transactions with their fees (`/block`, `/validators`).
- For any chain (cometbft, cosmos-sdk, cosmos/evm, ibc-go, etc), low tier, ordering skew only
  - condition: targeted transactions are included, but placed behind transactions they should precede
  - threshold: in ≥ 10 blocks proposed by honest validators, the targeted transaction is ordered after a control transaction that paid ≤ its fee and entered the proposer's mempool no earlier, while the same sequence without the attacker's input orders them by fee and arrival.
  - measurement: submit the targeted and control transactions together, snapshot each proposer's mempool order at proposal time (`/unconfirmed_txs`), and read each block's transaction order and fees (`/block`), with a run without the attacker's input as the control.

For the Low impact **"Information disclosure"**, this is defined as where sensitive data is exposed to parties who should not see it. In this ecosystem, the impact is usually limited unless the leaked data is security-critical.

Bug reports covering this impact may be downgraded further, including to the ineligible Informational level, where any of the following conditions applies:

- The exposed secrets are single, low-value, or public-by-design, or are isolated to a template or documentation configuration.
- The issue is confined to build or npm tooling, not the chain runtime, or to a single device with no chain effect.
- The attack requires an authenticated request to be redirected cross-origin.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any repo, node, or device
  - condition: a secret is recovered by an unentitled party
  - threshold: the retrieved value equals the protected value.
  - measurement: retrieve the value as the unentitled party from the public repository, log, tooling output, node RPC/query surface, or device (under the emulator), and compare it against the protected value.

For the High impact **"Relayer / off-chain service key and wallet compromise"**, it is defined as an off-chain service that holds signing keys and funded wallets, such as an IBC relayer paying gas on every chain it serves, is compromised, letting an attacker extract keys, sign arbitrary transactions as the service, or drain its hot wallets across all configured chains at once.

Bug reports covering this impact may be downgraded to Medium severity where any of the following conditions applies:

- The issue is only reachable under an operator-chosen insecure configuration (a plaintext key in a world-readable file, a management API bound to a public interface).

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For relayers and other off-chain services and node signing RPCs
  - condition: an attacker can sign as the service
  - threshold: a signature over an attacker-chosen payload verifies under the service/node/operator public key.
  - measurement: obtain the signature with leaked key material (from logs, memory, or config) or by driving the service with ingested data or an unauthenticated request, and verify it over the attacker's payload.

For the Medium impact **"Supply-chain / CI-CD / RCE / account takeover"**, it is defined as a case whereby the software's build, release, dependency, or operator tooling is compromised. This is outside the chain's consensus, but able to put attacker-controlled code or content in front of node operators and users.

Bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- The impact is confined to a single off-chain asset (one bucket, site, or subdomain) or to the build/CI environment, with no on-chain effect.
- The attack requires the referenced resource to be unclaimed or dangling, or requires the attacker to first register a freed namespace and the victim to rebuild.
- The attack requires a non-default configuration or flag, or build-time or install-time-only conditions.
- The attack requires privileged users to intentionally approve a malicious workflow.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For any repo CI and release artifacts
  - condition: attacker content reaches the pipeline or a release
  - threshold: attacker-chosen content executes in a pipeline run or appears in a published artifact or manifest.
  - measurement: real CI run logs with the pinned workflow files cited (or a replica lab mirroring them), or recompute the artifact/manifest from the claimed source and diff it against the published one.

For the Medium impact **"Signing-display tamper / blind signing"**, it is defined as a case whereby a signing device or interface shows the user benign or incomplete information while a different or fuller payload is actually signed, so the user is tricked into authorizing something they did not intend. Bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- The attack requires a contrived input (more than 255 displayable items) and is single-user and single-transaction with no chain effect.

The following scenarios are not in-scope for this impact:

- The fields remain visible to the user through a different, non-default mode (e.g. expert mode on a Ledger device).

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For ledger devices
  - condition: the signed bytes differ from what was reviewed or validated
  - threshold: ≥ 1 field of the signed bytes is missing from or different in what the device displayed or the swap/auto-sign gate validated.
  - measurement: capture the device display or drive the swap/auto-sign path, and verify the returned signature over the true signed bytes.

For the Medium impact **"Relayer / off-chain service fund exhaustion (economic griefing)"**, it is defined as when an attacker crafts on-chain activity that forces an off-chain service to spend its own funds with no compensation until it can no longer operate. For an IBC relayer, this means spamming packets it relays at a loss, or forcing redundant or expensive client updates, draining its gas wallet and stopping relaying.

Bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- The attack is mitigated by fee middleware or relayer-side filtering.
- The attack only affects an operator running an uneconomic or misconfigured relaying policy.
- The attack financially punishes the attacker just as much as the relayer.
- The attack requires a connection to a malicious chain (i.e. it is not demonstrated how an attacker could force an honest chain to produce a value or input that would cause the fund exhaustion) or a compromised RPC node.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For relayers and other off-chain services
  - condition: the services wallet drains to non-operation
  - threshold: the gas wallet can no longer pay for one relay transaction.
  - measurement: starting from a stated wallet balance, drive the attacker activity and track wallet balance, fees received, and gas paid on each served chain, recording the attacker's own cost, with the input shown reproducible from an honest chain.

For the Medium impact **"Relayer / off-chain service liveness failure"**, this is defined as when a crafted untrusted input or network-level abuse crashes, hangs, deadlocks, or exhausts an off-chain delivery service so it stops doing its job. For an IBC relayer, this halts packet, acknowledgement, or timeout delivery and client updates, which strands in-transit user funds and can let an IBC light client expire, freezing the channel until a governance recovery.

Bug reports covering this impact may be downgraded to Low severity where any of the following conditions applies:

- The service simply crashes and is restartable with no stuck funds or client expiry, and another relayer can cover the path.
- The attack requires a contrived input or a non-default configuration.
- The attack requires a connection to a malicious chain (i.e. it is not demonstrated how an attacker could force an honest chain to produce a value or input that would cause the relayer DoS) or a compromised RPC node.

This impact is measured by the following oracle(s), ensure your PoC satisfies at least one of the following:

- For relayers and other off-chain services
  - condition: the relayer stops delivering
  - threshold: the relayer delivers no pending packet, ack, or timeout for ≥ 10 minutes after the input.
  - measurement: monitor the pending queue and process liveness (crash, hang, deadlock, resource exhaustion, or deterministic rejection of consensus-valid input), plus the light-client trusting-period countdown, with the input shown reproducible from an honest chain.

**Informational Findings**

Findings with no real security consequence, such as cosmetic issues, problems confined to documentation or build tooling that never runs on-chain, behavior that is safe-by-design, or bugs with no demonstrated impact or no demonstrated exploit, are classified as Informational and are not eligible for a reward.

**Program Wide Severity Downgrade Conditions**

In addition to the impact-specific conditions above, the severity level of a bug report may be downgraded by one severity level where any of the following conditions applies:

- The attack requires a race condition to occur in which the timing is not within the attacker's control.
- Performing the attack requires the attacker to be within a permissioned set, such as a validator within the active set or a user with the ability to deploy contracts on a restricted chain.
- The attack requires a governance action to be taken in order for the attack to take place, such as an on-chain consensus parameter change.
- The attack requires validator collusion of one third or more, of voting power.
- The vulnerability is easily recoverable with built-in tooling that mitigates the impact.
- The attack requires a relayer to behave maliciously

## Rewards

- [blockchain_dlt] Critical: fixedReward=$50,000, rewardCalculationPercentage=0, rewardModel=fixed
- [blockchain_dlt] High: fixedReward=$4,000, rewardModel=fixed
- [blockchain_dlt] Medium: fixedReward=$1,000, rewardModel=fixed
- [blockchain_dlt] Low: fixedReward=$500, rewardModel=fixed

## Reward notes

# **Rewards by Threat Level**

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below.

Informational reports are not eligible for a reward. Repeated informational or inapplicable submissions will be treated as spam and may result in exclusion from the program.

**Informational Findings**

Findings with no real security consequence, such as cosmetic issues, problems confined to documentation or build tooling that never runs on-chain, behavior that is safe-by-design, or bugs with no demonstrated impact or no demonstrated exploit, are classified as Informational and are not eligible for a reward.

**Program Wide Severity Downgrade Conditions**

In addition to the impact-specific conditions above, the severity level of a bug report may be downgraded by one severity level where any of the following conditions applies:

- The attack requires a race condition to occur in which the timing is not within the attacker's control.
- Performing the attack requires the attacker to be within a permissioned set, such as a validator within the active set or a user with the ability to deploy contracts on a restricted chain.
- The attack requires a governance action to be taken in order for the attack to take place, such as an on-chain consensus parameter change.
- The attack requires validator collusion of one third or more, of voting power.
- The vulnerability is easily recoverable with built-in tooling that mitigates the impact.
- The attack requires a relayer to behave maliciously

**Important Note for All Bug Reports**

While Cosmos aims to provide as clear as possible objective downgrade reasoning in this bug bounty program text, it cannot cover all scenarios that would warrant a downgrade, especially given the uniqueness of the Cosmos structure compared with other bug bounty programs on Immunefi. Because of this, all reports to the Cosmos bug bounty program may be further downgraded by Cosmos separate from or in addition to the downgrade conditions here. The Cosmos team thus retains full discretion on the final severity level of all reports. However, the Cosmos team adheres to providing a reason for all these special additional downgrades.

**Feasibility Limitations**

The following standard feasibility limitations apply for the bug bounty program:

- [Chain Rollbacks](https://immunefisupport.zendesk.com/hc/en-us/articles/16913153448721-Chain-Rollbacks?utm_source=immunefi)
- [Attack Investment Amount](https://immunefisupport.zendesk.com/hc/en-us/articles/17243068885265-Attack-Investment-Amount?utm_source=immunefi)
- [Attacks With A Financial Risk To The Attacker](https://immunefisupport.zendesk.com/hc/en-us/articles/17454897136401-Attacks-With-A-Financial-Risk-To-The-Attacker?utm_source=immunefi)
- [When Is An Impactful Attack Downgraded To Griefing?](https://immunefisupport.zendesk.com/hc/en-us/articles/17455102268305-When-Is-An-Impactful-Attack-Downgraded-To-Griefing?utm_source=immunefi)

**Proof of Concept (PoC) Requirements**

A PoC is required for all bug reports.

- The PoC must be code that can be read and run by the security team. Written descriptions of an attack alone do not count as a valid PoC.
- PoCs must demonstrate real user flows. Mock-only or database-only calls are insufficient.
- Bug reports without adequate detail may be closed or returned for revision.

A PoC is required for all severity levels. All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules?utm_source=immunefi). Bug report submissions without a PoC will not be provided with a reward.
For all Medium, High, and Critical reports, the PoC must demonstrate the vulnerability end-to-end on a local 4-node network, from an external point of view. The vulnerability must be shown against the running network as an external actor would encounter it, not in isolation.
The following are the requirements for a valid PoC:

- The PoC must spin up a local 4-node network and demonstrate the vulnerability against that running network.
- The vulnerability must be demonstrated from an external perspective. If the attack requires a malicious node, the PoC may inject the necessary code into a single instance to make it malicious, but the impact must be demonstrated against the network as a whole.
- The ideal PoC is a self-contained bash script that spins up the network, applies any required modifications, and runs the CLI commands that carry out and prove the attack.
- The PoC should be uploaded inline within the report, or as a GitHub Gist. They should **not** be uploaded as attachements to the report or in comments.

The following are not accepted as valid PoCs on their own:

- Unit tests
- Integration tests
- Written explanations, descriptions, or theoretical demonstrations without a working end-to-end PoC against the local network
  Reports that do not demonstrate the vulnerability end-to-end on a local network, as described above, will be considered insufficient and will not be eligible for a reward until a valid PoC is provided.

All PoC's should include a metadata `poc.json` file. The `poc.json` file should have the following structure:

```json
{
  "target": {
    "repo": "<github repository link>",
    "tags": ["<released tag being targed, may be multiple>"],
    "commits": ["<full commit hash being targeted, may be multiple>"],
    "binary": "<binary being exploited, evmd, simd, etc>"
  },
  "claim": {
    "impact": "<claimed impact from impacts section>",
    "severity": "<critical, high, medium, low, or none",
    "summary": "<flaw, entrypoint, and effect in one or two sentences>"
  },
  "oracle": "<specify the oracle you are using for your claimed impact, triage will independently verify the impact via this oracle>"
}
```

The specified `claim.severity` should include all downgrade scenarios that apply to your report's selected impact. For example if the specified impact has a medium seveirty, but a single downgrade scenario applies bringing the report to low severity, the `claim.severity` should be "low".

**Other Terms and Information**

- Release Policy Requirement - Only released code is eligible for a reward. To be considered valid and in-scope, the issue must exist in released code that is tagged and actively maintained under the [Cosmos Release Family Policy](https://docs.cosmos.network/sdk/latest/release-family?utm_source=immunefi#upgrades-and-support). Code that exists only on main, master, or other development branches is not in-scope. In addition, the issue must be exploitable in an intended deployed environment and configuration.

## Out of scope (program-specific)

# Out of Scope & Rules

These impacts are out of scope for this bug bounty program.

All Categories

* Issues requiring a previously compromised environment to exploit (e.g. a compromised node or a majority-compromised consensus).

* Assets not explicitly listed as in-scope, including assets not owned by participating teams.

* Issues already publicly or privately addressed, and issues fixed upstream.

* Downstream effects of previously resolved bounty issues.

* Third-party services and websites.

* Web vulnerabilities, including but not limited to XSS, CSRF, CORS, cookie flags, TLS configuration, headers, and email configuration.

* Documented configuration behaviors in expected deployment scenarios.

* Governance misconfiguration-specific issues.

* Package registry or dependency management issues without Cosmos-specific exploit PoCs, and dependency vulnerability reports without demonstrated impact on in-scope systems.

* Scanner-generated, automated, or informational-only reports without demonstrated impact.

* Architectural critiques without immediate exploitability.

* Vulnerabilities caused by user error or misconfiguration by the user, going against documented operational procedures. An example of this would be RPC endpoints intended for debug or developer/non-production usage only

* Vulnerabilities requiring privileged access to a local network or machine, without demonstrating how that access is gained.

* Impacts requiring attacks that the reporter has already exploited themselves, leading to damage.

* Impacts caused by attacks requiring access to leaked keys/credentials.

* Impacts caused by attacks requiring access to privileged addresses without additional modification of the privileges attributed. For avoidance of doubt, attacks requiring membership of a permissioned participant set (for example, an active-set validator) are handled under the Program Wide Severity Downgrade Conditions rather than this exclusion.

* Impacts requiring phishing or other social engineering attacks against project employees and/or users.

* Best practice recommendations.

* Feature requests.

* Impacts on test files and configuration files unless stated otherwise in the bug bounty program.

* Attacks where the cost of executing an attack is greater than the potential or deterministically proven impact in terms of damage caused.

* Incorrect data supplied by third party oracles. This does not exclude oracle manipulation attacks.

* Impacts involving centralization risks.

* Attacks that require honest users to directly interact with, transfer to, or deposit into a malicious chain, IBC channel/client, or contract on their own.

* State-sync vulnerabilities which prevent honest nodes from joining the network and rely on honest nodes accepting snapshots from untrusted or malicious peers.

### The following activities are prohibited by this bug bounty program:

* Any testing against live mainnet or public testnet networks, deployed code, or production infrastructure. All testing should be done on local forks, local test clusters, or private deployments.

* Any denial of service attacks executed against project assets or live networks.

* Automated testing of services that generate significant amounts of traffic.

* Violating the privacy of users, disrupting production systems, destroying data, or harming the user experience.

* Accessing more data than is required for a proof of concept. If sensitive user data (PII, PHI, financial data, or proprietary information) is encountered, testing must cease immediately and a bug report must be submitted.

* Using accounts other than test accounts the security researcher owns or has explicit permission to use.

* Attempting phishing or other social engineering attacks against project employees and/or users.

* Any testing with third-party systems, applications, or websites.

* Public disclosure of an unpatched vulnerability, or disclosure of a vulnerability before it is remediated and disclosure is approved.

* Extortion or other coercive behavior.

* Any other actions prohibited by the Immunefi Rules.

### Other Terms and Information:

* Gaia \- Gaia is included only as a reference implementation of the Cosmos Stack. All Cosmos Hub-specific features, third-party modules, and non-core functionality in the Gaia repository are out-of-scope.

* Cosmos SDK modules \- Following [https://github.com/cosmos/cosmos-sdk/pull/25090](https://github.com/cosmos/cosmos-sdk/pull/25090), the x/group, x/circuit, x/crisis, and x/nft modules are no longer maintained and are not in-scope. Bug reports on maintained Cosmos SDK modules other than those highlighted in the Assets in Scope section are also accepted, provided the module is covered by the Release Family Policy.

* Cosmos EVM \- The x/precisebank module in Cosmos EVM is not covered by this bug bounty program and is no longer maintained. Older versions of this software will not be patched, and users are urged to no longer use it.

* iavl \- The iaviewer application itself is not in-scope, unless there is an underlying bug in the iavl library that can be exploited through the application or through other applications using the iavl library.

* Hermes \- Issues specific to the Penumbra integration within Hermes are out-of-scope.

* When an issue is on track to be mitigated or remediated, Cosmos Labs will coordinate with the security researcher to credit the finding in advisories and release notes, and to support disclosure of valid issues after remediation.

* Memory Exhaustion (OOM) Reports - Minimum Threshold: For reports demonstrating an out-of-memory (OOM) condition through increased node memory consumption, the report must demonstrate a memory increase that exceeds 16 GB in order to be considered valid. Reports that do not demonstrate memory consumption above this threshold will be considered out of scope, as they do not sufficiently prove the ability to exhaust a node's memory and cause a crash.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- The displayed item count was not aligned with the range supported by the UI item index. viewfunc_getItem_t accepts an int8_t index, meaning only items with indices 0–127 can be requested. Previously, items beyond this limit were included in the total count but could not be retrieved or displayed, causing them to be omitted during review.
This fix we applied ensures the reported item count is capped to the maximum addressable UI index range, preventing inaccessible items from being counted. (https://github.com/cosmos/ledger-cosmos/pull/203)
