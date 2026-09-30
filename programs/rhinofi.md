# Rhino.fi

- Page: https://immunefi.com/bug-bounty/rhinofi/scope/
- Max bounty: $2,000,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (9)

- [smart_contract] https://arbiscan.io/address/0x10417734001162ea139e8b044dfe28dbb8b28ad0#code — ARB Bridge
- [smart_contract] https://arbiscan.io/address/0x15ca1fC728Cce7cd06151C8007e89dEe70260228#code — ARB MultiSig
- [smart_contract] https://bscscan.com/address/0x7Af3828c0B061552AF3479806Add982eEf04f0c8#code — BSC MultiSig
- [smart_contract] https://bscscan.com/address/0xB80A582fa430645A043bB4f6135321ee01005fEf#code — BSC Bridge
- [smart_contract] https://explorer.zksync.io/address/0x1fa66e2B38d0cC496ec51F81c3e05E6A6708986F#contract — zkSync Bridge
- [smart_contract] https://optimistic.etherscan.io/address/0x0bCa65bf4b4c8803d2f0B49353ed57CAAF3d66Dc — Smart-Contract Optimism Bridge
- [smart_contract] https://polygonscan.com/address/0x249aAbb1d67A76404Cc1197fa37ADAf358B1E212#code — MATIC MultiSig
- [smart_contract] https://polygonscan.com/address/0xba4eee20f434bc3908a0b18da496348657133a7e#code — MATIC Bridge
- [smart_contract] https://zkevm.polygonscan.com/address/0x65A4b8A0927c7FD899aed24356BF83810f7b9A3f#code — zkEVM Bridge

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

Though only the proxy contracts are listed as in-scope, current implementation and any further updates to the implementation contracts are considered in scope. When reporting a bug, please make sure to select the relevant proxy smart contract as the target. 

If an impact can be caused to any other asset managed by Rhino.fi that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project. This only applies to Critical impacts.

No assumption can be made of access to authorized accounts. Such assumption will nullify the report

## Impacts in scope (17)

- [smart_contract] Critical: Any governance voting result manipulation that could lead to theft of funds
- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties. This must be an exploit which can be applied to steal funds from any user under normal circumstances.
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield. This must be an exploit which can be applied to steal funds from any user under normal circumstances.
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Direct theft of a user funds
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Medium: Temporary freezing of funds for other users for at least 28 days
- [smart_contract] Low: Block stuffing for profit
- [smart_contract] Low: Denial of service preventing Operator interaction with smart contracts
- [smart_contract] Low: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Low: Theft of gas

## Impact notes

No assumption can be made of access to authorized accounts. Such assumption will nullify the report

## Rewards

- [smart_contract] Critical: maxReward=$2,000,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$2,000, rewardModel=range
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the  [Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported. 

All Smart Contract bug reports require a PoC to be eligible for a reward. Explanations and statements are not accepted as PoC and code is required.

For critical Smart Contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 2,000,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 100,000 is to be rewarded in order to incentivize security researchers against withholding a bug report.  
All High and Medium rewards for the project bug bounty program are scaled based on an internally established team criteria, taking into account the exploitability of the bug, the impact it causes, and the likelihood of the vulnerability presenting itself, which is especially factored in with bug reports requiring multiple conditions to be met that are currently not in-place. However, there is a minimum reward for each severity level, rewards will be provided at the determined fair value by the team depending on these conditions, assuming that the bug report is in-scope of the bug bounty program.

The following vulnerabilities relating to those contracts are not eligible from this specific bounty, but can be submitted instead to [https://immunefi.com/bounty/starkex/](https://immunefi.com/bounty/starkex/):

- [https://github.com/starkware-libs/starkex-contracts/tree/master/audit](https://github.com/starkware-libs/starkex-contracts/tree/master/audit) 
- All vulnerabilities found in any audit documents in [https://github.com/rhinofi/contracts_public](https://github.com/rhinofi/contracts_public)

Payouts are handled by the __rhino.fi__ team directly and are denominated in USD. However, payouts are done in __USDT__ and __USDC__, with the choice of the ratio at the discretion of the team.

## Out of scope (program-specific)

- Best practice critiques
- Miner-extractable value (MEV)
- Smart contract unable to operate due to lack of token funds 
- Non-exploitable re-entrancy (no state change)
- Defects not exploitable in compiler version

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
