# RootstockLabs

- Page: https://immunefi.com/bug-bounty/rootstocklabs/scope/
- Max bounty: $200,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications, Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, smart_contract - critical, smart_contract - high, websites_and_applications - critical
- End date: (none)

## Assets in scope (20)

- [blockchain_dlt] https://github.com/rsksmart/powpeg-node — powpeg-node
- [blockchain_dlt] https://github.com/rsksmart/rsk-powhsm/releases/latest — PowHSM
- [blockchain_dlt] https://github.com/rsksmart/rskj — rskj
- [blockchain_dlt] https://www.rootstocklabs.com/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://immunefi.com/bug-bounty/rootstocklabs — Primacy of Impact (primacy of impact)
- [smart_contract] https://rootstock.blockscout.com/address/0x9270733402dc7c5730ea24268fc11039fd75e189 — PegInContract
- [smart_contract] https://rootstock.blockscout.com/address/0x9a0678742cfb567874eb4e99df2106bded78f5e4 — PegOutContract
- [smart_contract] https://rootstock.blockscout.com/address/0x9a48c6b18aa000d0bd35d55616bcc98ad3553e7a — FlyoverDiscovery
- [smart_contract] https://rootstock.blockscout.com/address/0xAAFF2c6D3185ccd03d9781e689005c314b936AC1?tab=contract — Quotes
- [smart_contract] https://rootstock.blockscout.com/address/0xB0824559dF4a0872A61b228466bAd12E733f7dEC — SignatureValidator
- [smart_contract] https://rootstock.blockscout.com/address/0xb2c65bbf276cc5ccae73c0ab29b609a129080639 — PauseRegistry
- [smart_contract] https://rootstock.blockscout.com/address/0xbe4d93b3afd9921cac66704ffd3caf662886fb73 — CollateralManagementContract
- [smart_contract] https://rootstock.blockscout.com/address/0xd8D956312222d8acaBB58569cc960a93b1aa2f7a — BtcUtils
- [smart_contract] https://rootstock.blockscout.com/token/0x2aCc95758f8b5F583470bA265Eb685a8f45fC9D5 — RIF Token
- [websites_and_applications] https://github.com/rsksmart/2wp-api — 2wp-api
- [websites_and_applications] https://github.com/rsksmart/2wp-app — 2wp-app
- [websites_and_applications] https://github.com/rsksmart/bridges-core-sdk — bridges-core-sdk
- [websites_and_applications] https://github.com/rsksmart/flyover-sdk — flyover-sdk
- [websites_and_applications] https://github.com/rsksmart/liquidity-provider-server — liquidity-provider-server
- [websites_and_applications] https://www.rootstocklabs.com/ — Primacy of Impact (primacy of impact)

## Asset notes

(none)

## Impacts in scope (53)

- [blockchain_dlt] Critical: Direct Theft of Bridge Funds
- [blockchain_dlt] Critical: Direct loss of significant non recoverable funds
- [blockchain_dlt] Critical: Remote extraction of HSM seed or private keys
- [blockchain_dlt] Critical: Total network shutdown (network not being able to confirm new transactions) via propagated/chained effect
- [blockchain_dlt] High: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior resulting in direct, exploitable risk to user funds (e.g., unauthorized transfer, permanent loss)
- [blockchain_dlt] High: Causing network processing nodes to process transactions from the mempool beyond set parameters
- [blockchain_dlt] High: Extraction of seed or private keys through local access to the HSM device or middleware
- [blockchain_dlt] High: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] High: Remote HSM seed wipe or remote transition of HSM into a wipe-required state
- [blockchain_dlt] High: Temporary freezing of network transactions by sustainably and substantially delaying block production (that could affect the network's gas consumption capabilities)
- [blockchain_dlt] High: Theft of funds via BTC path signing through local access to the HSM device or middleware
- [blockchain_dlt] High: Unintended chain split (network partition)
- [blockchain_dlt] Medium: A bug in the VM implementation that results in incorrect smart contract execution relative to expected VM semantics, with demonstrable security impact, but no direct risk to funds
- [blockchain_dlt] Medium: Attacks that allow producing an authentic attestation on a device with a pre-generated or well-known seed
- [blockchain_dlt] Medium: Attacks that fake an authentic attestation on a device running different versions of either the UI or Signer.
- [blockchain_dlt] Medium: Extraction of seed or private keys through physical access to the HSM device
- [blockchain_dlt] Medium: RPC API crash
- [blockchain_dlt] Medium: Remote shutdown of targeted nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Medium: Temporary remote disruption of the HSM device or middleware requiring a device reboot or firmware update for recovery, without loss of seed/key material
- [blockchain_dlt] Medium: Theft of funds via BTC path signing through physical access to the HSM device or middleware
- [blockchain_dlt] Low: Local access to HSM device resulting in crash due to memory corruption issues in secure element part
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
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
- [websites_and_applications] High: Taking down the application/website
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

For the Critical impact "Direct loss of significant non recoverable funds", the word "significant" here is defined as **USD 100,000** or more. Therefore, any report where the theft is below USD 100,000 may be downgraded or considered as out of scope.

__Vector Definition__

__Deployment assumptions__

- HSM, middleware, and Powpeg-Node run on the same host.
- HSM and middleware expose no external network interfaces (no inbound remote access paths).
- Powpeg-Node is the only externally connected component, used to sync blockchain data and forward it to the middleware, and its public exposure is limited.

__Remote__

“Remote” means the attacker cannot directly reach the HSM or middleware over the network and has no local access to the host. The only realistic remote reachability is indirect, via untrusted but consensus-valid on-chain data produced and propagated by the RSK network, synchronized by Powpeg-Node, and forwarded to the middleware (and subsequently to the HSM) for processing, where it may trigger vulnerable parsing/validation/logic.

__Local__

“Local” means the attacker has obtained root (or equivalent) control of the host running Powpeg-Node, the middleware, and the HSM (for example via shell/SSH access, a compromised account, or malware), but does not require physical access to the machine or device. With this level of access, the attacker can directly issue commands to the HSM via its local interfaces, ultimately affecting HSM operations.

__Physical__

“Physical” means the attacker has obtained physical access to the HSM device, enabling direct interaction and potential hardware tampering. With this level of access, the attacker may be able to probe, manipulate, reset, fault, or modify the device or its connections, potentially bypassing logical protections and ultimately affecting HSM operations.

## Rewards

- [blockchain_dlt] Critical: maxReward=$200,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: maxReward=$10,000, minReward=$5,000, rewardModel=range
- [blockchain_dlt] Medium: maxReward=$5,000, minReward=$2,500, rewardModel=range
- [blockchain_dlt] Low: maxReward=$2,500, minReward=$1,000, rewardModel=range
- [smart_contract] Critical: maxReward=$100,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$2,500, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$10,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,500, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)

Final severity is determined by combining the potential impact of the vulnerability with the likelihood of successful exploitation. In assessing likelihood, we consider factors such as attacker motivation, the capital required (and whether it exceeds potential gains), and whether the exploit provides a direct benefit to the attacker.

__Reward Calculation for Critical Level Reports__

For critical Blockchain/DLT bugs on HSM Firmware, the reward amount is 10% of the funds directly affected, capped at the maximum critical reward **USD 200 000**. However, a minimum reward of **USD 20 000** is to be rewarded in order to incentivize security researchers against withholding on a bug report.

For critical Blockchain/DLT bugs on powpeg-node and rskj, the reward amount is 10% of the funds directly affected, capped at the maximum critical reward USD 50 000. However, a minimum reward of USD 10 000 is to be rewarded in order to incentivize security researchers against withholding on a bug report.

For critical Blockchain/DLT bugs with a non-funds-at risk impact, the reward will be paid out as follows:
- Total network shutdown (network not being able to confirm new transactions) via propagated/chained effect USD $10 000

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 10 000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

For critical web/apps bugs, reports will be rewarded with USD 10 000, only if the impact leads to:
- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of USD 5 000. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. 
- The amount of funds at risk will be calculated with the impact of the first attack being at **100%** and then a reduction of **25%** from the amount of the first attack for every **[150 blocks]** the attack needs for subsequent attacks from the first attack, rounded down.

__Reward Calculation for High Level Reports__

For all High level bugs found on HSM Firmware, the reward will be USD 10 000. For High level bugs found on powpeg-node and rskj, the reward will be USD 5 000.

__Reward Calculation for Medium Level Reports__

For all Medium level bugs found on HSM Firmware, the reward will be USD 5 000. For Medium level bugs found on powpeg-node and rskj, the reward will be USD 2 500.

__Reward Calculation for Low Level Reports__

For all Low level bugs found on HSM Firmware, the reward will be USD 2 500. For Low level bugs found on powpeg-node and rskj, the reward will be USD 1 000.

__Reward Payment Terms__

Payouts are handled by the RootstockLabs team directly and are denominated in USD. However, payments are done in USDC on ETH.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

These impacts are out of scope for this bug bounty program. 

__All Categories:__

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program
- Impacts requiring phishing or other social engineering attacks against project's employees and/or customers


__Blockchain/DLT & Smart Contract Specific:__

- Incorrect data supplied by third party oracles
- Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks
- Impacts requiring physical access or local user level access to a user's device.
- Impact from previously known vulnerable libraries without a working PoC.
- Attacks requiring thousands of transactions, peg-ins, or substantial capital expenditure to cause minimal impact.
- Denial-of-service scenarios that are economically impractical to execute, including those requiring fees considerably higher above prevailing network averages.
- Issues that require privileged access, operator misconfiguration, or cannot be realistically triggered by an unauthenticated external attacker under default configurations.
- Self-inflicted impact: losses or negative outcomes resulting from use of the protocol or software outside of supported, documented, or expected functionality.
- Reports describing purely theoretical or extremely impractical attack scenarios.
- Rsk-powhsm:
    - Impacts related to the Ledger devices used on rsksmart/rsk-powhsm; including their physical security.
    - Impacts which ultimately don't allow for the arbitrary or unsecure use of the keys derived from the device seed for project rsksmart/rsk-powhsm.
    - Impacts related to the TCPSigner component, which is made solely for testing and fuzzing purposes for project rsksmart/rsk-powhsm.
    - Impacts related to code under the following path firmware/src/hal/src/x86/ since it’s a part of the code related to the TCPSigner component for project rsksmart/rsk-powhsm.
    - Impacts related to the SGX code for project rsksmart/rsk-powhsm.
    - Impacts related to DoS by physical or local access to the Ledger device.
    - Impacts related to Ledger company source code will be eligible for rewards after 90 days from the initial disclosure from Ledger.
    - Impacts related to Ledger company source code will be rewarded according to the general reward table specified for the bug bounty program, rather than the powHSM project reward table.
- Rskj
    - Impacts related to the encryption or access control of the integrated wallet of rsksmart/rskj.
    - Impacts related to the configuration option that allows storing private keys on disk.
    - JSON RPC personal module and the filter API including eth_newFilter, eth_blockFilter,eth_getLogs for rsksmart/rskj.
    - DoS attacks on any JSON RPC module that is not enabled by default (admin, debug, trace, etc).
    - DoS or resource consumption issues are limited to nodes deployed following the official Ubuntu installation guide (https://dev.rootstock.io/node-operators/setup/installation/ubuntu), as it reflects the intended production setup with the correct system-level settings for node operators. Any DoS or resource consumption issues affecting nodes installed or configured using any other method are out of scope.
    - DoS reports based solely on long-running transaction, contract, or block execution are out of scope if execution completes within RSK's expected block time (~30 seconds).
    - Denial-of-service attacks on P2P networking protocols (peer discovery, RSK wire protocol) are temporarily out of scope and will not be accepted at this time.
    - Vulnerabilities in features that are under development and not enabled by default.
    - Liquidity-bridge-contract
    - contracts/Quotes.sol and contracts/LiquidityBridgeContract.sol are out-of-scope for rsksmart/liquidity-bridge-contract
- RIF Token:
   - Only Critical severity vulnerabilities with a fork test as POC are accepted for this asset.

__Websites and Apps__

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


__Prohibited Activities:__

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- False Positive Reports (https://docs.google.com/document/d/161O90SVWDMGG5x3jLFCf_j2ehk1D-aA_E4H9PaLEEzw/edit?tab=t.0#heading=h.cv82oamvvho)
