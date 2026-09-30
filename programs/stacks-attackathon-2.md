# Attackathon | Stacks II

- Page: https://immunefi.com/bug-bounty/stacks-attackathon-2/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Blockchain/DLT, Smart Contract
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-03-27T08:00:00.000Z

## Assets in scope (3)

- [blockchain_dlt] https://github.com/stacks-network/sbtc/blob/immunefi_attackaton_1.0/Cargo.toml#L31 — WSTS GitHub repository. Refer to `rev` as specified in the WSTS entry of the Cargo.toml file in the sBTC repository. Vulnerabilities related to WSTS will only be considered in scope if they can be exploited in sBTC.
- [blockchain_dlt] https://github.com/stacks-network/sbtc/tree/immunefi_attackaton_1.0 — sBTC GitHub repo
- [smart_contract] https://github.com/stacks-network/sbtc/tree/immunefi_attackaton_1.0 — sBTC GitHub repo

## Asset notes

Build commands, test commands, and how to run them can be found [here on the Stacks Academy](https://immunefi.com/academy/stacks-attackathon-2/?utm_source=explore_results#400).
### Project Technical Info

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?**

SIP10 is the only token standard supported https://github.com/stacksgov/sips/blob/main/sips/sip-010/sip-010-fungible-token-standard.md 

**What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?**

Deposit processing can be paused by shutting down the Emily API server. In the case of vulnerabilities in deposit handling, this can be used to reduce the impact of an ongoing attack.

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

Signers are permissioned and whitelisted operators. Any attack that requires a majority of signers to be malicious should be out of scope. Attacks that require a minority of signers to be malicious would still be in scope but with reduced severity. 

**Which chains and/or networks will the code in scope be deployed to?**

Stacks L2

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

This attackaton focuses on sBTC V1, which adds (wrt previous attackathon for version 0.9) the ability to withdraw sBTC back into Bitcoin (on the L1). 

The main differences include:

- The new code related to withdrawals;
- all existing code (including the previous code related to deposits);
- key rotation, which allows the signer set to agree on a new aggregate key and start using it;
- the WSTS cryptographic library that powers threshold signature on Bitcoin.

Code until https://github.com/stacks-network/sbtc/releases/tag/0.0.9-rc7.1  is related to deposits. Anything more recent is related to withdrawals.

**Where do you suspect there may be bugs?**

The end-to-end flow of processing new Bitcoin deposits and minting sBTC on Stacks is relatively complex and error prone. Issues here could allow DoS of valid deposits or incorrect minting/burning of unbacked sBTC.

Vulnerabilities in the sBTC smart contracts hosted on Stacks could break the core assumptions of the system. Any attack that leads to a mismatch between the BTC collateral and the sBTC would be highly interesting to us.

Any attacks against the threshold signature scheme used on Bitcoin

**Where might Security Researchers confuse out-of-scope code to be in-scope?**

Vulnerabilities in the Stacks L2 blockchain itself should be reported directly to the [Stacks Immunefi bug bounty](https://immunefi.com/bug-bounty/stacks/information/).

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

**Previous Audits**

Stacks’s completed audit reports can be found at https://stacks.org/audits . As well as the [sBTC audit here,](https://security.bitcoinl2labs.com/audits) which the 3rd audit report from the top of the list.

Unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

**Public Disclosure of Known Issues**

Bug reports for publicly disclosed bugs are not eligible for a reward. 

- https://github.com/stacks-network/sbtc/issues
- https://github.com/stacks-network/sbtc/pulls

The Stacks team will label known issues with the label 'immunefi-scope' ( https://github.com/stacks-network/sbtc/labels/immunefi-scope ) to allow security researchers to easily filter them out.

**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

**Stacks’ Feasibility Limitations**

In addition to our [standard feasibility limitations](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards), the following also apply:

- Non-Criticals which can be objectively determined to only be able to affect <1% of users may be downgraded by 1 severity.
- Non-Critical impacts that are dependent on execution to have a malicious signer involved, may be downgraded by 1 severity level.
- Vulnerabilities related to WSTS will only be considered in scope if they can be exploited in sBTC.

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

### Rewards Terms

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

Rewards are denominated in USD and distributed in STX.

The reward pool is **$250,000 USD**, regardless of bugs found.

**On top of the above rewards**, the yield generated from 1 Million STX over 3 months will be distributed either among exceptional bug reports or equally among all SRs who submit a valid report, at Stacks’ discretion. Estimated to be worth about $50,000 USD as of December 1st, 2024.

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
