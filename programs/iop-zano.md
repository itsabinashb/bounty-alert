# IOP | Zano

- Page: https://immunefi.com/bug-bounty/iop-zano/scope/
- Max bounty: $25,000
- KYC required: yes
- Paused: no
- Invite only: yes
- Program type: Blockchain/DLT, Websites and Applications
- PoC required for: blockchain_dlt - critical, blockchain_dlt - high, blockchain_dlt - medium, blockchain_dlt - low, websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: 2025-03-10T14:00:00.000Z

## Assets in scope (0)

(none)

## Asset notes

(none)

## Impacts in scope (32)

- [blockchain_dlt] Critical: Direct loss of funds
- [blockchain_dlt] Critical: Network not being able to confirm new transactions (total network shutdown)
- [blockchain_dlt] Critical: Permanent freezing of funds (fix requires hardfork)
- [blockchain_dlt] Critical: Unintended permanent chain split requiring hard fork (network partition requiring hard fork)
- [blockchain_dlt] High: Causing network processing nodes to process transactions from the mempool beyond set parameters
- [blockchain_dlt] High: RPC API crash affecting programs with greater than or equal to 25% of the market capitalization on top of the respective layer
- [blockchain_dlt] High: Temporary freezing of network transactions by delaying one block by 500% or more of the average block time of the preceding 24 hours beyond standard difficulty adjustments
- [blockchain_dlt] High: Unintended chain split (network partition)
- [blockchain_dlt] Medium: A bug in the respective layer 0/1/2 network code that results in unintended smart contract behavior with no concrete funds at direct risk
- [blockchain_dlt] Medium: Increasing network processing node resource consumption by at least 30% without brute force actions, compared to the preceding 24 hours
- [blockchain_dlt] Medium: Shutdown of greater than or equal to 30% of network processing nodes without brute force actions, but does not shut down the network
- [blockchain_dlt] Low: Modification of transaction fees outside of design parameters
- [blockchain_dlt] Low: Shutdown of greater than 10% or equal to but less than 30% of network processing nodes without brute force actions, but does not shut down the network
- [websites_and_applications] Critical: Changing NFT metadata
- [websites_and_applications] Critical: Direct theft of user NFTs
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] Critical: Taking down the NFT URI
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Improperly disclosing confidential user information, such as:
- Email address
- Phone number
- Physical address, etc.
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Changing the first/last name of user
- Enabling/disabling notifications
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Changing details of other users (including modifying browser local storage) without already-connected wallet interaction and with significant user interaction, such as:
- Iframing leading to modifying the backend/browser state (must demonstrate impact with PoC)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.
- [websites_and_applications] Low: Temporarily disabling user to access target site, such as:
- Locking up the victim from login
- Cookie bombing, etc.

## Impact notes

**Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?**

We are concerned the most about implementation of cryptography and core rules (Bulletproofs, CLSAG etc). 

Most concerning attack vectors are:
- Emission bugs (printing coins out of air)
- Consensus bugs (double spend attack vectors, PoS grinding attacks)

**What external dependencies are there?**

Boost and OpenSSL

**What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc**

This repository contains papers that describe math behind the project:  [https://github.com/hyle-team/docs/tree/master/zano](https://github.com/hyle-team/docs/tree/master/zano)

## Rewards

- [blockchain_dlt] Critical: level=critical, payout=portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] High: level=high, payout=portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Medium: level=medium, payout=portion of the Reward Pool, pocRequired=True
- [blockchain_dlt] Low: level=low, payout=portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Critical: level=critical, payout=portion of the Reward Pool, pocRequired=True
- [websites_and_applications] High: level=high, payout=portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Medium: level=medium, payout=portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Low: level=low, payout=portion of the Reward Pool, pocRequired=True

## Reward notes

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

Total budget: $25,000 broken down as follows:

**Reward pool:**

If bugs are found → USD $15k (see [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms))

If only Insights are found → USD $1,35k (9% of the Reward pool)

**Guaranteed rewards:**
$5k per SR → $10k total (for 2 SRs)

Duplicate submissions of bugs are valid. Duplicate submissions of Insights are invalid.

**Proof of Concept (PoC) Requirements**

For this program, runnable PoC code is not required. Whitehats are instead required to write a step-by-step explanation of the PoC and impact.

## Out of scope (program-specific)

(none)

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (1)

- Any attacks related to lock time in transaction are out of scope. We removed this parameter from API but it still possible to create transaction with locked outputs. we are aware of this situation and it’s known to exist. Also, the default wallet behaviour is ignoring such transactions. (https://github.com/immunefi-team/zano-iop)
