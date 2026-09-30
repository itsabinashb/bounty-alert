# IOP | Term Structure Institutional

- Page: https://immunefi.com/bug-bounty/iop-term-structure/scope/
- Max bounty: $6,000
- KYC required: yes
- Paused: no
- Invite only: yes
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-06-16T10:00:00.000Z

## Assets in scope (0)

(none)

## Asset notes

(none)

## Impacts in scope (16)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Temporary freezing of funds for at least 24 hour
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

__Build Commands, Test Commands, and How to Run Them__

```install denpendencies```
forge soldeer update

```build```
forge build

```test```
forge test –skip Fork

__Previous Audits__

- Term Structure Institutional’s has no audit report as of 28 May 2025.


__Where might Security Researchers confuse out-of-scope code to be in-scope?__

- Security researchers may incorrectly assume that the collateral management system is within scope because they might question whether collateral that is locked in the lender's wallet can be successfully retrieved during liquidation or repayment events. This confusion arises because the retrieval process is partially controlled by the business logic in the backend, which could lead researchers to believe that the collateral locking and unlocking mechanisms are part of the attackable surface area.


__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

- No. This is a new product from scratch.

__Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?__

- We are most concerned about arithmetic overflow and loss of precision issues, which are commonly overlooked in DeFi protocols but can have severe consequences. Given TSI's complex financial calculations, several areas are particularly vulnerable:


__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?__

- ERC20

__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

- The signer who signs the settlement information is out of scope.

__Which chains and/or networks will the code in scope be deployed to?__

- Ethereum.

__What external dependencies are there?__

- Oracles from Chainlink or RedStone. DEXs for liquidation.

__Are there any unusual points about your protocol that may confuse Security Researchers?__

- All participating addresses use Fireblocks' 2-of-2 Multi-Party Computation (MPC) wallets, where users hold one key share and Fireblocks (not TSI directly) holds the other key share. This creates an unusual custody model that may confuse researchers:

*Key Unusual Points:*

- **Non-Custodial but Coordinated:** While TSI never holds user funds directly, the collateral locking mechanism relies on lender pre-approval rather than traditional smart contract escrow. Lenders must pre-sign transactions that allow the settlement smart contract to automatically transfer collateral from their wallet during repayment or liquidation events.

- **Hybrid Settlement Model:** Unlike typical DeFi protocols where assets are deposited into smart contracts, TSI's settlement contracts facilitate direct wallet-to-wallet transfers. The contracts don't hold funds but coordinate simultaneous exchanges between parties.

- **Backend-Triggered Automation:** TSI's backend system can trigger certain automated actions (like unlocking collateral during liquidation) because it coordinates with Fireblocks' MPC infrastructure, even though TSI doesn't control the private keys directly.

- **Device-Bound Keys:** User key shares are bound to specific browsers/devices, making the typical "connect any wallet" assumption invalid.

Researchers might incorrectly assume TSI has direct key control or that smart contracts hold collateral, when in reality the system uses a sophisticated coordination layer between MPC wallets and pre-authorized transaction execution.

__What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)__

- [https://docs.institutional.ts.finance/]
- https://www.youtube.com/watch?v=usyhq0ucMOw&list=PLW028xWwhYBHSmzbGLFjd4BybCTrBdjaE

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

__Rewards Terms__

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

Rewards are denominated in USD and distributed in USDC on Ethereum.

The reward pool is $4,000 USD if any bug is found.

If not a single bug is found (Insights do not count as bugs) the reward pool is $360 USD

On top of this, each participating SR will receive a guaranteed reward of $1,000 USD.

**Proof of Concept (PoC) Requirements**

For this program, runnable PoC code is not required. Whitehats are instead required to write a step-by-step explanation of the PoC and impact.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

*The "Insight" severity was introduced on Boost (Audit Competitions) & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

Duplicates of Insight reports are not eligible for a reward.

__KYC is Required__

Term Structure Institutional requires KYC information to pay for bug submissions. The following information will be required:
- Full name 
- Date of birth
- Proof of address (either a redacted bank statement with address or a recent utility bill)
- Copy of Passport or other Government issued ID

Security researchers are required to submit KYC within 14 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (3)

- Centralization issues related to Fireblock flow, such as allowance management and fund locking mechanism. (https://docs.institutional.ts.finance/)
- Problems with Oracle and other third-party contracts. (https://docs.institutional.ts.finance/)
- Security issues caused by private key or permission leakage. (https://docs.institutional.ts.finance/)
