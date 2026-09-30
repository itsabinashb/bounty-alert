# Arkadiko

- Page: https://immunefi.com/bug-bounty/arkadiko/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, websites_and_applications - critical
- End date: (none)

## Assets in scope (13)

- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-token?chain=mainnet — DIKO
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-data-v1-1?chain=mainnet — Vaults data
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-helpers-v1-1?chain=mainnet — Vaults Helpers
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-manager-v1-2?chain=mainnet — Vaults Manager
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-operations-v1-3?chain=mainnet — Vaults Operations
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-pool-active-v1-1?chain=mainnet — Vaults Pool Active
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-pool-fees-v1-1?chain=mainnet — Vaults Pool Fees
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-pool-liq-v1-2?chain=mainnet — Vaults Pool Liq
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-sorted-v1-1?chain=mainnet — Vaults Sorted
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.arkadiko-vaults-tokens-v1-1?chain=mainnet — Vaults Token
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.usda-token?chain=mainnet — USDA
- [smart_contract] https://explorer.hiro.so/txid/SP2C2YFP12AJZB4MABJBAJ55XECVS7E4PMMZ89YZR.wstx-token?chain=mainnet — WSTX
- [websites_and_applications] https://app.arkadiko.finance — Arakdiko App

## Asset notes

(none)

## Impacts in scope (18)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:  Modifying transaction arguments or parameters, Substituting contract addresses, Submitting malicious transactions
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:   Changing registration information, Commenting, Voting, Making trades, Withdrawals, etc.

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Critical: maxReward=$25,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the[ Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100 000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 20 000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.


__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 


For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of USD 1 000 to USD 20 000 depending on the funds at risk, capped at the maximum high reward.  

In the event of temporary freezing, the reward doubles from the full frozen value for every additional [24h] that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

For critical web/apps bug reports will be rewarded with USD 25 000, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of USD 5 000. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Reward Payment Terms__

Payouts are handled by the Arkadiko team directly and are denominated in USD. However, payments are done in USDC on Ethereum

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
