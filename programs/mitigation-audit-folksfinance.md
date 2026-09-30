# Mitigation Audit | Folks Finance

- Page: https://immunefi.com/bug-bounty/mitigation-audit-folksfinance/scope/
- Max bounty: $25,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2024-09-05T11:00:00.000Z

## Assets in scope (34)

- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/11 — fix: use CCTP source domain in message keys
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/13 — feat: can override existing invite if one exists
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/16 — fix: don’t increase total deposits by the interest paid when repaying with collateral
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/18 — fix: consider Wormhole publish message fee
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/21 — fix: round in the protocol’s favour when withdrawing and repaying with collateral
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/23 — fix: handle case where Pyth publish time is newer than block timestamp
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/25 — feat: reduce gas consumption for failed messages
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/27 — fix: cannot delete account
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/29 — fix: cannot add zero address adapter
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/31 — fix: check adapter address match to handle zero adapter id edge case
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/35 — fix: various small fixes for price deviation (same oracle) node
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/37 — fix: make rebalance up and rebalance down a permissioned operation
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/4 — fix: some oracle contracts used floating pragma
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/40 — fix: frontrun protection for the create account and create loan operations
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/43 — fix: delete collaterals and borrows mappings
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/45 — fix: check available liquidity when borrowing
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/48 — fix: handle zero deposits and zero borrows
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/5 — fix: NodeManager didn’t follow EIP-165
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/50 — fix: round in the protocol’s favour  when calculating the average stable rate
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/52 — fix: remove unused same oracle node
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/56 — fix: make retry and reverse message permissioned retry + can override the return message params
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/58 — fix: check the loan is over-collateralised in the switch borrow type operation
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/60 — fix: outdated deposit interest rate
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/62 — fix: hanlde PythNode exponent which is less than -18
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/64 — fix: don’t use cached chainlink node decimals
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/66 — fix: cannot mix borrows when liquidating
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/68 — fix: cannot rebalance up to a lower stable rate
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/70 — fix: reduce the loan type collateral used in by the liquidation fee
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/72 — fix: stable borrow balance increases
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/74 — fix: scale down the repay borrow amount by the liquidation bonus
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/75 — fix: check the available liquidity when withdrawing
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/76 — refactor: add extra checks to the math library
- [smart_contract] https://github.com/Folks-Finance/folks-finance-xchain-contracts/pull/9 — fix: incorrect implementation of Chainlink TWAP
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)

## Asset notes

__Asset Accuracy Assurance__

Bugs found on assets incorrectly listed in-scope will be considered valid and be rewarded.

__Primacy of Impact vs Primacy of Rules__

Folks Finance adheres to the Primacy of Impact for all Impacts stated within this page.

The primary objectives of a Mitigation Audit include verifying whether the fix fully resolves the reported vulnerability by addressing its root cause. Additionally, SRs must ensure that the fix covers all potential attack vectors, preventing any partial fixes that leave other exploitation avenues open. Any vulnerabilities that are discovered in other sections of the code that were introduced by the mitigation of another bug i.e. fix introduces a new vulnerability in another part of the system, should be reported under that fix.

Bugs unrelated to any fixes found on any of these `contracts https://github.com/Folks-Finance/folks-finance-xchain-contracts/tree/1eb10075d5ce2208cdf6e4560c2968eafa414327/contracts` should be reported under the Primacy of Impact.


__Eligibility Criteria__

Security researchers who wish to participate must adhere to the rules of engagement set forth in this program and cannot be:
- On OFACs SDN list 
- Official contributor, both past or present
- Employees and/or individuals closely associated with the project 
- Security auditors that directly or indirectly participated in the audit review

__Responsible Publication__

Whitehats may publish their bug reports after they have been fixed & paid, or closed as invalid, with the following exceptions:
- Bug reports in mediation may not be published until mediation has concluded and the bug report is resolved.

Immunefi may publish bug reports submitted to this audit competition and a leaderboard of the participants and their earnings.

__Feasibility Limitations__

The project may be receiving reports that are valid (the bug and attack vector are real) and cite assets and impacts that are in scope, but there may be obstacles or barriers to executing the attack in the real world. In other words, there is a question about how feasible the attack really is. Conversely, there may also be mitigation measures that projects can take to prevent the impact of the bug, which are not feasible or would require unconventional action and hence, should not be used as reasons for downgrading a bug's severity.

Therefore, Immunefi has developed a set of [feasibility limitation standards](https://immunefisupport.zendesk.com/hc/en-us/articles/16913132495377-Feasibility-Limitation-Standards) which by default states what security researchers, as well as projects, can or cannot cite when reviewing a bug report.

__Immunefi Standard Badge__

By adhering to Immunefi’s best practice recommendations, Folks Finance has satisfied the requirements for the [Immunefi Standard Badge](https://immunefisupport.zendesk.com/hc/en-us/articles/15006865432209-The-Immunefi-Standard-Badge).

## Impacts in scope (13)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds of at least 24h
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

__Proof of Concept (PoC) Requirements__

A PoC, demonstrating the bug's impact, is required for this program and has to comply with the Immunefi PoC Guidelines and Rules.

__Whitehat Educational Resources & Technical Info__

1. Design Overview for Cross-chain Lending Protocol: [Link to Google Docs](https://docs.google.com/document/d/19HjdYSmSxoXf7b0RIjiv8cff7jwdGZ1lkFrjqRrogiE/edit?usp=sharing)

2. Operation lifecycle in cross-chain lending protocol: [Link to Google Docs](https://docs.google.com/document/d/1UEV2JHpW23ChARUp_AcHJjuuq6A9T-n85T3FDYQTuGM/edit?usp=sharing)

3. Formulae Used in Cross-chain Lending Protocol: [Link to Google Docs](https://docs.google.com/document/d/1UU-zhy-Ik6h-EhKS2TvcIsd0Q377H7HKF6MGP5WdwAk/edit?usp=sharing)

4. Testnet for Cross-chain Lending Protocol:
   [Link to Testnet](https://testnet.xapp.folks.finance/)

5. Smart Contract README for Cross-chain Lending Protocol:
   [Link to GitHub README](https://github.com/Folks-Finance/folks-finance-xchain-contracts/blob/main/README.md)

6. Docs for Existing Folks Finance Products:
   [Link to Folks Finance Docs](https://docs.folks.finance/)

7. Medium Articles:
   [Link to Medium Articles](https://folksfinance.medium.com/)

__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

This is a new cross chain lending protocol that follows a similar model to our existing Algorand lending protocol. The loans and economic structure are the same with the only difference being how liquidations work. All the cross chain infrastructure is new. 

The cross chain lending protocol also uses an oracle design from Synthetix which takes up less than 5% of the total codebase. The codebase language is fully Solidity. 


__Where do you suspect there may be bugs? Useful aspects of this question are:__

Which parts of the code are you most concerned about?
What attack vectors are you most concerned about?
Which part(s) of the system do you want whitehats to attempt to break the most?
Are there any assumed invariants that you want whitehats to attempt to break?

In general all parts of the code should be checked and attack vectors explored. We write here some areas to look at in particular but this is not to discount any other areas.

One area to explore is the communication between chains. Messages are relayed between the spoke chain and the hub chain via Chainlink CCIP and Wormhole Messaging. In addition, Circle CCTP is used for USDC transfers. It is important to verify that we are using these protocols as intended and have correctly reasoned about the lifecycle of a message. 

We have a contract named “HubAdapter” which mimics the behaviour of the Chainlink CCIP and Wormhole messaging, without actually relaying anything. Its purpose is to have a common interface for interacting with the protocol through the spoke contracts regardless of whether on the hub chain or not.

We also have a new process for liquidations which should be checked both economically and codewise. The oracle integration is also new and should be checked for resistance against tampering.

One invariant to ensure that there is sufficient funds such that if all borrowers repaid their loans, all depositors can withdraw their tokens. Not an invariant, but the average stable interest rate should be closely tracking the weighted average of all the stable borrows for a given pool.

__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported? Which are not?__

ERC20 and ERC777 are the only two supported. The modular design allows ERC1155 to be supported in the future too if needed.

__What emergency actions may you want to use as a reason to invalidate or downgrade an otherwise valid bug report?__

We have rate limiting which sets the maximum amount which can be withdrawn or deposited. If the limit is consumed through a denial of service attack, we have the ability to temporarily boost the capacity.

Other mitigating actions we can take involve removing/adding an adapter, lowering rate limits, lowering pool caps and deprecating a pool. If the bug report’s impact is small in the scope of the protocol as a whole, considering the possible mitigations, then that could be reason to invalidate or downgrade the severity.


__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

E.g An ‘Operator’ address with the ability to pause smart contracts who could use their privileged functions to exploit a bug and steal funds

All admin and role addresses, as well as 3rd party infrastructure the project relies on. 


__What external dependencies are there?__

- Chainlink Price Feeds
- Pyth Price Feeds
- Folks Finance Centralised Fallback Oracle
- Wormhole’s Messaging
- Chainlink’s CCIP
- Circle’s CCTP

__WWhat are some of the most significant changes to the protocol from the fixes made?__

Most of the fixes were errors in the logic that don’t change the protocol intention. These should be checked to ensure they correctly fix the underlying issue. 

Some more significant changes were:
- The retry and reverse message operations are permissioned so only the relevant user can call these. In addition, you can now override the return message parameters if need be.
- The account id and loan id are generated on-chain for front-running protection. 
- We no longer save the entire failed message but rather a hash of the failed message, significantly reducing gas consumption.
- In the account management, you can override an existing invite and no longer unregister all connected addresses.  



__Where might whitehats confuse out-of-scope code to be in-scope?__

The external services such as the WormholeRelayer, Chainlink CCIP RouterClient and external oracle services. 

Are there any unusual points about your protocol that may confuse whitehats?

We have our own standard of sending and receiving messages. Certain operations require finality as they involve a value transfer while the others can be immediately relayed. There is the “HubAdapter” too which is mentioned above.

We split tokens into two categories in our lending protocol. The first are tokens which are not bridged and remain on the spoke chain e.g. ETH, Link. The second are tokens which are bridged and reside on the hub chain e.g. USDC.

Our lending protocol also is different from others in that a user can have multiple loans, and that a loan can have multiple collaterals and borrows within it. We also define various loan types which have their own respective parameters. One of these is the “deposit” loan type which has borrow caps of zero for every token.


__What is the test suite setup information?__

If this is already provided in Github, then linking that resource is enough.

It will be in the GitHub report with the rest of the code. 

__Public Disclosure of Known Issues__

Bug reports covering previously-discovered bugs (listed below) are not eligible for a reward within this program. This includes known issues that the project is aware of but has consciously decided not to “fix”, necessary code changes, or any implemented operational mitigating procedures that can lessen potential risk. 

- Griefing through consuming external rate limits of tokens e.g. Circle CCTP rate limits for USDC
- Griefing through consuming internal rate limits where we have the ability to respond by temporarily boosting capacity
- Dust positions not being liquidated because of gas fees
- Manipulation of stable borrow rate to get cheaper borrow
- Liquidation leading to bad debt when we are prioritising the certainty of a lesser amount of bad debt against the risk of incurring a larger amount of bad debt
- LiquidationLogic::getMaxRepayBorrowValue can panic if privileged address sets certain parameters 

__Previous Audits__

- Folks Finance’s completed audit reports can be found at https://github.com/Folks-Finance/audits/blob/13f8d8307902e8ff7018fe9b6df0b5668c638863/OtterSec%20-%20Audit%20of%20XChain%20Lending%20-%20May%202024.pdf. Any unfixed vulnerabilities mentioned in these reports are not eligible for a reward.

- Folks Finance’s up to date codebase can be found at https://github.com/Folks-Finance/folks-finance-xchain-contracts. 

- Folks Finance’s link to full list of changes: https://github.com/Folks-Finance/folks-finance-xchain-contracts/pulls?q=is%3Apr+is%3Aclosed 

- Folks Finance’s link to full list of issues:
https://github.com/Folks-Finance/folks-finance-xchain-contracts/issues?q=is%3Aissue+is%3Aclosed

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the $25,000 USD Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the $25,000 USD Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the $25,000 USD Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the $25,000 USD Reward Pool, pocRequired=True

## Reward notes

The following reward terms are a summary, for the full details read our [Folks Finance Mitigation Audit Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/27853859981969-Mitigation-Audit-Folks-Finance-Reward-Terms)

The purpose of a Mitigation Audit is for whitehats to assess whether the set of fixes from the original [Folks Finance Audit Competition](https://immunefi.com/audit-competition/folksfinance-boost/information/#top) both fully resolve the reported vulnerabilities and do not introduce new ones. Hunting on a Mitigation Audit involves understanding the root cause of the issues and verifying that the patches or mitigations directly address the causes.

This is crucial to ensure that the vulnerabilities are fully fixed and do not leave other avenues open for exploitation.

The rewards pool is partly distributed with the following formula, and partly at Immunefi’s discretion. The main purpose of a Mitigation Audit is to reward vulnerabilities, exploiting the fixes of the original Audit Competition. 

The portion of the reward pool is to reward high-quality whitehat contributions, such as valuable but technically invalid bug reports which are called Insights. More information about Insight reports can be found in this Help Center article.

The reward pool size for Mitigation Audit | Folks Finance is $25,000 USD. If no bugs or only Insights are found, the reward pool will be - 10% of the largest reward pool ($2,500 USD). 

For this Audit, duplicates are valid for a reward.

## Out of scope (program-specific)

(none)

## Out of scope and rules

Only the following impacts are accepted within this bug bounty program. All other impacts are not considered as in-scope, even if they affect something in the assets in scope table.

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
