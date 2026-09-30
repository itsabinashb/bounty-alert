# IPOR

- Page: https://immunefi.com/bug-bounty/ipor/scope/
- Max bounty: $1,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical
- End date: (none)

## Assets in scope (13)

- [smart_contract] https://etherscan.io/address/0x137000352B4ed784e8fa8815d225c713AB2e7Dc9 — AmmTreasuryUsdcProxy
- [smart_contract] https://etherscan.io/address/0x16d104009964e694761C0bf09d7Be49B7E3C26fd — IporProtocolRouterProxy
- [smart_contract] https://etherscan.io/address/0x28BC58e600eF718B9E97d294098abecb8c96b687 — AmmTreasuryUsdtProxy
- [smart_contract] https://etherscan.io/address/0x364f116352EB95033D73822bA81257B8c1f5B1CE — AmmStorageUsdtProx
- [smart_contract] https://etherscan.io/address/0x63395EDAF74a80aa1155dB7Cd9BBA976a88DeE4E — AmmTreasuryEthProxy
- [smart_contract] https://etherscan.io/address/0x77Fe3a8E8d1d73Df54Ca07674Bf1bD6C5841e3b5 — Ethereum - AmmStorageWeEthProxy
- [smart_contract] https://etherscan.io/address/0x7c0e72f431FD69560D951e4C04A4de3657621a88 — ipUSDC
- [smart_contract] https://etherscan.io/address/0x9Bd2177027edEE300DC9F1fb88F24DB6e5e1edC6 — ipUSDT
- [smart_contract] https://etherscan.io/address/0xB3d1c1aB4D30800162da40eb18B3024154924ba5 — AmmStorageUsdcProx
- [smart_contract] https://etherscan.io/address/0xaC5B04988BC71bEE96f8D93040777Db3ef166125 — Ethereum - ipweETH
- [smart_contract] https://etherscan.io/address/0xc40431b6C510AeB45Fbb5e21E40D49F12b0c1F0c — ipstETH
- [smart_contract] https://etherscan.io/address/0xcC2fF2D38666723ea56c122097F6215B90d74196 — Ethereum - AmmTreasuryWeEthProxy
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

Impacts only apply to assets in active use by the project like contracts on mainnet or web/app assets used in production. Any impact that applies to assets not in active use, like test or mock files, are out-of-scope of the bug bounty program unless explicitly mentioned as in-scope. 

__Smart Contracts__ 

- __Smart Contracts - PoC__, Smart Contract bug reports are to include a runnable Proof of Concept (PoC) in order to prove impact.  
- For more information on PoCs please visit: [Proof of Concept (PoC) Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)


Whitehats are highly encouraged to review any potential subdomains and what specific port(s) are in scope. Even though the domain may be the same, different ports may point to different assets.  

__Dev Environment and Documentation:__

IPOR has included dev documentation and/or instructions to help in reviewing code and exploring for bugs:
- [https://docs.ipor.io/](https://docs.ipor.io/)
- [https://github.com/IPOR-Labs/ipor-protocol/blob/main/README.md](https://github.com/IPOR-Labs/ipor-protocol/blob/main/README.md)
- [https://github.com/IPOR-Labs/ipor-power-tokens/blob/main/README.md](https://github.com/IPOR-Labs/ipor-power-tokens/blob/main/README.md)

__Impacts to other assets:__

Hackers are encouraged to submit issues outside of the outlined Impacts and Assets in Scope. 

If whitehats can demonstrate a critical impact on code in production for an asset not in scope, IPOR encourages you to submit your bug report using the “primacy of impact exception” asset. 

__Impacts in Scope:__

(For Blockchain/DLTR and Smart Contracts Only) This program is considered to be governed by Primacy of Impact. For more information on what this means visit: [Best Practice - Primacy of Impact vs Primacy of Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/12340245635089-Best-Practices-Primacy-of-Impact) 

Impacts are based on the [Immunefi Vulnerability Severity Classification System V2.2.](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2/)

At Immunefi, we classify bugs on a simplified 5-level scale:
- Critical
- High
- Medium
- Low
- None

## Impacts in scope (2)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: fixedReward=$1,000, rewardCalculationPercentage=0, rewardModel=fixed

## Reward notes

Please review how rewards are distributed based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale system with separate scales for Smart Contracts and Websites/Apps.

__Payouts and Payout Requirements:__

Payouts are handled by the IPOR team directly and are denominated in USD. However, payouts are done in USDC and IPOR. For critical vulnerability, IPOR DAO will pay 50% in USDC and 50% in IPOR tokens.  IPOR commits to honoring payouts according to the terms set out in this program at the time of report submission, and to treat this program as the agreement and source of truth concerning bug reports and responsible disclosures. 

| Impact     | Criteria for assessing economic damage     |
| ---------- | ---------- |
| Critical       | Risk Ratio = Funds at Risk / ( IPOR TVL). If the risk ratio is at or below 0.5, the payout is calculated linearly between 0$ and 25K. If the risk ratio is above 0.5, the payout is calculated linearly between USD $25K and USD $100K; with a maximum cap of $100K. In the event that the funds at risk is greater than the IPOR TVL, the maximum reward will not exceed USD $100K.

For the purposes of determining report validity, this is a Primacy of Impact program. 

Learn more about report validity best practices here: [Best Practice - Primacy of Impact vs Primacy of Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/12340245635089-Best-Practices-Primacy-of-Impact) 

__KYC Requirements:__

IPOR __does not__ have a Know Your Customer (KYC) requirement for bug bounty payouts. 

__Audit Discoveries and Known Issues:__

Bug reports covering previously-discovered bugs are not eligible for any reward through the bug bounty program. If a bug report covers a known issue, it may be rejected together with proof of the issue being known before escalation of the bug report via Immunefi. 

__Description of known issue:__
- IPOR index value manipulation through AAVE & Compound
- reports reported via github [https://github.com/IPOR-Labs/ipor-audit-reports](https://github.com/IPOR-Labs/ipor-audit-reports)
- The issue with liquidity pools amount equals zero
- asset management relies on the published token exchange rate (gas optimization)
- when opening swaps the asset management holdings are calculated without the interest (gas optimisation)

## Out of scope (program-specific)

- Broken link hijacking is out of scope
- Best practice critiques
- IPOR index value manipulation through AAVE & Compound
- Issues when the liquidity of liquidity pools equals zero
- Interest Rate Swaps opening and closing

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

The following activities are prohibited by this bug bounty program. Violation of these rules can result in a temporary suspension or permanent ban from the Immunefi platform at the sole discretion of the Immunefi team, which may also result in: 1) the forfeiture and loss of access to all bug submissions, and 2) zero payout.
Please note that Immunefi has no tolerance for spam/low-quality/incomplete bug reports, “beg bounty” behavior, and misrepresentation of assets and severity. Immunefi exists to protect the global crypto community, not facilitate grift.

## Known issues (0)

(none)
