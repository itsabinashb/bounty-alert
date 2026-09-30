# Kleidi

- Page: https://immunefi.com/bug-bounty/kleidi/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical
- End date: (none)

## Assets in scope (19)

- [smart_contract] https://basescan.org/address/0x146dfd96Da039FDE3B58D5964feF8E8357df2028 — BytesHelper
- [smart_contract] https://basescan.org/address/0x56b6d03b995022A612aF6a212C74902f233F52Cc — RecoverySpellFactory
- [smart_contract] https://basescan.org/address/0xCe90BA68BbcdCCe9aed1fCDDcb114d1DCdBc68C9 — TimelockFactory
- [smart_contract] https://basescan.org/address/0xE138136bFF8c6A9337805DE19177E3b29fef2783 — InstanceDeployer
- [smart_contract] https://basescan.org/address/0xFE49DD6d0CD41C4EC8F151C79f2d4019f5C5AD18 — Guard
- [smart_contract] https://basescan.org/address/0xd1db2c4A9d2BEBd56d42E59F2d90F4136164faD6 — AddressCalculation
- [smart_contract] https://etherscan.io/address/0x146dfd96Da039FDE3B58D5964feF8E8357df2028 — BytesHelper
- [smart_contract] https://etherscan.io/address/0x56b6d03b995022A612aF6a212C74902f233F52Cc — RecoverySpellFactory
- [smart_contract] https://etherscan.io/address/0xCe90BA68BbcdCCe9aed1fCDDcb114d1DCdBc68C9 — TimelockFactory
- [smart_contract] https://etherscan.io/address/0xE138136bFF8c6A9337805DE19177E3b29fef2783 — InstanceDeployer
- [smart_contract] https://etherscan.io/address/0xFE49DD6d0CD41C4EC8F151C79f2d4019f5C5AD18 — Guard
- [smart_contract] https://etherscan.io/address/0xd1db2c4A9d2BEBd56d42E59F2d90F4136164faD6 — AddressCalculation
- [smart_contract] https://immunefi.com/bug-bounty/kleidi/information/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://optimistic.etherscan.io/address/0x146dfd96Da039FDE3B58D5964feF8E8357df2028 — BytesHelper
- [smart_contract] https://optimistic.etherscan.io/address/0x56b6d03b995022A612aF6a212C74902f233F52Cc — RecoverySpellFactory
- [smart_contract] https://optimistic.etherscan.io/address/0xCe90BA68BbcdCCe9aed1fCDDcb114d1DCdBc68C9 — TimelockFactory
- [smart_contract] https://optimistic.etherscan.io/address/0xE138136bFF8c6A9337805DE19177E3b29fef2783 — InstanceDeployer
- [smart_contract] https://optimistic.etherscan.io/address/0xFE49DD6d0CD41C4EC8F151C79f2d4019f5C5AD18 — Guard
- [smart_contract] https://optimistic.etherscan.io/address/0xd1db2c4A9d2BEBd56d42E59F2d90F4136164faD6 — AddressCalculation

## Asset notes

(none)

## Impacts in scope (4)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency

## Impact notes

Deployed Instances. All Timelock, Safe, and RecoverySpell instances deployed through the in-scope factory contracts are also considered in-scope assets. However, vulnerabilities arising from user misconfiguration — such as whitelisting unsafe calldata, failing to configure a guardian, adding an unsafe module, using compromised signing keys, or setting incompatible delay parameters, or setting insecure parameters — are out of scope. See KNOWN_ISSUES.md and EDGECASES.md for documented configuration risks.

[https://github.com/solidity-labs-io/kleidi/blob/main/docs/KNOWN_ISSUES.md](https://github.com/solidity-labs-io/kleidi/blob/main/docs/KNOWN_ISSUES.md)

[https://github.com/solidity-labs-io/kleidi/blob/main/docs/EDGECASES.md](https://github.com/solidity-labs-io/kleidi/blob/main/docs/EDGECASES.md)

## Rewards

- [smart_contract] Critical: maxReward=$50,000, minReward=$5,000, rewardCalculationPercentage=10, rewardModel=range

## Reward notes

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of **USD 50 000**.  The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of **USD 5 000** is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward.
- The amount of funds at risk will be calculated with the impact of the first attack being at **100%** and then a reduction of **25%** from the amount of the first attack for every **[300 blocks]** the attack needs for subsequent attacks from the first attack, rounded down.

__Reward Payment Terms__

Payouts are handled by the Kleidi team directly and are denominated in USD. However, payments are done in USDC on Ethereum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (2)

- EDGECASES.md (https://github.com/solidity-labs-io/kleidi/blob/main/docs/EDGECASES.md)
- KNOWN_ISSUES.md (https://github.com/solidity-labs-io/kleidi/blob/main/docs/KNOWN_ISSUES.md)
