# Beanstalk

- Page: https://immunefi.com/bug-bounty/beanstalk/scope/
- Max bounty: $1,100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - medium, smart_contract - high, websites_and_applications - critical
- End date: (none)

## Assets in scope (22)

- [smart_contract] https://arbiscan.io/address/0x1BEA054dddBca12889e07B3E076f511Bf1d27543 — Unripe Bean ERC-20 token
- [smart_contract] https://arbiscan.io/address/0x1BEA059c3Ea15F6C10be1c53d70C75fD1266D788 — Unripe LP ERC-20 token
- [smart_contract] https://arbiscan.io/address/0x555555987d98079b9f43CDcDBD52DbB24FfEEef5 — Shipment Planner
- [smart_contract] https://arbiscan.io/address/0x5A5A5ADe4C9713172a5228703213d4D39608E2cD — Junctions
- [smart_contract] https://arbiscan.io/address/0xBA150002660BbCA20675D1C1535Cd76C98A95b13 — Multi Flow Pump
- [smart_contract] https://arbiscan.io/address/0xBA15000450Bf6d48ec50BD6327A9403E401b72b4 — Constant Product 2 Well Function
- [smart_contract] https://arbiscan.io/address/0xBA51055dAD14d3920e1798D2e8A152d91CaDb461 — Stable 2 Well Function, Lookup Table with A = 1
- [smart_contract] https://arbiscan.io/address/0xBA5106bd62b342afAcB93f1078fe60177A62d1a9 — Well Implementation
- [smart_contract] https://arbiscan.io/address/0xBA510995783111be5301d93CCfD5dE4e3B28e50B — Upgradable Well Implementation
- [smart_contract] https://arbiscan.io/address/0xBA51AAAa8C2f911AE672e783707Ceb2dA6E97521 — Aquifer
- [smart_contract] https://arbiscan.io/address/0xBEA0005B8599265D41256905A9B3073D397812E4 — Bean ERC-20 token
- [smart_contract] https://arbiscan.io/address/0xCCCCCC35b53c8a16404Ae414AFa31F30A5B35626 — LSD Chainlink Oracle
- [smart_contract] https://arbiscan.io/address/0xD1A0060ba708BC4BCD3DA6C37EFa8deDF015FB70 — L2 Beanstalk
- [smart_contract] https://arbiscan.io/address/0xD6Fc4a63d7E93267c3007eA176081052369A4749 — Unwrap and Send ETH
- [smart_contract] https://arbiscan.io/address/0xFEFEFE2cfb089aEF0b0578573eF3CFAbC15f1490 — Fertilizer Implementation
- [smart_contract] https://arbiscan.io/address/0xFEFEFECA5375630d6950F40e564A27f6074845B5 — Fertilizer ERC-1155 token
- [smart_contract] https://arbiscan.io/address/0xb1bE000644bD25996b0d9C2F7a6D6BA3954c91B0 — Pipeline
- [smart_contract] https://arbiscan.io/address/0xba150052e11591D0648b17A0E608511874921CBC — Stable 2 Well Function
- [smart_contract] https://arbiscan.io/address/0xdeb0f082ed3b0efe9257aea9f2e6e974aa4120c3 — Depot
- [smart_contract] https://etherscan.io/address/0xC1E088fC1323b20BCBee9bd1B9fC9546db5624C5 — L1 Beanstalk
- [websites_and_applications] https://app.bean.money — Beanstalk UI
- [websites_and_applications] https://basin.exchange — Basin UI

## Asset notes

__Additional Resources__

All Beanstalk smart contracts and the Beanstalk UI can be found at [https://github.com/BeanstalkFarms/Beanstalk](https://github.com/BeanstalkFarms/Beanstalk). However, only those in the Assets in Scope section are considered as in-scope of the bug bounty program. The following links may also be helpful:

Beanstalk
  - [Beanstalk Whitepaper](https://bean.money/beanstalk.pdf)
  - [Beanstalk Docs](https://docs.bean.money/almanac/)
  - [Beanstalk Technical Docs](https://docs.bean.money/developers)
  - [Beanstalk GitHub](https://github.com/BeanstalkFarms/Beanstalk)
  - [Beanstalk Discord](https://discord.gg/beanstalk)
  - [Beanstalk on Louper](https://louper.dev/diamond/0xc1e088fc1323b20bcbee9bd1b9fc9546db5624c5) 

Basin
  - [Basin Whitepaper](https://basin.exchange/basin.pdf)
  - [Multi Flow Pump Whitepaper](https://basin.exchange/multi-flow-pump.pdf)
  - [Basin Docs](https://docs.basin.exchange/)
  - [Basin GitHub](https://github.com/BeanstalkFarms/Basin)
  - [Basin Discord](https://basin.exchange/discord)

Pipeline
  - [Pipeline Whitepaper](https://evmpipeline.org/pipeline.pdf)
  - [Pipeline GitHub](https://github.com/BeanstalkFarms/Pipeline)

## Impacts in scope (18)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] High: Illegitimate minting of protocol native assets
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 1 hour
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Contract fails to deliver promised returns, but doesn't lose value
- [smart_contract] Medium: Exploit is possible but is exclusively prevented by an invariant
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Invariant is missing on a function where it should be implemented
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [websites_and_applications] Critical: Ability to execute arbitrary system commands
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Injecting code that results in malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as voting in governance

## Impact notes

If an impact can be caused to any other asset related to Beanstalk that isn’t on this section but for which the impact is in the Impacts in Scope section below, bug bounty hunters are encouraged to submit it for consideration by the BIC. 

Note that unexpected outcomes (like loss of funds) due to misuse of Pipeline and/or Depot do not qualify as valid bug reports. Read more [here](https://evmpipeline.org/pipeline.pdf?utm_source=immunefi#section.6).

Also note that the various ecosystem subgraphs ([Beanstalk](https://graph.node.bean.money/subgraphs/name/beanstalk/graphql), [Bean](https://graph.node.bean.money/subgraphs/name/beanstalk/bean), [Basin](https://graph.node.bean.money/subgraphs/name/beanstalk/basin), etc.) are not included as Assets in Scope. 

__Undeployed Code in Scope__

The BIC also maintains a list of pull requests/repositories whose code is considered in-scope but has not yet been deployed on-chain. This code has been audited. The following code is in-scope of the bug bounty program:
  - None at this time

## Rewards

- [smart_contract] Critical: maxReward=$1,100,000, minReward=$100,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$100,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Critical: maxReward=$50,000, minReward=$1,000, otherImpactMaxReward=$0, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). The following is a simplified 3-level scale, focusing on the impact of the vulnerability reported. The complete scope can be found below.

In order to be considered for the maximum potential reward, bug reports must come with a Proof of Concept (PoC). Explanations and statements are not accepted in lieu of a PoC. Bug reports that do not come with a PoC may qualify for a maximum of up to 30% of the potential reward outlined below, as determined by the Beanstalk Immunefi Committee. 

Funds at Risk for a given bug report are defined as follows:

  - Funds at Risk are determined based on the token amounts and USD values at time of the bug report submission;
  - For Beans, Funds at Risk are determined based on the liquidatable USD value of the Beans at risk;
  - For non-Beans (ETH, WETH, 3CRV, USDC, DAI, USDT, etc.) in any in-scope assets, the Funds at Risk are determined based on their respective USD values;
  - For Circulating non-Beans (i.e., outside of any in-scope assets), the Funds at Risk are determined to be 50% of their respective USD values; and
  - If the smart contract where the vulnerability exists can be upgraded or paused, only the Funds at Risk in initial attacks that can be executed within the first hour will be considered for a reward.

__Reward Calculation for Critical Smart Contract Reports__

Rewards for Critical smart contract vulnerabilities are capped at the lower of (a) 10% of practicable economic damage, or (b) __USD 1 100 000__, primarily taking into consideration the Funds at Risk. However, there is a minimum reward of __USD 100 000__ for Critical severity smart contract bug reports.

__Reward Calculation for High Smart Contract Reports__

Rewards for High smart contract vulnerabilities are capped at the lower of (a) 10% of practicable economic damage, or (b) __USD 100 000__, primarily taking into consideration the Funds at Risk. However, there is a minimum reward of __USD 10 000__ for High severity smart contract bug reports.

__Reward Calculation for Medium Smart Contract and All Website and Applications Reports__

Rewards for Medium severity smart contract vulnerabilities and all website and applications vulnerabilities are scaled based on a set of internal criteria established by the BIC. However, there is a minimum reward of USD 1 000 for Medium smart contract bug reports and Critical website and applications bug reports. The BIC will primarily take into account:

  - The exploitability of the bug;
  - The impact it causes; and
  - The likelihood of the vulnerability presenting itself.

__Reward Payment Terms__

Payouts are handled by the [Beanstalk Immunefi Committee Multisig (BICM)](https://docs.bean.money/almanac/governance/beanstalk/bicm-dashboard) directly and are done in BEAN. Note that due to the decentralized governance process for rewarding bug bounties, rewards can take several days to be paid out after a report is confirmed to be valid.

__BIC Determination__

The BIC shall determine whether a submitting party is entitled to a bug bounty/reward, and if so, the amount of such bounty/reward (and specifically, whether such submission qualifies for a Critical, High or Medium Impact bounty/reward, what is the potential practicable economic damage of such bug based on the Funds at Risk, and what the appropriate bounty/reward should be within each Impact range). The BIC’s determination of (i) whether such submission qualifies for a Critical, High or Medium Impact bounty/reward, (ii) what is the potential practicable economic damage of such bug based on the Funds at Risk, and (iii) whether such submission came with a PoC, thereby enabling it to be considered for the maximum potential applicable reward (vs. a submission that did not come with a PoC, thereby limiting such submission to a maximum of up to 30% of the applicable reward), shall be made in the BIC’s sole and absolute discretion absolute and shall be final, and not be subject to any appeal or challenge.

A submitting party may only dispute the BIC’s determination (a) that a submitting party is not entitled to any bug bounty/reward, or (b) what the appropriate bounty/reward should be within each Impact range. In such disputes, Immunefi will conduct a binding mediation. If the submitting party disputes the BIC’s decision that a submitting party is not entitled to any bug bounty/reward, Immunefi will mediate, and shall determine, in its sole and absolute discretion, which is non-appealable, whether the submitting party is entitled to any bug bounty/reward, and if so, the amount of such bug bounty/reward, up to __USD 10 000__ in the case of a smart contract bug reports (i.e., as if it were a Medium Impact fix), and up to __USD 1 000__ in the case of a website and applications bug report (i.e, as if it were a Critical Impact fix). If the submitting party disputes the BIC’s determination what the appropriate bounty/reward should be within a specific Impact range, Immunefi will mediate, and shall determine, in its sole and absolute discretion, which is non-appealable, the amount of such bug bounty/reward in the relevant Impact category; however, Immunefi may not modify or change (i) the practicable economic damage determination made by the BIC, or (b) the BIC’s determination whether such submission came with a PoC, thereby enabling it to be considered it for the maximum potential applicable reward (vs. a submission that did not come with a PoC, thereby limiting such submission to a maximum of up to 30% of the applicable reward).

## Out of scope (program-specific)

- Impacts related to attacks that the reporter has already exploited themselves, leading to damage;
- Impacts caused by attacks requiring access to leaked keys/credentials;
- Impacts caused by attacks requiring access to privileged addresses (owner address);
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in the code;
- Impacts that involve frontrunning transactions, i.e., impacts that require users to send transactions through the public mempool;
- Mentions of secrets, access tokens, API keys, private keys, etc. in GitHub will be considered out of scope;
- Best practice recommendations;
- Feature requests; and
- Impacts on test and configuration files unless stated otherwise in the bug bounty program.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
