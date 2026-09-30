# Gamma

- Page: https://immunefi.com/bug-bounty/gamma/scope/
- Max bounty: $50,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical
- End date: (none)

## Assets in scope (3)

- [smart_contract] https://etherscan.io/address/0x26805021988F1a45dC708B5FB75Fc75F21747D8c — xGamma
- [smart_contract] https://etherscan.io/address/0x83de646a7125ac04950fea7e322481d4be66c71d — UniProxy
- [smart_contract] https://etherscan.io/address/0xa8076ae31e4b6c64d07b1ed27889924a962a70d3 — Hypervisor

## Asset notes

However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

## Impacts in scope (6)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Medium: Permanent freezing of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds
- [smart_contract] Medium: Theft of unclaimed yield

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$50,000, rewardCalculationPercentage=0, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the Immunefi Vulnerability Severity Classification System. This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit. 

All bug reports must come with a PoC in order to be considered for a reward. 

The following known issues would be considered as out-of-scope of this bounty program: 
  - For the UniProxy contract, its deposit configuration is its operational context. Attacks which depend on different configuration than provided for their example hypervisor contract are not to be considered
  - For the xGamma contract, an attack is possible wherein the attacker deposits just before and withdraws just after rebase. In our operational context, they do not send funds (rebase) to the xGamma contract outside of private rpc.

Payouts are handled by the __Gamma__ team directly and are denominated in USD. However, payouts are done in either __GAMMA__, __ETH__ or __USDC__, up to the discretion of the team.

## Out of scope (program-specific)

- Attacks which require differing operational configuration than targets supplied
  - Best practice critiques

## Out of scope and rules

The following vulnerabilities are excluded from the rewards for this bug bounty program:

  - Attacks that the reporter has already exploited themselves, leading to damage
  - Attacks requiring access to leaked keys/credentials
  - Attacks requiring access to privileged addresses (governance, strategist)
  - Attacks which require differing operational configuration than targets supplied

__Smart Contracts and Blockchain__

  - Incorrect data supplied by third party oracles
    - Not to exclude oracle manipulation/flash loan attacks
  - Basic economic governance attacks (e.g. 51% attack)
  - Lack of liquidity
  - Best practice critiques
  - Sybil attacks

The following activities are prohibited by this bug bounty program:

  - Any testing with mainnet or public testnet contracts; all testing should be done on private testnets
  - Any testing with pricing oracles or third party smart contracts
  - Attempting phishing or other social engineering attacks against our employees and/or customers
  - Any testing with third party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
  - Any denial of service attacks
  - Automated testing of services that generates significant amounts of traffic
  - Public disclosure of an unpatched vulnerability in an embargoed bounty

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
