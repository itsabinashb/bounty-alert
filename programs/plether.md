# Audit Competition | Plether

- Page: https://immunefi.com/bug-bounty/plether/scope/
- Max bounty: $80,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2026-11-16T10:00:00.000Z

## Assets in scope (4)

- [smart_contract] https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/HousePool.sol — HousePool.sol - Holds active LP USDG - 1,427 nSLOC
- [smart_contract] https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/MarginClearinghouse.sol — MarginClearinghouse.sol - Holds trader USDG - 1,343 nSLOC
- [smart_contract] https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/TrancheVault.sol — TrancheVault.sol - Handles pending LP deposits and funded withdrawals. Deployed as two instances, one per tranche; both are in scope - 1,657 nSLOC
- [smart_contract] https://github.com/immunefi-team/audit-comp-plether/tree/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src — All other contracts, libraries, router contracts and interfaces in packages/perps/src, except the six view-only contracts listed as out of scope below - about 17,000 nSLOC

## Asset notes

## Build Commands, Test Commands, and How to Run Them

```
Requirements: Foundry (Forge 1.5.1). Contracts use Solidity 0.8.35, compiled with via-IR.

git clone --recurse-submodules https://github.com/immunefi-team/audit-comp-plether.git
cd audit-comp-plether
# Check out the exact commit and its pinned submodules
git checkout --detach a82d4fefb02768e5b3bddcc97dee371eee24fea8
git submodule update --init --recursive
# Build perps; downloads Solidity 0.8.35 if needed
make build-perps
# Run the perps quick test suite
make test-perps

Without make: forge build --root packages/perps and forge test --root packages/perps.
```

`make test-perps` runs the quick test suite.

**Fork testing.** Release v2.0.0 deploys the in-scope perps contracts to Arbitrum Sepolia, to make fork testing with Anvil easier. The release was built from commit 1209ca8a5b94a4fb6323c7c4585846ed93db3932, and packages/perps/src is identical at the commit in scope, so the deployed contracts match the code in scope. Contract addresses and the deployment manifest are in https://github.com/immunefi-team/audit-comp-plether/tree/a82d4fefb02768e5b3bddcc97dee371eee24fea8/deployments/releases/2026-10-28-perps-arbitrum-sepolia-v2.0.0 and in the release: https://github.com/Plether-Fi/plether-core/releases/tag/v2.0.0

This deployment is for testing only. Its configuration (a single owner address, test liquidity, mock USDG) is not the production configuration, and severity is assessed with the parameters stated on this page. Run tests on a local fork; do not send transactions to the deployed contracts.

## Impacts in scope (13)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hours
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

## Known Issues and Previous Audits

Issues in the known-issues list below, or in Plether's previous audit reports (including their accepted-risk and acknowledged sections), are not eligible for a reward. Only entries published before the submission count.

Previous audit reports:

- Cecuro AI audit (October 16, 2026): https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-ai-audit-report-2026-10-26.pdf
- SC Audit Studio pre-audit: https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-pre-audit-report.pdf
- AI scan findings (October 15, 2026): https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/scan-plether-fi-plether-core-d4541b49.md

Known Issues:

- For findings marked as fixed or Acknowledged in the reports above, a report on the same root cause is valid only if it shows that the fix at commit a82d4fefb02768e5b3bddcc97dee371eee24fea8 is incomplete or introduces a new bug.
- Open findings from the Cecuro audit: MED-7 (partly fixed: a caller can still pick an older valid signed price per feed), MED-13 (a governance oracle rotation retargets armed stop-losses), MED-16 and LOW-57 (opens committed against a stale cached price, and the keeper bounty sized from it), MED-22 (carry rounding), MED-24 and MED-29 (LP refund epochs and redemption rounding), MED-30 (partly fixed: stop-losses have no automatic frozen-market trigger).
- Arbitrum and Pyth clock alignment (HIGH-1): commit time is the Arbitrum block timestamp, which can trail a Pyth price that is already published. A trader may commit after seeing a price and be filled at it. A new report on this root cause is valid only with a proof of concept showing a repeatable, net-profitable extraction from LPs beyond this limitation.
- Limitations documented in packages/perps/SECURITY.md (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/SECURITY.md): Known Limitations, Router and keeper limitations, Known limitation: live basket component selection, and Arbitrum and Pyth clock alignment.

Findings from an audit running in parallel become known issues only once they are added to this list. A report submitted before a finding is added remains eligible for a reward.

A report is invalid if its root cause was publicly disclosed in the program's listed repositories before the submission timestamp (merged or open PR, public commit, or public issue). A fix dated after the submission does not invalidate it.

## Trusted Roles and Non-Public Services

The following roles and addresses are trusted:

- Owner of each perps contract (set by Plether at deployment): after a 72-hour delay, can change risk, fee, carry, calendar, price freshness and router settings, and rotate the oracle contract. Immediately, can pause and unpause, set the treasury, recapitalize the pool, clear degraded mode, seed the tranches and activate trading, admit or sweep unaccounted USDG, assign ownerless pool assets, and rescue tokens other than USDG.
- Pauser (the EmergencyPauseCoordinator): can pause; cannot unpause.
- Guardian (set by Plether at deployment): can trigger three fixed actions through the EmergencyPauseCoordinator (emergency pause, LP epoch settlement hold, full containment). Cannot unpause, change settings, set prices or move funds.
- Protocol treasury and Junior fee recipient: receive fees.

The following services are operated by Plether and are out of scope: keepers, oracle worker, gas sponsor (paymaster) and bundler.

Out of scope: attacks that require a trusted role to act maliciously, to be compromised, or to act outside its documented operational procedures, and attacks that require direct access to a service listed above.

In scope: a legitimate, documented action by a trusted role that triggers a bug harming users or the protocol. A bug that grants an address privileges it did not originally hold is also in scope, and may be downgraded by one severity level.

A report is not out of scope only because a privileged address is affected by the exploit. Reference: Attacks Involving Access to Privileged Addresses (https://immunefisupport.zendesk.com/hc/en-us/articles/27383440951313).

Setting a parameter to a value the code allows is a trusted action, not a bug. Keepers are not trusted: anyone can execute orders, liquidations, price updates and protections, so harm caused by any caller acting as a keeper is in scope.

## Active Features and Networks

The code in scope is commit a82d4fefb02768e5b3bddcc97dee371eee24fea8, to be deployed on Arbitrum One with USDG as the settlement token. Active at launch: trading on the six-currency basket, Senior and Junior tranches, take-profit and stop-loss, and permissionless keepers. Not active at launch: the Across bridge route. Severity is assessed with the release parameters in packages/perps/DEPLOYMENT.md at this commit: maintenance margin 0.1%, initial margin 0.2%, frozen-market margin 3%, execution fee 0.04%, frozen-close spread 0.50%, Senior cap 40M USDG and 80% of the pool. Issues reachable only through features, flags, configurations or networks that are not active on the listed deployment are out of scope.

## Third-Party and Underlying Protocol Code

Plether provides reference keepers for permissionless order execution, liquidations, position protection, oracle updates, LP settlement, and queue cleanup. Trading workers live in plether-app; this repository includes operator tooling and an LP keeper script.

Keepers have no special privileges: all actions remain subject to on-chain checks. Researchers should consider any contract-permitted behavior, including deviations from the reference implementation.

The reference setup requires funded keepers and paid Hermes API access for signed Pyth updates, separately from gas and on-chain oracle fees. Some actions pay no bounty, so availability depends on operator funding.

https://github.com/Plether-Fi/plether-app/blob/master/apps/backend/README.md

## Operating Assumptions and Downgrade Criteria

Bookkeeping inconsistency and emergency containment: Independent off-chain checks can compare reconstructed positions, liabilities, and NAV against on-chain accounting. If an inconsistency is detected, an authorized guardian can pause new trading risk, LP deposits, and LP epoch settlement. This safeguard may justify reduced severity only where demonstrated monitoring coverage and response timing establish that containment limits the reported exploit. All impact achievable before containment, or through paths unaffected by the selected pause, remains assessable. Closes, liquidations, and already-funded claims remain available.

The existence of monitoring or pause functionality alone does not justify a downgrade. No detection or response deadline is assumed unless explicitly documented for the competition.

## Feasibility Limitations

A report may be valid, cite an in-scope asset, and demonstrate an in-scope impact, while still facing real-world obstacles to executing the attack. Feasibility limitations define what may and may not be cited when evaluating those obstacles.

Impact is calculated first, separately from feasibility. Feasibility limitations do not change the impact or severity of a finding, only the amount paid for it. A finding with a large impact that is infeasible retains that impact and severity, but is rewarded at a reduced amount.

The following standards apply to this competition. Where this program page defines a specific rule, the program page prevails.

**Attack Investment Amount**
A high capital requirement is generally not a valid reason to downgrade a report. Attacks requiring USD 100 million or more to execute are considered case by case. Flashloan-based attacks are valid where sufficient liquidity exists at submission or is expected within 12 months.
https://immunefisupport.zendesk.com/hc/en-us/articles/17243068885265

**Attacks With A Financial Risk To The Attacker**
Financial risk to the attacker only justifies a downgrade where the risk massively outweighs the reward. Low return on investment alone is not sufficient, and high risk alongside high return is not sufficient either. Evaluation is made from the perspective of an external user, not from information only the project holds.
https://immunefisupport.zendesk.com/hc/en-us/articles/17454897136401

**When Is An Impactful Attack Downgraded To Griefing?**
Applies to High or Critical findings where the attacker gains no profit. The baseline is that spending USD 1 to cause USD 10 or less in damage is Griefing, while spending USD 1 to cause USD 100 or more in damage is not. Ratios between these are evaluated case by case.
https://immunefisupport.zendesk.com/hc/en-us/articles/17455102268305

**Chain Rollbacks**
The ability to roll the chain back to a previous state is not a valid reason to downgrade impact, severity, or payout. Projects intending to rely on rollbacks as a safety mechanism should reflect that in their reward amounts rather than citing it after a report is submitted.
https://immunefisupport.zendesk.com/hc/en-us/articles/16913153448721

**Pre-Impact Bug Monitoring**
Where a project can objectively prove that automated tooling would prevent an exploit with 100 percent certainty, this may justify a downgrade of one severity level. Where prevention depends on human action following automated detection, the project must demonstrate 100 percent objective certainty of both detection and prevention.
https://immunefisupport.zendesk.com/hc/en-us/articles/19430444320401

**Attacks Involving Access to Privileged Addresses for Smart Contract Impacts**
A report is out of scope where the attack vector itself requires the use of a privileged address. It is not out of scope merely because a privileged address is affected by the exploit. Exceptions apply where a code vulnerability grants privileges the address did not originally hold, which may result in a one-level downgrade, and where an in-scope impact arises from a logic error that a privileged address can trigger, which remains valid.
https://immunefisupport.zendesk.com/hc/en-us/articles/27383440951313

**Attacks Involving Undeployed Code on GitHub or Equivalent for Smart Contract Impacts**
Bugs in undeployed code are valid only where the project has publicly stated the code will be deployed without further changes and the asset is in scope. In those cases the impact is treated as real, but any scaling element of the reward, such as funds at risk or freezing duration, is scaled to the minimum.
https://immunefisupport.zendesk.com/hc/en-us/articles/27871612917649

**Theft of Unclaimed Yield**
https://immunefisupport.zendesk.com/hc/en-us/articles/18753869210641

**Theft Of Unclaimed Royalties**
https://immunefisupport.zendesk.com/hc/en-us/articles/18753902288785

**Calculating the value of NFTs at risk**
https://immunefisupport.zendesk.com/hc/en-us/articles/19055304658065

For the full set of standards, see Feasibility Limitation Standards: https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377

## Proof of Concept (PoC) Requirements

Every report must include a proof of concept that demonstrates the impact it claims. If the PoC does not prove that impact, the report is invalid, whatever its description says.

PoC or it is not a finding. Observations that code “looks wrong”, without a PoC that shows the impact, do not count as findings.

These rules do not apply to Insights, which follow the Insight Reporting rules on the Information tab.

PoCs must run either in the repository's Foundry test suite at the commit in scope, or on a local Anvil fork of the Arbitrum Sepolia v2.0.0 deployment (see Build Commands), without modifying the contracts in scope. Mocks may only replace components outside the scope, such as Pyth price updates and USDG.

No PoC requires testing on production or a public testnet. Where an impact depends on a production configuration, the configuration stated on this page applies.

A runnable PoC is required. For more information, please read the Web3 PoC Guidelines (link: https://immunefisupport.zendesk.com/hc/en-us/articles/18722863230353).

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False

## Reward notes

# Rewards Terms

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873)

Rewards are denominated in USD and distributed in USDC on Ethereum.

The reward pool is **$80,000 USD** if any bug is found. That means that even if 1 Low severity bug is found, the whole reward pool is unlocked and has to be fully distributed between security researchers.

If not a single security vulnerability is found (Insights do not count as bugs) the reward pool is **15% of the Reward Pool.**

## Private Known Issues Reward Policy

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward at their full severity and unlock the corresponding reward pool without any downgrade.

Public known issues are invalid.

## Out of scope (program-specific)

## Out of Scope

Only the code listed in the Assets in Scope table is in scope. Everything else in the repository is out of scope, including:

- These six view-only contracts in packages/perps/src, which hold no funds:
    - CfdEngineAccountLens.sol: https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/CfdEngineAccountLens.sol
    - PerpsPublicLens.sol: https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/PerpsPublicLens.sol
    - CfdClosePreview.sol: https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/CfdClosePreview.sol
    - SettlementMonitorLens.sol: https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/SettlementMonitorLens.sol
    - SettlementMonitorLensSidecar.sol: https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/SettlementMonitorLensSidecar.sol
    - CfdEngineOpenQuoter.sol: https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/src/CfdEngineOpenQuoter.sol
- The other packages in the repository: packages/shared, packages/spot, packages/options, packages/perps-aa and packages/perps-aa-client. They are not part of this audit or of the next deployment.
- Everything in packages/perps outside the src folder: tests, scripts, deployment files and documentation.
- All other folders in the repository, including integration/src, script, scripts, tasks and deployments, and the dependencies in lib (OpenZeppelin, Morpho Blue, forge-std and halmos-cheatcodes).
- Keepers and the oracle worker (in the separate plether-app repository), the Across bridge route (disabled at launch) and the frontend.

In-scope perps code imports DecimalConstants and the IPyth interface from packages/shared. A bug in how in-scope perps code uses them is in scope. A bug inside packages/shared itself is not.

**All Categories:**

- Theoretical impacts without any proof or demonstration
- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations, except when submitted as Insights under the Insight Reporting section.
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program
- Issues reachable only through feature gates, flags, configurations or networks that are not active on the listed deployment are out of scope.
- Attacks that require a malicious or compromised privileged role (admin, operator, sequencer, prover, guardian, governance), or direct access to a service that is not publicly exposed, are out of scope.

**Smart Contract Specific:**

- Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks

**Prohibited Activities:**

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (13)

- All findings in the AI scan findings (October 15, 2026), including accepted-risk and acknowledged sections. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/scan-plether-fi-plether-core-d4541b49.md)
- All findings in the Cecuro AI audit report, including accepted-risk and acknowledged sections. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-ai-audit-report-2026-10-26.pdf)
- All findings in the SC Audit Studio pre-audit report, including accepted-risk and acknowledged sections. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-pre-audit-report.pdf)
- Arbitrum and Pyth clock alignment (HIGH-1): commit time is the Arbitrum block timestamp, which can trail a Pyth price that is already published. A trader may commit after seeing a price and be filled at it. A new report on this root cause is valid only with a proof of concept showing a repeatable, net-profitable extraction from LPs beyond this limitation. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/SECURITY.md)
- Cecuro MED-13: a governance oracle rotation retargets armed stop-losses. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-ai-audit-report-2026-10-26.pdf)
- Cecuro MED-16 and LOW-57: opens committed against a stale cached price, and the keeper bounty sized from it. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-ai-audit-report-2026-10-26.pdf)
- Cecuro MED-22: carry rounding. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-ai-audit-report-2026-10-26.pdf)
- Cecuro MED-24 and MED-29: LP refund epochs and redemption rounding. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-ai-audit-report-2026-10-26.pdf)
- Cecuro MED-30 (partly fixed): stop-losses have no automatic frozen-market trigger. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-ai-audit-report-2026-10-26.pdf)
- Cecuro MED-7 (partly fixed): a caller can still pick an older valid signed price per feed. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/audits/plether-ai-audit-report-2026-10-26.pdf)
- SECURITY.md: Known Limitations. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/SECURITY.md)
- SECURITY.md: Known limitation: live basket component selection. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/SECURITY.md)
- SECURITY.md: Router and keeper limitations. (https://github.com/immunefi-team/audit-comp-plether/blob/a82d4fefb02768e5b3bddcc97dee371eee24fea8/packages/perps/SECURITY.md)
