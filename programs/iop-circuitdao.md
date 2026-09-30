# IOP | CircuitDAO

- Page: https://immunefi.com/bug-bounty/iop-circuitdao/scope/
- Max bounty: $10,000
- KYC required: yes
- Paused: no
- Invite only: yes
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: 2025-04-24T14:42:00.000Z

## Assets in scope (0)

(none)

## Asset notes

(none)

## Impacts in scope (21)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Manipulation of governance voting result deviating from voted outcome and resulting in a direct change from intended effect of original results
- [smart_contract] Critical: Oracle price manipulation without assuming data providers are untrustworthy or can be attacked off-chain
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Permanent significant depeg of stablecoin (BYC), e.g. by forcing undercollateralization
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Theft of funds from protocol treasury
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds for at least 24 hours
- [smart_contract] High: Temporary significant depeg of stablecoin (BYC) for at least 24  hours, e.g. by forcing undercollateralization
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Temporary freezing of funds for at least 1 hour
- [smart_contract] Medium: Temporary significant depeg of stablecoin (BYC) for at least 1 hour, e.g. by forcing undercollateralization
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value

## Impact notes

__Where might Security Researchers confuse out-of-scope code to be in-scope?__

N/A. There shouldn’t be any confusion. 


__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

No. As a CDP protocol, we have taken some inspiration from MakerDAO, both the initial single-collateral DAI system as well as some innovations of the multi-collateral version such as Dutch liquidation auctions. However, the implementation is completely different due to Chia’s coinset (UTXO) model and Chialisp as smart contract language.


__Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?__

See the list of in-scope bugs below. The higher the severity, the more concerned we are about the respective exploit.


__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?__

The protocol makes use of Chia Asset Token (CAT) standard (https://chialisp.com/cats/), singletons (https://chialisp.com/singletons/) and various custom coin types. An overview can be found here: https://docs.circuitdao.com/technical-manual/overview#list-of-protocol-coins

__What emergency actions may you want to use as a reason to downgrade an otherwise valid bug report?__

Mitigation measures that can be taken by governance. As an (out-of-scope) example, if Announcers collude to manipulate the Oracle price, governance can swap out the Oracle by updating the ORACLE_LAUNCHER_ID Statute within STATUTES_PRICE_DELAY. 

__What addresses would you consider any bug report requiring their involvement to be out of scope, as long as they operate within the privileges attributed to them?__

None

__What addresses would you consider any bug report requiring their involvement be out of scope, even if they exceed the privileges attributed to them?__

None

__Which chains and/or networks will the code in scope be deployed to?__

The project will eventually be deployed on Chia (mainnet and testnet11). 

__What external dependencies are there?__

See the pyproject.toml files in ‘puzzles’ and ‘circuit’ Github repos.
In terms of security context, the Chialisp code from ‘puzzles’ repos will get deployed on Chia mainnet. We will run a Chia fullnode service to connect the dapp backend to the blockchain.

__Are there any unusual points about your protocol that may confuse Security Researchers?__

The protocol differs from many other DeFi projects is that governance is done completely on-chain by governance token (CRT) holders. Governance proposals are created, vetoed on, and implemented (“enacted”) on-chain. There is no governance multi-sig (controlled by a foundation or otherwise).

The protocol is largely immutable, with governance being limited to changing the value of certain parameters (“Statutes”) or outputting custom conditions. The one exception to this is the Oracle singleton, which governance can replace entirely (by changing the value of the Oracle launcher ID at Statutes index 0)

__What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)__

Documentation for Circuit protocol can be found at: https://docs.circuitdao.com/
Note that the documentation is not up-to-date with the latest commit and contains inaccurate descriptions in several places. However, the docs should work well as an introduction to and general overview of the protocol.

SRs may also be interested in the audit report by Zellic: 

Chialisp-related documentation can be found at: https://chialisp.com/

The protocol makes use of modern chialisp features: https://chialisp.com/modern-chialisp/

## Rewards

- [smart_contract] Critical: level=critical, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] High: level=high, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] Medium: level=medium, payout=Portion of the reward pool, pocRequired=True
- [smart_contract] Low: level=low, payout=Portion of the reward pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

Total budget: **$10,000** broken down as follows:


**Reward pool:**

If bugs are found → USD $6k (see [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms))

If only Insights are found → USD $900 (9% of the Reward pool)

**Guaranteed rewards:**
$2k per SR → $4k total (for 2 SRs)

Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.

**Proof of Concept (PoC) Requirements**

For this program, runnable PoC code is not required. Whitehats are instead required to write a step-by-step explanation of the PoC and impact.
Read our [New Audit Competition Proof-of-Concept Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/33260632501777-Proof-of-Concept-Rules-for-Audit-Competitions )

**Insight reports can be submitted**. 
Read our [Insight validity rules](https://immunefisupport.zendesk.com/hc/en-us/articles/34179768760337-Insight-Severity-Level )

## Out of scope (program-specific)

- Impacts that come up when several announcers or data providers work together in dishonest or unfair ways.
- Economic attacks that rely on borrowing/shorting of governance tokens other than by flash loan

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
