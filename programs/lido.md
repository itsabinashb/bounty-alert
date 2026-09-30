# Lido

- Page: https://immunefi.com/bug-bounty/lido/scope/
- Max bounty: $2,000,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (29)

- [smart_contract] https://docs.lido.fi/deployed-contracts
- [smart_contract] https://github.com/lidofinance/aave-delivery-infrastructure
- [smart_contract] https://github.com/lidofinance/aragon-apps
- [smart_contract] https://github.com/lidofinance/circuit-breaker — circuit breaker
- [smart_contract] https://github.com/lidofinance/community-staking-module
- [smart_contract] https://github.com/lidofinance/core
- [smart_contract] https://github.com/lidofinance/dual-governance
- [smart_contract] https://github.com/lidofinance/easy-track
- [smart_contract] https://github.com/lidofinance/governance-crosschain-bridges
- [smart_contract] https://github.com/lidofinance/lido-council-daemon
- [smart_contract] https://github.com/lidofinance/lido-keys-api
- [smart_contract] https://github.com/lidofinance/lido-l2
- [smart_contract] https://github.com/lidofinance/lido-l2-with-steth
- [smart_contract] https://github.com/lidofinance/lido-oracle
- [smart_contract] https://github.com/lidofinance/lido-vesting-escrow
- [smart_contract] https://github.com/lidofinance/mev-boost-relay-allowed-list
- [smart_contract] https://github.com/lidofinance/oz-merkle-tree
- [smart_contract] https://github.com/lidofinance/stonks
- [smart_contract] https://github.com/lidofinance/validator-ejector
- [websites_and_applications] http://dao.lido.fi/
- [websites_and_applications] http://stvaults.lido.fi/
- [websites_and_applications] https://blog.lido.fi — Auxiliary Services
- [websites_and_applications] https://csm.lido.fi
- [websites_and_applications] https://docs.lido.fi — Auxiliary Services
- [websites_and_applications] https://github.com/lidofinance/onchain-mon — Auxiliary Services
- [websites_and_applications] https://lido.fi
- [websites_and_applications] https://operators.lido.fi — Auxiliary Services
- [websites_and_applications] https://stake.lido.fi
- [websites_and_applications] https://trp.lido.fi — Auxiliary Services

## Asset notes

Smart Contracts labeled or categorized as testnet are not in scope of this bug bounty program. 

Reports regarding domains not listed under the scope section are paid at contributors discretion.

## Impacts in scope (31)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Acquiring owner/admin rights or roles without contract’s owner/admin action
- [smart_contract] High: Economic/financial attacks
- [smart_contract] High: Missing access controls / unprotected internal interfaces
- [smart_contract] High: Off-chain apps sensitive data extraction (e.g. Oracle private keys)
- [smart_contract] High: Permanent freezing of tokenized staking yield
- [smart_contract] High: Reversible freezing of funds
- [smart_contract] High: Theft of tokenized staking yield
- [smart_contract] High: Theft or loss of funds from a treasury
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Susceptibility to frontrunning
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
- [websites_and_applications] High: Retrieve sensitive data/files from a running server, such as:  /etc/shadow database passwords blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] Medium: Improperly disclosing confidential user information such as email address, phone number, IP address, etc.
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript injection such as HTML injection, replacing existing text with arbitrary text, arbitrary file uploads, etc.
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Changing non- sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the first/last name of user, or en/disabling
- [websites_and_applications] Low: Taking down the application/website
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.

## Impact notes

If the smart contract where the vulnerability exists can be paused, only the initial attack window of 1-hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by pausing the component where the vulnerability exists.

If the smart contract where the vulnerability exists can only be upgraded, only the initial attack window of 5-days for Critical issues and 9 days for other issues will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading the component where the vulnerability exists.

## Rewards

- [smart_contract] Critical: maxReward=$2,000,000, minReward=$50,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$250,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$50,000, minReward=$1,000, rewardModel=range
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$100,000, minReward=$50,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$50,000, minReward=$5,000, rewardModel=range
- [websites_and_applications] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Low: fixedReward=$500, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3). This is a simplified 4-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

All web and app bugs must come with a PoC in order to be accepted. All web and app bug reports without a PoC will be rejected with a request for a PoC.

### Smart Contracts Rewards Breakdown

**Critical**

- **Loss of user funds:**
    - When a minimum of 2,000,000 USD of assets is at risk
    - Reward: **Minimum 100,000 USD**, **Maximum 2,000,000 USD**
- **Loss of non-user funds (e.g., treasury):**
    - When a minimum of 1,000,000 USD of assets is at risk
    - Reward: **Minimum 50,000 USD**, **Maximum 1,000,000 USD**

 **High**

- When a minimum of 250,000 USD of assets is at risk
- Reward: **Minimum 10,000 USD**, **Maximum 250,000 USD**

**Medium**

- When a minimum of 50,000 USD of assets is at risk
- Reward: **Minimum 1,000 USD**, **Maximum 50,000 USD**

**Low**

- Reward: **1,000 USD**

---

### Web/App Rewards Breakdown

#### Critical

* Reward: **Minimum 50,000 USD**, **Maximum 100,000 USD**

#### High

* Reward: **Minimum 5,000 USD**, **Maximum 50,000 USD**

#### Medium

* Reward: **Minimum 1,000 USD**, **Maximum 5,000 USD**

#### Low

* Reward: **500 USD**

---

- (Smart contracts Out Of Scope) Rewards on partner contracts are paid at contributors discretion.
- Reports regarding domains not listed under the scope section are paid at contributors discretion.

Payouts are handled by the __Lido__ contributors directly and are denominated in __USD__. Payouts can be done in __USDC__, __USDS__, __DAI__, or __USDT__, at the decision of the bug bounty hunter.

## Out of scope (program-specific)

- Best practice critiques.
- Only accept reports targeting deployed contracts, not latest contracts in repos.
- Only accept reports associated with releases, not develop or feature branches.
- All impact of an attack on Oracles or KAPI must be described in t
erms of impact on protocol itself and classified accordingly.
- All impact of an attack on re-entrancy must be described in terms of impact on protocol itself and classified accordingly.
- Rewards on partner contracts are paid at contributors discretion.
- For Auxiliary services only accept vulnerabilities leading to application takeover as "Execute arbitrary system commands"
- Reports regarding domains not listed under the scope section are paid at contributors discretion.
- Smart Contracts labeled or categorized as testnet are not in scope of this bug bounty program.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

Public disclosure of an unpatched vulnerability in an embargoed bounty
Automated testing of services that generates significant amounts of traffic
Any denial of service attacks that are executed against project assets
Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
Attempting phishing or other social engineering attacks against our contributors and/or stakers
Any testing with pricing oracles or third-party smart contracts
Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
Any other actions prohibited by the Immunefi Rules - https://immunefi.com/rules/

## Known issues (1)

- When someone creates a motion, its snapshot block is set to the current block.number. While, theoretically, it's totally correct and reasonable, there is a possibility to take a flashloan of the Lido governance token (LDO) and object the motion multiple times from different accounts until the objection threshold is reached. (https://github.com/lidofinance/easy-track/issues/26)
