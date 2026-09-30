# LayerZero

- Page: https://immunefi.com/bug-bounty/layerzero/scope/
- Max bounty: $15,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low
- End date: (none)

## Assets in scope (25)

- [smart_contract] https://aptoscan.com/account/0x54ad3d30af77b60d939ae356e6606de9a4da67583f02b962d2d3f2e481484e90 — Endpoint (Aptos)
- [smart_contract] https://etherscan.io/address/0x07245eEa05826F5984c7c3C8F478b04892e4df89 — FPValidator.sol
- [smart_contract] https://etherscan.io/address/0x1a44076050125825900e736c501f859c50fe728c#code — EndpointV2 (EVM)
- [smart_contract] https://etherscan.io/address/0x245b6e8ffe9ea5fc301e32d16f66bd4c2123eefc#code — ReceiveULN301 (EVM)
- [smart_contract] https://etherscan.io/address/0x4d73adb72bc3dd368966edd0f0b2148401a178e2#code — UltraLightNodeV2.sol
- [smart_contract] https://etherscan.io/address/0x589dedbd617e0cbcb916a9223f4d1300c294236b#code — DVN (EVM)
- [smart_contract] https://etherscan.io/address/0x66A71Dcef29A0fFBDBE3c6a460a3B5BC225Cd675#code — Endpoint (EVM)
- [smart_contract] https://etherscan.io/address/0xD231084BfB234C107D3eE2b22F97F3346fDAF705#code — SendULN301 (EVM)
- [smart_contract] https://etherscan.io/address/0xbb2ea70c9e858123480642cf96acbcce1372dce1#code — SendULN302 (EVM)
- [smart_contract] https://etherscan.io/address/0xc02ab410f0734efa3f14628780e6e695156024c2#code — ReceiveULN302 (EVM)
- [smart_contract] https://explorer.solana.com/address/4VDjp6XQaxoZf5RGwiPU9NR1EXSZn2TP4ATMmiSzLfhb — DVN (Solana)
- [smart_contract] https://explorer.solana.com/address/6doghB248px58JSSwG4qejQ46kFMW4AMj7vzJnWZHNZn — SendULN302 (Solana)
- [smart_contract] https://explorer.solana.com/address/76y77prsiCMvXMjuoZ5VRrhG5qYBrUMYTE5WgHqgjEn6 — EndpointV2 (Solana)
- [smart_contract] https://explorer.solana.com/address/7a4WjyR8VZ7yZz5XJAKm39BUGn5iT9CKcv2pmG9tdXVH — ReceiveULN302 (Solana)
- [smart_contract] https://github.com/LayerZero-Labs/devtools/tree/main/examples/oft-solana — OFT (Solana)
- [smart_contract] https://github.com/LayerZero-Labs/devtools/tree/main/packages/oapp-evm/contracts/oapp — OApp (EVM)
- [smart_contract] https://github.com/LayerZero-Labs/devtools/tree/main/packages/oft-evm/contracts — OFT (EVM)
- [smart_contract] https://github.com/LayerZero-Labs/solidity-examples/blob/main/contracts/token/oft/v1/OFT.sol — OFT (EVM)
- [smart_contract] https://github.com/LayerZero-Labs/solidity-examples/blob/main/contracts/token/oft/v2/OFTV2.sol — OFTv1.2 (EVM)
- [smart_contract] https://github.com/LayerZero-Labs/solidity-examples/blob/main/contracts/token/onft1155/ONFT1155.sol — ONFT1155 (EVM)
- [smart_contract] https://github.com/LayerZero-Labs/solidity-examples/blob/main/contracts/token/onft721/ONFT721.sol — ONFT721 (EVM)
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [smart_contract] https://tonviewer.com/0:0d122dec4ec8bd66c68344faf0dd471d727a7d57a21b62051705bbe2e4c272a7 — DVNProxy (TON)
- [smart_contract] https://tonviewer.com/0:150645746e25be5486eb3b2f5d98b44c6b324697c48d495d059f96fc9d3ec368 — ULNManager (TON)
- [smart_contract] https://tonviewer.com/0:1eb2bbea3d8c0d42ff7fd60f0264c866c934bbff727526ca759e7374cae0c166 — Controller (TON)

## Asset notes

All smart contracts of LayerZero can be found at [https://github.com/LayerZero-Labs.](https://github.com/LayerZero-Labs) However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

Impacts found in contracts which are deployed to multiple chains will be treated as one singular issue.

Documentation and instruction for PoC can be found here:
- GitHub README:[ https://github.com/LayerZero-Labs/LayerZero](https://github.com/LayerZero-Labs/LayerZero)
- Gitbook: [https://layerzero.gitbook.io/docs/](https://layerzero.gitbook.io/docs/)
- V2 Docs: [https://docs.layerzero.network](https://docs.layerzero.network)

If an impact can be caused to any other asset managed by LayerZero that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project. The vulnerability will then be evaluated by LayerZero Labs in good faith to determine where it would lie on the vulnerability scale.

## Impacts in scope (5)

- [smart_contract] Critical: Exploits resulting in the permanent locking or theft of user funds
- [smart_contract] Critical: Permanent DoS attacks (excluding volumetric attacks)
- [smart_contract] High: Any governance voting result manipulation
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Low: All above impacts for OApp, OFT & ONFT related contracts

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$15,000,000, rewardCalculationPercentage=10, rewardModel=up_to
- [smart_contract] High: maxReward=$250,000, rewardModel=up_to
- [smart_contract] Medium: maxReward=$25,000, rewardModel=up_to
- [smart_contract] Low: maxReward=$10,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the  [Immunefi Vulnerability Severity Classification System V2.2. ](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2/)This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported. 

V1 Smart Contract rewards are classified by Group 1 and Group 2. Group 1 consists of: Ethereum, BNB Chain, Avalanche, Polygon, Arbitrum, Optimism, Fantom. Group 2 consists of all other chains. Group 1 rewards are notated in the rewards table by the higher ranges listed by severity level, while Group 2 rewards are notated by the lower ranges listed by severity level. 

All bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. Bug reports are required to include a runnable PoC in order to prove impact. Exceptions may be made in cases where the vulnerability is objectively evident from simply mentioning the vulnerability and where it exists. However, the bug reporter may be required to provide a PoC at any point in time.

All vulnerabilities marked in the [https://github.com/LayerZero-Labs/Audits ](https://github.com/LayerZero-Labs/Audits) are not eligible for a reward.

All Impacts for OFT and [ONFT](https://github.com/LayerZero-Labs/solidity-examples/tree/main/contracts/token/onft) related contracts will be treated as low severity classifications and respective rewards. 

Critical V1 smart contract vulnerability payouts for Group 1 are a minimum of __USD $250,000__, or 10% of the value at risk at the time of report submission, with a hard cap of __USD $15,000,000__, whichever is larger. Value at risk should be calculated primarily (though not exclusively) based on concrete and demonstrable funds at risk. Any supplementary reward beyond the minimum USD $250,000 or 10% of value at risk is at the discretion of the team.

Critical V1 smart contract vulnerability payouts for Group 2 are a minimum of __USD $25,000__, or 10% of the value at risk at the time of report submission, with a hard cap of __USD $1,500,000__, whichever is larger. Value at risk should be calculated primarily (though not exclusively) based on concrete and demonstrable funds at risk. Any supplementary reward beyond the minimum USD $25,000 or 10% of value at risk is at the discretion of the team.

Critical V2 smart contract vulnerability payouts are a minimum of __USD $100,000__, or __10%__ of the value at risk at the time of report submission, with a hard cap of __$2,000,000__, whichever is larger. Value at risk should be calculated primarily (though not exclusively) based on concrete and demonstrable funds at risk. Any supplementary reward beyond the minimum __USD $100,000__ or __10%__ of value at risk is at the discretion of the team.

All non-critical rewards for the project bug bounty program are scaled based on an internally established team criteria, taking into account the exploitability of the bug, the impact it causes, and the likelihood of the vulnerability presenting itself, which is especially factored in with bug reports requiring multiple conditions to be met that are currently not in-place. Rewards will be provided at the determined fair value by the team depending on these conditions, assuming that the bug report is in-scope of the bug bounty program.

LayerZero requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed are: 
- Invoice is required with Name, Address, and Payment Instructions
- Proof of address (either a redacted bank statement with your address or a recent utility bill with your name, address, and issuer of the bill)
- Copy of your passport or other Government ID will be required
- Bounty hunters must pass OFAC Screening. Rewards cannot be paid out if hunters are on the OFAC SDN list 

The collection of this information will be done by the project team.

Payouts are handled by __LayerZero Labs__  directly and are denominated in USD. However, payouts are done in __Fiat USD via wire transfer, or USDC, USDT and BUSD__, with the choice of ratio at the discretion of the team.

## Out of scope (program-specific)

- Sybil attacks
- Impacts to OApps themselves as a result of their own misconfiguration (including but not limited to eg. configuring bad libraries, verifier networks, executors…).
- DoS of LayerZero infrastructure is not eligible for bug bounty rewards
- Reports regarding bugs that LayerZero Labs was previously aware of are not eligible for a reward
- Dependencies & Third Party Code
- Temporary impacts resulting from configuration adjustment race-conditions

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
