# sBTC

- Page: https://immunefi.com/bug-bounty/sbtc/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Blockchain/DLT
- PoC required for: blockchain_dlt - critical, smart_contract - critical, blockchain_dlt - high, smart_contract - high, blockchain_dlt - medium, blockchain_dlt - low
- End date: (none)

## Assets in scope (5)

- [blockchain_dlt] https://github.com/stacks-sbtc/sbtc/tree/main/emily — The sBTC Emily implementation
- [blockchain_dlt] https://github.com/stacks-sbtc/sbtc/tree/main/sbtc — The sBTC deposit library
- [blockchain_dlt] https://github.com/stacks-sbtc/sbtc/tree/main/signer — The sBTC signer implementation
- [blockchain_dlt] https://github.com/stacks-sbtc/sbtc/tree/main/wsts — The WSTS library
- [smart_contract] https://github.com/stacks-sbtc/sbtc/tree/main/contracts/contracts — The sBTC smart contracts

## Asset notes

(none)

## Impacts in scope (11)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] High: The sBTC signers not being able to confirm new transactions (a sustained total sBTC shutdown)
- [blockchain_dlt] Medium: Emily API crash preventing correct processing of sBTC deposits/withdrawals
- [blockchain_dlt] Medium: Temporarily freezing sBTC transactions
- [blockchain_dlt] Low: Denial of service caused by brute-force or simple resource exhaustion (for example, by connection flooding)
- [blockchain_dlt] Low: Modification of STX transaction fees outside of design parameters
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds

## Impact notes

Rewards are distributed based on the vulnerability's impact, as defined in the Impacts in Scope section. If there is any discrepancy between the classification in the Impacts in Scope section and the Immunefi Vulnerability Severity Classification System, the classification in the Impacts in Scope section will take precedence.

Stipulations:
- Vulnerabilities that can be objectively determined to affect <1% of users may be downgraded by 1 severity.
- Impacts that depend on execution involving a malicious signer may be downgraded by 1 severity level.
- Impacts on availability (e.g., denial-of-service) that depend on execution involving a malicious signer will be downgraded by 1 or more severity levels, to no lower than Low.

Malicious signer threat model: An attacker operates one or more signers whose public keys are members of the current on-chain sBTC signer set. The attacker controls those signers' legitimate credentials. They may run modified software, deviate from the protocol, and craft, replay, withhold, or reorder messages.

## Rewards

- [blockchain_dlt] Critical: maxReward=$250,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: maxReward=$25,000, minReward=$5,000, rewardModel=range
- [blockchain_dlt] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [blockchain_dlt] Low: fixedReward=$1,000, rewardModel=fixed
- [smart_contract] Critical: maxReward=$250,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$25,000, minReward=$5,000, rewardModel=range

## Reward notes

Payouts are handled by the Stacks Endowment team directly and are denominated in USD. However, payments will be made in the USD equivalent in the Stacks token (STX).

## Out of scope (program-specific)

- Any attacks on 3rd party services, including but not limited to AWS or Datadog.
- Any sub-optimal default configuration.
- Any phishing, social engineering, or related attacks against the Stacks ecosystem or any members thereof.
- Any reporting of findings that are already public or known to us, including but not limited to: vulnerabilities described or referenced in [GitHub issues](https://github.com/stacks-sbtc/sbtc/issues); vulnerabilities described or referenced in open or closed [pull requests in the sBTC repository](https://github.com/stacks-sbtc/sbtc/pulls); previous findings reported by other researchers; bugs disclosed in CVEs, security advisories, or other public forums; findings discovered during currently-active third-party security assessments; and duplicated results of concluded assessments as posted here: [https://stacks.org/audits](https://stacks.org/audits), [https://reports.immunefi.com/stacks-ii-attackathon](https://reports.immunefi.com/stacks-ii-attackathon), or [https://reports.immunefi.com/stacks-i-attackathon](https://reports.immunefi.com/stacks-i-attackathon). Novel attack methods that lead to an already documented impact are allowed.
  - Note: If your report demonstrates a materially higher severity impact or a novel exploit path for a known issue, please note this explicitly — such reports may be considered in scope.
- Any findings requiring access to or the cooperation of a Bitcoin miner.
- Any theoretical attacks without substantial evidence and supporting documentation.
- Any automated scanner findings or fuzz test results without an associated functional proof-of-concept.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (8)

- Audits (https://docs.stacks.co/learn/network-fundamentals/audits)
- Audits (https://docs.stacks.co/learn/network-fundamentals/audits)
- GitHub issues (https://github.com/stacks-sbtc/sbtc/issues?utm_source=immunefi)
- GitHub issues (https://github.com/stacks-sbtc/sbtc/issues?utm_source=immunefi)
- Stacks I Attackathon (https://reports.immunefi.com/stacks-i-attackathon?utm_source=immunefi)
- Stacks II Attackathon (https://reports.immunefi.com/stacks-ii-attackathon?utm_source=immunefi)
- pull requests in the sBTC (https://github.com/stacks-sbtc/sbtc/pulls?utm_source=immunefi)
- pull requests in the sBTC (https://github.com/stacks-sbtc/sbtc/pulls?utm_source=immunefi)
