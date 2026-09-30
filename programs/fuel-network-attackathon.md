# Attackathon | Fuel Network

- Page: https://immunefi.com/bug-bounty/fuel-network-attackathon/scope/
- Max bounty: $1,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Smart Contract, Websites and Applications
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium
- End date: 2024-07-29T08:00:00.000Z

## Assets in scope (13)

- [blockchain_dlt] https://github.com/FuelLabs/fuel-core/tree/v0.31.0 — fuel-core :: The blockchain client for the L2
- [blockchain_dlt] https://github.com/FuelLabs/fuel-vm/tree/v0.55.0 — fuel-vm :: The fuelvm and the low level shared libraries with Fuel (ie. tx types, assembly code, etc)
- [blockchain_dlt] https://github.com/FuelLabs/fuels-ts/tree/v0.91.0 — fuel-ts :: The typescript sdk which interacts with the blockchain client and compiler
- [blockchain_dlt] https://github.com/fuellabs/fuels-rs/tree/d3ac1d3f8910cc12c662ccbe5ff51d9e9354ed1a — fuel-rs :: The rust sdk which interacts with the blockchain client and compiler
- [smart_contract] https://github.com/FuelLabs/fuel-bridge/tree/e3e673e31f9e72d757d68979bb6796a0b7f9c8bc/packages/fungible-token — fungible-token :: The L2 contract on fuel which verifies the deposit receiver and mints the actual tokens
- [smart_contract] https://github.com/FuelLabs/fuel-bridge/tree/e3e673e31f9e72d757d68979bb6796a0b7f9c8bc/packages/message-predicates — message-predicates :: The L2 deposit receiver which enables minting of funds on Fuel from the bridge
- [smart_contract] https://github.com/FuelLabs/fuel-bridge/tree/e3e673e31f9e72d757d68979bb6796a0b7f9c8bc/packages/solidity-contracts — solidity-contracts :: The L1 contracts for the Fuel bridge that handle deposits and withdrawals on Ethereum
- [smart_contract] https://github.com/FuelLabs/sway-libs/tree/0f47d33d6e5da25f782fc117d4be15b7b12d291b — sway-libs :: Common Sway libraries
- [smart_contract] https://github.com/FuelLabs/sway-standards/tree/v0.5.1 — sway-standards
- [smart_contract] https://github.com/FuelLabs/sway/tree/v0.61.2 — sway :: The sway compiler and most Sway tooling (ie. forc, standard library, etc)  *Note: Only the fuelvm target is in scope. The evm and midenVM target are out of scope
- [websites_and_applications] https://github.com/FuelLabs/fuel-connectors/tree/v0.8.1 — fuel-connectors :: Web2 library that enables apps to connect to fuel supported wallets
- [websites_and_applications] https://github.com/FuelLabs/fuels-wallet/tree/v0.22.0 — fuel-wallet :: Web2 Fuel Wallet extension that allows users to interact with fuel network and stores the private keys / seed phrase of the user
- [websites_and_applications] https://github.com/fuellabs/fuel-explorer/tree/3af2f6dd3dea07ed071858b07378fba1c24d2f77 — fuel-explorer :: Web2 bridge and explorer UI, that allows users to bridge funds from sepolia to the Fuel Network and also visualize the transactions of the network

## Asset notes

**Fuel's changelog per repo at the end of the code update period is:**
- Fuel Bridge : https://github.com/FuelLabs/fuel-bridge/commit/e3e673e31f9e72d757d68979bb6796a0b7f9c8bc 
- sway : https://github.com/FuelLabs/sway/releases/tag/v0.61.2
- sway-libs : Unchanged
- sway-standards : https://github.com/FuelLabs/sway-standards/releases/tag/v0.5.1
- fuel-core : https://github.com/FuelLabs/fuel-core/blob/2faae02d57be88d271893c822c781f34e5f445bc/CHANGELOG.md#version-0310
- fuel-vm : https://github.com/FuelLabs/fuel-vm/blob/2604237c9ff4a755e48b40b2c006711d22cff19f/CHANGELOG.md#version-0550
- fuel-ts : https://github.com/FuelLabs/fuels-ts/releases/tag/v0.91.0 
- fuel-rs : Unchanged
- fuel-connectors: https://github.com/FuelLabs/fuel-connectors/releases/tag/v0.8.1 
- fuel-wallet : https://github.com/FuelLabs/fuels-wallet/releases/tag/v0.22.0
- fuel-explorer : Unchanged

Additional Known Issues have also been added to the section 'Post Code Update Period Known Issues'. When these issues are fixed they will no longer be considerd known issues and the code will be brought back into scope to find bugs in the fixes. All intended fixes are included in the 'Known Issues' section.


Fuel Network’s codebase can be found here https://github.com/FuelLabs/ . Each asset in scope listed above is of a given hash which is the source of truth of what’s in scope.

Fuel Network will strive to have the Testnet match their Github assets. In cases where they differ, the links in the assets in-scope table will be the source-of-truth as to what’s in-scope. 

**Out of Scope Assets:**
- Only the fuelvm target is in scope for the asset: https://github.com/FuelLabs/sway/tree/7b56ec734d4a4fda550313d448f7f20dba818b59 . The evm and midenVM target are out of scope
- Any smart contract with text stating that THIS CONTRACT IS DEPRECATED is out of scope.
- FuelERC721Gateway contracts are also out of scope because they are pending development of a new version.

**The Testnet deployment can be found here:**

- FuelChainState - https://sepolia.etherscan.io/address/0x404F391F96798B14C5e99BBB4a9C858da9Cf63b5 
- Fuel Message Portal - https://sepolia.etherscan.io/address/0x01855B78C1f8868DE70e84507ec735983bf262dA 
- FuelERC20GatewayV4 - https://sepolia.etherscan.io/address/0xa97200022c7aDb1b15f0f61f374E3A0c90e2Efa0


**Previous Audits & Public Disclosure of Known Issues**

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

Fuel Network’s completed audit reports can be found at https://github.com/FuelLabs/audits . Any unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

**Post Code Update Period Known Issues:**
- P2P is doing a lot of database lookups - https://github.com/FuelLabs/fuel-core/issues/2023
- Sequential opcodes return an error when touching the last storage key - https://github.com/FuelLabs/fuel-core/issues/2022
- Unlimited spamming of TxPool - https://github.com/FuelLabs/fuel-core/issues/2021
- Transaction pool can be manipulated to do a lot of cleanups - https://github.com/FuelLabs/fuel-core/issues/2020
- The block production should take into account the available number of transactions - https://github.com/FuelLabs/fuel-core/issues/2019
- During block production should modify the block after passing all checks - https://github.com/FuelLabs/fuel-core/issues/2018
- Slow GraphQL request sender can drain resources of the node - https://github.com/FuelLabs/fuel-core/issues/2017
- WDCM and WQCM implementation mismatch with the specification - https://github.com/FuelLabs/fuel-vm/issues/791

The following fixes will be deployed for the above known issues, at which point they'll no longer be known issues and will be brough back into scope to find bugs in again:
- Optimize getting of transactions for blocks during network synchronization to decrease the load from p2p service.
- Fix for the edge case for sequential opcodes to not return an error when the last key of operation is still in the range.
- Handled the gas price and number of available transactions during the selection of the transaction in the TxPool.
- Updated the executor's block production logic to modify the block only after transaction is valid.
- Added increasing the base gas price based on the demand.
- Optimize SMT updates within the transactions execution.
- Fix 'WDCM' and `WQCM` to match the specification.

**Miscellaneous issues:**

- https://github.com/FuelLabs/fuels-rs/issues/1361
- https://github.com/FuelLabs/sway/issues/6060
- https://github.com/FuelLabs/sway-playground/issues/56
- https://github.com/FuelLabs/sway/issues/5727
- https://github.com/FuelLabs/fuels-wallet/issues/1322
- https://github.com/FuelLabs/fuels-ts/issues/2443
- https://github.com/FuelLabs/sway/issues/6091
- https://github.com/FuelLabs/fuels-ts/issues/2492
- https://github.com/FuelLabs/sway/issues/6118
- https://github.com/FuelLabs/fuel-explorer/issues/366
- https://github.com/FuelLabs/sway/issues/418
- https://github.com/FuelLabs/sway/issues/5892
- https://github.com/FuelLabs/sway/issues/5124
- https://github.com/FuelLabs/sway/issues/15
- https://github.com/FuelLabs/sway/issues/5886
- https://github.com/FuelLabs/sway/issues/5049 
- https://github.com/FuelLabs/fuel-core/issues/1961
- https://github.com/FuelLabs/fuel-core/issues/1966
- https://github.com/FuelLabs/fuel-core/issues/1967
- https://github.com/FuelLabs/fuel-core/issues/1049
- https://github.com/FuelLabs/fuel-core/issues/1968
- https://github.com/FuelLabs/fuel-core/issues/1969
- https://github.com/FuelLabs/fuel-core/issues/1970
- https://github.com/FuelLabs/fuel-core/issues/1971
- https://github.com/FuelLabs/fuel-vm/issues/764
- https://github.com/FuelLabs/fuel-vm/issues/757

There may be other low severity findings tracked in these repos github issues which are not exhaustively listed here. You can check for publicly described issues on GitHub before sending the submission by using keywords from the finding.

## Asset In Scope Policies

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

**Primacy of Impact vs Primacy of Rules**

Fuel Network adheres to the Primacy of Rules, which means that the whole Attackathon is run strictly under the terms and conditions stated within this page.

## Impacts in scope (46)

- [blockchain_dlt] Critical: Bypassing the bridge timelock
- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Permanent freezing of funds on the L1 Bridge side
- [blockchain_dlt] Critical: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] High: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] High: Temporary freezing of network transactions by delaying one block by 3000% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments
- [blockchain_dlt] Medium: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Medium: Causing network processing nodes to process transactions from the mempool beyond set parameters (e.g. prevents processing transactions from the mempool)
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Medium: RPC API crash affecting projects with greater than or equal to 25% of the market capitalization on top of the respective layer
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Low: Compiler bug
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network
- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs for at least 1 hour
- [smart_contract] High: Temporary freezing of funds for at least 1 hour
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Compiler bug
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Temporary freezing of NFTs up to 1 hour
- [smart_contract] Low: Temporary freezing of funds up to 1 hour
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] High: Taking down the application/website
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:  HTML injection without JavaScript, Replacing existing text with arbitrary text, Arbitrary file uploads, etc
- [websites_and_applications] Medium: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Medium: Malicious interactions with an already-connected wallet, such as:  Modifying transaction arguments or parameters, Substituting contract addresses, Submitting malicious transactions
- [websites_and_applications] Medium: Retrieve sensitive data/files from a running server, such as:   /etc/shadow, database passwords, blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)

## Impact notes

Bugs in the Fuel VM and Compiler are the top priority for Fuel. Whitehats who focus here will earn the greatest rewards and acclaim from Fuel.

**Proof of Concept (PoC) Requirements**

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules).

**Feasibility Limitations**

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Fuel Attackathon Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/25655313192721-Fuel-Attackathon-Reward-Terms).

The reward pool size varies based on the severity of bugs found:

- If one or more Low severity bugs are found the reward pool will be $100,000 USD
- If one or more Medium severity bugs are found the reward pool will be $250,000 USD
- If one or more High severity bugs are found the reward pool will be $500,000 USD

- If 1 Critical severity bug is found the reward pool will be $800,000 USD
- If 2 Critical severity bugs are found the reward pool will be $900,000 USD
- If 3 or more Critical severity bugs are found the reward pool will be $1,000,000 USD

For this Attackathon, duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

**Reward Payment Terms**

Payouts are handled by the Fuel Network team directly and are denominated in USD. However, payments are done in USDC.

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

**Insight Rewards Payment Terms**

Insight Rewards: Portion of the Rewards Pool

* The "Insight" severity was introduced on Boost & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

## Out of scope (program-specific)

(none)

## Out of scope and rules

**KYC Requirement**

Fuel Network will be requesting KYC information in order to pay for successful bug submissions to whitehats who earn $500 USD or more. The following information will be required:

- Full name 
- Date of birth
- Proof of address (either a redacted bank statement with address or a recent utility bill)
- Copy of Passport or other Government issued ID

**Eligibility Criteria**

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:

- On OFACs SDN list 
- From a restricted country or territory: North Korea, Iran, Cuba, Syria, certain regions of Ukraine (Crimea, Donetsk and Luhansk), West Bank and Gaza regions of Israel, Venezuela, Afghanistan
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review, or who work fo the company which did the audit review


**Responsible Publication**

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:

- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.
- Immunefi may publish bug reports submitted to this Attackathon and a leaderboard of the participants and their earnings.

**Immunefi Standard Badge**

By adhering to Immunefi’s best practice recommendations, Fuel Network has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209).

## Out of Scope Impacts

- Impacts on Example Code provided by Fuel Network or smart contract code that was deployed by the user.

**All Categories:**

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the b

**Blockchain/DLT & Smart Contract Specific:**

- Incorrect data supplied by third party oracles
- - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks

**Websites and Apps:**


- Theoretical impacts without any proof or demonstration
- Impacts involving attacks requiring physical access to the victim device
- Impacts involving attacks requiring access to the local network of the victim
- Reflected plain text injection (e.g. url parameters, path, etc.)
- This does not exclude reflected HTML injection with or without JavaScript
- This does not exclude persistent plain text injection
- Any impacts involving self-XSS
- Captcha bypass using OCR without impact demonstration
- CSRF with no state modifying security impact (e.g. logout CSRF)
- Impacts related to missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”) without demonstration of impact
- Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces
- Impacts causing only the enumeration or confirmation of the existence of users or tenants
- Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows
- Lack of SSL/TLS best practices
- Impacts that only require DDoS
- UX and UI impacts that do not materially disrupt use of the platform
- Impacts primarily caused by browser/plugin defects
- Leakage of non sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)
- Any vulnerability exploit requiring browser bugs for exploitation (e.g. CSP bypass)
- SPF/DMARC misconfigured records)
- Missing HTTP Headers without demonstrated impact
- Automated scanner reports without demonstrated impact
- UI/UX best practice recommendations
- Non-future-proof NFT rendering

## Prohibited Activities:

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
