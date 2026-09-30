# DAWN USD.infra Vault

- Page: https://immunefi.com/bug-bounty/dawn/scope/
- Max bounty: $50,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - low, websites_and_applications - medium
- End date: (none)

## Assets in scope (6)

- [smart_contract] https://bscscan.com/address/0x15a6f1f2705b3916b5b1d2b19b10f320778744c1 — InfraFi's on-chain contract on BNB Chain that receives, validates and stores the vault exchange rate published by infrafi-api, implements additional sanity checks and is used for downstream oracle consumption. In scope: rate-publishing authorization, staleness/validation, and any path to posting a manipulated or ripcord-blocked rate.
- [smart_contract] https://solscan.io/account/4rXteUmbxiXvgLqP14eQwtqkLyVNXVCBHnXyLQ9vZkSh — Loopscale credit vault holding InfraFi capital - loan book, NAV and share price computed on-chain by Loopscale; DAWN is the sole whitelisted borrower via a Squads V4 multisig. On-chain Anchor IDL fetchable. In scope: InfraFi's vault configuration and integration — deposit/withdraw, borrow/repay, and deal-valuation integration; borrower authorization; and the exchange-rate/share-price semantics DAWN reads and publishes. Loopscale protocol and program internals are out of scope (see below).
- [smart_contract] https://solscan.io/account/EZ8sq2FNnmqQo254irAMGNp7c6B7DPuKh22SyXAwuXSn — Loopscale credit vault holding InfraFi capital - loan book, NAV and share price computed on-chain by Loopscale; DAWN is the sole whitelisted borrower via a Squads V4 multisig. On-chain Anchor IDL fetchable. In scope: InfraFi's vault configuration and integration — deposit/withdraw, borrow/repay, and deal-valuation integration; borrower authorization; and the exchange-rate/share-price semantics DAWN reads and publishes. Loopscale protocol and program internals are out of scope (see below).
- [smart_contract] https://solscan.io/token/dawn7ZUF7h7anFuEsDdAU1Y3HYwikwqNMAENZsQJdNL — USD.tel stablecoin — M0 wrapped-M issued on Solana's Token-2022 program with the Pausable extension. In scope: InfraFi's mint configuration and pause-authority operation.
- [websites_and_applications] https://api.infrastructure.finance — Public API surface of infrafi-api consumed from the internet by the web dashboard (GET /project, GET /project/metrics, GET /nav/*, GET /vault/solana/nav, GET /health).
- [websites_and_applications] https://app.infrastructure.finance — Public USD.infra vault capital-provider dashboard (Next.js). Wallet connect, deposit/redeem flows, and NAV/exchange-rate display.

## Asset notes

(none)

## Impacts in scope (44)

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
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [websites_and_applications] Critical: A loss of funds involving an attack that does not require any user action
- [websites_and_applications] Critical: Changing NFT metadata
- [websites_and_applications] Critical: Direct theft of user NFTs
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Private key or private key generation leakage leading to unauthorized access to user funds
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
- [websites_and_applications] Critical: Taking down the NFT URI
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
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:
- Locking up the victim from login
- Cookie bombing, etc.

## Impact notes

-

## Rewards

- [smart_contract] Critical: maxReward=$50,000, minReward=$25,000, rewardCalculationPercentage=0, rewardModel=range
- [smart_contract] High: fixedReward=$3,500, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$2,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$50,000, minReward=$25,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: fixedReward=$3,500, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$2,000, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

.

## Out of scope (program-specific)

- **Upstream / third-party program code:** the M0 wrapped-M / Token-2022 program internals (only
  USD.infra mint configuration and pause-authority operation are in scope); and the Loopscale
  credit-vault program, its vault/loan/NAV/share-price primitives, and its oracle keeper, authored and
  operated by Loopscale (only InfraFi's vault configuration and integration are in scope). Also
  excludes Squads V4, Pyth/Chainlink, wallet libraries (reown/AppKit), and all npm/cargo dependencies.

- Off-chain internal services (infrafi-manager, indexer) and anything behind the WireGuard VPN, except
  as reachable via the public web/API assets.
- Known issues listed
- Findings requiring compromise of an operator's machine, Slack workspace account, hardware wallet, or
  multisig/Squads signer key, or of Loopscale's protocol-admin co-signer (assumed-trusted operators
  and counterparty).
- Debug-build-only behavior (e.g. the in-process change-request auto-apply path); production ships
  `--release`.
- NAV read staleness within the documented snapshot window (historical NAV is served from local
  snapshots), and fee-accrual / share-price drift within the documented conservation tolerance.
- Best-practice / missing-hardening reports with no demonstrated exploit; and standard web boilerplate
  (missing security headers, CSRF on unauthenticated reads, self-XSS, clickjacking on stateless pages,
  SPF/DKIM, rate-limiting on public reads, automated-scanner output).

## infrafi-manager & api.infrastructure.finance — admin surface

Out of scope:

The VPN-gated admin/manager surface (infrafi-manager) and all authenticated/admin API routes — including /admin/*, project/building mutations, valuation posting, borrow/repay proposals, and the /slack/interactive callback — when performed by a trusted operator acting within the four-eyes approval flow and the post-time delta bounds.

In scope:

The public, unauthenticated read routes of api.infrastructure.finance.
Any bug that bypasses the four-eyes approval or the post-time delta bounds.
Any path that lets deal valuations (or borrow/repay / mutations) be executed or manipulated without the trusted-operator role.

## Program Rules — Relationship to Loopscale's Bug Bounty Program

InfraFi's credit vault runs on Loopscale's on-chain program, which is covered by Loopscale's own bug
bounty program. Vulnerabilities in the Loopscale protocol, program, vault primitives, oracle keeper,
or any Loopscale-operated infrastructure are out of scope here and must be reported to Loopscale. Only
DAWN / InfraFi's own vault configuration and integration — as defined under *Assets in Scope* — are
eligible under this program.

**No double payment.** A report describing the same underlying vulnerability (same root cause) that is
eligible for, has been submitted to, or has been rewarded by Loopscale's bug bounty program will not
receive a separate reward from InfraFi. Where a single issue touches both programs, the researcher may
be compensated under one program only; InfraFi will coordinate with Loopscale on attribution and will
not duplicate a bounty already paid or payable by Loopscale for the same root cause. Deliberately
submitting the same finding to both programs to obtain two payouts is considered abuse and may result
in disqualification.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (5)

- Flat admin role — every authenticated manager admin has full privileges; segregation of duties is enforced by the Slack approval step, not by RBAC. (https://immunefi.com/bug-bounty/dawn/information/)
- LocalStorage JWT storage in the manager (accepted XSS trade-off behind the VPN). (https://immunefi.com/bug-bounty/dawn/information/)
- No replay-window/timestamp check on the Slack interactive webhook signature (idempotency guard makes replay a no-op state-wise). (https://immunefi.com/bug-bounty/dawn/information/)
- Seeded default admin (admin@usd.tel) created on first boot; rotated on deploy by process, not code. (https://immunefi.com/bug-bounty/dawn/information/)
- ripcord is a coordination signal, not an enforced kill switch — the API does not block reads/writes when it is true; integrators are trusted to act. (https://immunefi.com/bug-bounty/dawn/information/)
