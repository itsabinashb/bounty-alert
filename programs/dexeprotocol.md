# DeXe Protocol

- Page: https://immunefi.com/bug-bounty/dexeprotocol/scope/
- Max bounty: $500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (11)

- [smart_contract] https://bscscan.com/address/0x41260f637a993ce714Ece1ee9875F489e483e9b3 — SphereXEngine
- [smart_contract] https://bscscan.com/address/0x427a1214f12117b1AD48C817c203c5CF3Eb7E7C4 — UserRegistry
- [smart_contract] https://bscscan.com/address/0x46B46629B674b4C0b48B111DEeB0eAfd9F84A1c0 — ContractsRegistry
- [smart_contract] https://bscscan.com/address/0x4fa2092E32934Dd3823E58C79ceD0e410a5B0D4b — PoolSphereXEngine
- [smart_contract] https://bscscan.com/address/0x85f86ef7E72e86BdEAb5F65e2B76A2c551f22109 — PoolFactory
- [smart_contract] https://bscscan.com/address/0x892B3292cF80CB298b7fA20D04EF4732640db404 — ERC721Expert
- [smart_contract] https://bscscan.com/address/0xB562127efDC97B417B3116efF2C23A29857C0F0B — DeXe DAO
- [smart_contract] https://bscscan.com/address/0xFEB26AAB75638440B3CEFe8B10de6118972f9C6B — PoolRegistry
- [smart_contract] https://bscscan.com/address/0xaB9d2a2347D5fF5B760C0226C52d5C673b8D9e44 — CoreProperties
- [smart_contract] https://bscscan.com/address/0xc7730074736c10ed0d3F928A10Ee4162DA9a7983 — PriceFeed
- [smart_contract] https://www.immunefi.com — Primacy of Impacts (primacy of impact)

## Asset notes

How DEXE Protocol works: [https://whitepaper.dexe.network/](https://whitepaper.dexe.network/)

## Impacts in scope (16)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$500,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is __10%__ of the funds directly affected up to a maximum of __USD 500 000__. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of __USD 10 000__ is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

  - If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attacks within the first hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

  - For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to __10%__ of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

  - High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of __USD 5 000 to USD 10 000__ depending on the funds at risk, capped at the maximum high reward. 

  - In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

__Reward Payment Terms__

Payouts are handled by the __DeXe Protocol__ team directly and are denominated in __USD__. All medium rewards will be paid out in __USDC__. All high rewards will be paid out in $DeXe. All critical rewards will be paid out in $DeXe with a 6-month linear vesting schedule.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
