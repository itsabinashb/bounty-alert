# IOP | Zano Trade

- Page: https://immunefi.com/bug-bounty/iop-zano-trade/scope/
- Max bounty: $20,000
- KYC required: no
- Paused: no
- Invite only: yes
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium, websites_and_applications - low
- End date: 2025-07-03T10:00:00.000Z

## Assets in scope (0)

(none)

## Asset notes

(none)

## Impacts in scope (18)

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
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
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
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
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

__Build Commands, Test Commands, and How to Run Them__

1. Postgres database is required

2. .env file example
PGUSER="postgres"
PGPASSWORD="root"
PGHOST="127.0.0.1"
PGDATABASE="zano_trade"
PGPORT="5432"
JWT_SECRET="any_string"
OWNER_ALIAS="leave empty, this functionality it out of testing scope"

3. Run commands
npm i
npm run build
npm start

4. app will be accessible here: http://localhost:3000/


__Previous Audits__

- Zano Trade has no audit report as of 18 June 2025.


__Where might Security Researchers confuse out-of-scope code to be in-scope?__

- In-scope code is everything under /dex and all subpages (/dex/) in frontend. In the backend in-scope are all routes that can be called from /dex/ pages. All routes in provided backend files are also in-scope, as some of them can be called using API, not directly from frontend.


__Is this an upgrade of an existing system? If so, which? And what are the main differences?__

- No. It's a new web app in beta. 

__Where do you suspect there may be bugs and/or what attack vectors are you most concerned about?__

- Most important potential vulnerabilities:
1. Need to ensure database security as users' trade history is sensitive data. Make sure we don't expose it.
2. Need to ensure user can't be tricked to sign unexpected ionic swap transaction (with different amount or assets from what is in their order)


__What ERC20 / ERC721 / ERC777 / ERC1155 token standards are supported?__

- Not Applicable, As it's based off confidential assets https://docs.zano.org/docs/build/confidential-assets/overview


__What external dependencies are there?__

- It's a standard next js app, so most external dependencies could be considered. 


__What are the most valuable educational resources already available? (Ie. Documentation, Explainer videos or articles, etc)__

- Main url: https://trade.zano.org
 
- Swap process explained: https://docs.zano.org/docs/build/confidential-assets/ionic-swaps
 
- How does web ui work: https://docs.zano.org/docs/use/zano-trade
 
- Api documentation: https://docs.zano.org/docs/build/zano-trade-api/overview
 
**Scope**

Backend routes:
- https://github.com/PRavaga/zano-p2p/blob/master/api/routes/auth.router.ts
- https://github.com/PRavaga/zano-p2p/blob/master/api/routes/dex.router.ts
- https://github.com/PRavaga/zano-p2p/blob/master/api/routes/orders.router.ts
- https://github.com/PRavaga/zano-p2p/blob/master/api/routes/transactions.router.ts
- https://github.com/PRavaga/zano-p2p/blob/master/api/routes/user.router.ts
 
Frontend pages:
- https://github.com/PRavaga/zano-p2p/tree/master/src/pages/dex (https://trade.zano.org/dex)
- https://github.com/PRavaga/zano-p2p/tree/master/src/pages/dex/trading (https://trade.zano.org/dex/trading/<PAIR_ID>)
- https://github.com/PRavaga/zano-p2p/tree/master/src/pages/dex/orders  (https://trade.zano.org/dex/orders)

## Rewards

- [websites_and_applications] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] High: level=high, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=True
- [websites_and_applications] Low: level=low, payout=Portion of the Reward Pool, pocRequired=True

## Reward notes

__Rewards Terms__

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms).

Rewards are denominated in USD and distributed in USDC on Ethereum.

The reward pool is **$14,000 USD** if any bug is found.

If not a single bug is found (Insights do not count as bugs) the reward pool is $1,260 USD

On top of this, each participating SR will receive a guaranteed reward of $2,000 USD.

**Proof of Concept (PoC) Requirements**

For this program, runnable PoC code is not required. Whitehats are instead required to write a step-by-step explanation of the PoC and impact.

__Insight Rewards Payment Terms__

Insight Rewards: Portion of the Rewards Pool

*The "Insight" severity was introduced on Boost (Audit Competitions) & Attackathon programs to recognize contributions that extend beyond identifying immediate vulnerabilities. Currently, it's not an option to select the Insight severity when submitting a report. However, our team or program will designate it accordingly if applicable. "Insights" underscores our commitment to valuing all types of contributions that contribute to a more secure environment and will always be rewarded. [View more information about Insights](https://immunefisupport.zendesk.com/hc/en-us/articles/13333032674961-Severity-Classification-System?utm_source=immunefi)

Duplicates of Insight reports are not eligible for a reward.

## Out of scope (program-specific)

(none)

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
