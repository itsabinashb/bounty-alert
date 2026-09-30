# Hathor Network

- Page: https://immunefi.com/bug-bounty/hathornetwork/scope/
- Max bounty: $20,000
- KYC required: yes
- Paused: yes
- Invite only: no
- Program type: Websites and Applications, Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - low, websites_and_applications - critical
- End date: (none)

## Assets in scope (5)

- [blockchain_dlt] https://github.com/HathorNetwork/hathor-core — Blockchain/DLT
- [websites_and_applications] https://github.com/HathorNetwork/hathor-wallet — Desktop wallet
- [websites_and_applications] https://github.com/HathorNetwork/hathor-wallet-headless — Headless wallet
- [websites_and_applications] https://github.com/HathorNetwork/hathor-wallet-lib — wallet-lib
- [websites_and_applications] https://github.com/HathorNetwork/hathor-wallet-mobile — Mobile wallet

## Asset notes

Only the latest release is in scope for Blockchain/DLT and Web/App assets. You can access the latest release for a repository by adding "releases/latest" to the end of a repository's URL.

Never run tests on Hathor's production environments such as the mainnet. If you believe your attack would only work in our production environment, get in touch with us at security@hathor.network. 

All config and test files are considered as out-of-scope of this bug bounty program. 

hathor-core/hathor/wallet is out-of-scope.  [https://github.com/HathorNetwork/hathor-core/tree/master/hathor/wallet](https://github.com/HathorNetwork/hathor-core/tree/master/hathor/wallet)

Nano Contracts have been launched in a controlled rollout. It currently does not have fees or proper sandboxing. For that reason, users cannot freely send contracts (blueprints, the code that runs nano contracts) to the network. Everything is reviewed by Hathor Labs before being added to the network. Therefore, reports such as unbounded loops or unmetered resources are not valid for nano contracts. Nano contracts code is here: [https://github.com/HathorNetwork/hathor-core/tree/master/hathor/nanocontracts](https://github.com/HathorNetwork/hathor-core/tree/master/hathor/nanocontracts)

All code of Hathor Network can be found at [https://github.com/HathorNetwork.](https://github.com/HathorNetwork) However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

Documentation and instruction for PoC can be found here:
- [https://hathor.gitbook.io/hathor/](https://hathor.gitbook.io/hathor/)
- [https://github.com/HathorNetwork/rfcs/blob/master/text/0033-private-network-guide.md](https://github.com/HathorNetwork/rfcs/blob/master/text/0033-private-network-guide.md)

## Impacts in scope (9)

- [blockchain_dlt] Critical: Creation of tokens, including HTR, without following blockchain and consensus rules
- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] High: Unintended chain split (network partition)
- [blockchain_dlt] Low: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [websites_and_applications] Critical: Direct theft of user NFTs
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands

## Impact notes

(none)

## Rewards

- [blockchain_dlt] Critical: maxReward=$20,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: fixedReward=$10,000, rewardModel=fixed
- [blockchain_dlt] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$10,000, otherImpactMaxReward=$0, rewardModel=fixed

## Reward notes

All Blockchain/DLT and Web/App bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. Bug reports are required to include a runnable PoC in order to prove impact. Exceptions may be made in cases where the vulnerability is objectively evident from simply mentioning the vulnerability and where it exists. However, the bug reporter may be required to provide a PoC at any point in time.

Hathor Labs requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed is a government ID and proof of address.

Unlike other bug bounty programs on Immunefi, all bug report submissions, including associated vulnerabilities, become the exclusive property of Hathor Labs. By making a submission to this program and in consideration for a bounty, the bug submitter conveys all ownership rights, titles, and interests in the bug report to Hathor Labs. Thus, the final decision on whether a postmortem will be written is at the sole discretion of Hathor Labs.

Payouts are handled by the __Hathor Labs__ team directly and are denominated in USD. However, payouts are done in __HTR__.

## Out of scope (program-specific)

Attacks that cost significantly more to execute than their expected payoff will not be eligible for rewards. For example, mining a block on the network is expensive due to the high hash rate. If an attack relies on producing a block but offers no financial benefit to the attacker, it will not be eligible to rewards.

To further clarify, one specific attack under this category is requiring a mined block to cause an error that crashes a full node.

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
