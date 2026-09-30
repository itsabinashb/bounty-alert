# Wormhole

- Page: https://immunefi.com/bug-bounty/wormhole/scope/
- Max bounty: $1,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (12)

- [blockchain_dlt] https://github.com/wormhole-foundation/wormhole/tree/main/node — Guardian Nodes
- [blockchain_dlt] https://github.com/wormhole-foundation/wormhole/tree/main/wormchain — Wormhole Gateway aka Wormchain
- [smart_contract] https://github.com/wormhole-foundation/native-token-transfers — Native Token Transfers
- [smart_contract] https://github.com/wormhole-foundation/wormhole-circle-integration — EVM, excluding the Circle Bridge
- [smart_contract] https://github.com/wormhole-foundation/wormhole/tree/main/algorand — Algorand
- [smart_contract] https://github.com/wormhole-foundation/wormhole/tree/main/aptos — Aptos
- [smart_contract] https://github.com/wormhole-foundation/wormhole/tree/main/cosmwasm — CosmWasm
- [smart_contract] https://github.com/wormhole-foundation/wormhole/tree/main/ethereum — Ethereum
- [smart_contract] https://github.com/wormhole-foundation/wormhole/tree/main/near — Near
- [smart_contract] https://github.com/wormhole-foundation/wormhole/tree/main/solana — Solana
- [smart_contract] https://github.com/wormhole-foundation/wormhole/tree/main/sui — Sui
- [smart_contract] https://wormhole.com/docs/build/reference/contract-addresses — Mainnet

## Asset notes

All Wormhole smart contracts can be found at https://github.com/wormhole-foundation. However, only those in the Assets in Scope table are considered in the bug bounty program's scope. In-scope items are those that are live on-chain or within an active Github release preparing for deployment.

## Impacts in scope (36)

- [blockchain_dlt] Critical: Any other vulnerabilities that lead to the impacts described in Tier 1-3
- [blockchain_dlt] Critical: Exploits resulting in the locking, loss, or theft of user funds from the Portal Token Bridge (locking only applies to non-upgradeable smart contracts)
- [blockchain_dlt] Critical: Forging of wormhole messages (i.e. VAAs) or circumventing VAA verification logic
- [blockchain_dlt] Critical: Gaining control of multiple Guardian nodes by exploiting a vulnerability that leads to Remote Code Execution.
- [blockchain_dlt] Critical: Theft of funds from exposure of production private keys of a quorum of Guardians
- [blockchain_dlt] Critical: Unauthorized changes to protocol parameters through governance resulting in direct loss of funds (i.e. spoofing Governance actions)
- [blockchain_dlt] High: Attacks that would be critical if a single Guardian were malicious.
- [blockchain_dlt] High: Bugs that allow forging of wormhole messages (i.e. VAAs) or circumventing VAA verification logic in the smart contracts but are outside of the “critical” category. For example, it is possible to spoof a VAA without being able to control the sender's address.
- [blockchain_dlt] High: Bugs that are very capital-intensive to carry out but could be critical
- [blockchain_dlt] High: Unrestricted bypass of rate limiters, including the Governor module (https://github.com/wormhole-foundation/wormhole/tree/main/node/pkg/governor])
- [blockchain_dlt] High: Unrestricted bypass of the Accountant (https://github.com/wormhole-foundation/wormhole/blob/main/whitepapers/0011_accountant.md)
- [blockchain_dlt] Medium: Attacks that would be critical if a super minority of Guardians were malicious, excluding denial of service vulnerabilities.
- [blockchain_dlt] Medium: Bugs that allow forging signed messages from a super-minority of Guardians
- [blockchain_dlt] Medium: Compromising a single guardian node
- [blockchain_dlt] Medium: Compromising a single guardian node
- [blockchain_dlt] Medium: Cryptographic implementation flaws and flaws in random number generation with limited impact
- [blockchain_dlt] Medium: Impacts of critical or high severity but require a feasible amount of Guardian or user interaction to exploit.
- [blockchain_dlt] Low: Attacks below Critical severity if a single Guardian were malicious
- [blockchain_dlt] Low: Bugs that are not currently exploitable but may become exploitable in future stages of development. This could refer to a configuration setting change or a likely code change causing a bug. The WH team determines the feasibility and likelihood of this.
- [blockchain_dlt] Low: Bugs that are unlikely to occur but would have a significant impact if so, e.g. race conditions
- [blockchain_dlt] Low: Denial of Service attacks against the Guardian network (excluding volumetric attacks) that would result in an extended (24 hours) degradation of performance
- [blockchain_dlt] Low: Unrestricted bypass of the Transfer Verifier (https://github.com/wormhole-foundation/wormhole/blob/main/whitepapers/0014_transfer_verifier.md)
- [smart_contract] Critical: Any other vulnerabilities that lead to the impacts described in Tier 1-3
- [smart_contract] Critical: Exploits resulting in the locking, loss, or theft of user funds from the Portal Token Bridge (locking only applies to non-upgradeable smart contracts)
- [smart_contract] Critical: Exposure of production private keys and/or other extremely sensitive information.
- [smart_contract] Critical: Forging of wormhole messages (i.e. VAAs) or circumventing VAA verification logic in the smart contracts
- [smart_contract] Critical: Governance manipulation
- [smart_contract] High: Attacks that would be critical if a minority of Guardians were malicious.
- [smart_contract] High: Bugs that allow the forging of wormhole messages (e.g., VAAs) or circumventing VAA verification logic in smart contracts are outside of the “critical” category.
- [smart_contract] High: Bugs that are very capital-intensive to carry out but could be critical
- [smart_contract] Medium: Bugs that allow forging signed messages from a minority of Guardians
- [smart_contract] Medium: Cryptographic implementation flaws and flaws in random number generation with limited impact
- [smart_contract] Medium: Exploit chains requiring user interaction
- [smart_contract] Low: Bugs that are likely to occur in future stages of development but do not manifest themselves yet
- [smart_contract] Low: Bugs that are unlikely to occur but would have a significant impact if so, e.g. race conditions
- [smart_contract] Low: Denial-of-service attacks against the Guardian network (excluding volumetric attacks) temporarily degrade performance.

## Impact notes

Bugs that are only triggerable against oneself and don’t affect other users, but are reasonable to be done on accident as an end user or application developer will be considered as no higher than low severity on a case-by-case basis. This excludes sending funds to unintended addresses which will not be rewarded.

For bugs related to a potential Governor bypass, this only applies to governed tokens (i.e. ungoverned tokens are deliberately ungoverned).

Native Token Transfer (NTT) is an open, flexible, and composable framework for transferring tokens across blockchains without liquidity pools. Only the listed GitHub repository is in the scope of this bounty program. Any forks or modifications are out of scope. Furthermore, only tagged releases with version v1.x.x and v2.x.x are considered in-scope. The severity of NTT-related findings will be dropped by a single category on the payout scale, such as a critical to a high or a medium to a low.

The IBC ICS20 token bridge is deprecated and thus out of scope. This includes the ICS20 IBC handling code in the Wormchain subdirectory, the ibc-translator CosmWasm smart contract, and anything else the team deems as part of this flow.

Any NFT Bridge or Cross Chain Queries (CCQ) reports are no-longer considered in-scope and will be closed.

Reports affecting Guardian software will be assessed using the program’s usual impact-based severity assessment. Reports affecting other in-scope off-chain components, including the Wormhole SDK, will generally receive a maximum severity rating of Medium.

## Rewards

- [blockchain_dlt] Critical: maxReward=$1,000,000, minReward=$100,000, rewardCalculationPercentage=0, rewardModel=range
- [blockchain_dlt] High: maxReward=$100,000, minReward=$10,000, rewardModel=range
- [blockchain_dlt] Medium: maxReward=$10,000, minReward=$2,000, rewardModel=range
- [blockchain_dlt] Low: maxReward=$1,000, rewardModel=up_to
- [smart_contract] Critical: maxReward=$1,000,000, minReward=$100,000, rewardCalculationPercentage=0, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$2,000, rewardModel=range
- [smart_contract] Low: maxReward=$1,000, rewardModel=up_to

## Reward notes

Please note that for any valid Critical severity reports, the maximum reward will be up to $1,000,000 USD, paid in W token, with the following tiers: 

- __Tier 1:__ Ability to Extract the TVL of all chains: Up to $1,000,000 in W
- __Tier 2:__ Ability to Extract the TVL of a single chain: Up to $500,000 in W 
- __Tier 3:__ Ability to permanently deny access to the TVL of one or many chains: Up to $250,000 in W 

All rewards are decided on a case-by-case basis, taking into account the bug's exploitability, the feasibility of the exploit scenario, the impact it causes, and the likelihood of the vulnerability presenting itself, particularly if it is nondeterministic or some of the conditions are not present at the time.

Because of the Governor, rewards for critical vulnerabilities in the Wrapped Token Bridge are further capped at 10% of extractable value during a 24-hour period. The Governor (https://github.com/wormhole-foundation/wormhole/tree/main/node/pkg/governor) is designed to limit the value that can be transferred out of one chain over time. Rewards for vulnerabilities resulting in the perpetual locking of funds are further capped at the lesser of 1% of destroyable value or $250,000 in W (where perpetual can only apply to non-upgradeable smart contracts).

Value is calculated based on the current market value and available liquidity for widely used tokens in the Portal Token Bridge, such as ETH and SOL. 

In cases where the report achieves more than one of the above objectives, rewards will be tiered to the higher of the two objectives and will not be aggregated (e.g., if you can extract and brick a complete TVL for a chain, you will be awarded a bounty as if you could only extract the complete TVL for that chain).

Rewards for bugs in dependencies and third-party code are at the discretion of the Wormhole team and will be based on the impact demonstrated on Wormhole. If the dependency has its own bug bounty program, your reward for submitting this vulnerability to Wormhole will be lowered by the expected payout of that other program. If the vulnerability is in a connected blockchain rather than the Wormhole code, the locked and wrapped assets on that chain are not included in the impact calculation.

Vulnerabilities known to the Wormhole team at the time of reporting are ineligible for reward. This includes external audit reports, vulnerabilities in Wormhole's dependencies that have been disclosed publicly, and internal company communications. If necessary, the program will provide proof of prior knowledge about the issue. Reports that copy public vulnerability disclosures, or reports that highlight patch gaps between Wormhole's forked repositories and their upstream codebases, are not eligible for a reward.

Wormhole Foundation will maintain full discretion on vulnerability payouts. We encourage bug reporters to submit issues outside of the above-mentioned payout structure, though we want to be clear that we’ll exercise discretion on a case-by-case basis regarding whether an issue warrants a payout and what that ultimate payout would be.

## Out of scope (program-specific)

The following vulnerabilities are excluded from the rewards for this bug bounty program:

  - Vulnerabilities that have been exploited, leading to damage.     
  - Network denial of service on Guardians is not eligible for bug bounty rewards.
  - Wormhole is an open source project with open development. We welcome feedback and PRs on features that are in development. Code that has not been deployed in production is generally out-of-scope.
  - Reports regarding bugs that the Wormhole project was previously aware of are not eligible for a reward.
  - In-scope assets with a "pre-release" tag are exempt from the above-mentioned deployed requirement and are aimed at allowing early access for white-hat community contribution. Once the chain is deployed in the mainnet, the new scope is whatever is deployed on the chain, which is often what is present in the main branch. Rewards for “pre-release” candidates will be eligible within the same reward structure as mainnet contracts.

The following person(s) are ineligible to receive bug bounty payout rewards: Staff, Auditors, Contractors, persons possessing privileged information, and all associated parties.

__Prohibited Activities__

  - Any testing with mainnet or public testnets; all testing should be done on private nets.
  - Public disclosure of a vulnerability before an embargo has been lifted. Wormhole follows the category 3 requirements for Immunefi Disclosure, requiring all public disclosure of valid bugs to be approved for publication.
  - Any testing with third-party smart contracts or infrastructure and websites.
  - Attempting phishing or other social engineering attacks against our employees and/or customers.
  - Any denial of service attacks.
  - Violating the privacy of any organization or individual.
  - Automated testing of services that generate significant amounts of traffic.
  - Any activity that violates any law or disrupts or compromises any data or property that is not yours.

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
