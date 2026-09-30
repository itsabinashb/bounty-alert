# Audit Comp | DeGate

- Page: https://immunefi.com/bug-bounty/boosteddegatebugbounty/scope/
- Max bounty: $400,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2023-12-04T09:00:00.000Z

## Assets in scope (5)

- [smart_contract] https://etherscan.io/address/0x0d2ec0a5858730e7d49f5b4ae6f2c665e46c1d9d#code — Timelock for ExchangeProxy
- [smart_contract] https://etherscan.io/address/0x2028834B2c0A36A918c10937EeA71BE4f932da52#code — Gnosis Multisig
- [smart_contract] https://etherscan.io/address/0x54D7aE423Edb07282645e740C046B9373970a168#code — DepositContractProxy
- [smart_contract] https://etherscan.io/address/0x9C07A72177c5A05410cA338823e790876E79D73B#code — ExchangeProxy
- [smart_contract] https://etherscan.io/address/0xf2991507952d9594e71a44a54fb19f3109d213a5#code — Timelock for DepositContractProxy

## Asset notes

__Assets in Scope__

All impacts resulting from the introduction of the in code listed in scope are in scope for this audit competition.

All impacts not resulting from the introduction of the code listed in scope should be submitted to [DeGate’s normal bug bounty program ](https://immunefi.com/bounty/degate/)instead.

Impacts on test files, mock files, and configuration files are out of scope, unless stated otherwise in the bug bounty program.
Timelock contracts source code (a fork from Compound): [https://github.com/degatedev/protocols/blob/degate1.1.0/packages/loopring_v3/contracts/thirdparty/timelock](https://github.com/degatedev/protocols/blob/degate1.1.0/packages/loopring_v3/contracts/thirdparty/timelock)

Upgradability contracts source code: [https://github.com/degatedev/protocols/blob/degate1.1.0/packages/loopring_v3/contracts/thirdparty/proxies](https://github.com/degatedev/protocols/blob/degate1.1.0/packages/loopring_v3/contracts/thirdparty/proxies)

Documentation directly pertaining to the in scope code can be found at: [https://github.com/degatedev/protocols/commit/180138015197c886ec3c87efa8bf0031b653359f#commitcomment-132582143](https://github.com/degatedev/protocols/commit/180138015197c886ec3c87efa8bf0031b653359f#commitcomment-132582143) 

__Further Resources__

DeGate is especially interested in bugs in how this new code interacts with their older code.

All DeGate’s smart contract code, including out of scope smart contract code, can be found at [https://github.com/degatedev/protocols/tree/degate1.1.0/packages/loopring_v3/contracts](https://github.com/degatedev/protocols/tree/degate1.1.0/packages/loopring_v3/contracts), along with the [Protocol Specification Docs](https://github.com/degatedev/protocols/blob/degate1.1.0/DeGate%20Protocol%20Specification%20Document.md?utm_source=immunefi), [Circuit Design Docs](https://github.com/degatedev/protocols/blob/degate1.1.0/Circuit%20Design.md?utm_source=immunefi) and [Smart Contract Design Docs.](https://github.com/degatedev/protocols/blob/degate1.1.0/Smart%20Contract%20Design.md?utm_source=immunefi)

DeGate Testnet is currently live on [https://testnet.degate.com,](https://testnet.degate.com) and more details can be found in the product documentation ([https://docs.degate.com/v/product_en/readme](https://docs.degate.com/v/product_en/readme) ). 

To ask DeGate or Immunefi questions directly, join the [DeGate Audit Competition Discord channel.](https://discord.com/channels/787092485969150012/1173840561455775744)

__Previous Audits & Known Issues__

Private known issues, meaning known issues which were not publicly disclosed, are valid for a partial reward. If a bug found during the event requires an immediate fix then that bug will be considered a publicly known issue as soon as the fix is deployed.
DeGate’s completed audit reports and known issues can be found at:

- Previous Code: 
https://github.com/degatedev/protocols/blob/degate_mainnet/packages/loopring_v3/security_audit/Trailofbits%20-%20DeGate%20Final%20Audit%20Report.pdf 
- Previous Code: https://github.com/degatedev/protocols/blob/degate_mainnet/packages/loopring_v3/security_audit/Least%20Authority%20-%20DeGate%20DAO%20DeGate%20Smart%20Contracts%20Updated%20Final%20Audit%20Report.pdf 
- Previous Code:
https://github.com/degatedev/protocols/blob/degate_mainnet/packages/loopring_v3/security_audit/Least%20Authority%20-%20DeGate%20Technology%20DeGate%20zk-SNARK%20Circuit%20Final%20Audit%20Report.pdf
- Previous Code: https://github.com/degatedev/protocols/blob/degate_mainnet/packages/loopring_v3/security_audit/DeGate_Report_EN-final2023.pdf 
- Previous Code: https://github.com/degatedev/protocols/blob/degate_mainnet/packages/loopring_v3/security_audit/DeGate_Report_EN-final20230912.pdf  
- Latest Code:
https://github.com/degatedev/protocols/blob/degate1.1.0/packages/loopring_v3/security_audit/DeGate_Report_EN-20231115.pdf

Any unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

__Known Issue Assurance__

DeGate commits to providing Known Issue Assurance to bug submissions through their program. This means that DeGate will either disclose known issues publicly, or at the very least, privately via a self-reported bug submission.

In a potential scenario of a mediation, this allows for a more objective and streamlined process, in order to prove that an issue is known. Otherwise, assuming the bug report is valid, it would result in the report being considered as in scope, and due a reward.

__Primacy of Impact vs Primacy of Rules__

This timeboxed bug bounty adheres to the Primacy of Rules, which means that the whole timeboxed bug bounty program is run strictly under the terms stated on this page.

If your bug report demonstrates an impact which does not originate from or depend on the assets in scope of this timeboxed bug bounty program then it may be valid for a reward on [DeGate’s normal bug bounty program](https://immunefi.com/bounty/degate/), which utilizes Primacy of Impact.

## Impacts in scope (24)

- [smart_contract] Critical: Direct theft of funds exceeding 1,000,000 USD from the Default Deposit Contract
- [smart_contract] Critical: Permanent freezing of funds exceeding 2,500,000 USD in the Default Deposit Contract.
- [smart_contract] High: Climbing blocks fails to recovery the asset tree (Zero Knowledge Proof Circuit)
- [smart_contract] High: Direct theft of user funds from the Default Deposit Contract that is less than 1,000,000 USD.
- [smart_contract] High: Force DeGate into Exodus Mode
- [smart_contract] High: Impact of this malicious contract verification through zk-proof
- [smart_contract] High: Permanent freezing of funds from the Default Deposit Contract that requires malicious actions from the DeGate Operator.
- [smart_contract] High: Permanent freezing of funds in the Default Deposit Contract that is less than 2,500,000 USD.
- [smart_contract] High: Permanent freezing of unclaimed rewards
- [smart_contract] High: Prevent new token from registering (Zero Knowledge Proof Circuit)
- [smart_contract] High: Prevent new users from registering (Zero Knowledge Proof Circuit)
- [smart_contract] High: Steal trading fee or gas fee (Zero Knowledge Proof Circuit)
- [smart_contract] High: Temporary freezing of funds: Minimum freezing of 15 days (Zero Knowledge Proof Circuit)
- [smart_contract] High: The account cannot be used (Zero Knowledge Proof Circuit)
- [smart_contract] High: The amount of tokens in the L2 is inconsistent with that of the L1, except for Non-Standard tokens (Zero Knowledge Proof Circuit)
- [smart_contract] High: Theft of funds from the Default Deposit Contract that requires malicious actions from the DeGate Operator.
- [smart_contract] High: Theft of unclaimed rewards
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds: Minimum 24hrs
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Circuit fails to work correctly, but doesn’t lose value (Zero Knowledge Proof Circuit)
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the [Immunefi PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)

__List of ERC20, ERC721, and ERC777 that DeGate Can Interact With:__

- DeGate is permissionless and can interact with all ERC20s. However, impacts involving balance changes and authority freezes caused by the token contract itself are out of scope, such as rebase tokens
- ERC721 and ERC777 are incompatible with DeGate

__Validity of bugs dependent on 100% trusted actors or privileged addresses:__

- DeGate is built on the principle of Trustlessness, or ‘Can’t do evil’. Impacts due to the unintended functions of an Operator are especially valuable and valid for a reward.
- DeGate is interested in all impacts caused by the unintended functionality of multisig owners. Such bugs are in scope and valid for a reward, with the exception of impacts dependent on the multisig owners proposing new malicious code that will only implement after a 45 day delay.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attacks within the first hour will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 
- For critical repeatable attacks on smart contracts that can not be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Feasibility Limitations__

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards ](https://immunefisupport.zendesk.com/hc/en-us/sections/18488140853905-Feasibility-Limitations)which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

## Rewards

- [smart_contract] Critical: level=critical, payout=Pool of USD $300,000, pocRequired=True
- [smart_contract] High: level=high, payout=Pool of USD $50,000, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Pool of USD $50,000 (baseline), pocRequired=True
- [smart_contract] Low: level=low, payout=Pool of USD $50,000 (baseline), pocRequired=True

## Reward notes

This audit competition has $400,000 USD in rewards split across 3 reward pools. $300,000 is allocated to the Criticals reward pool, $50,000 to the Highs reward pool, and $50,000 to the Baseline rewards pool.

__Reward Payment Terms__

Payouts are handled by the DeGate team directly and are denominated in USD. However, payouts are done in USDC.

Rewards will be distributed all at once after the event has concluded and the final bug reports have been resolved.

The following reward rules are a summary, for an in-depth explanation read our [Reward Distribution Rules article](https://immunefisupport.zendesk.com/hc/en-us/articles/20215594250385-DeGate-s-Boosted-Bug-Bounty-Reward-Distribution-Rules). The reward mechanisms are designed to reward all high quality whitehat work, with the greatest rewards for Critical issues and unique findings.

__Duplicate & Private Known Issue Reward Policy__

Duplicate bug reports which are in-scope for this event are considered valid and will be rewarded in a Sybil-resistant manner. Attempts to abuse the duplicate reward policy will result in a ban and forfeit of all rewards.
Private known issues, meaning bugs known to the project but not publicly disclosed, which are in scope for this event are considered valid and will be rewarded at a reduced rate of 25%.

__Baseline Reward Pool__

The $50,000 USD baseline reward pool is distributed among all participants. 80% is split among all valid report submissions based on the bug’s severity. 20% is distributed at Immunefi’s discretion to highly valuable reports, even if they’re technically invalid, and other significant contributions.
The entire baseline reward pool will be distributed even if no valid bugs are found.

__Criticals Reward Pool__

The $300,000 USD Criticals reward pool is distributed among all valid Critical severity reports. This reward pool is split among all Critical bug submissions with 80% going to the primary finder and 20% going to all other finders in a Sybil-resistant way. The primary finder is the first whitehat to demonstrate how the bug is Critical severity.
If no Critical severity bugs are found then this reward pool is not distributed.

__Highs Reward Pool__

The $50,000 USD Highs reward pool is distributed among all valid High severity reports. This reward pool is split among all High bug submissions with 80% going to the primary finder and 20% going to all other finders in a Sybil-resistant way. The primary finder is the first whitehat to demonstrate how the bug is High severity.
If no High severity bugs are found then this reward pool is not distributed.

## Out of scope (program-specific)

(none)

## Out of scope and rules

These impacts are out of scope for this bug bounty program. 

__All Categories:__

- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
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
- Impacts involving balance changes and authority freezes caused by the token contract itself, such as rebase tokens
- Impacts involving the need to use more than 300 ETH in gas fees to force entry into Exodus Mode through block stuffing, storage occupation, or executing other potential economic attacks.

__Prohibited Activities:__

- Any testing on mainnet or public testnet deployed code; all testing should be done on local-forks of either public testnet or mainnet
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Out-of-scope bugs which are in-scope for DeGate’s normal bug bounty program may not be published. Such bug reports are to be submitted to [DeGate’s normal bug bounty program.](https://immunefi.com/bounty/degate/)
- Bug reports in mediation may not be published until mediation has concluded.

Immunefi may publish bug reports submitted to this audit competition.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
