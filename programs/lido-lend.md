# Lido Lend

- Page: https://immunefi.com/bug-bounty/lido-lend/scope/
- Max bounty: $2,000,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: (none)
- End date: (none)

## Assets in scope (6)

- [smart_contract] https://docs.lido.fi/lend/deployed-contracts/ — Deployed contracts
- [smart_contract] https://github.com/lidofinance/lend — Core
- [smart_contract] https://github.com/lidofinance/lend-guardian-daemon — Guardian daemon
- [smart_contract] https://github.com/lidofinance/lend-irm — Interest rate models
- [smart_contract] https://github.com/lidofinance/lend-markets — Markets
- [websites_and_applications] https://lend.lido.fi — Website

## Asset notes

Smart Contracts labeled or categorized as testnet are not in scope of this bug bounty program.

Domains not listed in scope are out of scope. Lido may still make a goodwill payment for such a report.

The program covers deployed code only:

- For a smart contract, the code in scope is the bytecode at an address on [docs.lido.fi/lend/deployed-contracts](https://docs.lido.fi/lend/deployed-contracts/). A listed repository holds its source.
- For the guardian daemon, the code in scope is its latest release or tag.
- A new contract enters the scope when that page lists it and a listed repository holds its source.

## Impacts in scope (24)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Theft or permanent freezing of protocol fees
- [smart_contract] High: Acquiring a Lido Lend role without its holder or governance granting it
- [smart_contract] High: An unprivileged attacker extracts the guardian daemon's signing key
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hours
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Retrieve sensitive data/files from a running server, such as: /etc/shadow database passwords blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Improperly disclosing confidential user information such as email address, phone number, IP address, etc.
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript injection such as HTML injection, replacing existing text with arbitrary text, arbitrary file uploads, etc.
- [websites_and_applications] Low: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the first/last name of user, or en/disabling notifications
- [websites_and_applications] Low: Taking down the application/website

## Impact notes

**Attack Window**

Lido considers only the initial attack window for a reward. The attack window is the time from the start of the attack until the protocol stops further exploitation. Its length depends on how the protocol can react and on the governance process:

- If an emergency pause can stop the attack, the window is 1 hour.
- If only an upgrade can stop the attack, the window is the time that governance needs to approve and execute the upgrade.
- If no pause and no upgrade can stop the attack, the full impact counts.

A market pause and an Exit Book pause both count as a pause. Example: only an upgrade can fix a bug in a Lido Lend oracle. But a market pause stops the attack, so the window is 1 hour.

**Report Requirements**

A smart contract report must include:

- the affected asset, one impact from the list, and the funds at risk with the calculation;
- a PoC that runs against the deployed contracts on a fork.

The PoC must:

- prove the impact, not only describe it;
- use the deployed in-scope contracts, not its own copies of them;
- change the state of in-scope contracts only with transactions, not with direct writes to their code, storage or balances;
- send only transactions that an attacker or an ordinary user can send. However, the PoC can execute a governance action that is already published, with its published parameters, e.g. activating a Lido Lend market.

## Rewards

- [smart_contract] Critical: maxReward=$2,000,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$50,000, minReward=$500, rewardModel=range
- [smart_contract] Low: maxReward=$1,000, minReward=$50, rewardModel=range
- [websites_and_applications] Critical: maxReward=$100,000, minReward=$10,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$50,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] Medium: maxReward=$5,000, minReward=$500, rewardModel=range
- [websites_and_applications] Low: maxReward=$500, minReward=$50, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3). This is a simplified 4-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

All web and app bugs must come with a PoC in order to be accepted. All web and app bug reports without a PoC will be rejected with a request for a PoC.

### Smart Contracts Rewards Breakdown

**Critical**

- **Loss of user funds:**
    - When a minimum of 2,000,000 USD of assets is at risk
    - Reward: 10% of the funds directly affected, **Minimum 20,000 USD**, **Maximum 2,000,000 USD**
- **Loss of protocol fees:**
    - When a minimum of 100,000 USD of assets is at risk
    - Reward: 10% of the funds directly affected, **Minimum 1,000 USD**, **Maximum 100,000 USD**

**High**

- When a minimum of 250,000 USD of assets is at risk
- Reward: **Minimum 5,000 USD**, **Maximum 100,000 USD**

**Medium**

- When a minimum of 50,000 USD of assets is at risk
- Reward: **Minimum 500 USD**, **Maximum 50,000 USD**

**Low**

- Reward: **Minimum 50 USD**, **Maximum 1,000 USD**

If the assets at risk are below the minimum of a level, the next lower level applies. An impact that puts no funds at risk gets the minimum reward of its level.

**Funds at Risk**

The assets at risk are the funds that the attack can take or freeze. The funds can be in the core, a vault or an Exit Book.

Lent-out tokens are with the borrowers, not in the contracts. They count only when the attack makes lenders lose them, for example when the attack erases a borrower's debt.

Each token counts once. Taken collateral counts minus the debt that its owner no longer has to repay.

Each market has a supply cap, which limits the total assets that lenders can supply. For an empty market, the assets at risk are its full supply cap. The reward is at most 10% of the supply caps of the affected markets, but never below the level minimum. For a market with no supply cap, the assets at risk are the funds in the market, and this limit does not apply.

---

### Web/App Rewards Breakdown

**Critical**

- Reward: **Minimum 10,000 USD**, **Maximum 100,000 USD**

**High**

- Reward: **Minimum 5,000 USD**, **Maximum 50,000 USD**

**Medium**

- Reward: **Minimum 500 USD**, **Maximum 5,000 USD**

**Low**

- Reward: **Minimum 50 USD**, **Maximum 500 USD**

---

Payouts are handled by the Lido contributors directly and are denominated in USD. Payouts are done in USDC on Ethereum.
All rewards are defined under Lido Discretion.

## Out of scope (program-specific)

- Best practice critiques.
- Only accept reports targeting deployed contracts, not latest contracts in repos.
- Only accept reports associated with releases, not develop or feature branches.
- All impact of an attack on offchain software must be described in terms of impact on protocol itself and classified accordingly.
- All impact of an attack on re-entrancy must be described in terms of impact on protocol itself and classified accordingly.
- Smart Contracts labeled or categorized as testnet are not in scope of this bug bounty program.
- Domains not listed in scope are out of scope. Lido may still make a goodwill payment for such a report.
- Bugs in the code of other Lido products or the Lido DAO governance contracts. The Lido bug bounty program covers them.
- The result of an action that a Lido Lend role takes within its intended authority. A role that acts beyond its limit stays in scope.
- Results of parameter choices by governance or a risk steward.
- Incorrect data from third-party screening providers to the guardian daemon.
- Normal competition between users for permissionless actions, including front-running of these actions.
- Rounding that the Lido Lend documentation describes. Other rounding counts only when an attack uses it to take or freeze funds.
- Bad debt from a market price change, and the write-off of that bad debt against the suppliers of the market.
- Guardian daemon code outside the `src/` folder.
- Guardian daemon impacts, except:
    - an early heartbeat, or a wrong or missing `flag` or `suspect` call, that an unprivileged on-chain user causes;
    - extraction of the guardian daemon's signing key by an unprivileged attacker.

**Known Issues are:**

- findings in the Lido Lend audit reports at https://github.com/lidofinance/audits/tree/main/lend;
- findings in the Morpho Blue, Morpho IRM and Morpho Bundler3 audit reports at https://github.com/morpho-org/morpho-blue/tree/main/audits, https://github.com/morpho-org/morpho-blue-irm/tree/main/audits and https://github.com/morpho-org/bundler3/tree/main/audits;
- behavior that the Morpho Blue whitepaper at https://github.com/lidofinance/lend/blob/v1.0.0/morpho-blue-whitepaper.pdf describes;
- behavior that the documentation of the repositories in the asset list describes as intended, or as an accepted risk with its effect;
- cases that a test in these repositories shows as expected behavior;
- issues in the GitHub issue trackers of these repositories, open or closed.

Documentation includes specifications and README files. An item counts only if it was public before the report, on any branch or in any pull request.

An item makes a report a known issue only when it describes the same root cause.

A bypass of a fix is a new issue, and it stays eligible.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
