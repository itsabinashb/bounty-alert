# Mars Ecosystem

- Page: https://immunefi.com/bug-bounty/marsecosystem/scope/
- Max bounty: $10,000
- KYC required: no
- Paused: no
- Invite only: no
- Program type: Smart Contract, Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, smart_contract - critical, smart_contract - high, smart_contract - medium
- End date: (none)

## Assets in scope (10)

- [smart_contract] https://bscscan.com/address/0x00789Cfb69499c65ac9A3a68fb4917c9b4FcA2a7 — Core
- [smart_contract] https://bscscan.com/address/0x01D152fF991E76b6cb310387c07cAfdFda790a25 — AirDrop
- [smart_contract] https://bscscan.com/address/0x22D8d50454203bd5a41B49ef515891f1aD9f3e53 — LiquidityMiningMaster V1.1
- [smart_contract] https://bscscan.com/address/0x381Facb9282770a5E3Ac6c8637096b442039C3dB#contracts — VestingMaster
- [smart_contract] https://bscscan.com/address/0x6f12482D9869303B998C54D91bCD8bCcba81f3bE — MarsSwapFactory
- [smart_contract] https://bscscan.com/address/0x7859B01BbF675d67Da8cD128a50D155cd881B576 — XMS
- [smart_contract] https://bscscan.com/address/0xC35a8BdBB93abFAb362aF6dC3383cD2c6aEA6cBc — Timelock
- [smart_contract] https://bscscan.com/address/0xb68825C810E67D4e444ad5B9DeB55BA56A66e72D — MarsSwapRouter
- [smart_contract] https://bscscan.com/address/0xc7B8285a9E099e8c21CA5516D23348D8dBADdE4a — LiquidityMiningMaster
- [websites_and_applications] https://app.marsecosystem.com

## Asset notes

All smart contracts of Mars Ecosystem can be found at [https://github.com/MarsEcosystem](https://github.com/MarsEcosystem). However, only those in the Assets in Scope table are considered as in-scope of the bug bounty program.

## Impacts in scope (17)

- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] High: Permanent freezing of unclaimed yield
- [smart_contract] High: Temporary freezing of funds
- [smart_contract] High: Theft of unclaimed yield
- [smart_contract] Medium: Smart contract unable to operate due to lack of token funds
- [smart_contract] Medium: Unbounded gas consumption
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet such as: Modifying transaction arguments or parameters, Substituting contract addresses, Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as: /etc/shadow, database passwords, blockchain key (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user: Changing registration info, Commenting, Voting, Making trades, Withdrawals, Changing the NFT metadata
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as: HTML injection without Javascript, Replacing existing text with arbitrary text, Arbitrary file uploads, etc
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction

## Impact notes

__SMART CONTRACT__

__Theft of user funds:__ is a worst case scenario for a project. An example of in-motion funds is a swap. A user is transferring funds to the contract with the full expectation to exchange them for an equivalent value of another asset. If an attacker can manipulate the system in such a way that a user incurs losses during the transfer and the attacker profits, this is considered direct theft of user funds. If users are losing their stake, principal, vault balances, etc, that is theft of user funds.

__Permanent Freezing of funds:__ This includes bricking a contract which holds tokens so that a user is no longer able to withdraw their funds. It may also include burning of funds so that they can no longer be accessed by the owner. This also includes things like self-destructing implementation contracts so that the proxy becomes useless. The impact here is that funds within a system are no longer accessible.

__Protocol Insolvency:__ Some protocols provide yield to some users that is paid by other users (e.g. Compound lenders are owed yield that is provided by borrowers). An error in this calculation could result in the amount owed to users exceeding the amount owed by other users. This is insolvency. Alternatively, the protocol could have debts that exceed its assets in other ways. Of course this does not include "bank run" situations where it’s temporarily not possible to withdraw money from the protocol, but the protocol is otherwise adequately collateralized

__Theft of Unclaimed Yield:__  A yield is any asset distributed as a reward for participation in a system. Any theft of these rewards before they are distributed or claimed is classified as theft of an unclaimed yield.

__Permanent Freezing of Unclaimed Yield:__ A yield is any asset distributed as a reward for participation in a system. Whenever an attacker can prevent the yield from being able to move from the contract, for example by making the harvest() function always fail, this would mean the yield is permanently frozen.

__Temporary Freezing of Funds:__ This classification refers to temporary freezing of funds belonging to the protocol or another user, which the attacker does not own. There may be an amount of time or number of blocks which is in an acceptable range of operation for a project and is therefore excluded from consideration under this impact; however, this range of operation should be kept as short as possible because attacker locked funds can significantly impact user experience and cause rippling issues for a protocol. If an attacker needs to submit many costly transactions to achieve this impact, it is instead "Griefing" and is classified as "Medium".

__Smart contract unable to operate due to lack of token funds:__ This classification refers to bugs that mark the smart contract as unable to operate or work correctly due to lack of token funds. There may be cases where the smart contract cannot pay out any rewards for staked tokens because the contract doesn't hold any funds or won't accept any reimbursements. Another example would be the LINK token required to pay for certain Chainlink services. If those services are required for proper function of the system and it's possible (or likely) for the funds to be depleted, that would be a vulnerability.

__Unbounded gas consumption:__ Any looping done over an arbitrarily sized array may be vulnerable to unbounded gas consumption. If an attacker can add enough items to cause the gas used to call the function to exceed the block gas limit, it can result in a denial of service attack and prevent the function from being called.

__WEBSITES AND APPLICATIONS__

__Execute arbitrary system commands__ This impact refers to a security vulnerability in a website or application that allows an attacker to execute arbitrary commands on the underlying system. This type of vulnerability is often called arbitrary command injection. The impact of this vulnerability can be severe, as it provides the attacker with the ability to perform unauthorized actions on the affected system like Remote Command Execution (RCE).

__Retrieve sensitive data/files from a running server__ This impact allows an attacker to access and retrieve sensitive data or files from the affected server. This type of vulnerability is often called "information disclosure" or "data leakage." The impact of this vulnerability can be significant, as it exposes sensitive information that can be used for malicious purposes or further attacks.

__Taking down the application/website__ An attack that results in the disruption or complete unavailability of a website or application. This impact is different from DoS as it only refers to a vulnerability found in the application logic/code. When a website or application is taken down, it affects the user experience and the ability of users to access services and resources provided by the affected application. This can lead to customer dissatisfaction and potential loss of revenue for businesses that rely on the availability of their online services. The longer the downtime, the greater the potential negative impact on both users and the organization behind the website or application.

__Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user__ The attacker found a way to bypass the access control protection and arbitrarily update the other data without any interaction requirement. An attacker is able to perform actions that modify the state of the system or the network on behalf of other users, without the users' knowledge or consent.

__Subdomain takeover with already-connected wallet interaction__ This impact refers to a security vulnerability where an attacker gains control over a subdomain of a website or application, particularly one that interacts with users' connected cryptocurrency wallets. This takeover allows the attacker to manipulate the content and functionality of the subdomain, potentially leading to unauthorized interactions with the connected wallets.

__Direct theft of user funds__ It refers to a security vulnerability or an attack that results in the unauthorized transfer or misappropriation of users' digital assets, such as cryptocurrencies or tokens, directly from their wallets or accounts. One way someone can do this is by making unauthorized calls on the RPC. RPC is a communication method used to interact with blockchain nodes for sending transactions, querying data, and performing other actions. If there is a vulnerability or misconfiguration in the RPC implementation, an attacker might exploit it to directly steal user funds.

__Malicious interactions with an already-connected wallet__

  - _Modifying transaction arguments or parameters_
The attacker found a way to substitute the contract address with a malicious contract address stored at the frontend level.

  - _Substituting contract addresses_
The attacker found a way to modify the parameters of the transaction calls made to the wallet connected to the front end.

  - _Submitting malicious transactions_
The attacker found a way to inject malicious javascript code into the frontend that could initiate a malicious transaction to the wallet connected to the frontend

__Injecting/modifying the static content on the target application without Javascript (Persistent)__
The attacker discovered a method to persistently inject HTML code or plain text into the frontend, which could potentially deceive users visiting the frontend into providing sensitive keys, navigating to an external site controlled by the attacker, or falling for phishing 

__Subdomain takeover without already-connected wallet interaction__
The attacker found a way to claim or hijack the subdomain and inject a malicious code that could be used as a phishing vector for victims visiting the subdomain.

## Rewards

- [smart_contract] Critical: fixedReward=$10,000, rewardCalculationPercentage=10, rewardModel=fixed
- [smart_contract] High: fixedReward=$3,000, rewardModel=fixed
- [smart_contract] Medium: fixedReward=$1,000, rewardModel=fixed
- [websites_and_applications] Critical: fixedReward=$2,500, otherImpactMaxReward=$0, rewardModel=fixed
- [websites_and_applications] High: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System 3.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3/). This is a simplified 5-level scale, with separate scales for websites/apps and smart contracts/blockchains, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit. 

All bug reports must come with a PoC with an end-effect impacting an asset-in-scope in order to be considered for a reward. Explanations and statements are not accepted as PoC and code is required.

Bugs reported in the following audits are not eligible for a reward:

  - [SlowMist Audit](https://github.com/MarsEcosystem/mars-resource/blob/master/audit/SlowMist%20Audit%20Report%20-%20Mars%20Ecosystem%20-%20EN.pdf)
  - [CertiK Audit](https://github.com/MarsEcosystem/mars-resource/blob/master/audit/Certik%20Audit%20Report%20-%20Mars%20Ecosystem.pdf)

Payouts are handled by the __Mars Ecosystem__ team directly and are denominated in __USD__. However, payouts are done in __XMS__ or __BUSD__, at the discretion of the team.

## Out of scope (program-specific)

__Smart Contracts and Blockchain__
 - Best practice critiques
  - Protocol Risks Caused by BlockChain(BNB Chain) Vulnerabilities
  - Sandwich attack during swap with the issues with victim leading to exploiting himself
  - The residual unowned rewards in the contract is frozen
  - Withdrawal of abnormally entered (such as direct transfer) assets through the contract public function
  - Assets entered abnormally (such as direct transfer) cannot be withdrawn
  - Issues with the LP contracts that are due to specific underlying tokens are not in scope.


__Websites and Apps__
  - Clickjacking
  - Misleading Unicode text (e.g. using right to left override characters)
  - HTTP security headers
  - Cache control issues

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
