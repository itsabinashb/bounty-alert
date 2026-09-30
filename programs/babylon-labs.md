# Babylon Labs

- Page: https://immunefi.com/bug-bounty/babylon-labs/scope/
- Max bounty: $500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Blockchain/DLT
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, blockchain_dlt - low
- End date: (none)

## Assets in scope (16)

- [blockchain_dlt] https://github.com/babylonlabs-io/babylon — Babylon Genesis chain node
- [blockchain_dlt] https://github.com/babylonlabs-io/covenant-emulator/tree/release/v0.15.x — Covenant Emulator
- [blockchain_dlt] https://github.com/babylonlabs-io/covenant-emulator/tree/release/v0.16.x — Covenant Emulator Signer Program
- [blockchain_dlt] https://github.com/babylonlabs-io/finality-provider/tree/release/v2.x — Finality Provider Tool Set
- [blockchain_dlt] https://github.com/babylonlabs-io/staking-expiry-checker/tree/release/v1.x — Staking Expiration Checker Micro-Service
- [blockchain_dlt] https://github.com/babylonlabs-io/staking-queue-client/tree/release/v1.x — Staking Queue Client
- [blockchain_dlt] https://github.com/babylonlabs-io/vigilante/tree/release/v0.24.x — Vigilante
- [blockchain_dlt] https://immunefi.com — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://github.com/babylonlabs-io/babylon-staking-indexer/releases/tag/v3.0.2 — Babylon Genesis and Bitcoin Indexer
- [websites_and_applications] https://github.com/babylonlabs-io/babylon-toolkit/tree/simple-staking/v1.4.6/packages/babylon-core-ui — Core UI
- [websites_and_applications] https://github.com/babylonlabs-io/babylon-toolkit/tree/simple-staking/v1.4.6/packages/babylon-proto-ts — Babylon Proto Libraries
- [websites_and_applications] https://github.com/babylonlabs-io/babylon-toolkit/tree/simple-staking/v1.4.6/packages/babylon-wallet-connector — Wallet Connect
- [websites_and_applications] https://github.com/babylonlabs-io/babylon-toolkit/tree/simple-staking/v1.4.6/services/simple-staking — Staking dApp
- [websites_and_applications] https://github.com/babylonlabs-io/btc-staking-ts/releases/tag/v2.8.2 — TypeScript BTC Staking Library
- [websites_and_applications] https://github.com/babylonlabs-io/staking-api-service/releases/tag/v3.0.3 — Staking API Service
- [websites_and_applications] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

For the Babylon repository, the code considered in scope is the code included in the latest official release published at the time a report is submitted.

Babylon Labs’ codebase can be found at [https://github.com/babylonlabs-io](https://github.com/babylonlabs-io). Documentation and further resources can be found on [https://docs.babylonlabs.io](https://docs.babylonlabs.io).

Below are general purpose technical documentations around the Bitcoin Staking Protocol and the lock-only system operated by the current testnet. Documentation on individual components of the system can be found in the component repositories.

- Our documentations website: [https://docs.babylonlabs.io](https://docs.babylonlabs.io)

__Bitcoin Staking Protocol and Litepaper:__ 
- [https://docs.babylonlabs.io/guides/research/btc_staking_litepaper/](https://docs.babylonlabs.io/guides/research/btc_staking_litepaper/)

__Introductory reading:__ 

Bitcoin staking 101 Series:

- [https://babylonlabs.io/blog/what-is-bitcoin-staking](https://babylonlabs.io/blog/what-is-bitcoin-staking)
- [https://babylonlabs.io/blog/technical-preliminaries-of-bitcoin-staking](https://babylonlabs.io/blog/technical-preliminaries-of-bitcoin-staking)
- [https://babylonlabs.io/blog/babylon-s-bitcoin-staking-contract](https://babylonlabs.io/blog/babylon-s-bitcoin-staking-contract)

__Bitcoin Staking Scripts:__ 
- [https://github.com/babylonlabs-io/babylon/blob/release/v1.x/docs/staking-script.md](https://github.com/babylonlabs-io/babylon/blob/release/v1.x/docs/staking-script.md)

__Creating Bitcoin Staking Transactions:__ 
- [https://github.com/babylonlabs-io/babylon/blob/release/v1.x/docs/transaction-impl-spec.md](https://github.com/babylonlabs-io/babylon/blob/release/v1.x/docs/transaction-impl-spec.md)

__Registering Bitcoin Stakes__
- [https://github.com/babylonlabs-io/babylon/blob/release/v1.x/docs/register-bitcoin-stake.md](https://github.com/babylonlabs-io/babylon/blob/release/v1.x/docs/register-bitcoin-stake.md)

## Impacts in scope (32)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Leakage of EOTS private keys without the holder double-signing
- [blockchain_dlt] Critical: Permanent freezing of funds
- [blockchain_dlt] Critical: Retrieve the private key of a covenant committee member
- [blockchain_dlt] High: Avoiding slashing despite malicious behavior
- [blockchain_dlt] High: Babylon node recognizes Bitcoin Staking protocol transactions and/or signatures as valid when they are invalid.
- [blockchain_dlt] High: Causing the Bitcoin light client tracked by Babylon Genesis to diverge from the canonical Bitcoin chain by more than 100 Bitcoin (BTC) blocks under normal network throughput and capacity conditions.
- [blockchain_dlt] High: Chain halt
- [blockchain_dlt] High: Generation of invalid  EOTS keys
- [blockchain_dlt] High: Generation of invalid EOTS key signatures/ Invalid verification of EOTS key signatures
- [blockchain_dlt] High: Permanently halting the Bitcoin Staking finalization of blocks.
- [blockchain_dlt] High: Preventing a covenant signer from activating staking requests indefinitely.
- [blockchain_dlt] High: Temporary freezing of funds for more than the staking timelock for a staking transaction or more than the unbonding timelock for an unbonding transaction.
- [blockchain_dlt] Medium: Babylon node recognizes Bitcoin Staking protocol transactions and/or signatures as invalid when they are valid.
- [blockchain_dlt] Medium: Generation of staking transactions that cannot be confirmed by the Bitcoin ledger
- [blockchain_dlt] Medium: Inability to process or activate new valid staking registrations under normal network throughput and capacity conditions.
- [blockchain_dlt] Medium: Preventing honest relayers from submitting Bitcoin headers or Bitcoin checkpoints to the Babylon Genesis chain indefinitely.
- [blockchain_dlt] Medium: Temporary denial of service of Babylon Genesis chain, lasting more than 24 hours, achievable at no economic cost to the attacker.
- [blockchain_dlt] Low: Causing temporary, minor or easily recoverable disruptions to normal Babylon Genesis chain operations
- [websites_and_applications] Critical: Direct theft of user funds or causing their freezing
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet without user interaction, such as:  Modifying transaction arguments or parameters Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:   /etc/shadow database passwords blockchain keys  This does not include non-sensitive environment variables, open source code, or usernames etc with no operational impact.
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:   Making trades
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:  HTML injection without JavaScript Replacing existing text with arbitrary text Arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] High: Taking down the API/website
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as their stored pending transactions.
- [websites_and_applications] Medium: Circumventing access restrictions on Web without using special tools
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:  Reflected HTML injection Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)

## Impact notes

Only the following impacts are accepted within this bug bounty program. All other impacts are not considered as in-scope, even if they affect something in the assets in scope table.

__For the Unbonding Pipeline Process, the following code components and branches are in-scope:__

Everything here [https://github.com/babylonlabs-io/cli-tools/blob/v0.2.x/](https://github.com/babylonlabs-io/cli-tools/blob/v0.2.x/), except the following test commands:
- createStakingTxCmd https://github.com/babylonlabs-io/cli-tools/blob/v0.2.x/cmd/createStakingTxCmd.go 
- createUnbondingTxCmd https://github.com/babylonlabs-io/cli-tools/blob/v0.2.x/cmd/createUnbondingTxCmd.go 
- createWithdrawTxCmd https://github.com/babylonlabs-io/cli-tools/blob/v0.2.x/cmd/createWithdrawTxCmg.go

## Rewards

- [blockchain_dlt] Critical: maxReward=$500,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [blockchain_dlt] High: maxReward=$15,000, minReward=$5,000, rewardModel=range
- [blockchain_dlt] Medium: maxReward=$3,000, minReward=$1,300, rewardModel=range
- [blockchain_dlt] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$70,000, minReward=$10,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$7,500, rewardModel=up_to
- [websites_and_applications] Medium: fixedReward=$3,000, rewardModel=fixed

## Reward notes

__Reward Calculation for Blockchain/DLT Critical Level Reports__

For critical Blockchain/DLT bugs, the reward amount is 10% of the funds directly affected, capped at the maximum critical reward __USD 500 000__. However, a minimum reward of __USD 20 000__ is to be rewarded in order to incentivize security researchers against withholding on a bug report.

All other impacts that would be classified as Critical would be rewarded with a minimum of __USD 20 000__. The rest of the severity levels are paid out according to the Impact in Scope table.

__Reward Calculation for Blockchain/DLT High Level Reports__

- If the vulnerability can be demonstrated to cause temporary freezing (without actually being exploited)  as defined in the impacts table, the reward doubles from the full frozen value for every additional **24h** that the funds are temporarily frozen, up to a max cap of the High reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

__Reward Calculation for Web/Apps Critical Level Reports__

For critical web/apps bug reports will be rewarded with __USD 70 000__, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Users funds being permanently inaccesible involving an attack that does not require any user action
- Unauthorized access to user funds due to a cryptographic or key management vulnerability

All other impacts that would be classified as Critical would be rewarded with a minimum of __USD 10 000__. 

The rest of the severity levels are paid out according to the Impact in Scope table.  

__Reward Payment Terms__

Payouts are handled by the Babylon Labs team directly and are denominated in USD. However, payments are done in USDC on Ethereum, BABY on Babylon Genesis or a mix as determined by Babylon Labs in its sole discretion. If payment or part of the payment is in BABY tokens the conversion price for the purposes of calculation shall be determined based on the arithmetic average of the daily closing prices of the BABY token over the immediately preceding fourteen (14) calendar days before the date of payment. The daily closing price for each day during the calculation period shall be obtained from the publicly available data published on Coingecko (https://www.coingecko.com/en/coins/babylon/historical_data). Babylon Labs shall perform the calculation in its sole but reasonable discretion.

## Out of scope (program-specific)

__Additional Blockchain/DLT Specific:__

- Impacts involving centralization risks
- Impacts involving Bitcoin not being live or safe.
- Impacts involving the Babylon validator set not being live or safe.
- Impacts involving the temporary downtime of relayers between Babylon and Bitcoin.
- Impacts involving the submission of a large number of transactions to the Bitcoin ledger and their delayed inclusion.
- Impacts involving >=⅓ malicious finality voting power.
- Impacts involving >= ⅓ malicious CometBFT voting power.
- Impacts involving a quorum of the covenant committee being malicious.
- Impacts preventing a quorum of the covenant committee to be reached due to a full quorum not being live.
- Impacts involving the confirmation depth and finalization timeout parameters being set to an improperly low value.
- Impacts involving a user’s staking transaction being included in a Bitcoin block in which different Bitcoin staking parameters than the ones the user used apply.

__Prohibited Activities:__

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles, third-party smart contracts or cloud services
- Attempting phishing or other social engineering attacks against our employees, and/or customers, service providers and community members
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
