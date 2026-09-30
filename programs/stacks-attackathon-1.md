# Attackathon | Stacks

- Page: https://immunefi.com/bug-bounty/stacks-attackathon-1/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Smart Contract
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-01-13T08:00:00.000Z

## Assets in scope (5)

- [blockchain_dlt] https://github.com/stacks-network/sbtc/tree/immunefi_attackaton_0.9/emily — Emily - An API that helps facilitate and supervise the sBTC Bridge - 6000
- [blockchain_dlt] https://github.com/stacks-network/sbtc/tree/immunefi_attackaton_0.9/protobufs — Protobuffs - Platform-neutral extensible mechanisms for serializing structured data. - 292
- [blockchain_dlt] https://github.com/stacks-network/sbtc/tree/immunefi_attackaton_0.9/sbtc — lib-sbtc - A library for creating BTC deposit transactions that can be handled by the sBTC signers. - 1186
- [blockchain_dlt] https://github.com/stacks-network/sbtc/tree/immunefi_attackaton_0.9/signer — sBTC Signer - a signer entity separate from the Stacks Nakamoto signer which signs sBTC operations, communicates with sBTC contracts, and manages sBTC UTXOs. - 19760
- [smart_contract] https://github.com/stacks-network/sbtc/tree/immunefi_attackaton_0.9/contracts/contracts — Smart Contract - sBTC contracts - The Clarity contracts for the sBTC protocol. - 645

## Asset notes

Learn more on the Stacks' Academy.

## Project Technical Info

What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?

- SIP10 is the only token standard supported https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md 

What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?

- Deposit processing can be paused by shutting down the Emily API server. In the case of vulnerabilities in deposit handling, this can be used to reduce the impact of an ongoing attack.

What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?

- Signers are permissioned and whitelisted operators. Any attack that requires a majority of signers to be malicious should be out of scope. Attacks that require a minority of signers to be malicious would still be in scope but with reduced severity. 

Which chains and/or networks will the code in scope be deployed to?

- Stacks L2

## Security Researcher Education

Is this an upgrade of an existing system? If so, which? And what are the main differences?

- sBTC is a new 1:1 Bitcoin-backed asset on the Stacks Bitcoin L2. The in-scope codebase is completely new. 

Where do you suspect there may be bugs?

- The end-to-end flow of processing new Bitcoin deposits and minting sBTC on Stacks is relatively complex and error prone. Issues here could allow DoS of valid deposits or incorrect minting of unbacked sBTC.

Vulnerabilities in the sBTC smart contracts hosted on Stacks could break the core assumptions of the system. Any attack that leads to a mismatch between the BTC collateral and the sBTC would be highly interesting to us.

- Any attacks against the threshold signature scheme used on Bitcoin

Where might Security Researchers confuse out-of-scope code to be in-scope?

- Vulnerabilities in the Stacks L2 blockchain itself should be reported directly to the [Stacks Immunefi bug bounty](https://immunefi.com/bug-bounty/stacks/information/). 

- The initial launch of sBTC does not enable withdrawals back to Bitcoin. While partial code to support withdrawals can be found in the codebase, issues that can’t be exploited in “deposit-only” mode will be downgraded.

Are there any unusual points about your protocol that may confuse Security Researchers?

- sBTC launches without support for withdrawals. Users can go from BTC -> sBTC, but the support for sBTC -> BTC is not fully implemented. This functionality will be part of a follow-up contest.

## Impacts in scope (24)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] High: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] High: Unintended chain split (network partition)
- [blockchain_dlt] High: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] Medium: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Medium: API crash preventing correct processing of deposits
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Medium: Temporarily Freezing Network Transactions
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24h
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1h
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

**Asset Accuracy Assurance**

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.
The initial launch of sBTC does not enable withdrawals back to Bitcoin. While partial code to support withdrawals can be found in the codebase, issues that can’t be exploited in “deposit-only” mode will be downgraded.

**Public Disclosure of Known Issues**

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 
- https://github.com/stacks-network/sbtc/issues?q=is%3Aissue+is%3Aopen+label%3A%22flagged+by+AR%22
- https://github.com/stacks-network/sbtc/issues

The project will share detailed changelogs when code changes are released during the Attackathon on Discord and they will be documented in our [Stacks changelog](https://immunefisupport.zendesk.com/hc/en-us/articles/30737752973073-Stacks-Attackathon-1-Code-Update-Changelog).

**Previous Audits**

Stacks’s completed audit reports can be found at https://stacks.org/audits. Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

**Primacy of Impact vs Primacy of Rules**

Stacks adheres to the Primacy of Rules, which means that the whole bug bounty program is run strictly under the terms and conditions stated within this page.

**KYC Information**

Stacks will be requesting KYC information in order to pay for successful bug submissions. The following information will be required:
- Full name
- Date of birth
- Proof of address (either a redacted bank statement with address or a recent utility bill)
- Copy of Passport or other Government issued ID

Security researchers are required to submit KYC within 14 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

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

The following reward terms are a summary, for the full details read our [Stacks Attackathon 1 Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/30553590157073-Stacks-Attackathon-1-Reward-Terms).

- **The reward pool size is $250,000 USD**, regardless of bugs found.

- **On top of the above rewards,** the yield generated from 1 Million STX over 3 months will be distributed equally among all SRs who submit a valid bug report. Estimated to be **worth about $50,000 USD** as of December 2nd, 2024.

Duplicates and private known issues are valid for a reward.

## Out of scope (program-specific)

Security researchers are required to submit KYC within 14 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
