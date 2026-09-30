# Livepeer

- Page: https://immunefi.com/bug-bounty/livepeer/scope/
- Max bounty: $40,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (23)

- [smart_contract] https://arbiscan.io/address/0x0B9C254837E72Ebe9Fe04960C43B69782E68169A — BondingVotes (Proxy)
- [smart_contract] https://arbiscan.io/address/0x10736ffaCe687658F88a46D042631d182C7757f7#code — MerkleSnapshot
- [smart_contract] https://arbiscan.io/address/0x148D5b6B4df9530c7C76A810bd1Cdf69EC4c2085#code — L2Migrator (Proxy)
- [smart_contract] https://arbiscan.io/address/0x289ba1701C2F088cf0faf8B3705246331cB8A839#code — LivepeerToken
- [smart_contract] https://arbiscan.io/address/0x35Bcf3c30594191d53231E4FF333E8A770453e40#code — Bonding Manager (Proxy)
- [smart_contract] https://arbiscan.io/address/0x6D2457a4ad276000A615295f7A80F79E48CcD318#code — L2LPTGateway
- [smart_contract] https://arbiscan.io/address/0x8bb50806D60c492c0004DAD5D9627DAA2d9732E6#code — PollCreator
- [smart_contract] https://arbiscan.io/address/0xC45f6918F7Bcac7aBc8fe05302b3cDF39776cdeb#code — SortedDoublyLL (Library)
- [smart_contract] https://arbiscan.io/address/0xC92d3A360b8f9e083bA64DE15d95Cf8180897431#code — ServiceRegistry (Proxy)
- [smart_contract] https://arbiscan.io/address/0xD8E8328501E9645d16Cf49539efC04f734606ee4#code — Controller
- [smart_contract] https://arbiscan.io/address/0xD9dEd6f9959176F0A04dcf88a0d2306178A736a6#code — Governor
- [smart_contract] https://arbiscan.io/address/0xa8bB618B1520E284046F3dFc448851A1Ff26e41B#code — TicketBroker (Proxy)
- [smart_contract] https://arbiscan.io/address/0xc20DE37170B45774e6CD3d2304017fc962f27252 — Minter
- [smart_contract] https://arbiscan.io/address/0xcFE4E2879B786C3aa075813F0E364bb5acCb6aa0 — LivepeerGovernor (Proxy)
- [smart_contract] https://arbiscan.io/address/0xd78b6bD09cd28A83cFb21aFa0DA95c685A6bb0B1#code — L2LPTDataCache
- [smart_contract] https://arbiscan.io/address/0xdd6f56DcC28D3F5f27084381fE8Df634985cc39f#code — RoundsManager (Proxy)
- [smart_contract] https://arbiscan.io/address/0xf82C1FF415F1fCf582554fDba790E27019c8E8C4 — Treasury
- [smart_contract] https://arbiscan.io/address/0xfdb06109032AD3671a8f14f5f2E78f4B9E81b567#code — DelegatorPool (Implementation + clones)
- [smart_contract] https://etherscan.io/address/0x1d24838b35A9c138Ac157A852e19e948aD6323D7#code — L1LPTDataCache
- [smart_contract] https://etherscan.io/address/0x2a69191B43c9DB47C927bD7287F9C93838d07759#code — L1Migrator
- [smart_contract] https://etherscan.io/address/0x6142f1C8bBF02E6A6bd074E8d564c9A5420a0676#code — L1LPTGateway
- [smart_contract] https://etherscan.io/address/0x6A23F4940BD5BA117Da261f98aae51A8BFfa210A#code — L1Escrow
- [smart_contract] https://etherscan.io/address/0x8dDDB96CF36AC8860f1DE5C7c4698fd499FAB405#code — BridgeMinter

## Asset notes

Only the contracts in the Assets in Scope table on the Scope tab are considered in-scope of the bug bounty program. Target (implementation) contracts are not listed because they change on upgrade. They can be looked up in the Controller contract listed in that table. Reports are evaluated against the implementation live at the time of submission.

Livepeer migrated to Arbitrum One under LIP-73, and the L1 protocol contracts on Ethereum mainnet have been paused since February 2022 and remain paused. L1 staking, round progression and ticket redemption are halted, so no exploit path can execute against these contracts.

Critical vulnerabilities in the go-livepeer client were recently added to the scope of the program. This scope also includes any direct livepeer hosted and developed dependencies within go-livepeer that lead to the direct critical exploits listed in the program.

## Impacts in scope (15)

- [smart_contract] Critical: Direct manipulation treasury voting that manipulate the outcome of the vote resulting in drained funds from the treasury
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Insolvency
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Unexpected calls to functions that should only be called by authorized addresses (i.e. Governor)
- [smart_contract] Critical: Unintended issuance of LPT on L1
- [smart_contract] High: Any unexpected balance inflation when transitioning between L1 and L2
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Manipulation of protocol governance vote or treasury voting that does not effect the result of the vote
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption or any other gas drainage
- [smart_contract] Low: Smart contract has unexpected behavior but doesn’t lose value

## Impact notes

## Repeatable attack limitations

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward.

The amount of funds at risk will be calculated with the impact of the first attack being at **100**% and then a reduction of **100**% from the amount of the first attack for every **24** hours the attack needs for subsequent attacks from the first attack, rounded down.

## Rewards

- [smart_contract] Critical: maxReward=$40,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: maxReward=$15,000, rewardModel=up_to
- [smart_contract] Medium: fixedReward=$2,500, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

All web/app bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

All vulnerabilities marked in the [security review](https://code4rena.com/reports/2022-01-livepeer) are not eligible for a reward.

Livepeer requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed is Visual Proof of Identity. The collection of this information will be done by the project team. 

Rewards for critical vulnerabilities are capped at 10% of the economic damage (following the linked examples) with the primary focus on possible loss of funds for Orchestrators, Delegators and Broadcasters at the Smart Contract level only. If there is a repeatable attack, only the first attack is considered unless further attacks cannot be mitigated via an upgrade or pause.

Rewards for high vulnerabilities will depend on the amount of unclaimed yield that is on the line and how long the funds can be frozen.

Payouts are handled by the __Livepeer__ team directly and are denominated in USD. However, payouts are done in __USDC__.

## Out of scope (program-specific)

- Best practice critiques
  - Oracle failure/manipulation
  - Consensus failure

- Client usability bugs not effecting theft of user value or keys

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (4)

- LivepeerGovernor allows proposals with zero opinionated votes to succeed, and proposals with 1 wei "against" / 0 "for" votes can succeed if quorum is met via "abstain" votes. (https://github.com/livepeer/protocol/issues/654)
- Missing freshness check in L2LPTDataCache.finalizeCacheTotalSupply leads to underpaid (or overpaid) rewards in the next rounds. (https://github.com/livepeer/protocol/issues/664)
- MixinReserve.claimableReserve() can produce per-claimant reserve caps above or below the fair R/N allocation when the live transcoder pool size and the current-round active set diverge mid-round (e.g. during resignation or activation). Overclaim is bounded by the ticket face value. No theft is possible. (https://github.com/livepeer/protocol/issues/656)
- Winning tickets can settle for less than their face value once the recipient’s reserve is exhausted. (https://github.com/livepeer/protocol/issues/663)
