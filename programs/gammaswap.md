# GammaSwap

- Page: https://immunefi.com/bug-bounty/gammaswap/scope/
- Max bounty: $40,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical
- End date: (none)

## Assets in scope (27)

- [smart_contract] https://arbiscan.io/address/0x3A46d5F9166EBd7844758a9c3525a84B824cFcA9#code — VaultRepayStrategy
- [smart_contract] https://arbiscan.io/address/0x3b72616376652cc82f17dd7a9b58f71cdb3b98b0 — PositionManager (Proxy)
- [smart_contract] https://arbiscan.io/address/0x3dc7860deba77aa3a49b4d65c056156012067477#code — BeaconProxyFactory
- [smart_contract] https://arbiscan.io/address/0x3f7cf127bf565d3dba9cb3e69a76b1347ac673f8#code — GS
- [smart_contract] https://arbiscan.io/address/0x4aA486351a665921175E3ca1C328e90266cC3E10#code — VaultBorrowStrategy
- [smart_contract] https://arbiscan.io/address/0x4c02a44be2f9e808bd0728b2e52c616138180f98#code — Airdrop
- [smart_contract] https://arbiscan.io/address/0x57e4Cc794949FaA564521352f816dd13B14227C8#code — RewardDistributor
- [smart_contract] https://arbiscan.io/address/0x5CfB6Fc76e270e35Da7aB9bDEB8B97f64b4A59bf#code — VaultExternalRebalanceStrategy
- [smart_contract] https://arbiscan.io/address/0x5FbE219e88f6c6F214Ce6f5B1fcAa0294F31aE1b#code — DeltaSwapRouter02
- [smart_contract] https://arbiscan.io/address/0x63c531ffed7e17f8adca4ed490837838f6fa1b66#code — MinimalBeaconProxy
- [smart_contract] https://arbiscan.io/address/0x755F72D7F22eFaeD6E00E589a8C7bD95A666fEF0#code — DeltaSwapPair
- [smart_contract] https://arbiscan.io/address/0x79297AD127f5bA287053789e2FEB4DE5Ba2C71A0#code — VaultRebalanceStrategy
- [smart_contract] https://arbiscan.io/address/0x878269d2ee6417edcdc030961618cc5259229367#code — BonusDistributor
- [smart_contract] https://arbiscan.io/address/0xB07772B295DD04398C1aaF39E57E04527a92b2E8#code — VaultExternalLiquidationStrategy
- [smart_contract] https://arbiscan.io/address/0xB953CeaDb508e24C6338325980421c8cA4393241#code — VaultLiquidationStrategy
- [smart_contract] https://arbiscan.io/address/0xC4993bf95fB30E5930C7Dc73604829993bb51243#code — Vester
- [smart_contract] https://arbiscan.io/address/0xCb85E1222f715a81b8edaeB73b28182fa37cffA8#code — DeltaSwapFactory
- [smart_contract] https://arbiscan.io/address/0xFD513630F697A9C1731F196185fb9ebA6eAAc20B#code — GammaPoolFactory
- [smart_contract] https://arbiscan.io/address/0xFF0C5047C6a96dD211C849fbDADD6729D016Dd04#code — VaultBatchLiquidationStrategy
- [smart_contract] https://arbiscan.io/address/0xa9379431C71c276411D9b838e70A50BBa274a363 — VaultShortStrategy
- [smart_contract] https://arbiscan.io/address/0xad64702F5556Bf897d4BA30Cc8e6e54891095cCC#code — LockableMinimalBeacon
- [smart_contract] https://arbiscan.io/address/0xb08d8becab1bf76a9ce3d2d5fa946f65ec1d3e83#code — GSTimelockController
- [smart_contract] https://arbiscan.io/address/0xbd6e02c05a274d77ba2958e4db93692ee12b311c#code — VaultGammaPool
- [smart_contract] https://arbiscan.io/address/0xc58221784f53b09f5ca2fa2d575e7a0f9af24ae4#code — StakingRouter
- [smart_contract] https://arbiscan.io/address/0xc5fa429C0492821d928D3ba03EB238E903BeBE03#code — CPMMMath
- [smart_contract] https://arbiscan.io/address/0xc964d02f1c11e1bb1156e7c270687d6080661e9c#code — FeeTracker
- [smart_contract] https://arbiscan.io/address/0xd04FBe195Be1313fc816D59E3c457eb6e0aD4088#code — RewardTracker

## Asset notes

All code of GammaSwap can be found at [https://github.com/gammaswap.](https://github.com/gammaswap) Documentation for the assets provided in the table can be found at [https://sneaky-nigella-b2d.notion.site/GammaSwap-Architecture-Overview-5c0eb0f7c92d41009cca81c995b8cb8e](https://sneaky-nigella-b2d.notion.site/GammaSwap-Architecture-Overview-5c0eb0f7c92d41009cca81c995b8cb8e)  

Other helpful links include:
- Attack Vectors & Countermeasures - [https://sneaky-nigella-b2d.notion.site/Attack-Vectors-Countermeasures-6e651c8e15484c539909a56d1ea41dba](https://sneaky-nigella-b2d.notion.site/Attack-Vectors-Countermeasures-6e651c8e15484c539909a56d1ea41dba)
- Flash Loan CFMM Fee Liquidation Attack - [https://sneaky-nigella-b2d.notion.site/Flash-Loan-CFMM-Fee-Liquidation-Attack-7001d6004f7c452d884d6ae17fd311d7](https://sneaky-nigella-b2d.notion.site/Flash-Loan-CFMM-Fee-Liquidation-Attack-7001d6004f7c452d884d6ae17fd311d7)
- Rebalance Formulas - [https://sneaky-nigella-b2d.notion.site/Rebalance-Formulas-20096ccac7684315b8c88a26337c891a ](https://sneaky-nigella-b2d.notion.site/Rebalance-Formulas-20096ccac7684315b8c88a26337c891a)
- Interest Rate Formula - [https://sneaky-nigella-b2d.notion.site/Interest-Rate-d2c06c248f454dd4856c43079f257fb7?pvs=4 ](https://sneaky-nigella-b2d.notion.site/Interest-Rate-d2c06c248f454dd4856c43079f257fb7?pvs=4)
- Loan to Value Ratio (How debt collateralization is calculated) - [https://sneaky-nigella-b2d.notion.site/LTV-Ratio-2e5f873eb4eb4d8cbf1439c640dd3ffc](https://sneaky-nigella-b2d.notion.site/LTV-Ratio-2e5f873eb4eb4d8cbf1439c640dd3ffc)
- Dynamic Origination Fee Logic - [https://sneaky-nigella-b2d.notion.site/Dynamic-Origination-Fee-1b0e7c98b5144ac4b9ee76dde18402c7](https://sneaky-nigella-b2d.notion.site/Dynamic-Origination-Fee-1b0e7c98b5144ac4b9ee76dde18402c7)
- Transfer Fees Attack Discovered on October 2023 - https://medium.com/gammaswap-labs/immunefi-bug-report-analysis-contract-re-deployment-283cbdfa0beb
- General Protocol Description - https://medium.com/gammaswap-labs/gammaswap-protocol-6a4430e4b0ad
- Staking Contracts Documentation - https://docs.google.com/presentation/d/1uUCY6km1kriJ7r6x88FiZnz9RjSxZaeBt29cdwySSb4/edit#slide=id.p

## Impacts in scope (3)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$40,000, minReward=$15,000, rewardCalculationPercentage=10, rewardModel=range

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Reward Calculation for Critical Level Reports__

For critical Smart Contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 40,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 15,000 is to be rewarded in order to incentivize security researchers against withholding a bug report.   

__Repeatable Attack Limitations__

In cases of repeatable attacks for smart contract bugs, only the first attack will be counted, regardless of whether the smart contract is upgradable, pausable, or killable.

__Reward Calculation for High Level Reports__

High smart contract vulnerabilities will be capped at up to 100% of the funds affected. There is a minimum reward of __$5,000 USD__. In the event of temporary freezing, the reward doubles for every additional  5  blocks that the funds or NFTs could be temporarily frozen, rounded down to the nearest multiple of 5, up to the hard cap of USD 10,000.  

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs acknowledged below are not eligible for any reward through the bug bounty program. 
- (Fail promised returns) Arbitrum block number mismatch with mainnet means that the next mainnet block update in arbitrum is usually 4 numbers higher than the previous one because Arbitrum syncs with mainnet every 1 minute. So a loan can be opened and closed in that timeframe to avoid paying an interest rate. However, they will still pay an origination fee.
- (Fail promised returns) We say GammaSwap performs as good or better than the undeerlying CFMM. However, it is possible for the CFMM to outperform GammaSwap. GammaSwap’s yield is capped at 250% and the return calculated as an annualized value from the yield since the last update. Therefore, if there are many transactions or one really large transaction in the CFMM and subsequently one in GammaSwap soon after so that the annualized yield of the CFMM during that period (calculated by GammaSwap) is greater than 250% then the CFMM will outperform GammaSwap because GammaSwap’s rates are capped at 250%. This means how much a GS LP token represents in CFMM LP tokens would decrease after that update. However, over a longer period since CFMM’s fees don’t sustain that level of activity constantly, such event is short lived and GammaSwap will outperform the CFMM. 
- (Fail promised returns) Protocol fees in the CFMM can make the cfmm fee index be less than 1. This can make the value of the liquidity of GS LP token holders seem greater than it really is before the protocol fee in the CFMM is charged. The CFMM protocol fees in UniswapV2 and its forks are charged during the call of the mint() and burn() functions. Therefore, they always update to accurate values after transactions in GammaSwap that call the mint and burn functions of the CFMM (borrow, repay, liquidate, depositReserves, withdrawReserves). This does not create a benefit to anyone, other than the illusion that the returns (to liquidity suppliers) and expenses (to liquidity borrowers) are greater than they really are prior to the payment of accrued protocol fees. A calculation of the returns or costs after the protocol fee is paid is always accurate.
- (Fail promised returns) Borrowing more liquidity has to be done in increments of the minBorrow amount. If minBorrow amount is of significant size then there’s not much granularity in borrowing liquidity. It doesn’t affect returns in the platform but it does affect the ease of use of the platform.
- (Fail promised returns) Long volatility buyers (liquidity borrowers) may show a large profit but when deciding to close their positions to cash in, their profits may be smaller than they expected. The reason is because rebalancing the collateral to repay liquidity debt can have substantial market impact that diminishes their profits. However, this does not create protocol insolvency. The positions are always capable of repaying the liquidity debts as long as they are overcollateralized enough to recover the liquidity borrowed and pay the trading fees in the CFMM to rebalance the collateral.
- (Fail promised returns, Temporary Freezing of Funds) A user may choose to LP into GammaSwap to become most of the liquidity deposited in the pool. Then borrow most of the liquidity in the pool at a relatively low origination fee. At last he may withdraw enough liquidity that he has LPed to leave the pool locked so nobody else can withdraw and spike up interest rates to 250%. This attack only affects liquidity borrowers, benefits LPs with high yields (although prevents them from withdrawing), and it’s a net cost to the attacker because 10% of the yield LPs receive goes to the protocol, and the attacker is paying most of this yield through interest in his large loan, while not receiving back 100% of the yield he earned. Liquidation rewards on undercollateralized loans are set at 25basis points of the collateral. So the attack may be worth it in some rare instances where there are enough loans close to liquidation that the attacker feels confident in being able to liquidate to cover his losses for spiking interest rates. However, the high rates may attract other LPs to provide liquidity, decreasing the time to liquidation of at risk loans. Also if these at risk loans are closed by their owners before the become undercollateralized then it is a loss to the attacker. Undercollateralization doesn’t mean bad debt in this case either. The current parameters leave a buffer of 50 basis points before reaching a bad debt scenario. That’s about 17.5 hours before a loan becomes bad debt at a constant interest rate of 250%
- (Fail promised returns) A block stuffing attack may be performed to prevent liquidation transactions, until a GamaPool starts accruing bad debt. The cost of such an attack is of no benefit to the attacker, and given costs to liquidate being 10 cents currently on arbitrum, with the fee reward being multiples higher. The attacker would have to spike up the fees many times for a sustained period of time to make the attack successful. Unlikely to be economically viable for long periods of time.
- (Fail promised returns) Since GammaPools track the liquidity of each loan as well as the sum of that whole liquidity as two separate numbers that compound separately using the same index. Mismatches may arise due to rounding issues that can accrue over time. The effect only affects the last person closing a loan. The result is that the payment of the last loan causes a write down, even if not undercollateralized, so that LPs do not earn the amount it was calculated they earned. The last person closing the loan is also not charged anymore than he was already aware he owed. These rounding differences however are so small and accrue at such a slow rate (e.g. grow by 1x10^-17 per day) that are unlikely to become a problem within any realistic timeframe.
- (Fail promised returns) Since solidity does not have native support for decimals or square root formulas, some of the rebalancing calculations may be off a bit due to rounding issues again and liquidity borrowers may get slightly different results from what they expect during rebalancing or closing of their positions. The rounding differences however are usually seen at levels much less than a basis point so they’re usually expected to be very small and more prevalent in tokens that have smaller decimals, such as USDC and USDT which only use 6 decimals. But even in these scenarios the rounding errors lead to differences in outcome of around a couple of basis points.
- (Fail promised returns) The LP token can be inflated away (e.g. through donations to the CFMM as in UniswapV2 and clones). When this happens it may change the actual reserve tokens a GS LP token represents due to rounding issues. This can lead to gains and losses to different LPs and borrowers. The effects are expected to be small except in early periods when a pool is first created.
- (Fail promised returns) Liquidations can lead to the loss of the entire profit of a loan under certain conditions, especially the more profitable a position is, through CFMM price manipulation. Therefore, borrowers should always try to close their positiosn and not rely on liquidators to close their positions for them. However, this does not lead to losses of LP funds. Since liquidation is an undesirable outcome for a loan, the loss to profitable borrowers is not considered an issue.
- (Fail promised returns) The code of the assets in scope for GammaPools, PositionManager, and Staking contracts are implementation contracts. Therefore, the implementation contracts may have security weaknesses, such as not initialized or initialized improperly. Those security issues are not part of this bounty. What is relevant is whether the proxy contracts that use those implementation contracts have security weaknesses using the current implementation contracts. In addition, proxy contracts might have been initialized with previous implementation contracts and therefore the initialization logic of the current implementation contracts may not be relevant anymore if a proxy contract can’t be initialized again. However, if a proxy contract is expected to be created again using the same implementation contract, as in the case of GammaPools for new pairs, or new staking pools, then initialization issues with the current implementation contract are relevant to this bounty.
- (Fail promised returns) The code regarding staking for loans in the staking contracts is not part of this bounty unless it could affect the staking contracts for LP tokens. The reason is because we don’t plan to use the staking contracts for loan staking anymore. So there will not be any staking pools for loans. We will only create staking pools for LP tokens.
- (Fail promised returns) The liquidityEMA and related parameters in DeltaSwap can be manipulated to help a token swapper avoid paying a transaction fee. This however, is no longer relevant since DeltaSwap’s parameters are now set to always charge a trading fee, and the GammaPool interest rate model depends on DeltaSwap always paying a trading fee. Therefore, we would never change this logic to not charge a trading fee.(Fail promised returns) 


__Previous Audits__

GammaSwap has provided these completed audit review reports for reference. Any unfixed vulnerability mentioned in these reports are not eligible for a reward.
- [GammaSwap_Labs_Core_Strategies_and_Periphery_Smart_Contract_Security_Audit_Report_Halborn_Final.pdf](https://drive.google.com/file/d/1ZT1oaNxvXG1NoQWEhJHhq3OkBd16nGth/view?usp=sharing)
- [GammaSwap Balancer Implementation - Zellic Audit Report March 14, 2023.pdf](https://drive.google.com/file/d/1RSi1IXCQt2FqK8qL6wn1ojDR2uQcJWS0/view?usp=sharing)
- [GammaSwap Strategies - Zellic Audit Report March 27, 2023.pdf](https://drive.google.com/file/d/1tjRZwX7vApS2SALbnrZYRQ-gASM2YzNs/view?usp=sharing)
- [GammaSwap - Zellic Audit Report June 5, 2023.pdf](https://drive.google.com/file/d/18pgiYsO3GM2fDAPtgnkQ126LdLuAuNnD/view?usp=sharing)
- [GammaSwap - Zellic Audit Report August 24, 2023.pdf](https://drive.google.com/file/d/1kBpi-jYXHlSgjM3LlnOKiySrNfKU4euf/view?usp=sharing)
- [Deltaswap - Zellic Audit Report.pdf](https://drive.google.com/file/d/1QfEbGNTNHkRRjZkeSXuyTJfF9dvMlucF/view)
- [Staking - Zellic Audit Report.pdf](https://drive.google.com/file/d/1e8AiZasbViKVDsiwSHyQklG2OyOon2lF/view?pli=1)

__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
- Smart Contract, Critical Severity Level
- Smart Contract, High Severity Level

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules) Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

Payouts are handled by the GammaSwap team directly and are denominated in USD. However, payments are done in USDC.

## Out of scope (program-specific)

- Best practice recommendations
- Impact in UniswapV2 code for DeltaSwap fork (Unless such code was materially changed by GammaSwap or used by the GammaSwap contracts)
- Impacts affecting only the state of implementation contracts
- Impacts affecting the value of parameters used to determine whether DeltaSwap will charge a trading fee or not (e.g. liquidityEMA, liquidityTradedEMA, etc.) Because DeltaSwap is set up to always charge a trading fee and the current GammaPool implementation requires that it must always charge a trading fee.
- GS, GSTimelockController, and Staking contracts are only eligible for at most high severity level rewards.
- Airdrop contract is not eligible for medium level bugs.

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
