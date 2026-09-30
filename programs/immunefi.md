# Immunefi

- Page: https://immunefi.com/bug-bounty/immunefi/scope/
- Max bounty: $50,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (7)

- [smart_contract] https://etherscan.io/address/0x03fd3d61423e6d46dcc3917862fbc57653dc3eb0 — Vault
- [smart_contract] https://etherscan.io/address/0x323498d3fb02594ac3e0a11b2dea337893ecabbe — Splitter
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://bugs.immunefi.com
- [websites_and_applications] https://immunefi.com
- [websites_and_applications] https://immunefi.com — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://ironscore.immunefi.com/ — Iron Score

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

Unless explicitly listed, only pages of the web/app assets in addition to the direct link are considered in-scope of the bug bounty program. Other subdomains are not considered as in-scope. However, for subdomain takeovers that lead to an impact on the in-scope asset, please refer to our page about [Reported Subdomain Takeovers](https://immunefisupport.zendesk.com/hc/en-us/articles/14352199704593-Reported-Subdomain-Takeovers).

## Impacts in scope (27)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of fee or royalties
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the smart contracts)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as: modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as: database passwords,blockchain keys, etc (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as: changing registration information, commenting, voting, making trades, withdrawals, etc
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: email or password of the victim, etc
- [websites_and_applications] High: Improperly disclosing confidential user information such as: email address, phone number, physical address, etc
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as: HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: changing the name of user, enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as: reflected HTML injection, loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing other users details (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction such as: iframing leading to modifying the backend/browser state
- [websites_and_applications] Low: Taking over broken or expired outgoing links such as: social media handles, etc
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as: locking up the victim from login, cookie bombing, etc

## Impact notes

Only the following impacts are accepted within this bug bounty program. All other impacts are not considered as in-scope, even if they affect something in the assets in scope table.

These accepted impacts are then based on the severity classification system of this bug bounty program. When submitting a bug report, please select the severity level you feel best corresponds to the severity classification system as long as the impact itself is one of the listed items. 

If an impact can be caused to any other asset managed by Immunefi that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for consideration by Immunefi.

## Rewards

- [smart_contract] Critical: maxReward=$50,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$10,000, minReward=$5,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$5,000, minReward=$2,000, rewardModel=range
- [websites_and_applications] Medium: fixedReward=$2,000, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

For critical Smart Contract bugs, the reward amount is __10%__ of the funds directly affected up to a maximum of __USD 50 000__. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of __USD 10 000__ is to be rewarded in order to incentivize security researchers against withholding a bug report.

Critical website and application bug reports will be rewarded with __USD 10 000__, only if the impact leads to a direct loss in funds involving an attack that does not require any user action at all. Additionally any impact that leads to “Retrieve sensitive data/files from a running server such as: database passwords,blockchain keys, etc (this does not include non-sensitive environment variables, open source code, or usernames” and to “Execute arbitrary system commands” would be rewarded  USD 10 000 USD, which is 2x the standard amount for Web/App critical impact. All other impacts that would be classified as Critical, or an impact resulting in a theft of funds that does not fall under this definition, would be rewarded __USD 5 000__.

__Repeatable Attack Limitations__

In cases of repeatable attacks for smart contract bugs, only the first attack is considered if the smart contracts where the vulnerability exists can be upgraded, paused, or killed. If the attack impacts a smart contract directly holding funds that cannot be upgraded or paused, the amount of funds at risk will be calculated with the first attack being at 100% of the funds that could be stolen and then a reduction of 25% from the amount of the first attack for every 300 blocks the attack needs for subsequent attacks from the first attack, rounded down. For avoidance of doubt, if a second attack would happen at 600 blocks and then a third at 900 blocks, the funds at risk would be counted at 50% and 25% of the reward from the first attack, respectively.

__Reward Calculation for High Level Reports__
High smart contract vulnerabilities will be capped at up to 100% of the funds affected. In the event of temporary freezing, the reward doubles for every additional 5 blocks that the funds could be temporarily frozen, rounded down to the nearest multiple of 5, up to the hard cap of USD 10 000 USD. 

__Restrictions on Security Researcher Eligibility__

Security researchers who fall under any of the following are ineligible for a reward

  - Countries that are restricted by OFAC and by UNSC resolutions.

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs acknowledged below are not eligible for any reward through the bug bounty program. 

  - Any well-known issues related to Gnosis Safe: [https://docs.gnosis-safe.io/learn/security/security-audits ](https://docs.gnosis-safe.io/learn/security/security-audits)

__Previous Audits__
Immunefi has provided these completed audit review reports for reference. Any unfixed vulnerability mentioned in these reports are not eligible for a reward.

  - Here’s the [internal audit](https://github.com/immunefi-team/vaults-splitter/blob/main/audits/2023-02-03%20-%20Immunefi%20-%20Internal%20Audit%20of%20the%20Vaults%20system.pdf) of the Vaults System 
  - Here’s the [Ourovoros audit](https://github.com/immunefi-team/vaults-splitter/blob/main/audits/2023-02-13%20-%20Ourovoros%20Audit.md) of the Vaults System 

__Feasibility Limitations__

Bug reports that require an attack that involve one or more other protocols (e.g. utilizing flash loans from a margin protocol or manipulating the spot prices on a DEX), either to make an attack more severe than it would be in isolation, or to achieve an attack that would otherwise be impossible or infeasible, would be downgrade by one severity level. However, they will be considered as in-scope and categorized according to the program rules as long as all of the following are true:

  - Losses or other negative effects of the attack are inflicted upon Immunefi ecosystem participants (including Immunefi’s customers) 

  - The additional protocols used must have enough liquidity in various assets to allow the attack to succeed at the time of bug report submission. For example: if an attack requires an ETH flash loan, but the amount is larger than all the ETH available for loan across the ecosystem

__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:

  - All Smart Contract bug reports

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules). Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Other Terms and Information__


Broken link hijacking of social handles on any social media website will be downgraded to Informational, and a goodwill payout will be rewarded by Immunefi.

Bug reports covering previously-discovered bugs are not eligible for the program. If a bug report covers a known issue, it may be rejected, and Immunefi will provide proof that the issue is already known.  

__Reward Payment Terms__

Payouts are handled by the Immunefi team directly and are denominated in USD. However, payments are done in USDC

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
