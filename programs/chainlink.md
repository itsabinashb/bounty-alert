# Chainlink

- Page: https://immunefi.com/bug-bounty/chainlink/scope/
- Max bounty: $3,000,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications, Smart Contract
- PoC required for: smart_contract - critical, smart_contract - high, smart_contract - medium, smart_contract - low, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: (none)

## Assets in scope (25)

- [smart_contract] https://github.com/smartcontractkit/ccip-owner-contracts/tree/main — CCIP Owner
- [smart_contract] https://github.com/smartcontractkit/chainlink-aptos/tree/develop/contracts — Aptos
- [smart_contract] https://github.com/smartcontractkit/chainlink-ccip/tree/main/chains/evm/contracts — CCIP EVM
- [smart_contract] https://github.com/smartcontractkit/chainlink-ccip/tree/main/chains/solana/contracts — CCIP Solana
- [smart_contract] https://github.com/smartcontractkit/chainlink-evm/tree/develop/contracts — Chainlink EVM Contracts
- [smart_contract] https://github.com/smartcontractkit/chainlink-solana/tree/develop/contracts — Solana programs
- [smart_contract] https://github.com/smartcontractkit/chainlink-sui/tree/develop/contracts/ccip — Sui CCIP
- [smart_contract] https://github.com/smartcontractkit/chainlink-sui/tree/develop/contracts/link — Sui LINK
- [smart_contract] https://github.com/smartcontractkit/chainlink-sui/tree/develop/contracts/mcms/mcms — Sui MCMS
- [smart_contract] https://immunefi.com — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://chain.link/ — Main Web App
- [websites_and_applications] https://cre.chain.link — CRE Web App
- [websites_and_applications] https://data.chain.link/ — Data
- [websites_and_applications] https://faucets.chain.link/ — Faucets
- [websites_and_applications] https://github.com/smartcontractkit/chainlink-aptos/tree/develop/relayer — Aptos Offchain Relayer
- [websites_and_applications] https://github.com/smartcontractkit/chainlink-ccip/tree/main/commit — CCIP OCR Commit Plugin
- [websites_and_applications] https://github.com/smartcontractkit/chainlink-ccip/tree/main/execute — CCIP OCR Execute Plugin
- [websites_and_applications] https://github.com/smartcontractkit/chainlink-common/tree/main/keystore — Common Keystore
- [websites_and_applications] https://github.com/smartcontractkit/chainlink-solana/tree/develop/pkg/solana — Solana Offchain
- [websites_and_applications] https://github.com/smartcontractkit/chainlink-sui/tree/main/relayer — Sui Offchain Relayer
- [websites_and_applications] https://github.com/smartcontractkit/chainlink/tree/develop/core — Chainlink Core Node
- [websites_and_applications] https://github.com/smartcontractkit/external-adapters-js/ — External Adapters
- [websites_and_applications] https://github.com/smartcontractkit/libocr — LibOCR
- [websites_and_applications] https://github.com/smartcontractkit/operator-ui — Chainlink Core Node UI
- [websites_and_applications] https://immunefi.com — Primacy of Impact (primacy of impact)

## Asset notes

The following are considered out of scope for the program:

  - Any files in a dev, example, test, dummy, mock folder
  - Any contract with a `typeAndVersion` string which contains `-dev`
  - Any files with XXX in their name
  - Any *.smartcontract.com assets
  - Any test, example, dummy, mock, or vendored code

Also, for any file to be in scope, it has to be part of a release, not including pre-releases.

If an impact can be caused to any other asset managed by Chainlink that isn’t on this table but for which the impact is in the Impacts in Scope section below, you are encouraged to submit it for consideration by the project.

## Impacts in scope (38)

- [smart_contract] Critical: Any governance voting result manipulation
- [smart_contract] Critical: Direct theft of any user funds, whether at-rest or in-motion, other than unclaimed yield
- [smart_contract] Critical: Misreporting of prices and/or data
- [smart_contract] Critical: Permanent freezing of funds
- [smart_contract] Critical: Predictable or manipulable RNG that results in abuse of downstream services
- [smart_contract] Critical: Protocol insolvency
- [smart_contract] Critical: RMN onchain curse bypass
- [smart_contract] High: Delaying delivery of oracle price feed updates unrelated to congestion of the underlying blockchain and unrelated to CCIP
- [smart_contract] High: Rate limit violations
- [smart_contract] High: Theft of protocol revenue unrelated to CCIP
- [smart_contract] Medium: Griefing in the condition where the cost of carrying out attack is less than or equal to the damage
- [smart_contract] Medium: Loss of protocol revenue unrelated to CCIP (i.e skipping all or part of protocol fees)
- [smart_contract] Medium: Theft of protocol revenue for CCIP
- [smart_contract] Medium: Unbounded gas consumption
- [smart_contract] Low: Griefing in the condition where the cost of carrying out attack is more than the damage
- [smart_contract] Low: Loss of protocol revenue for CCIP (i.e skipping all or part of protocol fees)
- [smart_contract] Low: Smart contract fails to deliver expected return(s) but doesn’t result in loss of value
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injecting code that results in malicious interactions with an already-connected wallet such as modifying transaction arguments or parameters, substituting contract addresses, submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server such as /etc/shadow, database passwords, and blockchain keys
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as email or password of the victim, etc
- [websites_and_applications] High: Delaying delivery of oracle price feed updates unrelated to congestion of the underlying blockchain and unrelated to CCIP
- [websites_and_applications] High: Improperly disclosing confidential user information such as email address, phone number, physical address, etc
- [websites_and_applications] High: Injecting/modifying the static content on the target application without Javascript (Persistent) such as HTML injection without Javascript, replacing existing text with arbitrary text, arbitrary file uploads, etc
- [websites_and_applications] High: Rate limit violations
- [websites_and_applications] High: Taking down the application/website with methods other than DDoS
- [websites_and_applications] High: Theft of protocol revenue unrelated to CCIP
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as changing the first/last name of user, or en/disabling notification
- [websites_and_applications] Medium: Griefing in the condition where the cost of carrying out attack is less than or equal to the damage
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without Javascript (Reflected) such as reflected HTML injection or loading external site data
- [websites_and_applications] Medium: Loss of protocol revenue unrelated to CCIP (i.e skipping all or part of protocol fees)
- [websites_and_applications] Medium: Subdomain takeover
- [websites_and_applications] Medium: Theft of protocol revenue for CCIP
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction such as iframing leading to modifying the backend/browser state (demonstrate impact with PoC)
- [websites_and_applications] Low: Griefing in the condition where the cost of carrying out attack is more than the damage
- [websites_and_applications] Low: Loss of protocol revenue for CCIP (i.e skipping all or part of protocol fees)
- [websites_and_applications] Low: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Temporarily disabling user's access to target resource

## Impact notes

Only the following impacts are accepted within this bug bounty program. All other impacts are out of scope, even if they affect an in scope asset.

## Rewards

- [smart_contract] Critical: maxReward=$3,000,000, minReward=$100,000, rewardCalculationPercentage=0, rewardModel=range
- [smart_contract] High: maxReward=$75,000, rewardModel=up_to
- [smart_contract] Medium: maxReward=$10,000, rewardModel=up_to
- [smart_contract] Low: maxReward=$5,000, rewardModel=up_to
- [websites_and_applications] Critical: maxReward=$100,000, otherImpactMaxReward=$0, rewardModel=up_to
- [websites_and_applications] High: maxReward=$10,000, rewardModel=up_to
- [websites_and_applications] Medium: maxReward=$2,000, rewardModel=up_to
- [websites_and_applications] Low: maxReward=$1,000, rewardModel=up_to

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.2](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-2/). This is a simplified 5-level scale, with separate scales for websites/apps, smart contracts, and blockchains/DLTs, focusing on the impact of the vulnerability reported.  

All Smart Contracts bug reports require a proof of concept (PoC) and a suggestion for a fix to be eligible for a reward. All Websites and Applications bug reports must come with a PoC with an end-effect impacting an asset in scope in order to be considered for a reward. Explanations and statements are not accepted as PoCs and code is required.

Rewards for Critical Smart Contract vulnerabilities are at the sole and exclusive discretion of Chainlink Labs, with maximum reward of USD $3,000,000.

Specific reward amounts are determined based on a number of factors, such as the impact of proposed issues, ease of exploitability, and how likely the exploit conditions might occur.

Any supplementary reward beyond the minimum for the assigned criticality rating is at the discretion of Chainlink Labs.

__KYC/KYB requirement__

To ensure compliance, Chainlink Labs requires Know-Your-Customer (KYC) or Know-Your-Business (KYB)  information to be provided for all reports prior to a bounty being awarded.

The information required:

- Full Legal Name of individual (First, middle, and last, plus any prefix, and/or suffix)
- Full Legal Name of entity (if applicable)
- If you are a U.S. citizen, permanent resident, partnership, LLC, corporation, estate or trust, please send a filled-out and signed W-9 (https://www.irs.gov/pub/irs-pdf/fw9.pdf)
- If you are not a U.S. citizen, permanent resident, partnership, LLC, corporation, estate or trust:
  - Please send a filled-out and signed W-8BEN for individual and W-8 BEN-E for entities (https://www.irs.gov/pub/irs-pdf/fw8ben.pdf; https://www.irs.gov/pub/irs-pdf/fw8bene.pdf)
  - Provide a statement to certify that all services are performed outside of the U.S.
- Ethereum Wallet Address (for transfer of payment)

All bug bounty reporters must pass a screening check, to include but not limited to Office of Foreign Asset Control (OFAC) and Specially Designated Nationals And Blocked Persons List (SDN). 

Payouts are denominated in USD and sent in USD Coin (USDC).

__Repeatable Attacks__

In the event a report applies to multiple contracts or can be triggered multiple times, if a contract or product can be paused (either through on or off-chain means) only the impact of the first usage will be considered. If a product is not pausable such that there is no realistic way to prevent repeated usage of the attack, the entire amount at risk will be considered when evaluating impact.

## Out of scope (program-specific)

- Best practice critiques
- Disclosure of vulnerabilities will require the approval of the Chainlink team
- Issues resulting in documentation-only mitigation

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
