# Ethena

- Page: https://immunefi.com/bug-bounty/ethena/scope/
- Max bounty: $3,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, websites_and_applications - critical, websites_and_applications - high
- End date: (none)

## Assets in scope (28)

- [smart_contract] https://etherscan.io/address/0x211cc4dd073734da055fbf44a2b4667d5e5fe5d2 — StakedUSDeOFTAdapter.sol
- [smart_contract] https://etherscan.io/address/0x2cc440b721d2cafd6d64908d6d8c4acc57f8afc3 — SingleAdminAccessControl.sol
- [smart_contract] https://etherscan.io/address/0x4c9edd5852cd905f086c759e8383e09bff1e68b3 — USDe.sol
- [smart_contract] https://etherscan.io/address/0x57e114B691Db790C35207b2e685D4A43181e6061 — ENA.sol
- [smart_contract] https://etherscan.io/address/0x58538e6a46e07434d7e7375bc268d3cb839c0133 — ENAOFTAdapter.sol
- [smart_contract] https://etherscan.io/address/0x5d3a1ff2b6bab83b63cd9ad0787074081a52ef34 — USDeOFTAdapter.sol
- [smart_contract] https://etherscan.io/address/0x73E35C5c35A274E34AdE6EB13cC7f62aEE323728 — USDtb PSM Contract
- [smart_contract] https://etherscan.io/address/0x7FC7c91D556B400AFa565013E3F32055a0713425 — USDeSilo.sol
- [smart_contract] https://etherscan.io/address/0x8707f238936c12c309bfc2B9959C35828AcFc512 — EthenaLPStaking.sol. Present on both Ethereum and Mantle: https://explorer.mantle.xyz/address/0xf2fa332bD83149c66b09B45670bCe64746C6b439?tab=contract
- [smart_contract] https://etherscan.io/address/0x8bE3460A480c80728a8C4D7a5D5303c85ba7B3b9#code — StakedENA.sol
- [smart_contract] https://etherscan.io/address/0x9d39a5de30e57443bff2a8307a4256c8797a3497 — StakedUSDe.sol
- [smart_contract] https://etherscan.io/address/0x9d39a5de30e57443bff2a8307a4256c8797a3497 — StakedUSDeV2.sol
- [smart_contract] https://etherscan.io/address/0xa3DDBf92077b850E29C4805Df0a2459Ae048416a — USDtbMinting.sol
- [smart_contract] https://etherscan.io/address/0xc139190f447e929f090edeb554d95abb8b18ac1c#code — USDtb.sol
- [smart_contract] https://etherscan.io/address/0xe3490297a08d6fC8Da46Edb7B6142E4F461b62D3#code — EthenaMinting.sol V2
- [smart_contract] https://etherscan.io/address/0xf2fa332bd83149c66b09b45670bce64746c6b439#tokentxns — StakingRewardsDistributor.sol
- [smart_contract] https://explorer.mantle.xyz/address/0x211Cc4DD073734dA055fbF44a2b4667d5E5fE5d2 — StakedUSDeOFT.sol - Present on the following chains: Mantle, Arbitrum One, Manta Pacific, Optimism, BNB, Kava, Scroll, Mode, Metis, Fraxtal, Linea, and some others updated here: https://docs.ethena.fi/solution-design/key-a
- [smart_contract] https://explorer.mantle.xyz/address/0x58538e6A46E07434d7E7375Bc268D3cb839C0133 — ENAOFT.sol - Present on the following chains: Mantle, Arbitrum One, Manta Pacific, Optimism, BNB, Kava, Scroll, Mode, Metis, Fraxtal, Linea, and some others updated here: https://docs.ethena.fi/solution-design/key-addresses
- [smart_contract] https://explorer.mantle.xyz/address/0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34 — USDeOFT.sol - Present on the following chains: Mantle, Arbitrum One, Manta Pacific, Optimism, BNB, Kava, Scroll, Mode, Metis, Fraxtal, Linea, and some others updated here: https://docs.ethena.fi/solution-design/key-addresses
- [smart_contract] https://immunefi.com/ — Primacy of Impact (primacy of impact)
- [smart_contract] https://tonviewer.com/EQAIb6KmdfdDR7CN1GBqVJuP25iCnLKCvBlJ07Evuu2dzP5f — USDe minter contract on TON
- [smart_contract] https://tonviewer.com/EQAjpnYUX43uNjL3IqrFA5LyLPC0vo9iTgOCeab1AF-2aYcq — USDe OFT contract on TON
- [smart_contract] https://tonviewer.com/EQChGuD1u0e7KUWHH5FaYh_ygcLXhsdG2nSHPXHW8qqnpZXW — tsUSDe vault on TON
- [smart_contract] https://tonviewer.com/EQDQ5UUyPHrLcQJlPAczd_fjxn8SLrlNQwolBznxCdSlfQwr — tsUSDe minter contract on TON
- [websites_and_applications] https://app.ethena.fi — Subdomain
- [websites_and_applications] https://claim.ethena.fi — Subdomain
- [websites_and_applications] https://immunefi.com — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://www.ethena.fi — Project Link

## Asset notes

(none)

## Impacts in scope (27)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:  Modifying transaction arguments or parameters, Substituting contract addresses, Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:   /etc/shadow, database passwords, blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:   Changing registration information, Commenting, Voting, Making trades, Withdrawals, etc.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:  Email, Password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:  Email address, Phone number, Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:  HTML injection without JavaScript, Replacing existing text with arbitrary text, Arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$3,000,000, minReward=$100,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$75,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$10,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$2,500, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$50,000, minReward=$20,000, otherImpactMaxReward=$0, primacy=primacy_of_impact, rewardModel=range
- [websites_and_applications] High: fixedReward=$15,000, primacy=primacy_of_rules, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the[ Immunefi Vulnerability Severity Classification System V2.3. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/)

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD $3 Million. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD $100,000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk.

For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of $10k to $75K depending on the funds at risk, capped at the maximum high reward.  


In the event of temporary freezing, the reward doubles from the full frozen value for every additional [1h] that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

For critical web/apps bug reports will be rewarded with $50,000, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of $20,000. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Reward Payment Terms__

Payouts are handled by the Ethena team directly and are denominated in USD. However, payments are done in USDC on Mainnet.

The calculation of the net amount rewarded is based on the average price between CoinMarketCap.com and CoinGecko.com at the time the bug report was submitted. No adjustments are made based on liquidity availability.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
