# Harvest Finance

- Page: https://immunefi.com/bug-bounty/harvest/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: websites_and_applications - high, websites_and_applications - critical, websites_and_applications - medium, smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (5)

- [smart_contract] https://github.com/harvestfi/harvest-strategy
- [smart_contract] https://github.com/harvestfi/harvest-strategy-arbitrum
- [smart_contract] https://github.com/harvestfi/harvest-strategy-arbitrum
- [smart_contract] https://github.com/harvestfi/harvest-strategy-polygon
- [websites_and_applications] https://harvest.finance/

## Asset notes

(none)

## Impacts in scope (34)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at rest or in motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Permanent freezing of unclaimed yield due to Harvest contract issue
- [smart_contract] Medium: Smart contracts unable to operate due to a lack of token funds
- [smart_contract] Medium: Theft of unclaimed yield due to Harvest contract issue
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Miner-extractable value (MEV)
- [smart_contract] Low: Theft of gas
- [smart_contract] Low: Unbounded gas consumption
- [websites_and_applications] Critical: ACE
- [websites_and_applications] Critical: Deletion of site data
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as /etc/shadow, database passwords, and blockchain keys(this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as, changing registration information, commenting, voting, making trades, withdrawals, etc
- [websites_and_applications] Critical: XSS/CSRF
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as the email or password of the victim, etc
- [websites_and_applications] High: Denial of service
- [websites_and_applications] High: DoS amplification
- [websites_and_applications] High: Improperly disclosing confidential user information such as email address, phone number, physical address, etc
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the name of a user, or enabling/disabling notifications
- [websites_and_applications] Medium: Incorrect modification of user data
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as reflected HTML injection or loading external site data
- [websites_and_applications] Medium: Leaking user data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: fixedReward=$10,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$5,000, otherImpactMaxReward=$0, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on
the [Immunefi Vulnerability Severity Classification System](/severity-system/). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from the consequence of exploitation to the privilege required to the likelihood of a successful exploit. 

The final reward amount for critical smart contract bugs is capped at 10% of 
economic damage based on the vulnerability reported with a minimum payout of 
**USD 50 000**.

Theft of yield/interest is considered as Medium for this bug bounty program.

All smart contract reports must include a PoC to be accepted. The PoC should provide clear proof of the vulnerability in a locally forked blockchain environment. All bug reports without a PoC will be rejected and require the submitter to resubmit with a PoC. 

The following table is used for the classification of web and app bug reports. In the event of conflict with the Immunefi Vulnerability Severity Classification System, the classification on this table will be what is considered.

| Severity | Vulnerability |
| :-- | :-: |
| **Critical** | Deletion of site data, XSS/CSRF, ACE |
| **High** | Denial of Service, DoS ampliciation |
| **Medium** | Incorrect modification of user data, leaking user data |

All web and app bug reports must include a PoC to be accepted. All web and app bug reports without a PoC will be rejected and require the submitter to resubmit with a PoC. 

Vulnerabilities that require moderator-approved access to be exploited will only receive a maximum of 20% of the advertised reward. For Critical Smart Contract and Blockchain vulnerability reports, this 20% is applied after the cap of 10% of economic damage.  

Payouts are handled by the **Harvest Finance** team directly and are denominated in USD. Payouts up to **USD 100 000** are paid in **USDC**.

## Out of scope (program-specific)

- Best practice critiques

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
