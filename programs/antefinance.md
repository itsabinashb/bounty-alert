# Ante Finance

- Page: https://immunefi.com/bug-bounty/antefinance/scope/
- Max bounty: $25,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: (none)

## Assets in scope (7)

- [smart_contract] https://etherscan.io/address/0x22075f4cD76299822Eb8D1546f5DcF775c90AA87 — Ante Pool
- [smart_contract] https://etherscan.io/address/0x28b549845B6fE1939783ba0bDb3ba1a598da0394 — Ante Pool
- [smart_contract] https://etherscan.io/address/0x5f3555Febf9bF4930ad581dB008f8b0F6239C6Fc — Ante Pool
- [smart_contract] https://etherscan.io/address/0x6e1000a6088Eb3dD1493492626E556F6d9A17BD1 — Ante Pool
- [smart_contract] https://etherscan.io/address/0xE48f6A36f3712E389ce666BCEcD88BA60c30aE50 — Ante Pool
- [smart_contract] https://etherscan.io/address/0xFc2Bd420ae071a812Ea238C5916198024E00fE33 — Ante Pool
- [smart_contract] https://etherscan.io/address/0xa03492a9a663f04c51684a3c172fc9c4d7e02edc — Ante Pool Factory

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

## Impacts in scope (18)

- [smart_contract] Critical: AntePool triggers test failure workflow when underlying AnteTest did not revert or fail
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Inability for stakers or challengers to withdraw funds from the pool (except in the case of a failed Ante Test)
- [smart_contract] Critical: Insolvency
- [smart_contract] Critical: Loss of funds in Ante Pool that is not triggered by a valid withdrawal of funds by the user who deposited or settlement (in the case of a failed Ante Test)
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Incorrect loss of funds from challengers due to challenger decay mechanism  (aside from inaccuracy described above)
- [smart_contract] High: Incorrect payment to stakers from challenger decay mechanism (aside from inaccuracy described above)
- [smart_contract] High: Incorrect payout to challengers on settlement following a failed Ante Test
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] High: Withdrawal of staked funds by stakers without waiting for 24 hr window to pass following initialization of unstake
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Smart contract fails to deliver promised returns, but doesn’t lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$25,000, rewardCalculationPercentage=0, rewardModel=fixed
- [smart_contract] High: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$2,500, rewardModel=fixed
- [smart_contract] Low: fixedReward=$500, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

The following vulnerabilities are not eligible for a reward:

  - Challenger decay calculation is inaccurate and slightly overestimates the decay paid by challengers (overall error is < 1%/year even in the worst case scenario). Calculation is more accurate the more often updateDecay() is called.
  - Staker and challenger balances are slightly underestimated due to rounding issues in intermediate calculations, overall loss is small relative to total pool balance flux (< 0.1%)
  - Test verification can be frontrun by challengers who stake small amounts of ether in every pool.
  - checkTest gas usage can be unbounded as it scales linearly with number of unique challengers
  - Any exploits related to malicious actors cloning and redeploying our contracts (i.e., deploying their own version of AntePoolFactory or deploying AntePools without the use of our AntePoolFactory contract)
  - Any exploits related to using malicious AnteTests to steal/lock user funds

In addition to Immunefi’s Vulnerability Severity Classification System, Ante classifies the following vulnerabilities as follows. In case of discrepancy, the one below will be followed. 

  - Medium
    - AntePool contract consumes unbounded gas aside from (i) known scaling of checkTest gas usage with number of challengers or (ii) due to malicious AnteTests that consume unbounded gas 

Ante requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed is the bug bounty hunter's full name, scan of ID, country and a self-certification that the bug bounty hunter is not a sanctioned person or otherwise prohibited by law from receiving payment from Ante. The collection of this information will be done by the Ante team. 

Payouts are handled by the __Ante__ team directly and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

- Best practice critiquesAttacks that are already known or outlined in any audits, https://github.com/antefinance/ante-v05-core/tree/v0.5/audit

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
