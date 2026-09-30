# Serai

- Page: https://immunefi.com/bug-bounty/serai/scope/
- Max bounty: $30,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - low
- End date: (none)

## Assets in scope (11)

- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/ciphersuite — ciphersuite
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/dalek-ff-group — dalek-ff-group
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/dkg/musig — dkg-musig
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/dkg/src — dkg
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/frost — modular-frost
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/multiexp — multiexp
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/schnorr — schnorr-signatures
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/schnorrkel — frost-schnorrkel
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/crypto/transcript — flexible-transcript
- [blockchain_dlt] https://github.com/serai-dex/serai/tree/develop/networks/bitcoin — bitcoin-serai
- [blockchain_dlt] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (9)

- [blockchain_dlt] Critical: Ability to forge proofs
- [blockchain_dlt] Critical: Reportedly received funds which weren’t actually received/spendable
- [blockchain_dlt] Critical: Signing of unintended messages
- [blockchain_dlt] Critical: Unintended, undocumented recovery of private spend keys (or private spend key shares)
- [blockchain_dlt] High: Incorrect/incomplete (in the academic sense) cryptographic formulae within a verifier's callstack
- [blockchain_dlt] Medium: Undocumented transcript collision
- [blockchain_dlt] Low: Incorrect/incomplete (in the academic sense) cryptographic formulae within a prover's callstack
- [blockchain_dlt] Low: Non-constant time implementation with regards to secret data
- [blockchain_dlt] Low: Undocumented panic reachable from a public API

## Impact notes

(none)

## Rewards

- [blockchain_dlt] Critical: fixedReward=$30,000, rewardCalculationPercentage=10, rewardModel=fixed
- [blockchain_dlt] High: fixedReward=$5,000, rewardModel=fixed
- [blockchain_dlt] Medium: fixedReward=$1,000, rewardModel=fixed
- [blockchain_dlt] Low: fixedReward=$250, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Overtime Attack Limitations__

In cases of attacks executed over time for smart contract and blockchain/DLT bugs, an explicit two hour window without human intervention is provided, starting from the first erroneous or malicious action. Only achievements during this window will be counted, regardless of further impact.

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs acknowledged below are not eligible for any reward through the bug bounty program. 
- [https://github.com/serai-dex/serai/issues](https://github.com/serai-dex/serai/issues)
- [https://github.com/serai-dex/serai/tree/develop/audits](https://github.com/serai-dex/serai/tree/develop/audits)

__Previous Audits__

Serai has provided these completed audit review reports for reference. Any unfixed vulnerability mentioned in these reports are not eligible for a reward.
- [https://github.com/serai-dex/serai/blob/develop/audits/Cypher%20Stack%20crypto%20March%202023/Audit.pdf](https://github.com/serai-dex/serai/blob/develop/audits/Cypher%20Stack%20crypto%20March%202023/Audit.pdf)

__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Blockchain/DLT - Critical

In addition, PoC will be required for the following low impact:
- Undocumented panic reachable from a public API

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules) Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

Payouts are handled by the Serai team directly and are denominated in USD. However, payments are done in USDC.

__ Exclusion with monero-oxide __

For submissions mutual to Serai DEX and monero-oxide, both programs should be submitted to yet only one will issue a reward (of the submitter's choice).

## Out of scope (program-specific)

- Attacks breaking BFT assumptions
- Best practice critiques
- Signature production by the threshold
- Attacks reliant on attacking an out of scope communication protocol between library users
- Invalid circumstances reachable by providing invalid hashes/curves/ciphersuites/algorithms/etc
- Attacks on the cross-group discrete logarithm proof, marked experimental
- Vulnerabilities/issues in tests/code explicitly for tests
- Bugs only reachable via unsafe code

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
