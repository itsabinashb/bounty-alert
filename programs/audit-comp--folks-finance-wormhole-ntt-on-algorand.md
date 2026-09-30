# Audit Comp | Folks Finance: Wormhole NTT on Algorand

- Page: https://immunefi.com/bug-bounty/audit-comp--folks-finance-wormhole-ntt-on-algorand/scope/
- Max bounty: $30,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-10-27T10:00:00.000Z

## Assets in scope (18)

- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/constants.py — constants.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/errors.py — errors.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/library/MathLib.py — MathLib.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/library/TrimmedAmountLib.py — TrimmedAmountLib.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/ntt_manager/NttManager.py — NttManager.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/ntt_manager/NttRateLimiter.py — NttRateLimiter.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/ntt_manager/interfaces/INttManager.py — INttManager.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/ntt_token/NttToken.py — NttToken.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/ntt_token/NttTokenExisting.py — NttTokenExisting.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/ntt_token/NttTokenNew.py — NttTokenNew.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/ntt_token/interfaces/INttToken.py — INttToken.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/transceiver/MessageHandler.py — MessageHandler.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/transceiver/Transceiver.py — Transceiver.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/transceiver/TransceiverManager.py — TransceiverManager.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/transceiver/WormholeTransceiver.py — WormholeTransceiver.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/transceiver/interfaces/ITransceiver.py — ITransceiver.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/transceiver/interfaces/ITransceiverManager.py — ITransceiverManager.py
- [smart_contract] https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/ntt_contracts/types.py — types.py

## Asset notes

**Insight Reporting**

Insight reports may be reported to this program and require a PoC. Insights are rewarded according to [Immunefi’s Standardized Competition Reward Terms.](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms)

**Dispute Resolution**

If there is any dispute over bug reports between projects and security researchers, Immunefi has final say on validity and severity based on the terms of this program.

**Responsible Publication Policy**

- Immunefi will publish bug reports, earnings, and a leaderboard for this Audit Competition.
- Security Researchers may publish their bug reports as well, but only after Immunefi has published the valid bug reports as part of the competition results.

**Eligibility Criteria**

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in an audit review of the code in scope (Such auditors may still participate in this program only if they receive project permission)

## Impacts in scope (9)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Bypass of rate limiting mechanism
- [smart_contract] High: Temporary freezing of funds for at least 24 hour
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

**Build Commands, Test Commands, and How to Run Them** 
Follow the setup, build and test commands in the repo README https://github.com/Folks-Finance/algorand-ntt-contracts/blob/main/README.md. 

**Asset Accuracy Assurance**
Bugs found on assets incorrectly listed in-scope are valid.

**Code Freeze Assurance**
Code of the assets in scope is frozen while the program is live.

**Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.**

The project commits to keeping private all info related to bug findings until this program is over. This means the project will not leak info about any bug findings or planned bug fixes, including bug findings found independently by the project or from concurrent private audits.

---

**Previous Audits**

Folks Finance’s completed audit reports can be found at https://github.com/Folks-Finance/audits/blob/bb69a84b2015280e903ee5b55e2bbbc5b880e54f/Adevar%20-%20Algorand%20Wormhole%20NTT%20-%20October%202025.pdf ]. Unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

**Public Disclosure of Known Issues**

- Bug reports for publicly disclosed bugs are not eligible for a reward. 
- The Algorand Wormhole NTT implementation doesn’t have the exact same behaviour/specification as the EVM/Solana/Sui Wormhole NTT implementation. 
- There is no support for the NTT Global Accountant.
- There is no support for “additional payload” in NttManager.
- There is no support for automatic relaying in WormholeTransceiver.
- It is the responsibility of the integrator to prevent overflow risk in TrimmedAmount by setting appropriate decimals.
- It is the responsibility of the integrator to set an appropriate threshold for attestations in the NttManager.
- It is the responsibility of the integrator to set appropriate rate limits in the NttManager.
- It is the responsibility of the integrator to add and manage appropriately the configured Transceivers e.g. consider the foreign reference limitations, opcode costs etc. 
- An ASA may have their clawback/freeze set.
- The NttToken, NttTokenNew and NttTokenExisting are provided as reference implementations. A project is able to implement their own concrete INttToken if needed to fit their custom needs.
- In general, Wormhole NTT is a framework so if X behaviour is not supported then integrators are recommended to modify the smart contracts for themselves.
- Opcode optimisation when prioritising clean and readable code.
- Not checking for rekey and close-to
- Some box storage cannot be deleted
- Box MBR funding is implicitly required
- Some box storage costs are not refunded after box deletion
- Block timestamp manipulation by block proposer


**Private Known Issues Reward Policy**

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.


---


**Where might Security Researchers confuse out-of-scope code to be in-scope?**

Although the smart contract code for all the following is out-of-scope, their impact and how they are used is in scope. Namely, on other chains, the Wormhole NTT implementation. On Algorand, the Wormhole Core smart contract, VaaVerify logic signature and TmplSig logic signature. 
If the rate limit is exceeded, the transfer is only delayed from completing. This is the intended design as it follows the equivalent EVM implementation. 


**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

It’s an extension to the existing Wormhole NTT framework, adding support for Algorand. The main differences between the Algorand and EVM implementation for Wormhole NTT is the introduction of a generic MessageHandler and a global TransceiverManager. 

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

Assumptions made about the compiled TEAL code when in reality it does something else. You can view what the Algorand Python compiles into by looking at the build folder generated named “specs/teal”.

Replay attacks where you can receive or execute the same message multiple times.

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

Algorand Standard Assets (ASAs)

**What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?**

The integrator has the ability to pause certain functionality in the NttManager and TransceiverManager. A rate limit can be configured for outbound and inbound transfer amounts. Configured Transceivers can be removed and added.

**What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?**

In the NttManager: default admin, upgradeable admin, ntt manager admin. In the NttTokenNew and NttTokenExisting: default admin, upgradeable admin. In the TransceiverManager: message handler admin. In the WormholeTransceiver: default admin, upgradeable admin, manager. 

**What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?**

None

**Which chains and/or networks will the code in scope be deployed to?**

Algorand

**What external dependencies are there?**

- Algorand smart contract library https://github.com/Folks-Finance/algorand-smart-contract-library. 
- The Wormhole NTT implementation on other chains https://github.com/wormhole-foundation/native-token-transfers. 
- The Wormhole Core implementation on Algorand https://github.com/wormhole-foundation/wormhole/tree/main/algorand. 

**Are there any unusual points about your protocol that may confuse Security Researchers?**

The external dependency of the Wormhole Core implementation on Algorand https://github.com/wormhole-foundation/wormhole/tree/main/algorand was written a long time ago so uses old outdated standards for Algorand development. 

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

- Algorand NTT Design - https://docs.google.com/document/d/1eli_csvdUgOrrE75dbtoSZQDxv-zAjZyBo61wyaN7jQ/edit?usp=sharing 
- Wormhole NTT explainer video https://youtu.be/Od5cTaxjTiw?si=WtT5MzZvrGMEwMrZ 
- Wormhole NTT Docs - https://wormhole.com/docs/products/token-transfers/native-token-transfers/overview/ 
- Algorand Python Docs - https://algorandfoundation.github.io/puya/ 
- Algorand Developer Portal - https://dev.algorand.co/

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of Reward Pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program](https://immunefi.com/allstars/) participants. 

Rewards are denominated in USD and distributed in USDC on Ethereum.

Flat Rewards:
The reward pool is **$30,000 USD** if any bug is found. That means that even if 1 Low severity bug is found, the whole reward pool is unlocked and has to be fully distributed between security researchers. 

If not a single bug is found (Insights do not count as bugs) the reward pool is **$4,500 USD**.
Private known issues, meaning known issues that were not publicly disclosed, are valid and unlock the corresponding reward pool.

**Proof of Concept (PoC) Requirements**
A **runnable PoC**, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (17)

- An ASA may have their clawback/freeze set. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- Block timestamp manipulation by block proposer (https://github.com/Folks-Finance/algorand-ntt-contracts)
- Box MBR funding is implicitly required (https://github.com/Folks-Finance/algorand-ntt-contracts)
- In general, Wormhole NTT is a framework so if X behaviour is not supported then integrators are recommended to modify the smart contracts for themselves (https://github.com/Folks-Finance/algorand-ntt-contracts)
- It is the responsibility of the integrator to add and manage appropriately the configured Transceivers e.g. consider the foreign reference limitations, opcode costs etc. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- It is the responsibility of the integrator to prevent overflow risk in TrimmedAmount by setting appropriate decimals. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- It is the responsibility of the integrator to set an appropriate threshold for attestations in the NttManager. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- It is the responsibility of the integrator to set appropriate rate limits in the NttManager. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- Not checking for rekey and close-to (https://github.com/Folks-Finance/algorand-ntt-contracts)
- Opcode optimisation when prioritising clean and readable code. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- Some box storage cannot be deleted (https://github.com/Folks-Finance/algorand-ntt-contracts)
- Some box storage costs are not refunded after box deletion (https://github.com/Folks-Finance/algorand-ntt-contracts)
- The Algorand Wormhole NTT implementation doesn’t have the exact same behaviour/specification as the EVM/Solana/Sui Wormhole NTT implementation. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- The NttToken, NttTokenNew and NttTokenExisting are provided as reference implementations. A project is able to implement their own concrete INttToken if needed to fit their custom needs. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- There is no support for automatic relaying in WormholeTransceiver. (https://github.com/Folks-Finance/algorand-ntt-contracts)
- There is no support for the NTT Global Accountant - https://github.com/wormhole-foundation/wormhole/tree/main/cosmwasm/contracts/ntt-global-accountant (https://github.com/Folks-Finance/algorand-ntt-contracts)
- There is no support for “additional payload” in NttManager. (https://github.com/Folks-Finance/algorand-ntt-contracts)
