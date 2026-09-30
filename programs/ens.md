# ENS

- Page: https://immunefi.com/bug-bounty/ens/scope/
- Max bounty: $250,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low, smart_contract - low
- End date: (none)

## Assets in scope (10)

- [smart_contract] https://github.com/ensdomains/ens-contracts/wiki/ENS-Contract-Deployments — Smart Contracts
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://app.ens.domains/ — ENS app
- [websites_and_applications] https://ens.domains — ENS landing page
- [websites_and_applications] https://github.com/ensdomains/ens-app-v3 — ENS app source code
- [websites_and_applications] https://github.com/ensdomains/ens-metadata-service — ENS Metadata service source code
- [websites_and_applications] https://github.com/ensdomains/ensdomains-landing — Ens landing page source code
- [websites_and_applications] https://immunefi.com — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://metadata.ens.domains/ — ENS Metadata service
- [websites_and_applications] https://metadata.ens.domains/docs — ENS Metadata service

## Asset notes

ENS’s codebase can be found at https://github.com/orgs/ensdomains/repositories. Documentation and further resources can be found on https://docs.ens.domains

## Impacts in scope (44)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Permanent freezing of treasury funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Retrieve sensitive data/files from a running server, such as:   Access tokens
- [smart_contract] Critical: Theft of treasury funds
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Permanent freezing of registration fees
- [smart_contract] High: Temporary freezing of NFTs
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of registration fee
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Low: Griefing where damage is reversible by any party at gas cost
- [smart_contract] Low: Temporary disruption of contract view-layer functions that self-heals through a permissionless call
- [websites_and_applications] Critical: Changing sensitive details of transactions (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: Registration Timer, Cached Transaction History
- [websites_and_applications] Critical: Direct theft of user NFTs
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:  Modifying transaction arguments or parameters, Substituting contract addresses, Submitting malicious transactions
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:   Changing registration information, Voting, Changing ENS records
- [websites_and_applications] High: Changing NFT metadata
- [websites_and_applications] High: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as: Iframing leading to modifying the backend/browser state (demonstrate impact with PoC)
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:  Email address, Phone number, Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:  HTML injection without JavaScript, Replacing existing text with arbitrary text, Arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:  Changing the name of user, Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:  Reflected HTML injection, Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Medium: Taking down the NFT URI
- [websites_and_applications] Medium: Taking down the application/website
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:  Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:  Locking up the victim from login, Cookie bombing, etc.

## Impact notes

# Program Structure

This program contains two independent reward tracks. Each track has its own severity classifications and reward ranges. A vulnerability shall be classified under one track only.

- **Track A: Smart Contract Vulnerabilities**
- **Track B: Websites and Applications Vulnerabilities**

**Cross-Track Classification**: Where a vulnerability involves both smart contract and web/application components, it shall be classified under the track corresponding to the root cause of the vulnerability. For example, a signature verification flaw in a smart contract is a Track A vulnerability even if its effects are visible through a web interface.

## Definitions & Calculations

### Impact Assessment

For many ENS vulnerabilities, the primary impact is to name ownership or resolution integrity rather than direct theft of funds. ENS therefore uses a two-part framework to assess impact: (1) the scope of names affected, and (2) a financial calculation where applicable.

### Part 1: Impact Scope

The scope of a vulnerability is assessed according to the following tiers:

- Tier 1 — Systemic: The vulnerability affects all ENS names, or all names of a major type (e.g., all .eth 2LDs, all names using a particular resolver). Tier 1 vulnerabilities will generally be assessed at the upper end of the applicable severity range.

- Tier 2 — Class-wide: The vulnerability affects a significant class of names (e.g., all DNS-imported names, all names registered through a specific registrar). Tier 2 vulnerabilities will generally be assessed at the mid-to-upper range.

- Tier 3 — Conditional: The vulnerability affects a subset of names defined by external conditions (e.g., names under TLDs with weak DNSSEC keys, names using a deprecated resolver version). Tier 3 vulnerabilities will generally be assessed at the mid range, subject to the External Dependency Discount where applicable.

- Tier 4 — Narrow: The vulnerability affects fewer than 50 individual names or accounts. Tier 4 vulnerabilities will generally be assessed at the lower end of the applicable severity range.

Within each tier, ENS will consider the categories of names affected. Not all names carry equal value or risk:

- .eth 2LDs — highest value (primary ENS namespace, active secondary market, significant transaction volume)
- DNS-imported names — moderate value (tied to external DNS ownership)
- Subdomains — variable (depends on parent name usage and configuration)
- Testnet names — lowest value (no real funds at risk)

### Part 2: Financial Calculation

Where a vulnerability involves direct theft or misdirection of funds (e.g., draining ETH from a contract, redirecting payments), "funds directly affected" means the aggregate on-chain value that could be misappropriated, misdirected, locked, or destroyed through exploitation of the vulnerability at the time of report submission.

For Tier 4 (narrow) vulnerabilities affecting name ownership or resolution, the following supplementary methodology may be used:

- The value of affected names may be calculated based on the most recent secondary market sale price or, if no sale has occurred, the annualized registration/renewal cost.

- Potential misdirection of funds (e.g., payments sent to a wrong address due to hijacked resolution) may be calculated based on the trailing 90-day transaction volume to addresses resolved through the affected names.

- Speculative or theoretical future losses are excluded from all calculations.

### General Provisions

The following sections apply to all vulnerabilities reported.

Primacy of Impact vs. Primacy of Rules

Primacy of Impact means that the impact is prioritized rather than a specific asset. This encourages security researchers to report on all bugs with an in-scope impact, even if the affected assets are not in scope. For more information, please see Best Practices: Primacy of Impact.

Primacy of Impact submissions remain subject to the program’s reward calculation methodology, including impact-based scaling, the External Dependency Discount, and discretionary adjustment.


### Feasibility Limitations

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug’s severity.

Therefore, Immunefi has developed a set of feasibility limitation standards which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

### Severity Assessment for XSS Reports

- Injection of malicious content into app.ens.domains to initiate a malicious transaction without requiring unusual user interaction will be considered Critical.
- Injection of malicious scripts into other ENS subdomains (besides app.ens.domains) that offer web3 wallet connections will be considered High for stored XSS and Medium for reflected XSS.
- XSS on static ENS websites like metadata.ens.domains, which do not offer web3 functionality, will be considered low.

## Rewards

- [smart_contract] Critical: maxReward=$250,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$25,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$10,000, primacy=primacy_of_rules, rewardModel=fixed
- [smart_contract] Low: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$25,000, otherImpactMaxReward=$10,000, rewardModel=fixed
- [websites_and_applications] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] Medium: fixedReward=$2,500, primacy=primacy_of_rules, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, primacy=primacy_of_rules, rewardModel=fixed

## Reward notes

**Classification & Reward Discretion**

Rewards are paid in USDC on Ethereum and are determined based on severity under the Immunefi Vulnerability Severity Classification System (V2.3).

Rewards are broadly based on the principles set forth within the [Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)

Final reward amounts are determined by ENS in its sole discretion after assessing factors such as:

- Likelihood of exploitation
- Scope of affected systems
- Ease of execution
- Quality of the report
- Whether the disclosure was responsible and novel
- Whether exploitation requires assuming that ENS Labs or its authorized operators act maliciously or are compromised rather than exploiting a flaw in the deployed smart contract logic. 

Final amounts will be no less than the respective minimum amounts of each severity level, based on the final severity classification of the bug report. ENS only pays for the first disclosure of a vulnerability. This discretion is exercised in good faith and is subject to mediation.

Depending on the severity and internal assessment, ENS retains the right to reward above the stated amounts at its discretion.

**The default 10% of funds at risk minimum reward calculation in VSC v2.3 does not apply.  The custom critical reward calculation set forth below controls.**

### External Dependency Discount

Where a valid vulnerability can only be exploited if a third-party system outside ENS's control fails or behaves abnormally (e.g., oracle failures, bridge compromises, or third-party dependency malfunctions), ENS may reduce the reward by up to 50% to reflect the conditional nature of the risk. This discount does not apply where ENS has the ability to mitigate or protect its users through its own action, in such cases, the full reward applies. Any reduction under this clause must be accompanied by a brief written explanation identifying the specific external dependency and the rationale for the discount applied.

For the sake of clarity, in the event of a conflict between that classification system and the rewards schema set forth below, the below language will control. 

### Critical Reward Calculation

The reward for critical smart contract vulnerabilities is calculated as 10% of funds directly affected, up to a maximum of USD 250,000, calculated as follows:

| &nbsp;&nbsp;&nbsp;Base: 10% of funds directly affected, up to $250,000 | Up to $250,000 |
| :---- | :---- |
| &nbsp;&nbsp;&nbsp;Where funds directly affected exceed $1,500,000: | Minimum $150,000 |
| &nbsp;&nbsp;&nbsp;Where funds directly affected are between $500,000 and $1,500,000: | Minimum $75,000 |
| &nbsp;&nbsp;&nbsp;Where funds directly affected are below $500,000, or not objectively calculable | Minimum $25,000 |
| &nbsp;&nbsp;&nbsp;Where the vulnerability affects fewer than 50 on-chain assets or accounts: reward may be &nbsp;&nbsp;&nbsp;further adjusted downward at the program’s discretion. | Minimum $10,000 |


__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused,only the initial attack will be considered for a reward within the mitigation window **48 hours for Security Council, 2 weeks for DAO vote.**
. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 

For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

### High Reward Calculation

The reward for high-severity smart contract vulnerabilities ranges between USD 25,000 and USD 100,000, based on the assessed impact and funds at risk.

| &nbsp;&nbsp;&nbsp;High vulnerabilities concerning theft or permanent freezing of unclaimed yield or &nbsp;&nbsp;&nbsp;royalties are considered at the full amount of funds at risk, capped at the maximum high &nbsp;&nbsp;&nbsp;reward. This is to encourage security researchers to uncover and responsibly disclose &nbsp;&nbsp;&nbsp;vulnerabilities that may not have significant monetary value today but could still be &nbsp;&nbsp;&nbsp;damaging to the project if left unaddressed. | Up to <br>$100,000 |
| :---- | :---- |
| &nbsp;&nbsp;&nbsp;Temporary freezing of funds is classified as High severity. The reward is determined within the &nbsp;&nbsp;&nbsp;High reward range based on the value of funds affected and the estimated duration of the &nbsp;&nbsp;&nbsp;freeze. | Up to<br>$100,000 |
| &nbsp;&nbsp;&nbsp;In cases where objective calculation is not feasible, there will be a base reward, with the &nbsp;&nbsp;&nbsp;discretion to increase the amount. | Base $25,000 |

**Track B:  Websites and Applications**

### **Critical Web / App Reward Calculation**

Critical web/application bug reports will be rewarded with USD 25,000, **only** if the impact leads to:

- A loss of funds involving an attack that does not require any user action  
- Unauthorized minting of tokens on-chain.  
- Private key or private key generation leakage leading to unauthorized access to user funds.

__Severity Assessment for XSS Reports:__

- Injection of malicious content into app.ens.domains to initiate a malicious transaction without requiring unusual user interaction will be considered critical.
- Injection of malicious scripts into other ENS subdomains (besides app.ens.domains) that offer web3 wallet connections will be considered high for stored XSS and medium for reflected XSS.
- XSS on static ENS websites like metadata.ens.domains, which do not offer web3 functionality, will be considered low.

__Reward Payment Terms__

Payouts are handled by the ENS team directly and are denominated in USD. However, payments are done in USDC.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## **Eligible Versions** 

This section defines (1) which code we accept reports against and (2) what is in scope on mainnet versus testnet. 
A deployment being tagged does not by itself place it in scope, eligibility is set by the rules below.

We identify code by its Git release tag:

vx.x.x (e.g. v1.2.3) — a finalized release (no suffix).
vx.x.x-RCX (e.g. v1.2.3-RC0) — a release candidate.
vx.x.x-<tag> (e.g. v1.2.3-testnet) — a pre-release build (e.g. a testnet build).

### Mainnet
Only the latest finalized release (vx.x.x) deployed to mainnet is in scope. Release candidates and other pre-release builds are not eligible on mainnet.

### Testnet carve-out

**Testnet and staging are out of scope by default.** Release candidates and other pre-release builds are handled here, not on mainnet. 

A testnet contract, including a release candidate, **is in scope only if **it meets both of the following:

**Version**: its version is greater than or equal to the latest mainnet release. Older or retired versions are out of scope.
Recognized deployment: it satisfies at least one of:
(a) the contract is included in a tagged GitHub release in an in-scope repository (ens-contracts/releases or contracts-v2/releases); OR
(b) the contract address is referenced in official ENS documentation at docs.ens.domains (e.g. the deployments page).

Any other testnet deployment, including contracts deployed by ENS-controlled accounts but not in a release or referenced in the documentation, is out of scope. 

Website and Application testnet and staging deployments are out of scope.

### Testnet rewards:

- **Critical** — up to USD 25,000
- **High** — USD 25,000 (flat)
- **Medium** — USD 2,500 (flat)
- **Low** — from USD 1,000 (flat, floor)

V1 contracts will remain in scope during the migration period and will be explicitly removed from scope once migration is complete.

## Out of scope (program-specific)

It is recommended to keep an eye on the audits secction, as the listed audits are constantly updated.

**For the avoidance of doubt, this Out of Scope exclusion controls over the Primacy of Impact provision.**

- Taking over broken links from sources that are no longer considered active, such as links related to meeting minutes, past events etc., as this content is left up for archival purposes and should not be changed. 

- Products funded or maintained by the DAO that are not on the published asset list are excluded regardless of impact

## Out of scope and rules

.

## Prohibited activities (program-specific)

https://ens.dev is Out of Scope of the Bug bounty program

## Known issues (3)

- Malicious DAO can reduce the expiration of names (https://discuss.ens.domains/t/security-advisory-a-malicious-dao-update-could-reduce-the-registration-duration-of-registered-eth-2lds/17576/12)
- Malicious DAO can steal names using an upgrade to the NameWrapper (https://discuss.ens.domains/t/security-advisory-a-malicious-dao-update-could-reduce-the-registration-duration-of-registered-eth-2lds/17576/12)
- Namewrapper race condition allowing fuses to be set inappropriately (https://discuss.ens.domains/t/front-running-vulnerability-in-namewrapper/19938)
