# GMTrade

- Page: https://immunefi.com/bug-bounty/gmtrade/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: (none)
- End date: (none)

## Assets in scope (6)

- [smart_contract] https://explorer.solana.com/address/GTuvYD5SxkTq4FLG6JV1FQ5dkczr1AfgDcBHaFsBdtBg/verified-build — Treasury
- [smart_contract] https://explorer.solana.com/address/Gmso1uvJnLbawvw7yezdfCDcPydwW2s2iqG3w6MDucLo/verified-build — Store
- [smart_contract] https://explorer.solana.com/address/LPMWczEVgXyQ3979XaqqEttanCXmYGvtJqPVtw1PvC8/verified-build — Liquidity Provider
- [smart_contract] https://github.com/gmsol-labs/gmx-solana/tree/main/programs/liquidity-provider — Liquidity-provider
- [smart_contract] https://github.com/gmsol-labs/gmx-solana/tree/main/programs/store — Store
- [smart_contract] https://github.com/gmsol-labs/gmx-solana/tree/main/programs/treasury — Treasury

## Asset notes

(none)

## Impacts in scope (8)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$15,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$15,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range

## Reward notes

**Maximum Payout Cap (Treasury-based). The total payout for any single valid report shall not exceed 10% of the protocol Treasury balance at the time the report is submitted. Where the standard calculation (including "% of funds at risk" for Critical) yields more, this cap controls. Minimum rewards remain payable. **

** Treasury balance is publicly verifiable on-chain at 4tf9zEjvj2BUR9ZaAr53sQdULDWGGpJTr2zngSrmjtN6.**

## Out of scope (program-specific)

Known Issues
Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. Every issue opened in the repo, closed PRs, previous contests and audits are out of scope.

All issues submitted by wardens to the GMTrade bounty will be added to this repo once they have been reviewed by the sponsors. These are considered known issues and are out-of-scope for bounty rewards.

https://github.com/gmsol-labs/gmx-solana/blob/main/README.md#known-issues


Previous Audits
Any previously reported vulnerabilities mentioned in past audit reports are not eligible for a reward.

GMTrade previous audits can be found below:

https://github.com/gmsol-labs/gmx-solana-audits


Specific Types of Issues
• Informational findings.
• Design choices or expected design behaviors related to protocol.
• Issues that are ultimately user errors and can easily be caught in the frontend. For example, transfers to the System Program.
• Rounding errors.
• Relatively high gas consumption.
• Attacks requiring access to Timelock or Oracles.
• Risk of loss due to decline in pool asset prices.
• Price manipulation on third-party exchanges.
• Exploits based on delayed or extreme price feed updates.
• Attacks that are not economically feasible.
• Vulnerabilities related to hosting providers.


Trusted Roles
• Program upgrade authorities responsible for deploying and upgrading program code.
• The administrators with control over the default store account authority, typically protected by multisig and timelock mechanisms.
• Any program-defined privileged roles granted or managed by the administrators.
• Keeper accounts responsible for critical operations or maintaining service availability.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Smart Contract Known Issues (https://github.com/gmsol-labs/gmx-solana/blob/main/README.md#known-issues)
