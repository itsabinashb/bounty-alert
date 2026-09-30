# Attackathon | Ethereum Protocol

- Page: https://immunefi.com/bug-bounty/ethereum-protocol-attackathon/scope/
- Max bounty: $1,500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Blockchain/DLT
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, blockchain_dlt - low, blockchain_dlt - medium, blockchain_dlt - high, blockchain_dlt - critical
- End date: 2025-01-25T14:00:00.000Z

## Assets in scope (18)

- [blockchain_dlt] https://github.com/Consensys/teku — Teku - [350k]
- [blockchain_dlt] https://github.com/NethermindEth/nethermind — Nethermind - [250k]
- [blockchain_dlt] https://github.com/chainsafe/lodestar — Lodestar - [100k]
- [blockchain_dlt] https://github.com/ethereum/consensus-specs — Specification - Consensus Specification
- [blockchain_dlt] https://github.com/ethereum/consensus-specs/blob/dev/specs/phase0/deposit-contract.md — Specification - Deposit Contract Specification
- [blockchain_dlt] https://github.com/ethereum/execution-specs — Specification - Execution Specification
- [blockchain_dlt] https://github.com/ethereum/go-ethereum — Go Ethereum - [200k]
- [blockchain_dlt] https://github.com/hyperledger/besu — Besu - [100k]
- [blockchain_dlt] https://github.com/ledgerwatch/erigon — Erigon - [350k]
- [blockchain_dlt] https://github.com/paradigmxyz/reth — Reth - [150k]
- [blockchain_dlt] https://github.com/prysmaticlabs/prysm — Prysm - [400k]
- [blockchain_dlt] https://github.com/sigp/lighthouse — Lighthouse - [200k]
- [blockchain_dlt] https://github.com/status-im/nimbus-eth2 — Nimbus Eth2 - [100k]
- [blockchain_dlt] https://immunefi.com — Primacy of Impact [Critical, High] (primacy of impact)
- [smart_contract] https://etherscan.io/address/0x00000000219ab540356cBB839Cbe05303d7705Fa#code — DepositContract.sol - [110]
- [smart_contract] https://github.com/ethereum/solidity — Solidity Compiler - [124k]
- [smart_contract] https://github.com/vyperlang/vyper — Vyper - [19k]
- [smart_contract] https://immunefi.com — Primacy of Impact [Critical] (primacy of impact)

## Asset notes

__KYC Requirement__

Immunefi will be requesting KYC information in order to pay for successful bug submissions to whitehats who earn $500 USD or more. The following information will be required:
- Full name 
- Date of birth
- Proof of address (either a redacted bank statement with address or a recent utility bill)
- Copy of Passport or other Government issued ID

__Eligibility Criteria__ 

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- From a restricted country or territory: North Korea, Iran, Cuba, Syria, certain regions of Ukraine (Crimea, Donetsk and Luhansk), West Bank and Gaza regions of Israel, Venezuela, Afghanistan
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review, or who work for the company which did the audit review
- Employees and contractors of the Ethereum Foundation may participate in the program only in the accrual of points and will not receive monetary rewards. Client teams may participate in finding vulnerabilities in other client team’s projects, however employees and contractors of individual client teams who self report vulnerabilities will only result in accrual of points and will not receive monetary rewards

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed or disclosed to Immunefi, are valid for a reward at one severity lower than what they’re confirmed as. However, bug reports that are private known issues do not unlock reward pool tiers. For example, a High bug that ended up being a private known issue, would be paid as a Medium and would not qualify for unlocking the $500k tier of the reward pool for this Attackathon.

__Primacy of Impact vs Primacy of Rules__

Ethereum Foundation adheres to the Primacy of Impact for the following impacts:
- Blockchain/DLT - Critical
- Blockchain/DLT - High
- Smart Contract - Critical

Primacy of Impact means that the impact is prioritized rather than a specific asset. This encourages security researchers to report on all bugs with an in-scope impact, even if the affected assets are not in scope. For more information, please see [Best Practices: Primacy of Impact](https://immunefisupport.zendesk.com/hc/en-us/articles/12340245635089-Best-Practices-Primacy-of-Impact).

When submitting a report on Immunefi’s dashboard, the security researcher should select the Primacy of Impact asset placeholder. If the team behind this project has multiple programs, those other programs are not covered under Primacy of Impact for this program. Instead, check if those other projects have a bug bounty program on Immunefi.

If the project has any testnet and/or mock files, those will not be covered under Primacy of Impact.

All other impacts are considered under the Primacy of Rules, which means that they are bound by the terms and conditions set within this program.

__Responsible Publication__

After the Attackathon concludes, whitehats may only publish more info on the fixed and paid bug reports that appear on the [Immunefi Audit Competitions Gitbook](https://reports.immunefi.com). Reports closed as invalid are also okay to publish after this time. This rule is to prevent premature publication of any bugs that will take considerable time to fix. 

Immunefi will also publish a leaderboard of the participants and their earnings.

__Feasibility Limitations__

The project may receive reports that are valid (the bug and attack vector are real) and that cite assets and impacts in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Ethereum has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/9522048467857-Immunefi-Standard-Badge).

## Impacts in scope (29)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] Critical: Unintended permanent chain split affecting greater than or equal to 25% of the network, requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Shutdown of greater than or equal to 33% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] High: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments affecting greater than or equal to 25% of the network
- [blockchain_dlt] Medium: Causing greater than or equal to 25% of network processing nodes to process transactions from the mempool beyond set parameters (e.g. prevents processing transactions from the mempool)
- [blockchain_dlt] Medium: Increasing greater than or equal to 25% of network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 10% or equal to but less than 33% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Medium: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments affecting less than 25% of the network
- [blockchain_dlt] Medium: Unintended chain split affecting greater than or equal to 25% of the network (Network partition)
- [blockchain_dlt] Medium: bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Low: (Specifications) A bug in specifications with no direct impact on client implementations
- [blockchain_dlt] Low: Causing less than 25% of network processing nodes to process transactions from the mempool beyond set parameters (e.g. prevents processing transactions from the mempool)
- [blockchain_dlt] Low: Increasing less than 25% of network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of less than 10% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Low: Unintended chain split affecting less than 25% of the network (Network partition)
- [smart_contract] Critical: (Compiler) Elimination of security checks
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: (Compiler) Incorrect bytecode generation leading to incorrect behavior
- [smart_contract] Medium: (Compiler) Encoding errors
- [smart_contract] Medium: (Compiler) Memory-Related errors
- [smart_contract] Low: (Compiler) Exception handling errors
- [smart_contract] Low: (Compiler) Optimization errors
- [smart_contract] Low: (Compiler) Semantic analysis errors
- [smart_contract] Low: (Compiler) Syntactic analysis errors
- [smart_contract] Low: (Compiler) Unexpected behavior

## Impact notes

Each asset in scope listed above points to the latest changes which is the source of truth of what’s in scope.

If a bug in the specifications results in an impact on client implementations, the relevant impact should be selected from the Blockchain/DLT impacts list. If an impact of the specification bug cannot be identified, you are encouraged to submit it under the Low severity “A bug in specifications with no direct impact on client implementations”, at which point it will be evaluated and may have its severity increased at the discretion of the Ethereum Foundation.

For compiler impacts, only those issues which affect runtime logic will be considered as in scope. If a bug is the result of an anti-pattern of the language, enabling experimental features, or use of inline assembly, it may be downgraded or considered out of scope. If there are no affected applications, a vulnerability may be downgraded due to feasibility limitations of exploitability. Compiler bugs should be tested against the latest release version. Bugs which are not known issues which impact previous versions may be considered if an on-chain impact can be demonstrated.

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

__Whitehat Educational Resources & Technical Info Architecture documents:__

Consensus client diversity will be calculated as an average of the following three data sources provided in https://clientdiversity.org/
- Sigma Prime's Blockprint
- Miga Labs
- Rated.Network

Execution client diversity will be calculated as an average of the following three data sources:
- [https://clientdiversity.org/](https://clientdiversity.org/)
- [https://ethernodes.org/](https://ethernodes.org/)
- [https://explorer.rated.network/network?network=mainnet&timeWindow=1d&rewardsMetric=average&geoDistType=all&hostDistType=all&soloProDist=stake](https://explorer.rated.network/network?network=mainnet&timeWindow=1d&rewardsMetric=average&geoDistType=all&hostDistType=all&soloProDist=stake)

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

The Ethereum Protocol is in scope, however, only the clients and codebases which are listed in the assets table above qualify for this program. The specifications of the consensus layer and execution layer are in scope, please see the following resource to understand how to find and report a bug in the specification documents.

__Where do you suspect there may be bugs? Useful aspects of this question are:__

- **Which parts of the code are you most concerned about?**
    - We are most concerned about code related to consensus, validators, cryptography, networking (libp2p, devp2p)
     - Bugs concerning the following mechanisms:
        - beacon-chain.md files: Any bugs that may cause the beacon chain to stop or consensus failure.
        - fork-choice.md files: This logic is likely the most complicated and requires a more sophisticated attack vector or fuzzing to detect potential bugs. Note that there are some known but too costly attacks. For example, accountable safety guarantees that no conflicting finalization can happen without 1/3 of the validator set being flashable.
        - p2p-interface.md files: These docs are primarily written in English words instead of executable and tested Python code. Networking experts can refer to these documents to find DOS attack vectors.
    - Bugs are mostly found in typing issues, such as:
        - Receiving a U256 instance in a variable expecting a Uint
        - Getting a Bytes20 in a Bytes slot
    - Edge case behavior that deviates from "true" Ethereum can also cause issues, including:
        - Opcode behavior at extremes (e.g., blockhash at 255/256 depth)
        - Precompiles decoding their arguments differently
    - Cryptography is a complex area where ensuring that libraries are correctly implemented and match mainnet behavior is crucial.
    - Discrepancies between the optimized and non-optimized modules may also be a valuable source of bugs.

- **What attack vectors are you most concerned about? Which part(s) of the system do you want whitehats to attempt to break the most?**
    - Specifically for the specifications:
        - Incorrect behavior is biggest attack vector, eg. What happens if a theoretical new Ethereum client follows the specification to the letter?
        - We are interested in cases when the chosen algorithm may not be suitable for a production client, or when simplifying assumptions (e.g., no re-orgs) are impractical in real-world scenarios.

- **Are there any assumed invariants that you want whitehats to attempt to break?**
    - We use many Python assertions (`assert`) to explicitly indicate the invariants in the markdown files.
    - We use [SSZ typing](https://github.com/ethereum/consensus-specs/blob/dev/ssz/simple-serialize.md) to determine the domain of variables.

__What external dependencies are there?__

- A functioning Ethereum execution client (geth, reth, etc.) to provide blocks
- [https://github.com/ethereum/execution-specs/blob/1e9a6e518adab7ae55ebddb15d72f91041240c8a/setup.cfg#L113-L117](https://github.com/ethereum/execution-specs/blob/1e9a6e518adab7ae55ebddb15d72f91041240c8a/setup.cfg#L113-L117)
- [https://github.com/ethereum/execution-specs/blob/1e9a6e518adab7ae55ebddb15d72f91041240c8a/setup.cfg#L152-L180](https://github.com/ethereum/execution-specs/blob/1e9a6e518adab7ae55ebddb15d72f91041240c8a/setup.cfg#L152-L180)

__Where might whitehats confuse out-of-scope code to be in-scope?__

- `docc` and its plugins are completely out of scope.
- Anything under src/ethereum_spec_tools is likely out of scope, but bug reports are still appreciated.
- Attacks that require manually making the JSON-RPC publicly available are not in scope for the execution layer or consensus layer. It is known that there are multiple attack vectors (DDoS) and it is not intended to make it public unless multiple layers of protection are in place.
- The JSON RPC is out of scope. Users are told not to expose the JSON RPC to the public as they are a well known attack vector.

__Are there any unusual points about your protocol that may confuse whitehats?__

- For the specifications, correctness and readability trump everything else, including performance.
- We use int64 FAR FUTURE EPOCH: 2**64 - 1 as a stab of the epoch time that is unlikely to reach. When testing the variables' bounds, we should consider the probability of occurrence when determining the impact.
- The Electra specs and “features” specs (under https://github.com/ethereum/consensus-specs/tree/dev/specs/_features folder) are still in development, so they are not in the scope.
- The deposit contract only accepts deposits. To withdraw funds, a validator must exit their node or do work. Learn more here.
- We use Python SSZ implementation [remerkleable](https://github.com/protolambda/remerkleable) a lot in pyspec. The bugs caused by remerkleable are not considered in scope as pyspec itself is not a product. Bugs must be considered in the context of client implementations.

__What is the test suite setup information?__

Please see each respective node software’s documentation regarding test suite setup.

__What qualifies as a hard fork of the network?__

A hard fork is the case when a potential attack’s damage is proven to be irreversible, and the only possible fix is splitting the network on a hard fork. It is a radical change to a network’s protocol that makes previously invalid blocks and transactions valid, or vice-versa. This means nodes (clients) that do not update to the new protocol will no longer be able to participate in or validate the same blockchain as the updated nodes.

If a hard fork is required for the uncle chain to fix consensus for those clients and continue building on the canonical chain, it does not qualify as critical, as the canonical chain remains unchanged and does not require a hard fork. The issue caused should have the downstream effect of clients needing to deploy patches to continue building blocks on the canonical chain.

__Previous Audits & Public Disclosure of Known Issues__

Bug reports covering previously discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

Ethereum’s completed audit reports can be found at [https://github.com/ethereum/public-disclosures](https://github.com/ethereum/public-disclosures). Any unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

There may be other findings tracked in these repositories’ GitHub issues which are not exhaustively listed here. Whitehat’s are responsible for ensuring a vulnerability is not publicly disclosed in the respective clients [known issues list or any previous audits](https://immunefi.slite.com/app/docs/npGhR5rBwFfnTi).

For reports related to the Solidity Compiler, rewards will not be issued for crashes of the solc compiler on maliciously generated data.

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Ethereum Attackathon Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/30287460669841-Ethereum-Protocol-Attackathon-Reward-Terms).

The reward pool size varies based on the severity of bugs found:
- If one or more Low severity bugs are found the reward pool will be **$250,000 USD**
- If one or more Medium severity bugs are found the reward pool will be **$500,000 USD**
- If one or more High severity bugs are found the reward pool will be **$900,000 USD**
- If one or more Critical severity bugs are found the reward pool will be **$1,500,000 USD**

Private known issues are considered valid.

**Duplicates are not valid for this Attackathon.**

Private known issues will unlock higher reward pools as though they were one severity level lower. For example, a Critical severity bug which was a private known issue would unlock the  reward pool conditional on a High severity bug being found.

The severity level of private known issues remains unchanged and SRs earn their portion of the reward pool and position on the leaderboard according to this unchanged severity level.

Public known issues are invalid as normal.

Rewards are distributed according to the impact of the vulnerability based on the Immunefi [Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/).

__Reward Payment Terms__

Payouts are handled by the Immunefi team directly and are denominated in USD. However, payments are done in ETH

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

- The "Insight" severity was introduced on Audit Competition & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi).

## Out of scope (program-specific)

Only the targets which directly affect the Ethereum network are part of the Ethereum Protocol Attackathon. This means that for example our infrastructure; such as webpages, dns, email etc, are not part of the bounty-scope. ERC20 contract bugs are typically not included in the bounty scope. However, we can help reach out to affected parties, such as authors or exchanges in such cases. ENS is maintained by the ENS foundation, and is not part of the bounty scope. Vulnerabilities requiring the user to have publicly exposed an API, such as JSON-RPC or the Beacon API, is out of scope of the bug bounty program.

These impacts are out of scope for this bug bounty program. 

- Impacts on Example Code provided by Ethereum or smart contract code that was deployed by the user.

Blockchain/DLT Specific:

- Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks

## Out of scope and rules

To be determined.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
