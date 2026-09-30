# IOP | Paradex

- Page: https://immunefi.com/bug-bounty/iop-paradex/scope/
- Max bounty: $45,000
- KYC required: yes
- Paused: no
- Invite only: yes
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-06-13T07:00:00.000Z

## Assets in scope (0)

(none)

## Asset notes

(none)

## Impacts in scope (13)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hour
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Theft of gas
- [smart_contract] Low: Unbounded gas consumption

## Impact notes

__Build Commands, Test Commands, and How to Run Them__

Included in repo readme

__Previous Audits__

Paradex’s completed audit reports can be found at [https://github.com/Cairo-Security-Clan/Audit-Portfolio/blob/main/Paradex_Audit_Report.pdf](https://github.com/Cairo-Security-Clan/Audit-Portfolio/blob/main/Paradex_Audit_Report.pdf). Unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

L1 Bridge contract is a fork of starknet’s starkgate bridge with some minor additions. Their audits are:
- [https://github.com/tradeparadex/paradex-docs/blob/main/fern/assets/Starknet_Core_Summary_Report_Sept_2022.pdf](https://github.com/tradeparadex/paradex-docs/blob/main/fern/assets/Starknet_Core_Summary_Report_Sept_2022.pdf)
- [https://github.com/tradeparadex/paradex-docs/blob/main/fern/assets/StarkGate_Oct_2023.pdf](https://github.com/tradeparadex/paradex-docs/blob/main/fern/assets/StarkGate_Oct_2023.pdf)
- [https://github.com/tradeparadex/paradex-docs/blob/main/fern/assets/StarkGate_Oct_2024.pdf](https://github.com/tradeparadex/paradex-docs/blob/main/fern/assets/StarkGate_Oct_2024.pdf)

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward.

__Optional Project Info__

**Is this an upgrade of an existing system? If so, which? And what are the main differences?**

Mainnet is currently running a slightly newer version of the code that’s being audited.

Starkgate contract is running exactly the same as the repo on mainnet

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

Attack Vectors:
- Stealing User Funds / Unauthorized fund transfers
- Market Manipulation

**What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?**

ERC20

**Which chains and/or networks will the code in scope be deployed to?**

We currently run on a starknet app chain

**What external dependencies are there?**

Openzeppelin, Alexandria Data Structures

**Are there any unusual points about your protocol that may confuse Security Researchers?**

Potentially, the way some transfer restrictions are implemented and some of the functionalities implemented on Vaults can be quite complex 

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)**

- [https://docs.paradex.trade/](https://docs.paradex.trade/)
- [https://l2beat.com/scaling/projects/paradex](https://l2beat.com/scaling/projects/paradex)

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

__Rewards Terms__

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

Rewards are denominated in USD and distributed in USDC on Ethereum.

The reward pool is $33k USD if any bug is found.

If not a single bug is found (Insights do not count as bugs) the reward pool is $2.97k USD

On top of this, each participating SR will receive a guaranteed reward of $3k USD.

**Proof of Concept (PoC) Requirements**

For this program, runnable PoC code is not required. Whitehats are instead required to write a step-by-step explanation of the PoC and impact.

__Insight Rewards Payment Terms__

*Insight Rewards*: Portion of the Rewards Pool

*The "Insight" severity was introduced on Boost (Audit Competitions) & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

Duplicates of Insight reports are not eligible for a reward.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
