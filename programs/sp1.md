# SP1

- Page: https://immunefi.com/bug-bounty/sp1/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium
- End date: (none)

## Assets in scope (9)

- [blockchain_dlt] https://docs.succinct.xyz/docs/sp1/introduction — Primacy of Impact (primacy of impact)
- [blockchain_dlt] https://github.com/succinctlabs/sp1/blob/main/crates/prover/src/verify.rs — sp1-prover verifier
- [blockchain_dlt] https://github.com/succinctlabs/sp1/tree/main/crates/core/executor — sp1-core-executor
- [blockchain_dlt] https://github.com/succinctlabs/sp1/tree/main/crates/core/machine — sp1-core-machine
- [blockchain_dlt] https://github.com/succinctlabs/sp1/tree/main/crates/hypercube — sp1-hypercube
- [blockchain_dlt] https://github.com/succinctlabs/sp1/tree/main/crates/recursion — sp1-recursion
- [blockchain_dlt] https://github.com/succinctlabs/sp1/tree/main/crates/zkvm/entrypoint — sp1-zkvm
- [blockchain_dlt] https://github.com/succinctlabs/sp1/tree/main/crates/zkvm/lib — sp1-lib
- [blockchain_dlt] https://github.com/succinctlabs/sp1/tree/main/slop/crates/ — slop (Succinct Library of Polynomials) - excluding whir, veil, spartan, pgspcs

## Asset notes

(none)

## Impacts in scope (5)

- [blockchain_dlt] Critical: Soundness bug where a malicious prover can forge a false proof for all 4 proof types (core, compressed, Plonk, Groth16) for a general class of programs.
- [blockchain_dlt] High: Soundness bug where a malicious prover can forge a false Compressed proof for a general class of programs.
- [blockchain_dlt] High: Soundness bug where a malicious prover can forge a false Groth16 and a Plonk proof for a general class of programs.
- [blockchain_dlt] Medium: Completeness bug affecting all proof types and a general class of programs.
- [blockchain_dlt] Medium: Soundness bug that allows forging a false core proof but not compressed or SNARK proofs.

## Impact notes

We prioritize soundness vulnerabilities affecting Groth16 and Plonk proof types.

The severity of a soundness or completeness finding may change due to the impact and scope of the finding, i.e. which types of programs are affected, and what types of incorrect execution becomes provable or what types of correct execution becomes unprovable.

## Rewards

- [blockchain_dlt] Critical: maxReward=$100,000, minReward=$15,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: maxReward=$15,000, minReward=$2,000, rewardModel=range
- [blockchain_dlt] Medium: maxReward=$2,000, minReward=$1,000, rewardModel=range

## Reward notes

SP1 provides rewards in USDC on Ethereum, denominated in USD.

## Out of scope (program-specific)

All reports must be valid on SP1's latest release commit, which can be found [here](https://github.com/succinctlabs/sp1/releases). The findings must be reproduced with production circuits and verification keys, with default production security checks. Findings that require Cargo features or paths intended solely for `experimental`, `mprotect`, `may_dump_elf`, debug, profiling, dummy, testing, benchmarking, or in-development circuits are out of scope. Findings on the usage of `proof_nonce` are also considered out of scope.
We are in the process of marking proof verification with non-zero `exit_code` as experimental, and therefore all findings relating to non-zero `exit_code` is considered out of scope. 
More precisely, the findings should use the compiler feature-set used to build the Docker images [here](https://github.com/succinctlabs/sp1-cluster/blob/main/.github/workflows/docker.yml); in particular, `sp1-prover/experimental` and `sp1-prover/mprotect` are off, `sp1-prover/native-gnark` is turned on, and they should demonstrate a completeness or soundness vulnerability in `sp1_sdk::prover::Prover::verify`.
Proofs of concept should be able to run on an Apple M3 chip or similar hardware in ten minutes or less.

The `whir`, `veil`, `spartan`, `pgspcs` crates within `slop` are out of scope. Findings that affect `slop` only as a standalone library and do not affect the in-scope proving and verification in SP1 are considered out of scope. 

A bug bounty submission for a completeness vulnerability should demonstrate an inherent and deterministic incorrectness inside an AIR constraint, recursive circuit, or production verifier that makes a valid execution unprovable, or makes its correctly generated proof unverifiable. Failures that are specific to a prover backend or prover implementation, hardware, insufficient resources, concurrency, timeouts, environment variables, or user configuration are out of scope.

All reports must be valid under the SP1 security model
- https://docs.succinct.xyz/docs/sp1/security/security-model
- https://docs.succinct.xyz/docs/sp1/security/safe-precompile-usage

This means that all eligible proofs of concept must use
- A memory-safe, non-malicious program.
- An ELF produced by the provided SP1 toolchain.
- Safe usage of precompiles and patched crates as explained in the documentation.
- Must not request a `Core` proof for an ELF that invokes the `VERIFY_SP1_PROOF` syscall.

Also, the PoC program should be generated through memory-safe Rust program, compiled through the usual SP1 zkvm entrypoint and libraries. In general, for a submission to be valid, it needs to work on all "general class of programs". As such, findings should be applicable for all programs that use a certain opcode or syscall in normal usecases. In short, the PoC's should be done with guest programs that are more standard, such as the Fibonacci ELF or the RSP program.

Only production soundness failures and protocol-level completeness failures as defined above are eligible for the bounty. Findings on DoS of prover and the verifier, as well as service availability, are considered out of scope. 

**Source**: [SP1](https://github.com/succinctlabs/sp1)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (3)

- List of Publicly Known Issues (https://github.com/code-423n4/2025-09-succinct#publicly-known-issues)
- Previous Bug Bounty Submissions (https://github.com/code-423n4/succinct-bug-bounty/issues?q=is%3Aissue%20state%3Aclosed%20label%3Asatisfactory)
- Security Advisories (https://github.com/succinctlabs/sp1/security/advisories)
