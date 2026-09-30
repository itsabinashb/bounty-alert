# Orderly Network

- Page: https://immunefi.com/bug-bounty/orderlynetwork/scope/
- Max bounty: $100,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (25)

- [smart_contract] https://arbiscan.io/address/0x173B47eDBeCa665125edc24C509bfE545CDA60a9 — Crosschain relay ARB
- [smart_contract] https://arbiscan.io/address/0x816f722424b49cf1275cc86da9840fbd5a6167e9 — Vault Arb
- [smart_contract] https://arbiscan.io/address/0xA2eA0a58b083c492AdC91A687FAc8B53AdB7c0Fd — Vault Admin ARB
- [smart_contract] https://arbiscan.io/address/0xa0a07a78c7d31E6f8698F48Fc9219f9a3030f38C — Vault cross-chain manager ARB
- [smart_contract] https://explorer.orderly.network/address/0x14a6342A8C1Ef9856898F510FcCE377e46668F33 — Vault manager
- [smart_contract] https://explorer.orderly.network/address/0x173B47eDBeCa665125edc24C509bfE545CDA60a9 — Crosschain relay
- [smart_contract] https://explorer.orderly.network/address/0x173B47eDBeCa665125edc24C509bfE545CDA60a9 — Crosschain relay
- [smart_contract] https://explorer.orderly.network/address/0x343Ca787e960cB2cCA0ce8cfB2f38c3739E28a1E — Fee manager
- [smart_contract] https://explorer.orderly.network/address/0x6F7a338F2aA472838dEFD3283eB360d4Dff5D203 — Ledger contract (Verifying Contract for  EIP712 Withdraw Msg)
- [smart_contract] https://explorer.orderly.network/address/0x7CC5B6433eb33164c88F6512f56C566CFC3420BF — Operator manager
- [smart_contract] https://explorer.orderly.network/address/0x9281CBc1e37d3bcDB8BAddFa4302B6eb5DAd2672 — Market manager
- [smart_contract] https://explorer.orderly.network/address/0xa0a07a78c7d31E6f8698F48Fc9219f9a3030f38C — Ledger crosschain manager
- [smart_contract] https://github.com/OrderlyNetwork/contract-evm/tree/main/src — All files under /main/src except tUSDC.sol contract
- [smart_contract] https://github.com/OrderlyNetwork/evm-cross-chain/tree/main/contracts — All files under /contracts/ folder except contracts/test, and contracts/layerzero/mocks
- [smart_contract] https://optimistic.etherscan.io/address/0x173B47eDBeCa665125edc24C509bfE545CDA60a9 — Crosschain relay OP
- [smart_contract] https://optimistic.etherscan.io/address/0x816f722424b49cf1275cc86da9840fbd5a6167e9 — Vault OP
- [smart_contract] https://optimistic.etherscan.io/address/0xA2eA0a58b083c492AdC91A687FAc8B53AdB7c0Fd — Vault Admin OP
- [smart_contract] https://optimistic.etherscan.io/address/0xa0a07a78c7d31E6f8698F48Fc9219f9a3030f38C — Vault cross-chain manager OP
- [smart_contract] https://polygonscan.com/address/0x173B47eDBeCa665125edc24C509bfE545CDA60a9 — Crosschain relay Polygon
- [smart_contract] https://polygonscan.com/address/0x816f722424b49cf1275cc86da9840fbd5a6167e9 — Vault Polygon PoS
- [smart_contract] https://polygonscan.com/address/0xa0a07a78c7d31E6f8698F48Fc9219f9a3030f38C — Vault cross-chain manager polygon
- [smart_contract] https://polygonscan.com/address/0xa2ea0a58b083c492adc91a687fac8b53adb7c0fd — Vault Admin Polygon PoS
- [websites_and_applications] https://api-evm.orderly.org — Api EVM
- [websites_and_applications] https://api.orderly.org — Api
- [websites_and_applications] https://orderly.network/ — Main Web App

## Asset notes

All code of Orderly Network can be found at https://github.com/OrderlyNetwork. Documentation for the assets provided in the table can be found at https://orderly.network/docs/build-on-evm/smart-contract-overview.

## Impacts in scope (19)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Contract fails to deliver promised returns, but doesn't lose value
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:   /etc/shadow, database passwords, blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking down the application/website (no DDoS)
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:  Email, Password of the victim etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application (persistent), such as:    - HTML injection, - Replacing existing text with arbitrary text, Arbitrary file uploads, etc.
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application (reflected), such as:  - Reflected HTML injection,  - Loading external site data
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:  Iframing leading to modifying the backend/browser state (demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:  Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:  Locking up the victim from login, Cookie bombing, etc.

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$100,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$20,000, minReward=$5,000, rewardModel=range
- [smart_contract] Medium: fixedReward=$5,000, rewardModel=fixed
- [smart_contract] Low: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: maxReward=$10,000, minReward=$7,500, otherImpactMaxReward=$7,500, rewardModel=range
- [websites_and_applications] High: fixedReward=$5,500, rewardModel=fixed
- [websites_and_applications] Medium: fixedReward=$4,000, rewardModel=fixed
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact the vulnerability could otherwise cause based on the Impacts in Scope table further below. 

__Reward Calculation for Critical Level Reports__
 
For critical Smart Contract bugs, the reward amount is 10% of the funds directly affected up to a maximum of USD 100,000. The calculation of the amount of funds at risk is based on the time and date the bug report is submitted. However, a minimum reward of USD 25,000 is to be rewarded in order to incentivize security researchers against withholding a bug report.   


__Repeatable Attack Limitations__

If the smart contract where the vulnerability exists can be upgraded or paused, only the initial attack will be considered for a reward. This is because the project can mitigate the risk of further exploitation by upgrading or pausing the component where the vulnerability exists. The reward amount will depend on the severity of the impact and the funds at risk. 


For critical repeatable attacks on smart contracts that cannot be upgraded or paused, the project will consider the cumulative impact of the repeatable attacks for a reward. This is because the project cannot prevent the attacker from repeatedly exploiting the vulnerability until all funds are drained and/or other irreversible damage is done. Therefore, this warrants a reward equivalent to 10% of funds at risk, capped at the maximum critical reward. 

__Reward Calculation for High Level Reports__

High vulnerabilities concerning theft/permanent freezing of unclaimed yield/royalties are rewarded within a range of $5,000 to $20,000 depending on the funds at risk, capped at the maximum high reward.  


In the event of temporary freezing, the reward doubles from the full frozen value for every additional 48h that the funds are temporarily frozen, up until a max cap of the high reward. This is because as the duration of the freezing lengthens, the potential for greater damage and subsequent reputational harm intensifies. Thus, by increasing the reward proportionally with the frozen duration, the project ensures stronger incentives for bug disclosure of this nature.

For critical web/apps bug reports will be rewarded with $10,000, only if the impact leads to:

- A loss of funds involving an attack that does not require any user action
- Private key or private key generation leakage leading to unauthorized access to user funds that results in lost user funds

All other impacts that would be classified as Critical would be rewarded a flat amount of $7,500. The rest of the severity levels are paid out according to the Impact in Scope table.  

__Previous Audits__

Orderly Network has provided these completed audit review reports for reference. Any unfixed vulnerability mentioned in these reports are not eligible for a reward.

- https://github.com/OrderlyNetwork/Audits 


__Proof of Concept (PoC) Requirements__

A PoC is required for the following severity levels:

- Smart Contract, Critical
- Smart Contract, High
- Smart Contract, Medium
- Smart Contract, Low
- Web/App, Critical
- Web/App, High
- Web/App, Medium
- Web/App, Low

All PoCs submitted must comply with the Immunefi-wide [PoC Guidelines and Rules](https://immunefisupport.zendesk.com/hc/en-us/articles/9946217628561-Proof-of-Concept-PoC-Guidelines-and-Rules). Bug report submissions without a PoC when a PoC is required will not be provided with a reward.

__Reward Payment Terms__

Payouts are handled by the Orderly Network team directly and are denominated in USD. However, payments are done in USDT.

## Out of scope (program-specific)

Any connection issues with third-party systems and applications(e.g. Discord boost sever)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
