# Gnosis Chain

- Page: https://immunefi.com/bug-bounty/gnosischain/scope/
- Max bounty: $2,000,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - high, smart_contract - critical, smart_contract - medium
- End date: (none)

## Assets in scope (4)

- [smart_contract] https://blockscout.com/xdai/mainnet/address/0x7301CFA0e1756B71869E93d4e4Dca5c7d0eb0AA6 — HomeBridgeErcToNative: DAI-xDAI TokenBridge contract on the Gnosis chain
- [smart_contract] https://blockscout.com/xdai/mainnet/address/0xf6A78083ca3e2a662D6dd1703c939c8aCE2e268d — HomeOmnibridge: OmniBridge contract on the Gnosis chain
- [smart_contract] https://etherscan.io/address/0x4aa42145Aa6Ebf72e164C9bBC74fbD3788045016 — XDaiForeignBridge: DAI-xDAI TokenBridge contract on the Ethereum Mainnet
- [smart_contract] https://etherscan.io/address/0x88ad09518695c6c3712AC10a214bE5109a655671 — ForeignOmnibridge: OmniBridge contract on the Ethereum Mainnet

## Asset notes

The smart contract regarding native xDAI bridging (XDaiForeignBridge and HomeBridgeErcToNative)  can be found at [https://github.com/gnosischain/tokenbridge-contracts/tree/xdaibridge-upgrade-sda](https://github.com/gnosischain/tokenbridge-contracts/tree/xdaibridge-upgrade-sda). The smart contracts regarding arbitrary ERC20 bridging (ForeignOmnibridge and HomeOmnibridge) can be found at [https://github.com/gnosischain/omnibridge/tree/master](https://github.com/gnosischain/omnibridge/tree/master).

Only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

If an impact can be caused to any other asset managed by Gnosis that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for the consideration by the project.

## Impacts in scope (20)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] Critical: Unintended alteration of what the NFT represents (e.g. token URI, payload, artistic content)
- [smart_contract] High: Miner-extractable value (MEV)
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing NFTs for at least  1 week
- [smart_contract] High: Temporary freezing of funds for at least  1 week
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Block stuffing for profit
- [smart_contract] Medium: Griefing (e.g. no profit motive for an attacker, but damage to the users or the protocol)
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$2,000,000, minReward=$50,000, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$50,000, minReward=$10,000, rewardModel=range
- [smart_contract] Medium: maxReward=$10,000, minReward=$1,000, rewardModel=range

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit.

All smart contract bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward.

Critical and High smart contract vulnerabilities are capped at 10% of economic damage, primarily taking into consideration funds at risk, but also PR and branding aspects, at the discretion of the team.

Payouts are handled by the __Gnosis Chain__ team directly and are denominated in __USD__. However, payouts are done in __USDC or xDAI__.

## Out of scope (program-specific)

- Best practice critiques
- The minter allowance granted by tokens to the `USDCTransmuter` can be exhausted to prevent successful USDC.e and EURC.e transfers.
- Omnibridge `onTokenTransfer()` function does not verify `msg.sender` and anyone can call this function to create fake bridge token.
- Validator signature collection on Home uses a static validator set defined at the time of transaction execution while signature verification uses the currently active validator set (potentially updated).
- callback through `onTokenBridged()` is not checked for success. Any failure in `onTokenBridged()` is silently swallowed.

test

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (4)

- Omnibridge onTokenTransfer() function does not verify msg.sender and anyone can call this function to create fake bridge token. (https://immunefi.com/bug-bounty/gnosischain/information/)
- The minter allowance granted by tokens to the USDCTransmuter can be exhausted to prevent successful USDC.e and EURC.e transfers. (https://immunefi.com/bug-bounty/gnosischain/information/)
- Validator signature collection on Home uses a static validator set defined at the time of transaction execution while signature verification uses the currently active validator set (potentially updated). (https://immunefi.com/bug-bounty/gnosischain/information/)
- callback through onTokenBridged() is not checked for success. Any failure in onTokenBridged() is silently swallowed. (https://immunefi.com/bug-bounty/gnosischain/information/)
