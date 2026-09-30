# Audit Comp | Alchemix

- Page: https://immunefi.com/bug-bounty/alchemix-boost/scope/
- Max bounty: $125,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - high, smart_contract - critical, smart_contract - medium, smart_contract - low
- End date: 2024-05-21T10:30:00.000Z

## Assets in scope (13)

- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/AlchemixGovernor.sol — AlchemixGovernor.sol - 55
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/BaseGauge.sol — BaseGauge.sol - 49
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/Bribe.sol — Bribe.sol - 256
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/CurveEthPoolAdapter.sol — CurveEthPoolAdapter.sol - 34
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/CurveMetaPoolAdapter.sol — CurveMetaPoolAdapter.sol - 30
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/FluxToken.sol — FluxToken.sol - 152
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/Minter.sol — Minter.sol - 124
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/RevenueHandler.sol — RevenueHandler.sol - 183
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/RewardPoolManager.sol — RewardPoolManager.sol - 102
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/RewardsDistributor.sol — RewardsDistributor.sol - 286
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/Voter.sol — Voter.sol - 335
- [smart_contract] https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/src/VotingEscrow.sol — VotingEscrow.sol - 887
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Private Known Issues Reward Policy__

Private known issues, meaning known issues that were not publicly disclosed, are valid for a reward equal to that of a bug one severity lower.

__Known Issue Assurance__

Alchemix commits to providing Known Issue Assurance to bug submissions through their program. This means that Alchemix will either disclose known issues publicly, or at the very least, privately via a self-reported bug submission. 

In a potential scenario of a mediation, this allows for a more objective and streamlined process, in order to prove that an issue is known. Otherwise, assuming the bug report is valid, it would result in the report being considered as in-scope, and due a reward.

__Primacy of Impact vs Primacy of Rules__

Alchemix adheres to the Primacy of Impact for all impacts.

Primacy of Impact means that the impact is prioritized rather than a specific asset. This encourages security researchers to report on all bugs with an in-scope impact, even if the affected assets are not in scope. For more information, please see [Best Practices: Primacy of Impact](https://immunefisupport.zendesk.com/hc/en-us/articles/12340245635089-Best-Practices-Primacy-of-Impact). 

When submitting a report on Immunefi’s dashboard, the security researcher should select the Primacy of Impact asset placeholder. If the team behind this project has multiple programs, those other programs are not covered under Primacy of Impact for this program. Instead, check if those other projects have a bug bounty program on Immunefi.

If the project has any testnet and/or mock files, those will not be covered under Primacy of Impact.

All other impacts are considered under the Primacy of Rules, which means that they are bound by the terms and conditions set within this program.

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this audit competition and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Alchemix has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (21)

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
- [smart_contract] High: Temporary freezing of funds for 12 hours
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the Immunefi PoC Guidelines and Rules.

__Whitehat Educational Resources & Technical Info__

- 1-year old medium article that is still largely correct: [https://alchemixfi.medium.com/vealcx-update-272e8900ac5a](https://alchemixfi.medium.com/vealcx-update-272e8900ac5a)
- Draft document that will eventually turn into a governance proposal to explain and define the launch parameters: [https://alchemixdao.notion.site/veALCX-Launch-Parameters-Proposal-60113919e018424db7fc03c346c34386?pvs=4](https://alchemixdao.notion.site/veALCX-Launch-Parameters-Proposal-60113919e018424db7fc03c346c34386?pvs=4)

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

This is a brand-new system to Alchemix, but is an upgrade of Velodromes veVELO (which is an upgrade of solidly’s vote-escrow system). The primary differences are:
- Alchemix is not a DEX, and therefore sends a majority of ALCX to external locations such as incentives for 3rd party DEX pools, and vote incentives on platforms such as votium, votemarket, etc. Therefore, the system requires both external and internal gauges (ie, gauges that send ALCX to 3rd party and internal contracts). 
- Alchemix has introduced a “continuous max lock” boolean that may be enabled to prevent decay in voting power and remaining lock time (thus eliminating the need to manually re-lock a position constantly)
- Alchemix has added the FLUX token, which is earned by veALCX lockers. Accrued FLUX credit can be burned to boost gauge voting power. Alternatively, credit can be burned to mint an ERC20 version of FLUX. The FLUX ERC20 is tradeable, and can be used to unlock a veALCX position early. The ERC20 can NOT be used to boost gauge voting power. 
- Alchemix has created a system by which any veALCX revenue asset can be whitelisted to be converted to alAssets to repay users’ debt so long as there is a direct swap path. Assets that are not whitelisted will be passed through directly to veALCX users. 

__Where do you suspect there may be bugs?__

- **Which parts of the code are you most concerned about?**

The highest concern is in the accounting of bribes, including ensuring the total supply is tracked correctly. 

- **What attack vectors are you most concerned about?** 

Any attack that would artifically inflate a user’s claim on bribes, rewards, or a user’s voting power, or any other means by which bribes and rewards could be stolen.

- **Which part(s) of the system do you want whitehats to attempt to break the most?**

The rewards distributor and voting system has the most complexity and handles bribes which could be a variety of assets as well as tracking voting

- **Are there any assumed invariants that you want whitehats to attempt to break?**
    - A user should never be able to claim more bribes than they have earned
    - A user should never be able to claim more revenue than they have earned
	- A user should never be able to claim more rewards than they have earned
	- A user should never be able to vote with more power than they have


__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?__

ERC20, ERC721, ERC4626

__What monitoring systems may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

None.

__What Roles are there, and what capacities do they have?__

users - veALCX holders: can create new veALCX tokens, vote, claim bribes, claim rewards (ALCX), claim revenue, claim / burn / boost vote with FLUX
delegates - addresses veALCX holders approved to act on their behalf 
admin - address (governance) that can update system state variables as needed

__Which Roles are trusted roles and what privileges do they hold?__

admin - address (governance) that can update system state variables as needed.

__Are there trusted roles for which you would consider any bugs invalid, even if the roles are not intended to have that capacity?__

Any malicious behavior that an admin can execute is acknowledged and invalid since the assumption is that admin will be a trusted party

__What external dependencies are there?__

Balancer pool - 0xf16aEe6a71aF1A9Bc8F56975A4c2705ca7A782Bc

Aura pool - 0x8B227E3D50117E80a02cd0c67Cd6F89A8b7B46d7

ALCX/ETH price feed - 0x194a9AaF2e0b67c35915cD01101585A33Fe25CAa

__Where might whitehats confuse out-of-scope code to be in-scope?__

The Balancer pool and Aura pools are out of scope and are acknowledged as a third-party pool integration. 

Dependencies should be audited to verify they are being referenced and utilized correctly, but the dependencies themselves do not need to be audited (ie, it should be assumed the dependencies function as intended). For example, it should be assumed the Balancer Pool Token always represents 80% balance of ALCX and a 20% balance of ETH that tracks the initial deposit. 

__Are there any unusual points about your protocol that may confuse whitehats?__

Voting power decay over time. If a user does not update their vote their voting power remains constant, however, they will not be eligible for future bribes or FLUX earnings until they vote. This is considered when accounting for the distribution of Bribes in a given Epoch. 

Rewards claiming with the Alchemists. If a user has an open debt position in an Alchemist (alETH, alUSD) they can claim revenue that pays off the debt in a given position, so long as that revenue asset is whitelisted to be swapped to the alAsset. 

Aura rewards with ALCX-BPT. Deposits are sent to the Aura rewards pool when a user creates a veALCX position. VotingEscrow.sol accounts for this and manages the deposit and withdrawal when a user deposits or withdrawals from the VotingEscrow.sol contract. 

Users can boost their vote only with unclaimed FLUX. Once FLUX has been claimed it can only be used to unlock a veALCX token early. It is intentional that it requires longer than the period their token is locked to accrue enough FLUX to unlock a veALCX position early. 

__What is the test suite setup information?__

[https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/README.md](https://github.com/alchemix-finance/alchemix-v2-dao/blob/main/README.md)

__Which chains are the smart contracts going to be deployed to?__

ETH Mainnet

__Public Disclosure of Known Issues__

Bug reports covering previously discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

- Ambiguous Proposal Executions via the TimelockController are acknowledged and a part of the governance management system. 
- We are assuming that the price of the alAsset will always be at or below the price of the revenue token. This is currently a safe assumption since this imbalance has always held true for alUSD and alETH since their inception

__Previous Audits__

Alchemix’s completed audit reports can be found at [https://drive.google.com/file/d/1YsO1t1-hSK1wkHajT_GAZ-u35O1Su74X/view?usp=sharing](https://drive.google.com/file/d/1YsO1t1-hSK1wkHajT_GAZ-u35O1Su74X/view?usp=sharing). Any unfixed vulnerabilities  mentioned in these reports are not eligible for a reward.

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the $125,000 USD Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the $100,000 USD Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the $75,000 USD Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the $75,000 USD Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Alchemix Audit Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/24665684227857-Alchemix-Audit-Competition-Reward-Terms).

The reward pool will be entirely distributed among participants. The size depends on the bugs found:
- If no High or Critical severity bugs are found the reward pool will be **$75,000 USD**
- If one or more High severity bugs are found the reward pool will be **$100,000 USD**
- If one or more Critical severity bugs are found the reward pool will be **$125,000 USD**

For this audit competition, duplicates and private known issues are valid for a reward.

Rewards are distributed according to the impact of the vulnerability based on the Immunefi [Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). 

__Reward Payment Terms__

Payouts are handled by the Alchemix team directly and are denominated in USD. However, payments are done in USDC

Rewards will be distributed all at once based on Immunefi’s distribution formula after the event has concluded and the final bug reports have been resolved.

## Out of scope (program-specific)

(none)

## Out of scope and rules

These impacts are out of scope for this bug bounty program. 

__All Categories:__

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program

__Blockchain/DLT & Smart Contract Specific:__

- Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
- Impacts requiring basic economic and governance attacks (e.g. 51% attack)
- Lack of liquidity impacts
- Impacts from Sybil attacks
- Impacts involving centralization risks

__Prohibited Activities:__

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
