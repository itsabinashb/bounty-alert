# Aster

- Page: https://immunefi.com/bug-bounty/aster/scope/
- Max bounty: $200,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, websites_and_applications - critical, websites_and_applications - high
- End date: (none)

## Assets in scope (12)

- [smart_contract] https://bscscan.com/address/0x184b72289c0992BDf96751354680985a7C4825d6 — asBTC Token Contract
- [smart_contract] https://bscscan.com/address/0x56F966fD321128A2a4E107aF82282455e9025D02 — USDF Dispatcher Contract
- [smart_contract] https://bscscan.com/address/0x5A110fC00474038f6c02E89C707D638602EA44B5 — USDF Token Contract
- [smart_contract] https://bscscan.com/address/0x77734e70b6E88b4d82fE632a168EDf6e700912b6 — asBNB Token Contract
- [smart_contract] https://bscscan.com/address/0x8a3C77E6c6A488d26CD44F403b95e44675f46e6A — asBTC Minting Contract
- [smart_contract] https://bscscan.com/address/0x917AF46B3C3c6e1Bb7286B9F59637Fb7C65851Fb — asUSDF Token Contract
- [smart_contract] https://bscscan.com/address/0xAd4836bBf3671EBd4f2e1F49119c1184655E47CA — USDF withdraw Vault Contract
- [smart_contract] https://bscscan.com/address/0xC271fc70dD9E678ac1AB632f797894fe4BE2C345 — USDF Minting Contract
- [smart_contract] https://bscscan.com/address/0xCb378a8A4afA40BA8c7e80F1B7E993c3c1AD6EFB — asBTC withdraw Vault Contract
- [smart_contract] https://bscscan.com/address/0xdB57a53C428a9faFcbFefFB6dd80d0f427543695 — asUSDF Minting Contract
- [smart_contract] https://www.asterdex.com/en — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://www.asterdex.com/en — Frontend: Home page

## Asset notes

(none)

## Impacts in scope (16)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$200,000, minReward=$50,000, primacy=primacy_of_impact, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Critical: fixedReward=$7,500, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$4,000, rewardModel=fixed

## Reward notes

__Rewards by Threat Level__

Rewards are distributed according to the impact of the vulnerability based on the Immunefi Vulnerability Severity Classification System V2.3. 

__Reward Calculation for Critical Level Reports__

For critical smart contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD $200,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD $50,000 is to be rewarded in order to incentivize security researchers against withholding a critical bug report.

For critical web/apps bugs, reports will be rewarded with USD $7,500, only if the impact leads to:
- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds 

All other impacts that would be classified as Critical would be rewarded a flat amount of $4,000. The rest of the severity levels are paid out according to the Impact in Scope table.

__Repeatable Attack Limitations__

- If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 


- For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward.

__Reward Calculation for High Level Reports__

- High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of $5,000 to $20,000 depending on the funds at risk, capped at the maximum high reward.  

- In the event of temporary freezing, the reward doubles from the full frozen value for every additional 24h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
