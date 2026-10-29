# LayerZero

- Page: https://immunefi.com/bug-bounty/layerzero/scope/
- Max bounty: $3,500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (11)

- [smart_contract] https://etherscan.io/address/0x1a44076050125825900e736c501f859c50fe728c#code — EndpointV2 (EVM)
- [smart_contract] https://etherscan.io/address/0xbb2ea70c9e858123480642cf96acbcce1372dce1#code — SendULN302 (EVM)
- [smart_contract] https://etherscan.io/address/0xc02ab410f0734efa3f14628780e6e695156024c2#code — ReceiveULN302 (EVM)
- [smart_contract] https://explorer.aptoslabs.com/object/0xc33752e0220faf79e45385dd73fb28d681dcd9f1569a1480725507c1f3c3aba9 — SendULN302 (Aptos)
- [smart_contract] https://explorer.aptoslabs.com/object/0xc33752e0220faf79e45385dd73fb28d681dcd9f1569a1480725507c1f3c3aba9 — SendULN302 (Aptos)
- [smart_contract] https://explorer.aptoslabs.com/object/0xe60045e20fc2c99e869c1c34a65b9291c020cd12a0d37a00a53ac1348af4f43c — Endpoint V2 (Aptos)
- [smart_contract] https://explorer.solana.com/address/6doghB248px58JSSwG4qejQ46kFMW4AMj7vzJnWZHNZn — SendULN302 (Solana)
- [smart_contract] https://explorer.solana.com/address/76y77prsiCMvXMjuoZ5VRrhG5qYBrUMYTE5WgHqgjEn6 — EndpointV2 (Solana)
- [smart_contract] https://explorer.solana.com/address/7a4WjyR8VZ7yZz5XJAKm39BUGn5iT9CKcv2pmG9tdXVH — ReceiveULN302 (Solana)
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [smart_contract] https://tonscan.org/address/EQAesrvqPYwNQv9_1g8CZMhmyTS7_3J1Jsp1nnN0yuDBZrEH — Smart Contract - Controller (TON)

## Asset notes

All smart contracts of LayerZero can be found at [here](https://docs.layerzero.network/v2/deployments/deployed-contracts). Impacts found in contracts which are deployed to multiple chains will be treated as one singular issue.

Documentation can be found here:
- LayerZero Docs: [https://docs.layerzero.network](https://docs.layerzero.network)

## Impacts in scope (4)

- [smart_contract] Critical: Exploits resulting in the permanent locking or theft of user funds
- [smart_contract] Critical: Permanent DoS attacks (excluding volumetric attacks)
- [smart_contract] High: Any governance voting result manipulation
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)

## Impact notes

If an impact can be caused to any other asset managed by LayerZero that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project. The vulnerability will then be evaluated by LayerZero Labs in good faith to determine where it would fall on the vulnerability scale.

## Rewards

- [smart_contract] Critical: maxReward=$3,500,000, minReward=$25,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$250,000, rewardModel=up_to
- [smart_contract] Medium: maxReward=$25,000, rewardModel=up_to

## Reward notes

Smart Contract rewards are classified by Group 1 and Group 2. Group 1 rewards are notated in the rewards table by the higher ranges listed by severity level, while Group 2 rewards are notated by the lower ranges listed by severity level. 

- Group 1 consists of: EVM Chains. 
- Group 2 consists of: Non-EVM Chains. 

All bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required. Bug reports are required to include a runnable PoC in order to prove impact. Exceptions may be made in cases where the vulnerability is objectively evident from simply mentioning the vulnerability and where it exists. However, the bug reporter may be required to provide a PoC at any point in time.

Critical smart contract vulnerability payouts for Group 1 are a minimum of __USD $250,000__, or 10% of the value at risk at the time of report submission, with a hard cap of __USD $3,500,000__, whichever is larger. Value at risk should be calculated primarily (though not exclusively) based on concrete and demonstrable funds at risk. Any supplementary reward beyond the minimum USD $250,000 or 10% of value at risk is at the discretion of the team.

Critical smart contract vulnerability payouts for Group 2 are a minimum of __USD $25,000__, or 10% of the value at risk at the time of report submission, with a hard cap of __USD $1,000,000__, whichever is larger. Value at risk should be calculated primarily (though not exclusively) based on concrete and demonstrable funds at risk. Any supplementary reward beyond the minimum USD $25,000 or 10% of value at risk is at the discretion of the team.

All non-critical rewards for the project bug bounty program are scaled based on an internally established team criteria, taking into account the exploitability of the bug, the impact it causes, and the likelihood of the vulnerability presenting itself, which is especially factored in with bug reports requiring multiple conditions to be met that are currently not in-place. Rewards will be provided at the determined fair value by the team depending on these conditions, assuming that the bug report is in-scope of the bug bounty program.

LayerZero requires KYC to be done for all bug bounty hunters submitting a report and wanting a reward. The information needed are: 
- Invoice is required with Name, Address, and Payment Instructions
- Proof of address (either a redacted bank statement with your address or a recent utility bill with your name, address, and issuer of the bill)
- Copy of your passport or other Government ID will be required

The collection of this information will be done by the project team.

Payouts are handled by LayerZero directly and are denominated in USD. However, payouts are done in Fiat USD via wire transfer, USDC, or USDT, with the choice of ratio at the discretion of the team.

## Out of scope (program-specific)

- LayerZero Offchain Infrastructure
- Sybil Attacks
- Impacts to OApps themselves as a result of their own misconfiguration (including but not limited to e.g. configuring bad libraries, verifier networks, executors, etc).
- Reports regarding bugs that LayerZero was previously aware of are not eligible for a reward
- Dependencies & Third Party Code
- Temporary impacts resulting from configuration adjustment race-conditions

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
