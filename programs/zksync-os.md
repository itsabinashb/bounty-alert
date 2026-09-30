# ZKsync OS

- Page: https://immunefi.com/bug-bounty/zksync-os/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Smart Contract
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium
- End date: (none)

## Assets in scope (232)

- [blockchain_dlt] https://github.com/matter-labs/airbender-platform/tree/a350ee3e08bef4cbe2b7bc968966bee45bc98a17/crates/airbender-crypto — Crypto (airbender-crypto)
- [blockchain_dlt] https://github.com/matter-labs/airbender-platform/tree/a350ee3e08bef4cbe2b7bc968966bee45bc98a17/crates/airbender-guest — airbender-guest: Airbender guest APIs: oracle input reading, output commitment, transport
- [blockchain_dlt] https://github.com/matter-labs/airbender-platform/tree/a350ee3e08bef4cbe2b7bc968966bee45bc98a17/crates/airbender-rt — airbender-rt: Airbender guest runtime (boot, trap/syscall glue, allocator, UART) - replaces former zksync_os/src runtime files
- [blockchain_dlt] https://github.com/matter-labs/zkos-wrapper/blob/585595f145cb53a09a130706ca36f80ddcac3961/wrapper/src/lib.rs — Public API for setup, proving, and verification across all wrapper layers
- [blockchain_dlt] https://github.com/matter-labs/zkos-wrapper/tree/585595f145cb53a09a130706ca36f80ddcac3961/circuit_mersenne_field — All in-circuit Mersenne field arithmetic (base, complex and quartic extensions) incl. range and reduction constraints
- [blockchain_dlt] https://github.com/matter-labs/zkos-wrapper/tree/585595f145cb53a09a130706ca36f80ddcac3961/wrapper/src/circuits — Wrapper circuits: RiscWrapperCircuit, CompressionCircuit, SnarkWrapperCircuit
- [blockchain_dlt] https://github.com/matter-labs/zkos-wrapper/tree/585595f145cb53a09a130706ca36f80ddcac3961/wrapper/src/inner_verifiers — In-circuit airbender verifiers (unified reduced machine, Blake2 delegation): shared verify/skeleton implementation and generated layout/quotient imports include!d into the circuit (part of the VK)
- [blockchain_dlt] https://github.com/matter-labs/zkos-wrapper/tree/585595f145cb53a09a130706ca36f80ddcac3961/wrapper/src/transcript — In-circuit Blake2s transcript (reduced-round Blake2s); must match the native transcript byte for byte
- [blockchain_dlt] https://github.com/matter-labs/zkos-wrapper/tree/585595f145cb53a09a130706ca36f80ddcac3961/wrapper/src/wrapper_utils — Allocates proof data into the circuit; range and reduction constraints
- [blockchain_dlt] https://github.com/matter-labs/zkos-wrapper/tree/585595f145cb53a09a130706ca36f80ddcac3961/wrapper_generator — Wrapper verifier generator: emits the generated in-circuit layout and quotient
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/constraint.rs — Definition of constraints
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/cs/circuit.rs — Main circuits logic (CS)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/cs/cs_reference.rs — Reference implementation of CS
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/cs/mod.rs — Circuit builder API (CS): module root
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/cs/oracle.rs — Circuit builder API (CS): witness oracle interface
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/cs/placeholder.rs — Circuit builder API (CS): placeholders
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/cs/spec_selection.rs — Orthogonal varians circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/cs/utils.rs — Utilities for constraint system
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/csr_properties.rs — Special csr properties table
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/devices/aux_data.rs — Helper data structures
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/devices/diffs.rs — Defines instruction execution state changes
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/devices/mod.rs — Circuit description framework: devices module root
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/devices/optimization_context.rs — Optimization framework for RISC-V circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/devices/risc_v_types.rs — RISC-V ISA type definitions
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/lib.rs — Constraint-system crate root
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/machine_configurations/minimal_state.rs — Utilities for minimal machine state
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/machine_configurations/mod.rs — Module coordinator that exports all machine configurations
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/mod.rs — Circuit description framework: machine module root
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/add_sub.rs — SUB/ADD circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/binops.rs — Binary operation circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/conditional.rs — Branch instructions circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/constants.rs — Instruction circuits: shared constants
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/jump.rs — Jump instructions circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/load.rs — Load instructions circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/lui_auipc.rs — LUI/AUIPC instructions circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/mod.rs — Instruction circuits: module root and shared helpers
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/mop.rs — Modular operation primitives
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/shift.rs — Shift operations circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/store.rs — Store instructions circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/utils.rs — Circuit description framework: machine utilities
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/types.rs — Core type definition
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/utils.rs — Constraint-system utilities
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/field/src/base.rs — Base field operations
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/field/src/complex.rs — Complex extensions
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/field/src/field.rs — Base field operations
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/field/src/field_like.rs — Base field operations
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/field/src/lib.rs — Base field operations
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/field/src/ops.rs — Base field operations
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/field/src/proc_macro_ops.rs — Base field operations
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/field/src/quartic.rs — Quartic extensions
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/blob/67ee094449abaebc77e58435f130ce6ea27721e5/prover/src/lib.rs — Prover crate definitions compiled into the recursion program (definitions_only feature): proof-structure types, leaf inclusion verifier, folding schedule
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/blake2s_u32 — Blake2s (u32) hash used for Merkle trees and transcript; compiled into the recursion program
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/bigint_with_control/verifier — Per-circuit verifier for bigint_with_control: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/blake2_with_compression/verifier — Per-circuit verifier for blake2_with_compression: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/keccak_special5/verifier — Per-circuit verifier for keccak_special5: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/add_sub_lui_auipc_mop/verifier — Per-circuit verifier for add_sub_lui_auipc_mop: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/inits_and_teardowns/verifier — Per-circuit verifier for inits_and_teardowns: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/jump_branch_slt/verifier — Per-circuit verifier for jump_branch_slt: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/load_store_subword_only/verifier — Per-circuit verifier for load_store_subword_only: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/load_store_word_only/verifier — Per-circuit verifier for load_store_word_only: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/mul_div/verifier — Per-circuit verifier for mul_div: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/mul_div_unsigned/verifier — Per-circuit verifier for mul_div_unsigned: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/shift_binary_csr/verifier — Per-circuit verifier for shift_binary_csr: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/circuit_defs/unrolled_circuits/unified_reduced_machine/verifier — Per-circuit verifier for unified_reduced_machine: generated layout, quotient evaluation and skeleton instance compiled into the recursion program (determines end_params)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/common_constants — Shared constants; compiled into the recursion program
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/definitions — Layout and proof-structure definitions (columns, constraints, lookups, memory/setup/witness trees, unrolled families)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/delegation — Delegation circuits (BigInt with control, Blake2 single round, Blake2 round with extended control, Keccak special5) and their shared definitions
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/instruction_decoding_data — Instruction decoding data
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/common_impls — Instruction circuits: common CSR implementations (non-determinism CSR, CSR with delegation)
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/machine/ops/unrolled — Unrolled RISC-V circuit families (9, incl. unified_reduced_machine): the circuits whose satisfaction a proof asserts
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/one_row_compiler — Circuit layout compiler: produces the compiled circuit artifact consumed by the verifier generator
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/cs/src/tables — Lookup tables
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/full_statement_verifier — Full statement verifier: composes per-circuit proofs into one execution claim; compiled into the recursion program
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/non_determinism_source — Non-determinism (oracle) CSR source read by the recursion program
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/prover/src/definitions — Prover crate definitions compiled into the recursion program (definitions_only feature): proof-structure types, leaf inclusion verifier, folding schedule
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/reduced_keccak — Reduced Keccak used by the full statement verifier; compiled into the recursion program
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/riscv_common — RISC-V guest runtime (boot sequence) of the recursion program
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/tools/generator — Driver for verifier_generator
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/tools/verifier — Recursion program source (main.rs, build.sh, rust-toolchain.toml): its built bytes determine end_params and the aux_params chain links
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/transcript — Verifier transcript (Blake2s-based Fiat-Shamir); compiled into the recursion program
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/verifier — Native verifier; the source compiled into the recursion program
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/verifier_common — Shared FRI folding, transcript sizing and proof-of-work logic
- [blockchain_dlt] https://github.com/matter-labs/zksync-airbender/tree/67ee094449abaebc77e58435f130ce6ea27721e5/verifier_generator — Generates the inlined, optimized Rust verifier that evaluates the constraint system
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/bellman/src/plonk/better_better_cs/cs.rs — bellman plonk/better_better_cs: the Plonk arithmetisation
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/bellman/src/plonk/better_better_cs/data_structures.rs — bellman plonk/better_better_cs: the Plonk arithmetisation
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/bellman/src/plonk/better_better_cs/lookup_tables.rs — bellman plonk/better_better_cs: the Plonk arithmetisation
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/bellman/src/plonk/better_better_cs/mod.rs — bellman plonk/better_better_cs: the Plonk arithmetisation
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/bellman/src/plonk/better_better_cs/utils.rs — bellman plonk/better_better_cs: the Plonk arithmetisation
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/copy_permutation.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/cs.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/evaluator_data.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/lookup_placement.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/lookup_table.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/mod.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/polynomial/mod.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/polynomial_storage.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/pow.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/proof.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/reference_cs.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/security_level_calculator.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/setup.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/setup_storage.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/transcript.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/utils.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/implementations/verifier.rs — boojum cs/implementations: builds the constraint system and the setup
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/constants.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/group_hash.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/lib.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/allocated_num.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/assignment.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/boolean.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/byte.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/counter.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/custom_5th_degree_gate_optimized.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/custom_rescue_gate.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/linear_combination.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/mod.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/simple_term.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/tables.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/utils.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/mod.rs — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/lib.rs — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/poseidon2/mod.rs — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/poseidon2/params.rs — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/poseidon2/poseidon2.rs — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/poseidon2/sponge.rs — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/poseidon2/transcript.rs — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/sponge.rs — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/traits.rs — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/blob/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/snark-wrapper/src/traits/circuit.rs — snark-wrapper traits/circuit: the in-circuit FRI verifier inside the Plonk circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/bellman/src/kate_commitment — bellman kate_commitment: the KZG code that computes the VK points
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/bellman/src/plonk/better_better_cs/gates — bellman plonk/better_better_cs gates: main gate definitions
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/bellman/src/plonk/better_better_cs/setup — bellman plonk/better_better_cs setup: Setup and VerificationKey structures and VK computation
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/cs/gates — boojum gates: the configured gate set (FmaGate variants, ReductionGate, SelectionGate, ParallelSelectionGate, ConditionalSwapGate, BooleanConstraintGate, ConstantsAllocatorGate, PublicInputGate, ZeroCheckGate, UIntXAddGate, U32AddCarryAsChunkGate, U32TriAddCarryAsChunkGate, NopGate, Blake2sStateGate): the gate set and its placement are the VK
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/blake2s — boojum gadgets/blake2s: in-circuit transcript hashing
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/boolean — boojum gadgets/boolean: primitive gadgets and lookup tables instantiated in the circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/impls — boojum gadgets/impls: primitive gadgets and lookup tables instantiated in the circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/num — boojum gadgets/num: primitive gadgets and lookup tables instantiated in the circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/recursion — boojum gadgets/recursion: recursive verifier used by the compression layer
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/tables — boojum gadgets/tables: primitive gadgets and lookup tables instantiated in the circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/traits — boojum gadgets/traits: primitive gadgets and lookup tables instantiated in the circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/u16 — boojum gadgets/u16: primitive gadgets and lookup tables instantiated in the circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/u32 — boojum gadgets/u32: primitive gadgets and lookup tables instantiated in the circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/gadgets/u8 — boojum gadgets/u8: primitive gadgets and lookup tables instantiated in the circuits
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/boojum/src/implementations/poseidon2 — boojum implementations/poseidon2: tree hasher used by the compression layer
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/bigint — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/bigint_new — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/goldilocks — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/plonk/circuit/hashes_with_tables — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/franklin-crypto/src/rescue — franklin-crypto: BN254-side gadgets used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/pairing/src/bn256 — pairing bn256: BN254 arithmetic used by bellman for the VK points
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/pairing/src/compact_bn256 — pairing compact_bn256: BN254 arithmetic used by bellman for the VK points
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/circuit — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/common — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/poseidon — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/rescue — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/rescue-poseidon/src/rescue_prime — rescue_poseidon: sponge used by the SNARK wrapper
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/snark-wrapper/src/implementations/poseidon2 — snark-wrapper implementations/poseidon2: the in-circuit FRI verifier inside the Plonk circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/snark-wrapper/src/verifier — snark-wrapper verifier: the in-circuit FRI verifier inside the Plonk circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-crypto/tree/bf2797e4ca13475bf797aa43e085389cdd6732f9/crates/snark-wrapper/src/verifier_structs — snark-wrapper verifier_structs: the in-circuit FRI verifier inside the Plonk circuit
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/basic_bootloader — Basic bootloader
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/basic_system — Basic system
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/callable_oracles — Callable oracles
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/evm_interpreter — EVM interpreter
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/oracle_provider/ — Oracle provider
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/proof_running_system — Proof running system
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/storage_models — Storage models
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/supporting_crates/delegated_u256 — Delegated U256
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/supporting_crates/modexp — Modexp
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/supporting_crates/u256 — U256
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/system_hooks/ — System hooks
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/zk_ee/ — ZK Execution Environment
- [blockchain_dlt] https://github.com/matter-labs/zksync-os/tree/ac442e73d80f4e964476a4fc36fa267d676da449/zksync_os/ — ZKsync OS program
- [blockchain_dlt] https://zksync.io — Primacy of Impact (primacy of impact)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/da-contracts/contracts/BlobsL1DAValidatorZKsyncOS.sol — BlobsL1DAValidatorZKsyncOS
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/da-contracts/contracts/EIP7702Checker.sol — EIP7702Checker
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/da-contracts/contracts/RollupL1DAValidator.sol — RollupL1DAValidator
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/da-contracts/contracts/da-layers/avail/AvailL1DAValidator.sol — AvailL1DAValidator
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/atomic-interop/AtomicFlowManager.sol — AtomicFlowManager
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/atomic-interop/L2InteropCommitmentTree.sol — L2InteropCommitmentTree
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/BridgedStandardERC20.sol — BridgedStandardERC20
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/L1Nullifier.sol — L1Nullifier
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/L2WrappedBaseToken.sol — L2WrappedBaseToken
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/UpgradeableBeaconDeployer.sol — UpgradeableBeaconDeployer
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/asset-router/L1AssetRouter.sol — L1AssetRouter
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/asset-router/L2AssetRouter.sol — L2AssetRouter
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/asset-tracker/L2AssetTracker.sol — L2AssetTracker
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/ntv/L1NativeTokenVault.sol — L1NativeTokenVault
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/bridge/ntv/L2NativeTokenVaultZKOS.sol — L2NativeTokenVaultZKOS
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/core/bridgehub/L1Bridgehub.sol — L1Bridgehub
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/core/bridgehub/L2Bridgehub.sol — L2Bridgehub
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/core/chain-asset-handler/L1ChainAssetHandler.sol — L1ChainAssetHandler
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/core/chain-asset-handler/L2ChainAssetHandler.sol — L2ChainAssetHandler
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/core/chain-registration/ChainRegistrationSender.sol — ChainRegistrationSender
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/core/ctm-deployment/CTMDeploymentTracker.sol — CTMDeploymentTracker
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/core/message-root/L1MessageRoot.sol — L1MessageRoot
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/core/message-root/L2MessageRoot.sol — L2MessageRoot
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/governance/ChainAdminOwnable.sol — ChainAdminOwnable
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/governance/Governance.sol — Governance
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/interop/InteropAttributeParser.sol — InteropAttributeParser
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/interop/InteropCenter.sol — InteropCenter
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/interop/L2InteropRootStorage.sol — L2InteropRootStorage
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/interop/L2MessageVerification.sol — L2MessageVerification
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/interop/interop-handler/L1InteropHandler.sol — L1InteropHandler
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/interop/interop-handler/L2InteropHandler.sol — L2InteropHandler
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-system/BaseTokenHolder.sol — BaseTokenHolder
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-system/EmptyContract.sol — EmptyContract (retired tracker implementation)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-system/zksync-os/L1MessengerZKOS.sol — L1MessengerZKOS
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-system/zksync-os/L2BaseTokenZKOS.sol — L2BaseTokenZKOS
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-system/zksync-os/SystemContext.sol — SystemContext (ZKsync OS)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-system/zksync-os/ZKOSContractDeployer.sol — ZKOSContractDeployer
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-upgrades/L2ComplexUpgrader.sol — L2ComplexUpgrader
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-upgrades/L2GenesisUpgrade.sol — L2GenesisUpgrade
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-upgrades/SystemContractProxy.sol — SystemContractProxy
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/l2-upgrades/SystemContractProxyAdmin.sol — SystemContractProxyAdmin
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/ZKsyncOSChainTypeManager.sol — ZKsyncOSChainTypeManager
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/chain-deps/DiamondProxy.sol — DiamondProxy
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/chain-deps/facets/Admin.sol — AdminFacet (Admin.sol)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/chain-deps/facets/Committer.sol — CommitterFacet (Committer.sol)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/chain-deps/facets/Executor.sol — ExecutorFacet (Executor.sol)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/chain-deps/facets/Getters.sol — GettersFacet (Getters.sol)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/chain-deps/facets/Mailbox.sol — MailboxFacet (Mailbox.sol)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/chain-deps/facets/Migrator.sol — MigratorFacet (Migrator.sol)
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/data-availability/RelayedSLDAValidator.sol — RelayedSLDAValidator
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/data-availability/RollupDAManager.sol — RollupDAManager
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/data-availability/ValidiumL1DAValidator.sol — ValidiumL1DAValidator
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/validators/MultisigCommitter.sol — MultisigCommitter
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/validators/PermissionlessValidator.sol — PermissionlessValidator
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/validators/ValidatorTimelock.sol — ValidatorTimelock
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/verifiers/ZKsyncOSVerifier.sol — ZKsyncOSVerifier
- [smart_contract] https://github.com/matter-labs/era-contracts/blob/e8e5d893b74363f9ef47bb139c06e78663ad17ed/l1-contracts/contracts/state-transition/verifiers/ZKsyncOSVerifierPlonk.sol — ZKsyncOSVerifierPlonk
- [smart_contract] https://zksync.io — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (13)

- [blockchain_dlt] Critical: Direct and publicly triggerable loss of funds
- [blockchain_dlt] High: Circuit, node, or program mismatches that make valid ZKsync OS executions unprovable and require verification key regeneration
- [blockchain_dlt] High: Underconstraints in the circuit that make invalid ZKsync OS executions provable
- [blockchain_dlt] Medium: Undocumented deviation from EVM behavior
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds (that cannot be fixed by upgrade)
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of funds (that can be fixed by upgrade)
- [smart_contract] High: Permanent stopping the priority queue
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [blockchain_dlt] Critical: maxReward=$100,000, minReward=$30,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: maxReward=$20,000, minReward=$10,000, rewardModel=range
- [blockchain_dlt] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [smart_contract] Critical: maxReward=$100,000, minReward=$50,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$25,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range

## Reward notes

For critical Blockchain/DLT bugs, the reward is dependent on the ratio between the funds at risk, which includes all affected projects on top of the respective blockchain/DLT, and the market cap according to the average between CoinMarketCap.com and CoinGecko.com, calculated at the time the bug report is submitted.

For critical Smart Contract bugs, the reward is 10% of the funds directly at risk, based on the PoC provided, with a minimum of USD 50,000 and a maximum of USD 100,000.

High and Medium rewards are set within the published range for the category according to the exploitability, impact and probability of the vulnerability, with special consideration given to reports that require multiple conditions not currently in place. High-severity Smart Contract rewards are additionally capped at 100% of the affected funds.

__Reward Payment Terms__

Payouts are handled by the ZKsync OS team directly and are denominated in **USD**. However, payments are done in **USDC** on **ZKsync Era**.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

The following ZKsync OS directories are out of scope because they are used for the Ethereum STF / Ethereum runner path, not the production ZKsync OS STF:

- `basic_bootloader/src/bootloader/transaction_flow/ethereum/`
- `basic_bootloader/src/bootloader/block_flow/ethereum/`
- `basic_system/src/system_implementation/ethereum_storage_model/`

Only behavior reachable in the production ZKsync OS STF, built with the `production` feature set, is in scope. Reports that only affect the Ethereum STF, Ethereum runner, test-only configurations, or non-production feature sets are out of scope unless the report also demonstrates the same impact in the production ZKsync OS STF.

Smart Contract assets:

- Any finding whose exploitation requires Gateway to be enabled and operating as a settlement layer is out of scope, since Gateway is not currently enabled and all chains settle directly to L1. This applies only to the Gateway precondition — the same code, when reachable by an L1-settling chain, stays in scope.
- Broken link hijacking is out of scope.
- Attacks requiring changing the verifier key.

Proving system:

- Prover implementations and their supporting code are out of scope: zksync-airbender `prover/`, `gpu_prover/`, `witness_eval_generator/`, `gpu_witness_eval_generator/`, `trace_holder/`, `worker/`, `fft/`, and the zksync-crypto-gpu crates (`shivini`, `proof-compression`, `zksync-gpu-prover`). A prover bug produces a proof that fails verification.
- Witness generation, benchmarking, fixtures, examples and test tooling, including `cs/src/cs/witness_placer/` and test files inside otherwise in-scope crates.
- CLI orchestration and setup-generation utilities (zksync-airbender `tools/cli/`, zkos-wrapper `wrapper/src/{interface,wrapper,gpu}/` and `main.rs`). These compute the verification key rather than determine it.
- Native SIMD implementations of the base field (`field/src/*avx*`, `field/src/*arm*`) that are not part of the RISC-V recursion binary.
- The Ethereum STF / Ethereum runner paths already listed above.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
