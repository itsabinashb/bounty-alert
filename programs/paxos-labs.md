# Paxos Labs

- Page: https://immunefi.com/bug-bounty/paxos-labs/scope/
- Max bounty: $500,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (15)

- [smart_contract] https://etherscan.io/address/0x353741aBa79974a90F88594f6CBd1a9c54651015#code — PAXGy Manager Contract.
- [smart_contract] https://etherscan.io/address/0x397e38359f169748a02bc11f98D4f451FE88C1fd#code — PAXGy Accountant contract. Stores the NAV of the vault shares.
- [smart_contract] https://etherscan.io/address/0x3B4decc43d2173280198B46532Ef570062FCc8f5#code — Transit RolesAuthority contract. Solmate library for auth logic.
- [smart_contract] https://etherscan.io/address/0x41AB5d8387e60E30AACCF11357C306f6d875A6f7#code — PAXGy Teller. Receives deposits for minting PAXGy.
- [smart_contract] https://etherscan.io/address/0x49AAA987b1a7e9E4AE091dcD8332c39F322D7d28#code — TransitStation contract. Receives orders and also allows execution of orders.
- [smart_contract] https://etherscan.io/address/0x666156ab52bb9984F5c3985726f048Dd4A73887a#code — Transit Manager contract. Part of BoringVault architecture that allows merkle root based permissions to move funds.
- [smart_contract] https://etherscan.io/address/0x69e0BF658bE5600864A946b4e5B911736D248FB4 — PAXGy WithdrawQueue. Facilitates user withdrawals.
- [smart_contract] https://etherscan.io/address/0x6E0A209672f6e357B2B5435AB6AEa2acbB4B8c6D#code — PAXGy DCD FeeModule. Determines deposit fees.
- [smart_contract] https://etherscan.io/address/0x6c6494Fd9962eB98B94ffA48F6679058F820700e#code — PAXGy Token BoringVault. Custodies funds and deploys them into strategies.
- [smart_contract] https://etherscan.io/address/0x91248711709bC6a09078Baf79Eb9f9bE5035870a#code — PAXGy FreezeListBeforeTransferHook. A hook that maintains the freeze list for PAXGy.
- [smart_contract] https://etherscan.io/address/0x91FE06C6E9F97E7DE4580A280E03046155f8e1e3 — Transit BoringVault contract. Custodies funds from user orders and allows it to be routed to various venues based on secure permissions.
- [smart_contract] https://etherscan.io/address/0xC444dA4DF6AF6A9A3891a720c1712a4188d899DD — PAXGy Roles Authority contract.
- [smart_contract] https://etherscan.io/address/0xF34942E8612ccE476307B30a6246B43ce42B5D20#code — Transit Decoder contract. Used in conjunction with the Manager contract for secure permissions.
- [smart_contract] https://etherscan.io/address/0xF41e79D6e646f334C2fc4ea5Ae609707AE82264D#code — PAXGy WithdrawQueue Fee Module. Determines withdrawal fees.
- [smart_contract] https://etherscan.io/address/0xF6dE922D08cF9Ee4e7cE25ca1f3936EC1AA1f62C#code — PAXGy DistributorCodeDepositor. A helper contract built on top of the Teller for facilitating more deposit logic.

## Asset notes

(none)

## Impacts in scope (15)

- [smart_contract] Critical: Direct theft of any user NFTs, whether at-rest or in-motion, other than unclaimed royalties
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of NFTs
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of the principal or NFT
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: Unauthorized minting of NFTs
- [smart_contract] High: Permanent freezing of unclaimed royalties
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of NFTs
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed royalties
- [smart_contract] Medium: Block stuffing
- [smart_contract] Medium: Theft of gas
- [smart_contract] Medium: Unbounded gas consumption

## Impact notes

(none)

## Rewards

- [smart_contract] Critical: maxReward=$500,000, minReward=$10,000, primacy=primacy_of_rules, rewardCalculationPercentage=10, rewardModel=range
- [smart_contract] High: maxReward=$10,000, minReward=$5,000, primacy=primacy_of_rules, rewardModel=range
- [smart_contract] Medium: fixedReward=$1,000, primacy=primacy_of_rules, rewardModel=fixed

## Reward notes

Rewards are processed via USDG on the Ethereum network.

## Out of scope (program-specific)

These rules add to Immunefi's default out-of-scope list. Where a rule below differs from a default item, the rule below applies to this program. Each rule is judged against the program and the deployed system as they stood when the report was submitted.

- **In-scope contracts** are the contracts deployed at the addresses listed in the Assets in Scope table. For a listed proxy, the implementation it points to when the report is submitted is also in scope.
- **A proof of concept** must reproduce the impact against the in-scope contracts, in a local or forked environment, including every condition the scenario needs. A condition does not have to exist on mainnet today if the proof of concept reproduces it, for example by forking a specific block or simulating a feed state, as long as the deployed system can reach that state. A report is theoretical, and out of scope, when it only asserts an impact or relies on a condition its proof of concept does not reproduce.

**1. Admin or privileged-role configuration**

Impacts that depend on a value set by an admin or other privileged role are out of scope when that value is possible but is not set in the deployed system. Such values include roles and permissions, Merkle roots, fees and fee modules, rate limits, exchange rate bounds, supported assets, cross-chain peers and gas settings.

This exclusion does not apply when:

- the value is set in the deployed system and the report demonstrates an impact; the report is then assessed under the normal scope and impact rules;
- an unprivileged actor can set or change the value, directly or through a vulnerability in the in-scope contracts; or
- a privileged function, called with a value the deployed system is designed to accept, causes an impact listed in Impacts in Scope because of a logic error.

**2. Third-party services and infrastructure**

Impacts caused solely by a third-party service or infrastructure that Paxos Labs does not control are out of scope, such as messaging networks and bridges, and compliance or screening providers. This covers their bugs, downtime, censorship, misconfiguration, and delayed or failed delivery. A vulnerability in the in-scope contracts remains in scope, including in how they handle a third-party failure.

This applies even when the third-party failure puts funds held by the in-scope contracts at risk, and whether or not Paxos Labs was already aware of the failure. A vulnerability in the protocol's own contracts, including in how they integrate with or rely on a third-party component, remains in scope.

**3. Oracle and market manipulation**

For this program, Immunefi's default exception for oracle manipulation and flash loan attacks is narrowed. Impacts that depend on manipulating the price or liquidity of an external market or oracle, including through flash loans, are out of scope unless the report includes a proof of concept that:

- runs against the in-scope contracts on a fork of mainnet;
- manipulates a market or oracle that the in-scope contracts read at the time of submission; and
- uses only liquidity that is available at the time of submission or expected within the next 12 months, as set out in Immunefi's [Attack Investment Amount](https://immunefisupport.zendesk.com/hc/en-us/articles/17243068885265) standard.

Hypothetical or assumed market conditions are not considered. An attack that is not profitable for the attacker is assessed under Immunefi's [griefing standard](https://immunefisupport.zendesk.com/hc/en-us/articles/17455102268305).

**4. Non-standard token behaviour**

Impacts that depend on non-standard token behaviour are out of scope when the token is not enabled as a supported asset in the deployed system. Such behaviour includes fee-on-transfer, rebasing, ERC-777 or other callback tokens, unusual decimals, and the ability to blacklist, freeze or pause balances. For a supported asset, its behaviour as deployed is in scope. Enabling a new token is an admin action, so rule 1 also applies.

**5. Positions and assets held in external protocols or markets**

Losses arising from positions or assets that the in-scope contracts hold in external protocols or markets are out of scope. This includes hacks of those protocols, bad debt, slashing, liquidations, and price movement or depegging of any asset. A loss caused by a vulnerability in the in-scope contracts' own logic for integrating with or handling those positions remains in scope. Financial risk management decisions, such as which external positions to hold and their limits, are not in scope.

**6. Code not deployed or not in production**

Only the in-scope contracts are in scope. Other code in the repository is out of scope, including undeployed or deprecated contracts, scripts, tests and mocks. Undeployed code is in scope only when Paxos Labs has publicly stated that it will be deployed without further changes as an upgrade of an in-scope contract, as set out in Immunefi's [standard for undeployed code](https://immunefisupport.zendesk.com/hc/en-us/articles/27871612917649).

**7. Rounding and precision loss**

Rounding errors and precision loss are out of scope unless the proof of concept demonstrates a loss to the protocol or its users of at least USD 100,000. The threshold can be met by repeating the operation or scaling the amounts, as long as the proof of concept runs the full sequence within the deployed system's current limits, such as rate limits and caps.

**8. Chain-level and network-level events**

Impacts that require a chain-level or network-level event outside Paxos Labs' control are out of scope. Such events include a sequencer or validator outage, censorship, network congestion, and a reorganization of blocks that the in-scope contracts or their messaging configuration already treat as final. This includes impacts that depend on a missing sequencer uptime check. Impacts on chains where the protocol is not deployed, including EVM differences, are also out of scope. How the in-scope contracts handle expected behaviour on the chains where they are deployed, such as a reorganization within the confirmation window they are configured to wait for, remains in scope.

**9. User error**

Impacts caused by a user's own error are out of scope, such as sending funds to an incorrect recipient or destination address, using a smart contract wallet the user does not control on the destination chain, sending tokens directly to a contract outside its intended flows, or setting slippage or minimum-output parameters that do not protect the user. A vulnerability that makes the in-scope contracts ignore or miscalculate a parameter the user supplied remains in scope.

**10. Compliance Error**

Impacts around compliance such as freezing / user screening is out of scope.

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Transit/PAXGy Known Issues (https://docs.google.com/document/d/14gImubrl0MNn_Jl_2_jCW1QPD4ra_MqYX-TV8S7JGlQ/edit?usp=sharing)
