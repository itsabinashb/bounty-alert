# mETH Protocol

- Page: https://immunefi.com/bug-bounty/mETH/scope/
- Max bounty: $500,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (10)

- [smart_contract] https://etherscan.io/address/0x1766be66fBb0a1883d41B4cfB0a533c5249D3b82 — ReturnsAggregator
- [smart_contract] https://etherscan.io/address/0x29Ab878aEd032e2e2c86FF4A9a9B05e3276cf1f8 — Pauser
- [smart_contract] https://etherscan.io/address/0x38fDF7b489316e03eD8754ad339cb5c4483FDcf9 — UnstakeRequestsManager
- [smart_contract] https://etherscan.io/address/0x8735049F496727f824Cc0f2B174d826f5c408192 — Oracle
- [smart_contract] https://etherscan.io/address/0x92e56d2146D54d5AEcB25CA36c89D027a6ea0D90 — OracleQuorumManager
- [smart_contract] https://etherscan.io/address/0xD4e11C28E04c0c2bf370b7a9989498B7eA02493f — ConsensusLayerReceiver
- [smart_contract] https://etherscan.io/address/0xD6E4aA932147A3FE5311dA1b67D9e73da06F9cEf — ExecutionLayerReceiver
- [smart_contract] https://etherscan.io/address/0xd5F7838F5C461fefF7FE49ea5ebaF7728bB0ADfa — mETH Token L1
- [smart_contract] https://etherscan.io/address/0xe3cBd06D7dadB3F4e6557bAb7EdD924CD1489E8f — Staking
- [smart_contract] https://explorer.mantle.xyz/address/0xcDA86A272531e8640cD7F1a92c01839911B90bb0 — mETH Token L2

## Asset notes

(none)

## Impacts in scope (9)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of staked funds
- [smart_contract] High: Acquiring owner/admin rights without contract’s owner/admin action
- [smart_contract] High: Permanent freezing of unclaimed or tokenized staking yield
- [smart_contract] High: Protocol insolvency
- [smart_contract] High: Theft of unclaimed yield or tokenized staking yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Susceptibility to frontrunning
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$500,000, minReward=$100,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$20,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 500 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 100 000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attacks within the first hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

__Reward Calculation for High Level Reports__

- High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are considered at the full amount of funds at risk, capped at the maximum high reward. This is to incentivize security researchers to uncover and responsibly disclose vulnerabilities that may have not have significant monetary value today, but could still be damaging to the project if it goes unaddressed.   
- In the event of temporary freezing, the reward increases at a multiplier of two from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lenghents, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.    

__Reward Payment Terms__

Payouts are handled by the mETH Protocol team directly and are denominated in USD. However, payments are done in USDC

## Out of scope (program-specific)

- Any issues identified in Published Audits [https://docs.mantle.xyz/meth/security/audits](https://docs.mantle.xyz/meth/security/audits)
- Impact of future improper configuration of contracts that are not deployed
- Impacts from an assumption of a malicious majority of oracles
- Gas optimization

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
