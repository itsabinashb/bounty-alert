# SushiSwap

- Page: https://immunefi.com/bug-bounty/sushiswap/scope/
- Max bounty: $200,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - low, smart_contract - medium, smart_contract - high, smart_contract - critical
- End date: (none)

## Assets in scope (3)

- [smart_contract] https://docs.sushi.com/contracts/clamm#deployments — clAMM (SuhiSwap V3)
- [smart_contract] https://docs.sushi.com/contracts/cpamm#deployments — cpAMM (SuhiSwap V2)
- [smart_contract] https://docs.sushi.com/contracts/red-snwapper#deployments — Red Snwapper

## Asset notes

__Submission Requirements__

In order to be considered for a reward, all bug reports must contain the following:
  - Description of suspected vulnerability
  - POC demonstrating the vulnerability for reproduction, can be a high-level POC
  - Steps to reproduce the issue
  - Your name and/or colleagues if you wish to be later recognized
  - (Optional) A patch and/or suggestions to resolve the vulnerability

__Ethical Behavior Requirements__

Responsible disclosure is predicated on ethical behavior. These guidelines outline best practices for the community as whole, whether you are reporting, or the recipient of a report. By stating that you adhere to this policy, you’re claiming to handle vulnerability information ethically, and abide by the following:

  - Do not attempt to leverage a vulnerability, or information of its existence as part of a financial trading strategy or otherwise for financial gain.
  - Do not attempt to compromise systems upon which development of a product relies; including but not limited to compromising development systems, accounts, domains, email, etc..
  - Do not attempt to sell vulnerability information or exploits.
  - Do not ask for any form of compensation from an affected party. You may compensate a disclosing party if you would like to after all known vulnerability details have been disclosed.
  - Do not disclose a bug or vulnerability on mailing lists, public boards, forums, social media or any other channel prior to Responsibly Disclosing to the organizations you have a published relationship with
  - Do not attempt any illegal acts, including phishing, physical attacks, DDoS, or any attempt to gain access without authorization.

__3rd Party Affected Projects__

In the case where we become aware of security issues affecting other projects that have never affected SushiSwap, our intention is to inform those projects of security issues on a best effort basis.

In the case where we fix a security issue in SushiSwap that also affects the following neighboring projects, our intention is to engage in responsible disclosures with them as described in the adopted standard, subject to the deviations described in the deviations section below.

__Deviations from the Standard__

In the case of a counterfeiting or fund-stealing bug affecting SushiSwap, however, we might decide not to include those details with our reports to partners ahead of coordinated release, as long as we are sure that they are not vulnerable.

__Notes on Expected Behaviors__

  - Any reports that involve tokens outside of ERC20s will not be considered in scope. (i.e. ERC777 tokens)

## Impacts in scope (11)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed inflation
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed inflation
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

When submitting a bug report, please select the severity level you feel best corresponds to the severity classification system.

## Rewards

- [smart_contract] Critical: maxReward=$200,000, minReward=$20,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: maxReward=$5,000, minReward=$1,000, rewardModel=range
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on
the [Immunefi Vulnerability Severity Classification System](/severity-system/). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

Reports involving **RedSwanpper** about executing any arbitrary executions would be considered **out of scope** as this is working as per design.

Theft of Yield vulnerability reports are temporarily not in scope for this bug bounty program, though this attack may be in the future.

All bug reports must come with a PoC. All bug reports without a PoC will not be accepted under this bug bounty program.

All critical payments for smart contracts are capped at 10% of economic damage. 

Sushiswap is open to rewarding bounties beyond the critical cap for
vulnerabilities with extreme impact.

Payouts are handled by the **SushiSwap** team directly and are denominated in **USD**. Payouts worth USD $100,000 and below are done in **USDC**. Payouts beyond USD $100,000 up to USD 200,000 are made in **SUSHI**, though the first $100,000 can be made in **USDC** if requested.

## Out of scope (program-specific)

- Loss of positive slippage through Sandwich Attacks  
  - Best practice critiques
  - Attacks that rely on social engineering

__Bug Bounty FAQ__

__Q:__ Is there a time limit for the Bug Bounty program? 
__A:__ No, the Bug Bounty program currently has no end date, but this can be changed at any time at the discretion of SushiSwap.

__Q:__ Can I submit bugs anonymously and still receive payment? 
__A:__ Yes, if you wish to remain anonymous you can do so and still be eligible for rewards as long as they are for valid bugs. Rewards will be sent to the valid Ethereum address that you provide.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

- Bug has not been publicly disclosed.
- Vulnerabilities that have been previously submitted by another contributor or already known by the SushiSwap development team are not eligible for rewards.
- Bugs must be reproducible in order for us to verify the vulnerability.
- Rewards and the validity of bugs are determined by the SushiSwap development team and any payouts are made at their sole discretion.
- Terms and conditions of the Bug Bounty program can be changed at any time at the discretion of SushiSwap.

## Known issues (0)

(none)
