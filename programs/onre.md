# OnRe

- Page: https://immunefi.com/bug-bounty/onre/scope/
- Max bounty: $100,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (1)

- [smart_contract] https://solscan.io/account/onreuGhHHgVzMWSkj2oQDLDtvvGvoepBPkqyaubFcwe — OnRe Program

## Asset notes

Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in-use in production

## Impacts in scope (17)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield from an unvetted address
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Manipulation of user roles inside the system via unvetted wallet or smart contract that may result in any critical severity issue
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Permanent freezing of funds from an unvetted address
- [smart_contract] Critical: Protocol insolvency from an unvetted address
- [smart_contract] High: Manipulation of user roles inside the system via unvetted wallet or smart contract that may result in any high severity issue
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$10,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$2,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below.
                                                                                                                
**Reward Calculation for Critical Level Reports**

For critical Smart Contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted, and is bounded by on-chain assets exposed by the vulnerability, including but not limited to the offer and redemption vault balances and the value of any ONyc that could be minted without corresponding deposit. Capital held off-chain by On Re SAC Ltd in the regulated Bermuda SAC is not reachable from the Solana program and is therefore excluded from the funds-at-risk calculation. A minimum reward of USD 10,000 applies in order to incentivize security researchers against withholding a bug report.

**Deployed Contract Requirement**

To be eligible for a reward, the reported vulnerability must be present in the most recently deployed smart contract and must produce an eligible impact against an asset in scope.

Vulnerabilities that exist only in the GitHub source code, but not in the deployed contract, are not eligible for a reward. This may happen where a vulnerability has already been fixed in the deployed artifact or on-chain program before the public source code or related communication has been updated.

For the purpose of reward eligibility, the deployed contract takes precedence over the GitHub source code.

**Repeatable Attack Limitations**

In cases of repeatable attacks for smart contract bugs, only the first attack will be counted, regardless of whether the smart contract is upgradable, pausable, or killable.
                                                                                                                
**Previous Audits**

OnRe has provided these completed audit reports for reference. Any unfixed vulnerability mentioned in these     
reports is not eligible for a reward.                                  
                                                                                                                
**Proof of Concept (PoC) Requirements**                                                                           
                                                                                                                
A PoC is required for the following severity levels:
- Smart Contract, Critical Severity Level
- Smart Contract, High Severity Level
- Smart Contract, Medium Severity Level                                                                         
- Smart Contract, Low Severity Level
                                                                                                                
All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules.](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules)
PoCs for the OnRe Solana program should be runnable in a deterministic local environment such as `solana-program-test`, `anchor-bankrun`, or LiteSVM, against the source at the commit specified in Assets in Scope. 
Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

**Reward Payment Terms**

Payouts are handled by the OnRe team directly and are denominated in USD. However, payments are done in USDC.

## Out of scope (program-specific)

(none)

## Out of scope and rules

.

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- The update_offer_fee instruction validated the new fee against `MAX_BASIS_POINTS` (10000 bps, 100%) instead of `MAX_ALLOWED_FEE_BPS` (1000 bps, 10%), the constant `make_offer` uses. This let an existing offer be updated to a fee above the protocol's 10% ceiling.

The instruction is gated to the protocol boss, which on mainnet is the Squads V4 multisig at `45YnzauhsBM8CpUz96Djf8UG5vqq2Dua62wuW9H3jaJ5`. No unprivileged path reaches this code. Fee mutability and timing are also covered by acknowledged finding W8 in the public Ackee Blockchain Security audit, and by the documented trust model (Report Revision 1.0, page 19).

The constant has been corrected and the cap now matches `make_offer`. Any submission describing the same constant mismatch or the resulting "fee escalates above 10% via `update_offer_fee`" behavior is a duplicate of this known issue. (https://github.com/onre-finance/onre-sol/commit/b1d24ca734b64d60ac72b06f2b69bd10f8aa4d9f)
