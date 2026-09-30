# Pareto Credit

- Page: https://immunefi.com/bug-bounty/pareto/scope/
- Max bounty: $50,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (27)

- [smart_contract] https://docs.pareto.credit/developers/addresses/product/credit-vaults
- [smart_contract] https://etherscan.io/address/0x06975bB418EFFB0029fe278A6fA15B92bb97496F — Bastion Trading Vault Strategy (Ethereum)
- [smart_contract] https://etherscan.io/address/0x0b4F695B05902efc14344d19ED1d0B0E061C8A3E — Fasanara Digital Vault Queue (Ethereum)
- [smart_contract] https://etherscan.io/address/0x14B8E918848349D1e71e806a52c13D4e0d3246E0 — Adaptive Frontier Vault Contract (Ethereum)
- [smart_contract] https://etherscan.io/address/0x17E9Ab2992dfecBe779a06A92a6cDB9fE6aEeEf3 — FalconX Vault Strategy (Ethereum)
- [smart_contract] https://etherscan.io/address/0x2Cd361544a3647Ab16A983cA2576f084abEA80D0 — TwoPrime Vault Queue (Ethereum)
- [smart_contract] https://etherscan.io/address/0x338e0a8008364a4d5139cB49E00e93bDb51290d6 — TwoPrime Vault Contract (Ethereum)
- [smart_contract] https://etherscan.io/address/0x3Fc0265E92EeafED0cCd9F8621764Ce0981882cE — RockawayX Vault Strategy (Ethereum)
- [smart_contract] https://etherscan.io/address/0x433D5B175148dA32Ffe1e1A37a939E1b7e79be4d — FalconX Vault Contract (Ethereum)
- [smart_contract] https://etherscan.io/address/0x4462eD748B8F7985A4aC6b538Dfc105Fce2dD165 — Bastion Trading Vault Contract (Ethereum)
- [smart_contract] https://etherscan.io/address/0x45054c6753b4bce40c5d54418dabc20b070f85be — Fasanara Digital Vault LP Token (Ethereum)
- [smart_contract] https://etherscan.io/address/0x5cC24f44cCAa80DD2c079156753fc1e908F495DC — FalconX Vault Queue (Ethereum)
- [smart_contract] https://etherscan.io/address/0x5eCF8bF9eae51c2FF47FAc8808252FaCd8e36797 — Adaptive Frontier Vault Queue (Ethereum)
- [smart_contract] https://etherscan.io/address/0x74E862277B5BEC233E2f1b0272CE1e215462507a — TwoPrime Vault Strategy (Ethereum)
- [smart_contract] https://etherscan.io/address/0x7A4E728B9fEbec04de724821eb9056828C2D1c06 — M1 Capital Vault Contract (Ethereum)
- [smart_contract] https://etherscan.io/address/0x9372a533Db980bD9591D3c7C457dC220Bf1A0Ab4 — M1 Capital Vault LP (Ethereum)
- [smart_contract] https://etherscan.io/address/0x9cF358aff79DeA96070A85F00c0AC79569970Ec3 — RockawayX Vault Contract (Ethereum)
- [smart_contract] https://etherscan.io/address/0xBC6cffAFC8F98d7DF780cE05fA55e14781C1C14D — RockawayX Vault Queue (Ethereum)
- [smart_contract] https://etherscan.io/address/0xC26A6Fa2C37b38E549a4a1807543801Db684f99C — FalconX Vault LP Token (Ethereum)
- [smart_contract] https://etherscan.io/address/0xC35D078092872Ec1f2ae82bcd6f0b6b89F0850de — Fasanara Digital Vault Strategy (Ethereum)
- [smart_contract] https://etherscan.io/address/0xC49b4ECc14aa31Ef0AD077EdcF53faB4201b724c — Bastion Trading Vault LP Token (Ethereum)
- [smart_contract] https://etherscan.io/address/0xD1624bb76743dd8dC8D8043246e7338A5CD23772 — TwoPrime Vault LP (Ethereum)
- [smart_contract] https://etherscan.io/address/0xa30bE796FB2BAbF9228359E86A041c14e29f86Fc — Adaptive Frontier Vault Strategy (Ethereum)
- [smart_contract] https://etherscan.io/address/0xae7913c672c7F1f76C2a1a0Ac4de97d082681234 — Adaptive Frontier Vault LP Token (Ethereum)
- [smart_contract] https://etherscan.io/address/0xf6223C567F21E33e859ED7A045773526E9E3c2D5 — Fasanara Digital Vault Contract (Ethereum)
- [smart_contract] https://etherscan.io/address/0xf6b24eC487680Aa3716f0DAEfB9264419b429384 — M1 Capital Vault Strategy (Ethereum)
- [smart_contract] https://etherscan.io/token/0xEC6a70F62a83418c7fb238182eD2865F80491a8B — RockawayX Vault LP Token (Ethereum)

## Asset notes

Only Senior Best Yield contracts will be considered in scope for the Best Yield. Governance and Utilities and ERC-4626 wrappers contracts are not covered under this bug bounty program. **Paused** contracts and contract market as **Deprecated**/**Decommissioned** in doc are not considered in scope

## Impacts in scope (8)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Miner-extractable value (MEV) if can freeze funds or cause protocol insolvency
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds

## Impact notes

For Credit Vaults  contract marked in the description as “Queue” should be considered out of scope. Paused contracts and contract market as Deprecated/Decommissioned in doc are not considered in scope

## Rewards

- [smart_contract] Critical: maxReward=$50,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: maxReward=$20,000, rewardModel=up_to
- [smart_contract] Medium: maxReward=$5,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System 2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2/). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit. 

The final reward for critical bounty payouts is capped at 10% of the funds at risk based on the vulnerability reported.

PoC is required for all levels.

Theft of yield or interest is considered as Medium but may be considered High depending on the amount of funds at risk.

Best practices critiques are not accepted under this program. 

The likelihood of exploitability is also taken into consideration in the
determination of the final payout amount based on the severity of the bug
reported according to the table below:

| | Medium | High | Critical |
|  :-- | :-- | :-- | :-: |
| Almost Certain | $5,000 | $20,000 | $50,000 |
| Likely | $3,000 | $10,000 | $25,000 | 
| Possible | $1,000 | $5,000 | $10,000 |
| Unlikely  | $500 | $1,000 | $5,000 |
| Almost Possible | $100 | $500 | $1,000 |

Payouts are handled by **Idle Finance** governance directly and are denominated
in **USD**. Payouts under $10,000 are done in **USDC**. When payouts are over
$10,000, the first $10,000 is paid in **USDC** and then the rest are paid in
**IDLE** up to the total of $50 000.

## Out of scope (program-specific)

- Best practice critiques
- Freezing of Funds after a borrower defaults
- Attacks the are considering either the manager or the owner a malicious actor
- Everything acknowledged on previous audits


Only Senior Best Yield contracts will be considered in scope for the Best Yield. Governance and Utilities and ERC-4626 wrappers contracts are not covered under this bug bounty program. **Paused** contracts and contract market as **Deprecated**/**Decommissioned** in doc are not considered in scope

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
