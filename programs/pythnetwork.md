# Pyth Network

- Page: https://immunefi.com/bug-bounty/pythnetwork/scope/
- Max bounty: $250,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, websites_and_applications - low, websites_and_applications - medium, websites_and_applications - high, websites_and_applications - critical
- End date: (none)

## Assets in scope (9)

- [smart_contract] https://github.com/pyth-network/governance/tree/main/staking/programs/staking — Pyth Governance
- [smart_contract] https://github.com/pyth-network/pyth-crosschain/tree/main/lazer/contracts/cardano — Pyth Lazer: Cardano
- [smart_contract] https://github.com/pyth-network/pyth-crosschain/tree/main/lazer/contracts/evm — Pyth Lazer: EVM
- [smart_contract] https://github.com/pyth-network/pyth-crosschain/tree/main/lazer/contracts/sui — Pyth Lazer: Sui
- [smart_contract] https://github.com/pyth-network/pyth-crosschain/tree/main/target_chains/ethereum/contracts/contracts/entropy — Pyth Entropy
- [smart_contract] https://github.com/pyth-network/pyth-crosschain/tree/main/target_chains/ethereum/contracts/contracts/pyth — Pyth Crosschain: Ethereum
- [smart_contract] https://github.com/pyth-network/pyth-crosschain/tree/main/target_chains/solana — Pyth Crosschain: Solana
- [smart_contract] https://github.com/pyth-network/pyth-crosschain/tree/main/target_chains/sui/contracts — Pyth Crosschain: Sui
- [websites_and_applications] https://staking.pyth.network/ — Pyth Staking

## Asset notes

Specific mainnet contract addresses can be found on [https://docs.pyth.network/price-feeds/contract-addresses](https://docs.pyth.network/price-feeds/contract-addresses) and [https://docs.pyth.network/entropy/contract-addresses](https://docs.pyth.network/entropy/contract-addresses).

## Impacts in scope (30)

- [smart_contract] Critical: Arbitrarily manipulate Pyth oracle prices or other published values
- [smart_contract] Critical: Assume ownership of Pyth’s contracts in mainnet
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Locking, loss, or theft of funds staked on Pyth
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Exposure of private keys controlled by the PDA or permissionless services
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Software flaws in the on-chain program cause Pyth to publish an inaccurate price when ≥ 3/4 of the contributing publishers are accurate.
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but  doesn't lose value
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$250,000, minReward=$50,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$50,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$2,500, rewardModel=range
- [smart_contract] Low: maxReward=$2,500, minReward=$1,000, rewardModel=range
- [websites_and_applications] Critical: maxReward=$50,000, minReward=$20,000, otherImpactMaxReward=$30,000, rewardModel=range
- [websites_and_applications] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] Medium: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)

__Reward Calculation for Critical Smart Contract Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of 250 000 USDC. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted.  For the avoidance of doubt, directly affected funds calculation does not include downstream protocols or users of the Pyth protocol or any effects on the $PYTH token price.

__Reward Calculation for Critical Websites and Applications Reports__

For Critical web/apps bug reports will be rewarded with **USD 50 000**, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Unauthorized minting of tokens on-chain
- Private key or private key generation leakage leading to unauthorized access to user funds
- The impact occurs on a user facing application, generally hosted under pyth.network

All other impacts that would be classified as **Critical** would be rewarded a flat amount of **USD 30 000**.

__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attacks within the first hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 


For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Smart Contract Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded up to $50,000 USDC depending on the funds at risk, capped at the maximum high reward.  


In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

__Reward Calculation for High Websites and Applications Reports__

For High web/app impacts, the maximum reward of **USD 20 000** will only be paid out for issues that affect our main user-facing applications, generally hosted under pyth.network.

__Reward Payment Terms__

Payouts are handled by the Pyth Data Association directly and are denominated in USD. However, payments are done in USDC. 

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

***existing/default list of of out of scope impacts***

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
