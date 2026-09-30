# Audit Comp | Quantus

- Page: https://immunefi.com/bug-bounty/audit-comp-quantus/scope/
- Max bounty: $20,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Websites and Applications
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - low, blockchain_dlt - medium, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - low, websites_and_applications - medium
- End date: 2026-08-25T10:00:00.000Z

## Assets in scope (7)

- [blockchain_dlt] https://github.com/immunefi-team/audit-comp-quantus-chain — The Substrate L1 node — runtime, FRAME pallets, QPoW consensus, quantus-node
- [blockchain_dlt] https://github.com/immunefi-team/audit-comp-quantus-qp-poseidon — Poseidon2 hash implementation for Quantus
- [blockchain_dlt] https://github.com/immunefi-team/audit-comp-quantus-qp-rusty-crystals/tree/audit-comp-ready/dilithium — ML-DSA/Dilithium signature implementation
- [blockchain_dlt] https://github.com/immunefi-team/audit-comp-quantus-qp-rusty-crystals/tree/audit-comp-ready/hdwallet — HD-wallet module
- [blockchain_dlt] https://github.com/immunefi-team/audit-comp-quantus-qp-zk-circuits — Zero-Knowledge circuits for Quantus
- [websites_and_applications] https://github.com/immunefi-team/audit-comp-quantus-apps/tree/audit-comp-ready/mobile-app — Mobile application
- [websites_and_applications] https://github.com/immunefi-team/audit-comp-quantus-apps/tree/audit-comp-ready/quantus_sdk — Quantus SDK

## Asset notes

Check out the many READMEs across the [GitHub](https://github.com/Quantus-Network/l) repositories!

Technical Walkthough:
- poseidon: https://www.loom.com/share/f762262d864a44e3a7498cb14269a56a
- dilithium: https://www.loom.com/share/3b147cd067e2496597509a028eb825aa
- hdwallet: https://www.loom.com/share/460c6a2930294ca4b9c9b766495660e2
- zk-circuits: https://www.loom.com/share/265d5bbdf33d4a74a25919c6dce50e3a
- chain: https://www.loom.com/share/19a1ecc31d4c49f598ff7d908f8f124a
- mobile-app: https://www.loom.com/share/aa04af79da214415adb2ffda4edc2157

## Impacts in scope (51)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [blockchain_dlt] Critical: Inflation bugs (unauthorized minting)
- [blockchain_dlt] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] Critical: Protocol insolvency
- [blockchain_dlt] Critical: Soundness bug in the ZK circuit
- [blockchain_dlt] Critical: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Causing network processing nodes to process transactions from the mempool beyond set parameters
- [blockchain_dlt] High: Permanent freezing of unclaimed royalties
- [blockchain_dlt] High: Permanent freezing of unclaimed yield
- [blockchain_dlt] High: RPC API crash affecting programs with greater than or equal to 25% of the market capitalization on top of the respective layer
- [blockchain_dlt] High: Temporary freezing of funds for at least 24 hour
- [blockchain_dlt] High: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments
- [blockchain_dlt] High: Theft of unclaimed royalties
- [blockchain_dlt] High: Theft of unclaimed yield
- [blockchain_dlt] High: Unintended chain split (network partition)
- [blockchain_dlt] Medium: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Medium: Block stuffing
- [blockchain_dlt] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [blockchain_dlt] Medium: Inaccuracies to the weight (similar to gas) accounting system that under or overcharge by more than 50% of the correct amount (and are not intentional as indicated by the program's terms)
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Medium: Smart contract unable to operate due to lack of token funds
- [blockchain_dlt] Medium: Temporary freezing of funds for at least 1 hour
- [blockchain_dlt] Medium: Theft of gas
- [blockchain_dlt] Medium: Unbounded gas consumption
- [blockchain_dlt] Low: Contract fails to deliver promised returns, but doesn't lose value
- [blockchain_dlt] Low: Inaccuracies to the weight (similar to gas) accounting system that under or overcharge by less than 50% of the correct amount (and are not intentional as indicated by the program's terms
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:
- Email address
- Phone number
- Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:
- Locking up the victim from login
- Cookie bombing, etc.

## Impact notes

### Asset Accuracy Assurance

Bugs found on assets incorrectly listed in scope are valid.

### Code Update Assurance

Duplicate submissions of bugs are valid until the relevant bug fix is public. Once a fix is public, the bug is out of scope and later submissions of it are invalid. Duplicate submissions of Insights are invalid.

The project commits to keeping all information about bug findings private until each fix is disclosed through the process described in the Bug Fix Policy. This includes bug findings found independently by the project or from concurrent private audits.

### Code Freeze Assurance

Code of the assets in scope is frozen while the program is live.

If a bug found during the competition requires an immediate fix, the bug will be considered a publicly known issue as soon as the fix is deployed. Submissions of the same bug after the fix is public are invalid, and a bypass of the fix is considered a new, valid bug.

Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.

The project commits to keeping private all information related to bug findings until this program is over. This means the project will not leak information about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

## Build, Test, and Run

Full instructions are in each repository's README.

- Rust components (chain, qp-poseidon, qp-zk-circuits, qp-rusty-crystals): build with `cargo build --release` and run tests with `cargo test --release`.
- Mobile app (Flutter): fetch dependencies with `flutter pub get`, run the app with `flutter run`, and run tests with `flutter test`.
- https://github.com/Quantus-Network/quantus-cli a command line tool you can use to make any kind of transaction accepted on chain. People can either build it from source or download it using cargo.

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [blockchain_dlt] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program](https://immunefi.com/allstars/) participants\]. 

Rewards are denominated in USD and distributed in USDC on Ethereum. 

- If any valid bug is found — even a single Low-severity bug — the full reward pool of **$20,000 USD** is unlocked and must be fully distributed among security researchers.
- If no security vulnerability is found (Insights do not count as bugs), the reward pool is **$3,000 USD**.


### Public Disclosure of Known Issues

Bug reports for publicly disclosed bugs are not eligible for a reward.

### Private Known Issues Reward Policy

Private known issues — known issues that were not publicly disclosed — are valid for a reward at their full severity and unlock the corresponding reward pool without any downgrade. Public known issues are invalid.

## Out of scope (program-specific)

These impacts are out of scope for this bug bounty program.   
**All Categories:**

* Impacts requiring attacks that the reporter has already exploited themselves, leading to damage  
* Impacts caused by attacks requiring access to leaked keys/credentials  
* Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible  
* Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code  
* Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production  
* Best practice recommendations  
* Feature requests  
* Impacts on test files and configuration files unless stated otherwise in the bug bounty program

**Blockchain/DLT & Smart Contract Specific:**

* Incorrect data supplied by third party oracles  
  * Not to exclude oracle manipulation/flash loan attacks  
* Impacts requiring basic economic and governance attacks (e.g. 51% attack)  
* Lack of liquidity impacts  
* Impacts from Sybil attacks  
* Impacts involving centralization risks

**Websites and Apps**

* Theoretical impacts without any proof or demonstration  
* Impacts involving attacks requiring physical access to the victim device  
* Impacts involving attacks requiring access to the local network of the victim  
* Reflected plain text injection (e.g. url parameters, path, etc.)  
* This does not exclude reflected HTML injection with or without JavaScript  
* This does not exclude persistent plain text injection  
* Any impacts involving self-XSS  
* Captcha bypass using OCR without impact demonstration  
* CSRF with no state modifying security impact (e.g. logout CSRF)  
* Impacts related to missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as “httponly”) without demonstration of impact  
* Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces  
* Impacts causing only the enumeration or confirmation of the existence of users or tenants  
* Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows  
* Lack of SSL/TLS best practices  
* Impacts that only require DDoS  
* UX and UI impacts that do not materially disrupt use of the platform  
* Impacts primarily caused by browser/plugin defects  
* Leakage of non sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)  
* Any vulnerability exploit requiring browser bugs for exploitation (e.g. CSP bypass)  
* SPF/DMARC misconfigured records)  
* Missing HTTP Headers without demonstrated impact  
* Automated scanner reports without demonstrated impact  
* UI/UX best practice recommendations  
* Non-future-proof NFT rendering

**Prohibited Activities:**

* Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet  
* Any testing with pricing oracles or third-party smart contracts  
* Attempting phishing or other social engineering attacks against our employees and/or customers  
* Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)  
* Any denial of service attacks that are executed against project assets  
* Automated testing of services that generates significant amounts of traffic  
* Public disclosure of an unpatched vulnerability in an embargoed bounty

## Additional Out of Scope information:

### Scope boundaries (out-of-scope code that may look in-scope)

Because most of the chain is inherited from Substrate, only Quantus's own code and modifications are in scope. The following are out of scope: unmodified upstream Substrate and all package dependencies; the upstream plonky2 proving system (only Quantus's modifications are in scope); the voting module in `qp-zk-circuits`; and the threshold module in `qp-rusty-crystals`.

### Privileged actors

Reports that require the involvement of the Technical Collective, acting within its attributed privileges, are out of scope — for example, runtime upgrades, which are not considered a vulnerability. A malicious genesis block is also out of scope. There are no actors whose involvement is out of scope when they exceed their attributed privileges (N/A).

#### Specific Out of scope clauses:

- **Upstream / third-party code.** Quantus is built on Polkadot's Substrate, and most of the blockchain's code is inherited from it. Unmodified upstream Substrate code and all package dependencies (approximately 1,200 in the chain) are out of scope — only Quantus's own code and modifications are in scope.
- **The plonky2 proving system.** `qp-zk-circuits` builds on qp-plonky2 — Quantus's fork of Polygon Zero's plonky2 SNARK/STARK proving system, providing proof generation, recursive verification, and the primitives used by qp-zk-circuits. The unmodified upstream plonky2 code is out of scope; only Quantus's own modifications to it are in scope.
- **The voting module** in `qp-zk-circuits`.
- **The threshold module** in `qp-rusty-crystals`.
- **A malicious genesis block.**
- **Account reaping leading to replayed transactions.**
- **Actions by privileged actors within their privileges.** The Technical Collective can perform runtime upgrades; this is not considered a vulnerability. Any bug report requiring the involvement of such privileged actors, as long as they operate within the privileges attributed to them, is out of scope. (There are no addresses whose involvement is out of scope when they exceed their attributed privileges — N/A.)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (3)

- At some point the volume of transactions will cause the zk-tree depth to exceed the current maximum, both on chain and in circuit. When that moment approaches we will do a runtime upgrade to update both the circuit and the chain. A similar reasoning works for when / if mining rewards ever drop well below the quantized minimum for the circuit. (https://immunefi.com/audit-competition/audit-comp-quantus/information/#:~:text=13%20May%202026-,Known%20Issues,-Reports%20covering%20previously)
- If a referendum member is removed, their votes on existing referendums are not removed. This is consistent with upstream Substrate and is acceptable. (https://immunefi.com/audit-competition/audit-comp-quantus/information/#:~:text=13%20May%202026-,Known%20Issues,-Reports%20covering%20previously)
- The connection between the miner and the node is expected to be on a trusted network, so the fact that the connection is in plaintext is not in scope (https://immunefi.com/audit-competition/audit-comp-quantus/information/#:~:text=13%20May%202026-,Known%20Issues,-Reports%20covering%20previously)
