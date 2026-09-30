# Ostium

- Page: https://immunefi.com/bug-bounty/ostium/scope/
- Max bounty: $200,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: websites_and_applications - critical, websites_and_applications - high
- End date: (none)

## Assets in scope (20)

- [smart_contract] https://arbiscan.io/address/0x083F97BabF33D4abC03151B5DEc98170761f4025 — ProxyAdmin - Admin for upgradeable proxy contracts
- [smart_contract] https://arbiscan.io/address/0x20D419a8e12C45f88fDA7c5760bb6923Cee27F98 — Vault - Vault for liquidity providers
- [smart_contract] https://arbiscan.io/address/0x260E349F643f12797fDc6f8c9d3df211D5577823 — PairsStorage - Pair configs (feeds/spreads/leverage)
- [smart_contract] https://arbiscan.io/address/0x3890243a8fc091c626ed26c087a028b46bc9d66c — PairInfos - Pair related info: funding rates rollover fees etc
- [smart_contract] https://arbiscan.io/address/0x52453FBC4A33F7A2A0a01d67B952625816f161b4 — PriceRouter - Routes price requests to feeds
- [smart_contract] https://arbiscan.io/address/0x52B2a78E12b09B66C6c8ce291D653D40bAb77f0c — PriceUpKeep - Automated price update keeper
- [smart_contract] https://arbiscan.io/address/0x6D0bA1f9996DBD8885827e1b2e8f6593e7702411 — Trading - Entry point for market and limit orders
- [smart_contract] https://arbiscan.io/address/0x7720fC8c8680bF4a1Af99d44c6c265a74e9742a9 — TradingCallbacks - Order execution and trade settlement
- [smart_contract] https://arbiscan.io/address/0x799a139aE56e11F0476aCE2f6118CfcAed9608d2 — Registry - Central contract registry and role management
- [smart_contract] https://arbiscan.io/address/0x959Da1452238F71F17f7DA5dbA2e9c04FEf57324 — TradesUpKeep - Automated trade execution keeper
- [smart_contract] https://arbiscan.io/address/0xB71ec9eBD8145daCaCF6724363143cb5667A3d36 — PrivatePriceUpKeep - Permissioned price update keeper
- [smart_contract] https://arbiscan.io/address/0xE607aC9FF58697c5978AfA1Fc1C5C437a6D1858c — OpenPnlFeed - Aggregated open PnL feed
- [smart_contract] https://arbiscan.io/address/0xb4f1123BE58f5d69E1cf565ED8756C7fcf31c8D3 — LockedDepositNft - NFT representing locked vault deposits
- [smart_contract] https://arbiscan.io/address/0xccd5891083a8acd2074690f65d3024e7d13d66e7 — TradingStorage - Central storage for trades and orders
- [smart_contract] https://arbiscan.io/address/0xd456939e54F68Ef9B0BE62aBB2EC4A37397Cb814 — Verifier - Price data signature verification
- [smart_contract] https://arbiscan.io/address/0xeB85dC6095c74D36500C9cdcaCc15EcDC223Bbf7 — TimeLockOwner - Timelock governance for ownership actions
- [smart_contract] https://www.ostium.com/ — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://immunefi.com/ — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://ostium.app/ — App
- [websites_and_applications] https://t.me/ostiumbot — Telegram App

## Asset notes

(none)

## Impacts in scope (41)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Execution of trades at incorrect prices through validation bypass
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] High: Bypassing collateral requirements to open undercollateralized or overleveraged positions
- [smart_contract] High: Bypassing liquidation mechanisms to keep insolvent positions open
- [smart_contract] High: Bypassing trading fees to trade at reduced or zero cost
- [smart_contract] High: Forcing incorrect liquidation of a healthy position
- [smart_contract] High: Manipulation of dynamic spread or price impact calculations to achieve better execution than intended
- [smart_contract] High: Manipulation rollover fees to extract value
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] High: Unauthorized execution, cancellation, or modification of another user's trades or orders
- [smart_contract] Medium: Blocking or delaying order execution, liquidations, or vault settlements without direct profit
- [smart_contract] Medium: Bypassing leverage limits or position size limits checks
- [smart_contract] Medium: Causing fee accounting divergence between actual fees paid and protocol-recorded fees
- [smart_contract] Medium: Causing stale trigger blocks or order timeouts through transaction ordering manipulation
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Spamming partial closes or micro-positions to drain oracle fees or accumulate dust rounding errors
- [smart_contract] Low: Incorrect event emission or missing event data that causes off-chain keepers to desync from on-chain state
- [smart_contract] Low: Limit orders or TP/SL executing at marginally worse prices than expected due to precision truncation
- [smart_contract] Low: Rounding errors in fee calculations (funding, rollover, opening) that result in negligible loss per trade but accumulate over time
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
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
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:
- Email address
- Phone number
- Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$200,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$50,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$50,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,000, primacy=primacy_of_rules, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 


__Reward Calculation for Critical Level Reports__

For critical web/apps bugs, reports will be rewarded with $25,000, only if the impact leads to:
- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of $5,000. The rest of the severity levels are paid out according to the Impact in Scope table.


__Reward Payment Terms__

Payouts are handled by the Ostium team directly and are denominated in USD. However, payments are done in USDC on Arbitrum.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

Privileged Roles & Admin Actions

  - All privileged role actions (gov, dev, manager, owner etc) are assumed to be performed correctly and in good faith.
  Issues arising from admin misconfiguration, incorrect parameter setting, or misuse of privileged functions are out
  of scope.
  - Contract upgradeability via proxy admin is a known trust assumption. Findings related to the ability of the proxy
   admin to upgrade contracts are out of scope.
  - Gov-controlled fee and parameter changes are by design. The gov role can adjust trading fees, funding rates,
  rollover fees, leverage limits, vault settlement parameters, and spread parameters. Reports about the gov role
  having this power are not valid findings.
  - Dev fee claims will not drain protocol funds. It is assumed that the dev role will only claim correct amount of fees, not
  create scenarios where fee withdrawal impacts the rest of the protocol.
  - Pause and kill-switch mechanisms are intentional. The manager can pause trading and the gov can trigger the
  done() kill-switch. Reports about these capabilities existing are not valid findings.
  - Timelock delays are a known trade-off. Issues related to governance actions being delayed by the timelock are by
  design.

  Keepers & Oracles

  - All registered keepers (PriceUpKeep, PrivatePriceUpKeep, TradesUpKeep) and their forwarders are assumed to
   be trusted and operating correctly. Issues requiring a compromised or malicious keeper are out of scope.
  - Price feeds (Chainlink and custom OstiumVerifier signers) are assumed to deliver accurate data. Oracle
  manipulation at the source (e.g., compromising Chainlink nodes or authorized signers) is out of scope. However,
  improper validation or handling of price data within the protocol contracts is in scope.
  - Price staleness within the configured maxTsValidity window is expected behavior. Reports about price data being
  slightly delayed within the allowed validity window are not valid findings.

  Economic & Griefing Thresholds

  - Griefing attacks that require significant capital (>$10,000) with no monetary gain to the attacker are out of
  scope or will be downgraded at protocol discretion. The protocol reserves the right to evaluate the
  practical feasibility and real-world impact of any griefing submission.
  - Attacks that require sustained, economically irrational behavior over multiple blocks or transactions to achieve
  minimal impact are out of scope.
  - Theoretical insolvency scenarios that require extreme and unrealistic market conditions (e.g., all pairs
  simultaneously hitting max leverage liquidation thresholds) are out of scope or may be downgraded at protocol discretion.

  External Dependencies & Integrations

  - Issues in third-party contracts (OpenZeppelin, Chainlink, Gelato) are out of scope unless the finding
  demonstrates that the protocol incorrectly integrates or uses these dependencies.
  - Arbitrum L2 sequencer behavior, downtime, or reorgs are out of scope. The protocol operates on Arbitrum and
  inherits its security properties. Findings that rely on L2 sequencer manipulation or downtime as an attack vector
  are not valid.
  - ERC-20 token behavior of USDC is assumed to be standard. Issues related to USDC blacklisting, upgradeability, or
  depegging are out of scope.

  General Exclusions

  - Front-running of governance/admin transactions is out of scope. Privileged operations are protected by timelocks
  and trusted execution.
  - Known gas inefficiencies in gov-only or manager-only batch functions (e.g., registerContracts, updateContracts)
  are out of scope. These are called infrequently by trusted roles who can manage gas limits.
  - Findings based on deprecated or dead code paths scheduled for removal in the next upgrade are out of scope unless
   they can be exploited in the current deployed state.
  - Loss-of-precision issues that result in insignificant rounding differences are out of scope.
  - Best practice recommendations, gas optimizations, and informational findings without a demonstrated impact are
  out of scope.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
