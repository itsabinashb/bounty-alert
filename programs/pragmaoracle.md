# Pragma Oracle

- Page: https://immunefi.com/bug-bounty/pragmaoracle/scope/
- Max bounty: $10,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high
- End date: (none)

## Assets in scope (2)

- [smart_contract] https://voyager.online/contract/0x024a55b928496ef83468fdb9a5430fe031ac386b8f62f5c2eb7dd20ef7237415 — PublisherRegistry
- [smart_contract] https://voyager.online/contract/0x02a85bd616f912537c50a49a4076db02c00b29b2cdc8a197ce92ed1837fa875b — Oracle

## Asset notes

(none)

## Impacts in scope (4)

- [smart_contract] Critical: Allow unauthorized actors to manipulate/publish any data entry
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results.
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Temporary freezing of funds

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$10,000, primacy=primacy_of_rules, rewardCalculationPercentage=10, rewardModel=fixed
- [smart_contract] High: fixedReward=$5,000, rewardModel=fixed

## Reward notes

Rewards depend on the vulnerability’s impact, as defined in the Impacts in Scope table below.

- **Critical smart contract bugs:** the reward amount is % of the funds directly affected up to a maximum of $10000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of $10000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.
- **Repeatable attacks:** Only the first attack counts, even if the contract can be upgraded, paused, or disabled.
- **Proof of Concept (PoC):** Critical and High smart contract reports require a PoC that follows [Immunefi’s guidelines](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules). Reports missing a required PoC receive no reward.
- **Known issues:** Bugs identified in [this audit report](https://github.com/NethermindEth/PublicAuditReports/blob/main/NM0147-FINAL_PRAGMA.pdf) are not eligible for rewards.
- **Payment:** Pragma pays rewards directly in USDC, based on their USD value.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
