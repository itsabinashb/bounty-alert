# Synthetix

- Page: https://immunefi.com/bug-bounty/synthetix/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: websites_and_applications - critical, websites_and_applications - high
- End date: (none)

## Assets in scope (6)

- [smart_contract] https://etherscan.io/address/0x45F91031b33Da2585932c8f1cdFF0faa6cD329ae#code — PermissionsRegistry (Proxy) — self-sovereign (owner, delegatee, permission) registry
- [smart_contract] https://etherscan.io/address/0x99E61877aF9Bc6805BCc3813F655D94Ed5f3782A#code — SynthetixDepositContractLens — view-only batch query helper
- [smart_contract] https://etherscan.io/address/0xD62595c3c23B690BAEE0935e107A209Cb1Dbd37B#code — SynthetixDepositContract (Proxy) — user collateral custody + multi-stage withdrawals
- [websites_and_applications] https://exchange.synthetix.io/ — Exchange website
- [websites_and_applications] https://governance.synthetix.io/ — Governance website
- [websites_and_applications] https://synthetix.io/ — Synthetix

## Asset notes

Unless explicitly listed, only pages of the web/app assets in addition to the direct link are considered in-scope of the bug bounty program. Other subdomains are not considered as in-scope. However, for subdomain takeovers that lead to an impact on the in-scope asset, please refer to our page about [Reported Subdomain Takeovers](https://immunefisupport.zendesk.com/hc/en-us/articles/14352199704593-Reported-Subdomain-Takeovers).

## Impacts in scope (25)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [websites_and_applications] Critical: A loss of funds involving an attack that does not require any user action
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
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
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: email or password of the victim, etc
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:  HTML injection without JavaScript Replacing existing text with arbitrary text Arbitrary file uploads, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Reflected) such as: reflected HTML injection, loading external site data
- [websites_and_applications] High: Manipulation of the governance voting UI with the intent of luring votes into voting for the wrong candidate
- [websites_and_applications] High: Redirecting users to malicious websites (Open Redirect)
- [websites_and_applications] High: Redirecting users to malicious websites (Open Redirect)
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Any vulnerability that allows an attacker to prevent users from accessing websites or services included in the program, excluding traditional DDoS attacks
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.

## Impact notes

Only the following impacts are accepted within this bug bounty program. All other impacts are not considered as in-scope, even if they affect something in the assets in scope table.

## Rewards

- [smart_contract] Critical: fixedReward=$100,000, rewardCalculationPercentage=10, rewardModel=fixed
- [smart_contract] High: fixedReward=$50,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$30,000, otherImpactMaxReward=$3,000, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$10,000, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Reward Calculation for Critical Level Reports__

For critical Smart Contract bugs, the reward amount is __10%__ of the funds directly affected up to a maximum of __USD $100,000__. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of __USD $10,000__ is to be rewarded in order to incentivize security researchers against withholding a bug report.   
For critical web/app bugs, the reward amount is __10%__ of the funds directly affected up to a maximum of __USD $30,000__. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of __USD $1,000__ is to be rewarded in order to incentivize security researchers against withholding a bug report.   

__Repeatable Attack Limitations__

In cases of smart contract vulnerabilities whereby the attacks can be repeated at certain time intervals, if the attack can be stopped by a configuration change, the     total value-at-risk from the consecutive attacks is computed by adding up the losses incurred and applying the below discount factors:

| Time Since Attack 1     | Discount Factor     |
| ---------- | ---------- |
| 0 to 15 minutes       | 0%       |
| 15 to 30 minutes       | 25%       |
| 30 to 60 minutes       | 50%       |
| 60 to 120 minutes       | 75%       |
| > 120 minutes       | 100%       |

If the attack cannot be stopped by configuration changes, the discount factors are adjusted by 50% (i.e. 0% / 12.5% / 25% … ), with the terminal discount factor being 100% at 4 hours (from the initial attack).

__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:
  - Critical
  - High

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules). Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System v. 2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). This is a simplified 4-level scale. The development of this scale took into consideration multiple factors that may affect a vulnerability and its likelihood of exploitation, but finalizes them largely by the impact that they cause.

The table below is mostly concerned with the consequence of a successful exploit. Keep in mind that if the exploit requires elevated privileges or uncommon user interaction, the level of the bug may be downgraded to reflect that or rejected. 

__Goodwill Payments__ 

This applies to the following severity and asset levels: 
  - Smart Contract - Low
  - Web/App - Medium
  - Web/App - Low

Synthetix is willing to offer discretionary “Goodwill Payments” for any bugs that fall under these categories and affect __TVL <$1,000__, 

Furthermore, if the value of the assets at risk cannot be estimated, then the bounty payment would be discretionary based on goodwill terms.

## Out of scope (program-specific)

- Security researchers from restricted countries, reference to the [terms](https://staking.synthetix.io/terms/), are not eligible for bounties regardless of the scope of the vulnerability disclosure
  - Activities that violate the whitehat [rules of engagement](https://immunefi.com/rules/) would result in revocation of the bounty regardless of the disclosure merit.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
