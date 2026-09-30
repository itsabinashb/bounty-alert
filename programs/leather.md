# Leather

- Page: https://immunefi.com/bug-bounty/leather/scope/
- Max bounty: $5,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - critical, websites_and_applications - high, websites_and_applications - medium
- End date: (none)

## Assets in scope (7)

- [websites_and_applications] http://api.leather.io — Leather backend
- [websites_and_applications] https://app.leather.io — Leather web app
- [websites_and_applications] https://apps.apple.com/us/app/leather-self-custody-wallet/id6499127775 — Leather iOS app
- [websites_and_applications] https://chromewebstore.google.com/detail/leather/ldinpeekobnhjjdofggfgjlcehhmanlj — Leather browser extension
- [websites_and_applications] https://github.com/leather-io/mono — Monorepo
- [websites_and_applications] https://leather.io/ — Primacy of Impact (primacy of impact)
- [websites_and_applications] https://play.google.com/store/apps/details?id=io.leather.mobilewallet — Leather Android app

## Asset notes

(none)

## Impacts in scope (27)

- [websites_and_applications] Critical: A loss of funds involving an attack that does not require any user action
- [websites_and_applications] Critical: Arbitrary code execution in a Leather-controlled context (extension, mobile, web, or backend) that exposes signing material, enables unauthorized or mutated signing, or leaks production secrets.
- [websites_and_applications] Critical: Bypassing wallet authentication (password, lock screen, or biometrics) to access accounts, decrypted secrets, or signing capability
- [websites_and_applications] Critical: Direct theft or loss of user funds resulting from a vulnerability in the Leather wallet software that causes unauthorized signing, authorization, or broadcast of a transaction.
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Extraction or leakage of a user's secret recovery phrase / seed mnemonic
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as:
- Modifying transaction arguments or parameters
- Substituting contract addresses
- Submitting malicious transactions
- [websites_and_applications] Critical: Manipulation of a multisig transaction between proposal and broadcast, causing signers to approve or co-sign details different from what was presented to them.
- [websites_and_applications] Critical: Private key or private key generation leakage leading to unauthorized access to user funds
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Signing a transaction or message without any user approval
- [websites_and_applications] Critical: Subdomain takeover with already-connected wallet interaction
- [websites_and_applications] Critical: Taking and/modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as:
- Changing registration information
- Commenting
- Voting
- Making trades
- Withdrawals, etc.
- [websites_and_applications] Critical: Tampering with transactions between user approval and signing/broadcast (the signed transaction differs from what was displayed and approved)
- [websites_and_applications] Critical: The wallet constructs, signs, broadcasts, or derives a transaction or address that moves/receives funds at an attacker-influenced destination, and the correct destination appears nowhere the user could catch it. The substitution is in the bytes/derived address the wallet uses, not a label; no user deception step is required (or it's silent, like a receive-address swap).
- [websites_and_applications] Critical: Wallet interaction modification resulting in financial loss
- [websites_and_applications] High: An externally exploitable path that causes attacker-chosen code to enter an official Leather release or live deployment, demonstrated without testing prohibited release infrastructure.
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as:
- Email
- Password of the victim etc.
- [websites_and_applications] High: Subdomain takeover without already-connected wallet interaction
- [websites_and_applications] High: The wallet displays a benign destination while signing a materially different transfer, and the true destination is disclosed on no part of the approval, so a user exercising normal care is deceived. Requires an approval, but the approval is actively misleading with no corrective signal anywhere.
- [websites_and_applications] Medium: A misleading destination in one field where corrective information is present elsewhere on the same approval (the called contract id, the post-condition asset, the raw args), so an attentive user can detect it; or the attack needs extra preconditions (an attacker-deployed contract the user must choose to interact with, a specific token holding, a phishing step).
- [websites_and_applications] Medium: Injecting/modifying the static content on the target application without JavaScript (reflected), such as:
- Reflected HTML Injection
- Loading external site data
- [websites_and_applications] Medium: Interacting with the wallet's RPC/provider interface from an origin that was never granted permission, or spoofing another origin's granted permissions
- [websites_and_applications] Medium: Permanent and unrecoverable loss of access to funds caused by Leather’s derivation, transaction construction, key storage, backup, or recovery logic.
- [websites_and_applications] Medium: Redirecting users to malicious websites (open redirect)
- [websites_and_applications] Low: Taking over broken or expired outgoing links, such as:
- Social media handles, etc.

## Impact notes

(none)

## Rewards

- [websites_and_applications] Critical: maxReward=$5,000, minReward=$3,000, otherImpactMaxReward=$0, rewardModel=range
- [websites_and_applications] High: maxReward=$3,000, minReward=$2,000, rewardModel=range
- [websites_and_applications] Medium: maxReward=$2,000, minReward=$1,000, rewardModel=range
- [websites_and_applications] Low: fixedReward=$1,000, rewardModel=fixed

## Reward notes

Rewards are distributed according to the impact of the vulnerability based on the [Immunefi Vulnerability Severity Classification System V2.3](https://immunefi.com/immunefi-vulnerability-severity-classification-system-v2-3). This is a simplified 5-level scale, encompassing everything from consequence of exploitation to privilege required to likelihood of a successful exploit. If there is any discrepancy with the classification in the Impacts in Scope section, the classification in the Impacts in Scope section will hold true.

**Websites and Applications**

- Critical: USD 3000 up to USD 5000
- High: USD 2000 up to USD 3000
- Medium: USD 1000 up to USD 2000
- Low: Flat USD 1000
- Informational: Only in exceptional circumstances and solely at our discretion

**Primacy of Impact:** where a vulnerability in an in-scope Leather asset can be chained to a direct loss of user funds on Bitcoin or Stacks, the report escalates to the corresponding Blockchain reward tier of the Stacks program rather than being capped at the Websites and Applications tier. Escalation requires a complete, demonstrated exploit chain from the initial vulnerability through to the fund-loss impact, with each step proven by a working proof of concept.

**We agree to:**

- Respond meaningfully to all reported issues in a timely manner.
- Not pursue legal action against or "counter-hack" any researchers acting in good faith and abiding by this program's rules.
- Consider well-argued, evidence-based reports on their merits.

**You must:**

- Undergo KYC before any reward is paid.
- Not be based or test from an OFAC-sanctioned country or region, or be a sanctioned individual or organization, as defined here: [https://ofac.treasury.gov/sanctions-programs-and-country-information](https://ofac.treasury.gov/sanctions-programs-and-country-information)
- Report all bugs using this template. **All fields are required unless otherwise marked**.
  * Executive summary of issue:
  * Finding details:
  * Affected in-scope asset and the published build or version tested:
  * Repository, file, and line of code where relevant:
  * Steps to replicate (against testnet or a local build):
  * Impact of finding (short term):
  * Impact of finding (long term):
  * Mitigation suggestions (short term):
  * Mitigation suggestions (long term):
  * (Optional) Suggested patch:
  * (Optional) Any useful links or resources:
  * (Optional) Do you want a shout-out on our Security Wall of Fame?
- Test only against testnet or a local build. Testing against mainnet with real user funds is forbidden.

A proof-of-concept is required for all submissions. Please include it in the corresponding form field.

Payouts are handled by the Stacks Endowment team directly and are denominated in USD. However, payments will be made in the USD equivalent in the Stacks token (STX).

## Out of scope (program-specific)

**All reports must include a working proof of concept demonstrated against testnet or a local build, clear reproduction steps, and the specific in-scope asset and impact affected.** Reports that are theoretical, that consist of unmodified automated scanner or AI-generated output, or that lack a working PoC will be closed as informational or spam without further review, regardless of claimed severity. Mass-submitted, templated, or duplicate reports will be closed.

**Only the current production releases are in scope:** the latest published build of the Leather extension on the Chrome Web Store, and the latest published build of the Leather mobile app on the Apple App Store and Google Play Store. Pre-release and beta builds, unreleased or experimental code, and any earlier version other than the current published release are out of scope. Reports must demonstrate the issue against the current published build; findings that only affect older versions or unreleased code will be closed as out of scope.

Before submitting, check our open issues (https://github.com/leather-io/mono/issues) and pull requests (https://github.com/leather-io/mono/pulls). Any issue already reported or already being fixed is out of scope.

The following are out of scope for this program:

### Assets and surfaces
- The Bitcoin, Ordinals, Runes, and Stacks protocols themselves (report Stacks blockchain issues via the Stacks Immunefi program)
- Third-party dApps, exchanges, or websites that connect to Leather. Only Leather's own provider and connection layer is in scope
- Third-party services such as fiat onramps, node/RPC providers, and price feeds
- Marketing or documentation pages on leather.io

### Wallet threat model
- Anything requiring physical access to an unlocked device, an already compromised, rooted, or jailbroken device, or pre-existing malware on the user's machine
- Loss of funds from user action, such as sending to the wrong address, approving a transaction after a clear and accurate confirmation screen, choosing a compromised password, using non-mainnet netrworks, or disclosing the secret recovery phrase
- Any issue requiring a modified, unofficial, or side-loaded build

### On-chain data rendering
- Misleading token names, scam airdrops, and spoofed NFT or contract metadata. Leather renders what exists on-chain and is not responsible for the accuracy or intent of that data, unless the rendering itself enables code execution or a signing bypass

### Low-value and noise reports
- Automated scanner or dependency-version output without a working exploit against production
- Missing security headers or cookie flags, SSL/TLS best practices, and SPF/DKIM/DMARC misconfigurations without a demonstrated exploit chain
- Version disclosure, fingerprinting, and verbose error messages
- Rate-limiting and brute-force concerns, including on local wallet unlock
- CORS, host header injection, content spoofing, tab-nabbing, and clickjacking unless chained to a demonstrated impact on funds, keys, or an active signing session
- Issues only exploitable on end-of-life browsers or OS versions
- Self-XSS, and DOM-based XSS unless demonstrated in a stored or privileged context
- Any theoretical chain without each link demonstrated by a working PoC
- Denial of service that does not lead to a loss of funds or a signing compromise.

### Prohibited
- Testing against mainnet with real user funds (use testnet or your own wallets)
- Phishing or social engineering against Leather staff, contributors, or users
- Testing third-party systems as the primary attack vector
- Public disclosure of an unpatched vulnerability before resolution and authorization

## Out of scope and rules

(none)

## Prohibited activities (program-specific)

(none)

## Known issues (0)

(none)
