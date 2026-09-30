# Audit Competition | ENS

- Page: https://immunefi.com/bug-bounty/audit-competition-ens/scope/
- Max bounty: $70,000
- KYC required: yes
- Paused: no
- Invite only: no
- Program type: Websites and Applications
- PoC required for: websites_and_applications - low, websites_and_applications - medium, websites_and_applications - high, websites_and_applications - critical
- End date: 2026-09-14T11:00:00.000Z

## Assets in scope (5)

- [websites_and_applications] https://github.com/immunefi-team/audit-comp-ens/tree/audit-comp-ready/apps/manager — Manager app Files
- [websites_and_applications] https://github.com/immunefi-team/audit-comp-ens/tree/audit-comp-ready/apps/portal — Explorer app Files
- [websites_and_applications] https://github.com/immunefi-team/audit-comp-ens/tree/audit-comp-ready/packages/smart-account — Smart-account
- [websites_and_applications] https://github.com/immunefi-team/audit-comp-ens/tree/audit-comp-ready/packages/transaction-manager — Transaction-manager
- [websites_and_applications] https://github.com/immunefi-team/audit-comp-ens/tree/audit-comp-ready/workers — Workers

## Asset notes

## Build Commands, Test Commands, and How to Run Them

### Prerequisites
* **Node:** `v22`
* **pnpm:** `v10` (pinned in `packageManager`; run `corepack enable`)
* **Docker:** Required for end-to-end (E2E) suites only

---

### Setup
```bash
pnpm install --frozen-lockfile
```

**Audited revision — commit hash:** `63772fd872af472ced58b009499355f3430c2a86`

---

### Environment Variables

#### ⚙️ Manager App (`apps/manager`)
Add to `apps/manager/.env.local`:
```bash
VITE_RHINESTONE_API_KEY=rs_FWMNwSvBEEhsk6jWi46yUUO50fC65fOe1lVSnDsls4
```
`VITE_TELEGRAM_BOT_ID` — optional; only used by the Telegram notification-channel login. The app runs fine without it. Telegram login widgets only work from the domain registered with the bot, so to exercise this flow locally, create your own bot with Telegram's @BotFather, register your local domain with it, and set this variable to your bot's numeric ID.

#### 🧭 Explorer App (`apps/portal`)
No configuration needed; the committed defaults use public endpoints.

---

### Application Commands

#### 🧭 Explorer App (`apps/portal`)
 **Server:** Runs on `http://localhost:3001`
 **Config:** Runs with no configuration; all defaults use public endpoints.
```bash
pnpm --filter portal dev      # Start dev server
pnpm build:portal             # Build (also typechecks)
pnpm typecheck:portal         # Typecheck only
pnpm test:portal              # Unit tests
pnpm test:portal:cov          # Unit tests with coverage
```

#### ⚙️ Manager App (`apps/manager`)
**Server:** Runs on `http://localhost:3000`
**Config:** Configuration values are supplied with the test environment (see Environment Variables above).
```bash
pnpm dev:manager              # Start dev server
pnpm build:manager            # Build
pnpm typecheck:manager        # Typecheck
pnpm test:manager             # Unit tests
pnpm test:manager:cov         # Unit tests with coverage
# Optional: Run Storybook on :6006
pnpm --filter manager storybook:dev
```

---

### End-to-End Tests (Playwright)
**Requirement:** Docker must be running locally.
```bash
pnpm e2e:infra:up             # Start local chain and services
pnpm e2e:manager              # Run Manager suite
pnpm e2e:portal               # Run Explorer suite
pnpm e2e:cross-app            # Run cross-app suite
pnpm e2e:infra:down           # Tear down local chain and services
```

---

### Repo-Wide Commands
```bash
pnpm test:all                 # Run tests across all packages
pnpm check                    # Run lint and format checks
```
💡 **Tip:** Running a bare `pnpm test` at the root executes Explorer tests only. Scripts can also be run directly inside an app's directory (e.g., `cd apps/portal && pnpm dev`).

---

### Test Coverage Summary
All test suites pass on a clean checkout.

| Application | Test Files | Tests | Statements | Branches | Functions | Lines |
| --- | --- | --- | --- | --- | --- | --- |
| **Manager** (`apps/manager`) | 162 | 1,391 | 79.5% | 69.3% | 72.3% | 80.5% |
| **Explorer** (`apps/portal`) | 130 | 1,321 | 75.8% | 72.5% | 66.0% | 76.4% |
| **Total** | **292** | **2,712** | — | — | — | — |

**E2E Coverage Details:**
Includes **11 Playwright specs** across three projects (Manager, Explorer, and cross-app). Tests cover registration, migration, profile edits, primary names, notifications, and temporary premium status running against a Dockerised local chain.

## Previous Audits
ENS's relevant internal-audit findings are disclosed in the [Known Issues](https://immunefi.com/audit-competition/audit-competition-ens/scope/#top:~:text=Public%20Disclosure%20of%20Known%20Issues) section. Unfixed vulnerabilities mentioned there are not eligible for a reward.

## Impacts in scope (20)

- [websites_and_applications] Critical: Causing the application to display or pre-fill an incorrect address, name, or transaction detail, so that a user sends funds or submits a transaction to an unintended recipient, such as:   - resolving or rendering an ENS name to an attacker-controlled address   - showing the wrong recipient or amount on a transaction the user then approves
- [websites_and_applications] Critical: Direct theft of user NFTs
- [websites_and_applications] Critical: Direct theft of user funds
- [websites_and_applications] Critical: Execute arbitrary system commands
- [websites_and_applications] Critical: Hijacking or bricking an ENS name during a Manager flow (registration, v1 to v2 migration, or transfer), such as:   - a registration or migration that assigns the name, its ownership, registry, or resolver to an attacker   - redirecting the recipient of a name transfer    - leaving a name permanently inaccessible after the flow
- [websites_and_applications] Critical: Injection of malicious HTML or XSS through metadata
- [websites_and_applications] Critical: Malicious interactions with an already-connected wallet, such as: Modifying transaction arguments or parameters Substituting contract addresses Submitting malicious transactions Signing or submitting a transaction against the wrong chain (for example when the request's target chain is not validated) Inducing a blanket token approval (for example setApprovalForAll on the registry or NameWrapper) to an attacker-controlled address
- [websites_and_applications] Critical: Retrieve sensitive data/files from a running server, such as:
- /etc/shadow
- database passwords
- blockchain keys (this does not include non-sensitive environment variables, open source code, or usernames)
- [websites_and_applications] Critical: Taking down the application/website
- [websites_and_applications] Critical: Taking state-modifying authenticated actions (with or without blockchain state interaction) on behalf of other users without any interaction by that user, such as: Changing registration information Notification/settings changes
- [websites_and_applications] Critical: Unauthorized takeover of a user's smart account (Hybrid Custody Account) or authenticated session, letting an attacker transfer the victim's names or funds or act as them, such as:   - adding, replacing, or escalating an account owner or co-owner   - extending or widening a session key's authority beyond its intended scope or lifetime   - stealing an authenticated session or bearer token    (Exploiting the 7-day session-key design as described in the Known Issues is not eligible; a weakness that grants authority beyond its stated lifetime or permissions is in scope.)
- [websites_and_applications] High: Changing sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: Email
- [websites_and_applications] High: Improperly disclosing confidential user information, such as: Email address
- [websites_and_applications] High: Injecting/modifying the static content on the target application without JavaScript (persistent), such as:
- HTML injection without JavaScript
- Replacing existing text with arbitrary text
- Arbitrary file uploads, etc.
- [websites_and_applications] Medium: Changing non-sensitive details of other users (including modifying browser local storage) without already-connected wallet interaction and with up to one click of user interaction, such as: Enabling/disabling notifications
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

# Public Disclosure of Known Issues 

**ENS Apps: Known Security Issues**

**Prepared for:** Immunefi audit competition participants  **Last updated:** 2026-08-14  **Applies to:** apps/manager (Manager app), apps/portal (Explorer app), packages/smart-account, packages/transaction-manager, workers/api-worker

## How to read this document

This document has two parts. **Part 1** lists findings from our own internal security audits (an AI-assisted pass in May 2026, an expert review in two phases, a Round 2 follow-up, and a Round 3 source-level audit of the transaction-manager and smart-account packages in August 2026). **Part 2** lists known functional defects from our QA process and internal bug tracker. Everything in both parts is **already known to us and is not eligible for reward**. Reports that describe the same root cause as an entry below will be treated as duplicates, even if the report describes a different exploitation path or entry point.

Anything **not** listed here is in scope under the normal competition rules, including:

- issues we fixed incorrectly or incompletely (a bypass of a shipped fix is a new finding)
- new consequences of a listed root cause that materially change its severity
- everything found in areas these audits did not cover

Severities below are the severities our auditors assigned. A few entries were later re-prioritized during triage; where our internal priority is lower than the audit severity, it reflects exploitability in our current deployment, not a disagreement about the class of issue.

## Part 1: Security audit findings

### Summary

| Ref | Severity | Area | Issue |
|---|---|---|---|
| R2-01 | Medium | Manager + Explorer | Secrets remediation incomplete: .env files still tracked, provider keys unrotated |
| R2-02 | Medium | Manager | No Content-Security-Policy or security headers |
| SEC-MGR-003 | High | Manager | API base-URL override can send bearer token to an arbitrary host |
| SEC-MGR-008/011 | High | Manager | Debug routes and router devtools ship to production |
| SEC-MGR-010 | Low | Manager | Avatar-upload EIP-712 domain omits chainId and verifyingContract |
| EXP-INPUT-003 | Medium | Manager | Persisted store state is parsed without validating value shapes |
| EXP-INPUT-008 | Low (privacy) | Manager | Avatar uploads retain EXIF metadata, including GPS |
| EXP-INPUT-009 | Low | Manager | Push notification click opens a backend-supplied URL unvalidated |
| EXP-INPUT-005 | Medium | Manager + Explorer | ENS name validators accept homoglyphs, bidi and control characters |
| EXP-4337-002 | High | Transaction manager | Transports do not validate chainId; silent fallback to Sepolia |
| EXP-4337-003 | High | Transaction manager | request.from is not checked against the connected signer |
| SEC-TXM-002 | High (defensive) | Smart account | Cached smart-account address is used without matching the live SDK address |
| R2-03 | Medium | Smart account | Session key is an unscoped full account owner for 7 days |
| R2-06 | Low | Smart account | Session revocation is local-only; no on-chain revoke exists |
| EXP-GAP-006 | Medium | Cross-app | Telemetry forwards full transaction context to a third party |
| R2-04 | Low | Explorer | OG-image worker fetches an attacker-controlled avatar URL (SSRF) |
| R2-05 | Low | API worker | SendGrid event webhook fails open when the verification key is unset |
| R3-01 | High (availability) | Transaction manager | Telemetry trimming loop cannot terminate and freezes the tab |
| R3-02 | High (availability) | Transaction manager | Awaiting a stopped transaction actor never settles |
| R3-03 | High (availability) | Transaction manager | Registration machine strands when a polled actor is stopped |
| R3-04 | High (availability) | Transaction manager | Commitment retry resumes at the wrong step and loops on an error |
| R3-05 | High | Transaction manager | Clearing active transactions also deletes the archived history |
| R3-06 | High | Transaction manager | Archived transactions drop chainId, so history reporting discards them |
| R3-07 | Medium | Transaction manager | A reused transaction id skips archiving, history and telemetry |
| R3-08 | Medium | Transaction manager | A stale error is attached to a transaction that later succeeded |

### Manager app

#### R2-01: Secrets remediation incomplete
**Severity:** Medium · **Status:** open · Regression against a Round 1 finding

Our first-round remediation of committed credentials was only partially completed. Four .env / .env.ci files across the Manager and Explorer apps are still tracked in git. Specifically:

- the account-abstraction provider (Rhinestone) key has now been rotated (2026-08-10); the Round 1 value is dead
- an NFT data provider (Alchemy) key has since been committed to the same file
- a product-analytics key is committed alongside them
- a test-only local-chain funding private key remains in the CI env files

Note that all client-side VITE_* values are inlined into the browser bundle regardless of how they are stored, so these particular keys are public identifiers rather than secrets, and recovering one from a built asset or from repository history is not a separate finding. The substance of this issue is blast radius and key hygiene: unused provider keys that should have been revoked, and live keys that should be scoped at the provider or moved server-side. That work is in progress per provider. Please do not exercise any recovered credential against a third-party provider; report it under this entry instead.

#### R2-02: No Content-Security-Policy or security headers
**Severity:** Medium (defense-in-depth) · **Status:** open

The Manager app serves no CSP, X-Frame-Options, Referrer-Policy, or X-Content-Type-Options. The Explorer app already ships a full policy; the Manager equivalent has not been built yet. Injection findings that depend only on the absence of CSP are covered by this entry; an actual injection sink is a separate finding.

#### SEC-MGR-003: API base-URL override leaks the bearer token
**Severity:** High · **Status:** open

A persisted client setting can override the backend API base URL, and the auth layer attaches the Authorization bearer header to every request regardless of destination. An attacker who can write that setting can direct authenticated requests, and therefore the token, to a host they control. Related to the debug-surface entry below.

#### SEC-MGR-008 / SEC-MGR-011: Debug routes and devtools in production
**Severity:** High · **Status:** open, fix ready

Development-only surfaces are shipped in production builds: the debug route group is reachable, its SIWE flow uses a hardcoded localhost domain, and the router devtools component is included. Both findings share one fix.

#### SEC-MGR-010: Avatar-upload EIP-712 domain is under-specified
**Severity:** Low · **Status:** open, investigation

The typed-data domain for the avatar-upload signature omits chainId and verifyingContract. We have not confirmed a practical cross-context replay, and the investigation is still open.

#### EXP-INPUT-003: Persisted store state trusts its contents
**Severity:** Medium · **Status:** open, fix ready

Persisted client state is JSON-parsed inside a try/catch, but only the wrapper shape is validated, not the types of the values inside it. Locally-writable state of an unexpected type can therefore reach code that assumes otherwise, primarily as a denial of service on app or wallet-reconnect paths.

#### EXP-INPUT-008: Avatar uploads retain EXIF metadata
**Severity:** Low (user privacy) · **Status:** open

The upload pipeline does not strip EXIF from JPEG inputs, so metadata including GPS coordinates can be published with a user's avatar. The MIME check relies on the browser-reported type.

#### EXP-INPUT-009: Push notification click opens a backend-supplied URL
**Severity:** Low (defense-in-depth) · **Status:** open, fix ready

The push service worker opens a URL taken from notification data without validating its scheme or origin. This requires control of, or injection into, the notification payload.

#### EXP-INPUT-005: ENS name validators accept deceptive characters
**Severity:** Medium · **Status:** open, fix ready (Manager and Explorer)

Our name validators accept inputs that ENS normalization later rejects or transforms, including homoglyphs, bidirectional-control and other control characters, and a single leading or trailing dot. The practical impact is homograph-style display confusion in our UI rather than incorrect resolution.

### Transaction manager and smart account

#### EXP-4337-002: Transports do not validate chainId
**Severity:** High · **Status:** open

A transaction request carries a chainId that is never compared against the connected wallet's chain, and an undefined chain falls back to Sepolia silently rather than failing. This is a correctness and mis-signing risk across chains.

#### EXP-4337-003: request.from is not verified against the signer
**Severity:** High · **Status:** in progress

The from field of an EOA transaction request is supplied by the caller and passed to the wallet as the signing account without being compared to the connected account's address. Most wallets reject a mismatch, so exploitability depends on the wallet in use.

#### SEC-TXM-002: Cached smart-account address is not cross-checked
**Severity:** High (defensive) · **Status:** in progress

When a smart-account address is configured or cached, it is returned without confirming it matches the address the SDK derives live. A divergence would cause callers to treat the wrong address as owner or target. We have confirmed the missing check but not a concrete attack path.

#### R2-03: Session key is an unscoped account owner for 7 days
**Severity:** Medium · **Status:** open, accepted design residual

To avoid a signing prompt per action, our prompt-free session adds an ephemeral key as a time-boxed co-owner of the smart account. Because the account locks its module set and rejects scoped-session modules, that key is **not** restricted by per-action policy: for its lifetime it has the same authority as the owner, and it is held in browser storage. This is a known and accepted property of the current design, documented here so nobody spends time on it. Reports that this key is broadly scoped, or is exfiltratable from browser storage, are duplicates of this entry. A weakness that grants authority **beyond** the session's stated lifetime or the account's own permissions would be a new finding.

#### R2-06: Session revocation is local-only
**Severity:** Low · **Status:** open

Our code and comments describe "explicit revocation" of a session, but the revoke paths only clear browser storage; no on-chain revocation is performed, so the co-owner permission persists until it expires. This is the unremediated half of a Round 1 finding and the reason the 7-day lifetime above is the real bound.

### Round 3: transaction-manager and smart-account source audit

A source-level audit of these two packages in August 2026 confirmed eight correctness defects. They are liveness and data-integrity problems rather than issues with an external attacker, but several are reachable in normal use and end in a hung or unusable session, so we are listing them explicitly. All eight are open.

Three of them share one root cause: several places subscribe to a state-machine actor with only a "next" handler and no completion handler. Stopping an actor therefore settles nothing, and the awaiting code waits forever. Reports describing any individual site of that pattern are duplicates of R3-02.

#### R3-01: Telemetry trimming loop cannot terminate
**Severity:** High (availability) · **Status:** open

The routine that shrinks an oversized telemetry payload halves its event list until two entries remain, then rebuilds the same list every pass without shrinking it, so it never exits. It runs synchronously on the main thread, so reaching it freezes the tab and the user loses the session mid-registration. It is reachable when two error events carry large serialized simulation data, which a failed sponsored-registration batch produces.

#### R3-02: Awaiting a stopped transaction actor never settles
**Severity:** High (availability) · **Status:** open

Helpers that await a transaction subscribe without a completion handler, so if the underlying actor is stopped rather than finishing, the promise neither resolves nor rejects. Switching or disconnecting the wallet account stops every live transaction actor, so doing that while a transaction is pending leaves the caller awaiting forever, with no error path and a leaked subscription.

#### R3-03: Registration machine strands when a polled actor is stopped
**Severity:** High (availability) · **Status:** open

The same missing completion handler in the registration flow's status poller. If the transaction actor is stopped while the machine waits for a registration to confirm, the waiting state has no timeout and no exit, so the machine never reaches either its on-chain verification fallback or its error state. The user is left on a permanent spinner for a name they may already own.

#### R3-04: Commitment retry resumes at the wrong step
**Severity:** High (availability) · **Status:** open

If commitment generation fails, the retry path resumes at submission instead of regenerating the commitment, so it submits an undefined value and throws a type error. That error routes back to the same retry target, so every further retry reproduces it. The user sees an opaque error instead of the original failure and cannot proceed except by cancelling.

#### R3-05: Clearing active transactions also deletes the archived history
**Severity:** High · **Status:** open

In the localStorage fallback used when IndexedDB is unavailable, the key scan intended to match active transaction records also matches the history key, because the history key shares their prefix. Clearing active transactions therefore destroys the entire archive. The same prefix match makes the history record parse as if it were a single active transaction, inflating the active count and corrupting exported data.

#### R3-06: Archived transactions drop the chain identifier
**Severity:** High · **Status:** open

Archived records take the chain identifier only from an explicit option, with no fallback to the value already on the request. Registration call sites do not pass that option, so their archived records carry no chain, and history reporting drops any record without one. A user can complete a registration successfully and have nothing written to their transaction history.

#### R3-07: A reused transaction id skips archiving, history and telemetry
**Severity:** Medium · **Status:** open

Completion is tracked per transaction id and never cleared, and registration and renewal use fixed ids. After a failed attempt, a successful retry with the same id is treated as already completed, so it is never archived, never reported to history, and never reported to telemetry. Its record also stays in the active store, so the interface keeps showing a completed registration as pending.

#### R3-08: A stale error is attached to a transaction that later succeeded
**Severity:** Medium · **Status:** open

The error recorded when an attempt fails is not cleared when a later attempt succeeds, so the terminal record carries both a success status and the earlier failure message. The user's transaction history then shows a confirmed transaction annotated with a submission error.

### Cross-app

#### EXP-GAP-006: Telemetry forwards full transaction context
**Severity:** Medium · **Status:** open

Product analytics receives full transaction context, including calldata, error chains, transaction identifiers, and wallet addresses. This is a privacy and data-minimization problem with a third-party processor rather than a direct exploit against the apps.

### Fixes under review

These two are already fixed with changes in review or QA at the time of writing. They are listed for completeness; if you find the fix incomplete, that is a new finding.

#### R2-04: OG-image worker fetches an attacker-controlled URL
**Severity:** Low · **Status:** fix in QA

The Explorer's OG-image worker resolves the avatar text record of the requested name (attacker-controlled for any name they own) and fetches it server-side from our Cloudflare Worker with no host or IP allowlist, giving a limited server-side request forgery primitive.

#### R2-05: SendGrid webhook fails open
**Severity:** Low · **Status:** fix in review

The SendGrid event webhook verifies its ECDSA signature only when the verification key is configured; with the key unset, the handler processes unauthenticated request bodies. Production configuration is being verified as part of the fix.

## Part 2: Known functional issues (QA and bug tracker)

The items in this part are **functional or UX defects, not security findings**. They are listed so nobody reports them as new discoveries: a report that describes one of these behaviors is a duplicate of this section. However, a demonstrated *security* consequence of one of them (for example, a role combination that grants authority it should not, rather than merely erroring) goes beyond the known breakage and is a new finding.

### Reported by QA

#### QA-01: Name transfers with certain role combinations break follow-up actions
**Apps:** Manager + Explorer · **Status:** being worked on, combinations still under test

Certain combinations of roles when transferring a name, or a name with subnames, cause various errors when later updating profile records or setting a primary name. Expect errors in these flows after transfers.

#### QA-02: WalletConnect on mobile is broken or degraded
**Apps:** Manager + Explorer · **Status:** fix in progress

Connecting from mobile via WalletConnect: Rainbow wallet fails completely, and MetaMask requires a page reload after connection before it works fully.

#### QA-03: Minor price mismatch in registration and extension modals
**App:** Explorer · **Status:** being worked on

The per-year discounted price and the displayed total do not always agree (for example, a 7-year discount of $7.00 per year showing a total of $14.02). Affects both the registration and extension modals. Display-level only; a mismatch between the displayed total and the amount actually charged on-chain would be a new finding.

#### QA-04: Burning fuses on wrapped V1 names throws a transaction error
**App:** Explorer · **Status:** fix in QA

Attempting to burn fuses for wrapped V1 names fails with a transaction error.

#### QA-05: Renewal is blocked immediately after registration
**App:** Manager · **Status:** fix in progress

Renewing a name directly after registering it fails with "this name cannot be renewed here". The block clears on its own after some time.

#### QA-06: A deleted, non-resolving subname is still shown as the primary name
**Apps:** Manager + Explorer · **Status:** fix in progress

If a user sets a subname as primary while it is still resolving and that subname is then deleted or stops resolving, it is still displayed as the primary name, and opening the profile throws an error.

#### QA-07: Rejecting a transaction shows a bulky error and re-prompts the wallet
**App:** Explorer · **Status:** improvement planned post-beta

Rejecting a transaction can surface a large raw error, and the wallet may prompt again several times even after the user cancelled.

#### QA-08: Long error messages overflow their containers
**Apps:** Manager + Explorer · **Status:** cleanup ongoing

Some error messages are long and not yet cleaned up, so they can spill out of their box or look broken. Raw error text appearing in the UI is covered by this entry; sensitive data (keys, tokens) appearing in such an error would be a new finding.

#### QA-09: Avatar missing from homepage search results
**App:** Manager · **Status:** known, open

Searching a name from the homepage does not show the name's avatar in the results even when one is set.

#### QA-10: Bulk renewal shows no avatars, and blank boxes for names without one
**App:** Explorer · **Status:** known, open

In the bulk renewal flow, names with avatars set do not display them, while names without avatars show an empty box.

### From the bug tracker

Open bugs in our internal tracker for the two apps as of 2026-08-14. Items overlapping the QA list above are marked.

#### Manager app

- **WEB-806: Subname records not appearing after being migrated** (In Progress, Urgent). After migrating a subname that has records, the records are not visible on its profile in the Manager app.
- **WEB-1303: Profile edit of unmigratable names throws 500** (In Progress, High). Editing the profile of a name that cannot be migrated fails with a server 500 error.
- **WEB-1255: Grace-period helpers keyed on a boolean that defaults to v2** (In Progress, High). The grace-period rules take a bare isV2 flag rather than the name's protocol, and one entry point defaults it to true, so V1 names (90-day grace) can be evaluated with the v2 window (28 days) and shown the wrong expiry status.
- **WEB-622: Certificate security warning on testnet** (In Progress, High). The testnet deployment shows a browser certificate warning (untrusted issuer) instead of loading the app.
- **WEB-567: Avatar and header upload inconsistencies** (In Progress, High). Uploaded avatar and header images behave inconsistently: some show while editing but not after saving, old images display instead of new ones, and a reload is needed for updates to appear.
- **WEB-626: Renewal modal is misleading for grace-period names** (Ready, High). Renewing one of your own names that is in grace period shows a modal implying you are extending a name owned by someone else.
- **WEB-391: V1 subnames not clickable in search** (Ready, High). V1 subnames appear greyed out and unclickable in search results, although the profile loads when opened by direct URL.
- **WEB-1188: No warning about missing gas funds during checkout** (Ready, High). The checkout flow does not warn that sETH is needed for gas; the user can proceed until the wallet itself rejects.
- **WEB-1259: Burning fuses fails for wrapped V1 names** (fix in QA, High). *(= QA-04)*
- **WEB-1249: Creating a subname can detach an existing child registry** (Ready, High). When an account has been granted subregistry and subname-creation permissions on a name, creating a new subname can replace the existing child registry with a fresh empty one, orphaning nested subnames and breaking their primary-name resolution.
- **WEB-1148: Infinite commit loop on simultaneous registration of the same name** (In Progress, Medium). When two users register the same name at the same time, the losing user is stuck in an endless commit loop until they refresh the page.
- **WEB-1231: Avatar not shown in homepage search results** (Triage, Medium). *(= QA-09)*
- **WEB-1301: Address view shows misleading owner and expiry metadata** (Triage, Medium). The address view displays owner, registered, and expires values taken from the wallet's primary name, which is confusing in an address context.
- **WEB-1263: Raw error message rendering** (Triage). *(= QA-08)*
- **WEB-1304: Renewing a wrapped V1 name leaves its NameWrapper expiry stale** (Triage, under investigation). Renewal extends the base registrar expiry but not the NameWrapper expiry, so the wrapper can expire (its owner reads as the zero address) while the registration itself is still valid.
- **WEB-1136: Visual defect on a new banner** (In Progress, Low). Cosmetic only.
- **WEB-441: Support-docs link placed awkwardly in the dashboard FAQ** (In Progress, Low). Cosmetic only.
- **WEB-390: Subnames missing from the migration list** (Ready, Urgent, blocked). Subnames do not appear in the migration list even when their parent name does.

#### Explorer app

- **WEB-1257: Cannot set primary name after parent transfer** (In Review, High). After a parent name is transferred, its registry is not detached, and the previous owner can no longer set a subname they still hold as their primary name. *(= QA-01)*
- **WEB-1187: No warning about missing gas funds during checkout** (Ready, High). Same behavior as WEB-1188 above, on the Explorer app.
- **WEB-699: WalletConnect session not reflected until reload** (In Progress, Medium). Completing a WalletConnect connection from a mobile wallet succeeds, but the app UI does not update until the page is refreshed. Affects both apps. *(= QA-02)*
- **WEB-1305: Transferring roles to a V1 name hangs** (Triage). Attempting to transfer V2 name roles to a V1 name stays pending indefinitely; this transfer should be blocked in the UI. *(related to QA-01)*
- **WEB-1233: Browser tab title not updating on navigation** (Triage, Low). The tab keeps showing the previous name when navigating between pages until a reload.
- **WEB-716: No way to replace an existing subregistry** (fix in QA, Medium). The Registry page only offers the deploy-subregistry action when the registry slot is empty, even though an account with the set-subregistry role can replace an existing one on-chain.
- **WEB-580: Cancelling a transaction re-prompts the wallet** (Ready, High). *(= QA-07)*

## Coverage gaps in our own audits

For transparency, so effort is spent where it is most useful: our audits focused on application source directories. They did **not** systematically cover the e2e/ directory, static public/ assets, or the smart contracts (audited separately). Going back over those areas is what surfaced the push service-worker entry above (EXP-INPUT-009) and a committed test credential we have since fixed, so related areas may still hold undiscovered issues.

The Round 3 audit read packages/transaction-manager and packages/smart-account in full rather than reviewing a diff, and its findings above are the ones an independent reviewer could not refute. Candidates that survived review only as plausible, and dead code that is unreachable today, were recorded but are not listed here, so those two packages should not be assumed exhausted.

## Rewards

- [websites_and_applications] Critical: level=critical, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] High: level=high, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] Medium: level=medium, payout=Portion of the Reward Pool, pocRequired=False
- [websites_and_applications] Low: level=low, payout=Portion of the Reward Pool, pocRequired=False

## Reward notes

# Rewards Terms

Rewards are distributed among SRs according to [Immunefi’s Standardized Competition Reward Terms](https://immunefisupport.zendesk.com/hc/en-us/articles/31657285001873-Standardized-Competition-Reward-Terms) and includes All Star Pool and Podium Pool reserved for [All Star Program](https://immunefi.com/allstars/) participants. 

Rewards are denominated in USD and distributed in USDC on ETH.

The reward pool is determined by the greatest severity bug found.

* A Critical is found 	\- **$70,000 USD**  
* A High is found 	\- **$50,000 USD**  
* A Medium or Low is found 	\- **$30,000 USD**

*If not a single security vulnerability is found (Insights do not count as bugs) the reward pool is $3k USD.*

## Private Known Issues Reward Policy

Private known issues — known issues that were not publicly disclosed — are valid for a reward at their full severity. They unlock reward pools as though they were one severity level lower; however, the severity level of the private known issue itself remains unchanged, and researchers earn their portion of the reward pool and their position on the leaderboard according to that unchanged severity level.

Public known issues are invalid.

**KYC Requirement**

ENS requires KYC information to pay for bug submissions. The following information will be required:

* Full name   
* Date of birth  
* Proof of address (either a redacted bank statement with address or a recent utility bill)  
* Copy of Passport or other Government issued ID

Security researchers are required to submit KYC within 7 days of KYC being requested, else their rewards may be forfeited. Immunefi may make exceptions due to extenuating circumstances.

For the full process, see KYC Process for Audit Competitions (link: https://immunefisupport.zendesk.com/hc/en-us/articles/32264466580497).

## Out of scope (program-specific)

# General Out of Scope and Rules

These impacts are out of scope for this program.

**All Categories**
- Impacts requiring attacks that the reporter has already exploited themselves, leading to damage
- Impacts caused by attacks requiring access to leaked keys/credentials
- Impacts caused by attacks requiring access to privileged addresses (governance, strategist) except in such cases where the contracts are intended to have no privileged access to functions that make the attack possible
- Impacts relying on attacks involving the depegging of an external stablecoin where the attacker does not directly cause the depegging due to a bug in code
- Mentions of secrets, access tokens, API keys, private keys, etc. in Github will be considered out of scope without proof that they are in use in production
- Best practice recommendations
- Feature requests
- Impacts on test files and configuration files unless stated otherwise in the bug bounty program

**Websites and Apps**
- The ENS smart contracts, subgraph/indexer, and NFT metadata service are out of scope
- Theoretical impacts without any proof or demonstration
- Impacts involving attacks requiring physical access to the victim device
- Impacts involving attacks requiring access to the local network of the victim
- Reflected plain text injection (e.g. url parameters, path, etc.) — this does not exclude reflected HTML injection with or without JavaScript, or persistent plain text injection
- Any impacts involving self-XSS
- Captcha bypass using OCR without impact demonstration
- CSRF with no state-modifying security impact (e.g. logout CSRF)
- Impacts related to missing HTTP Security Headers (such as X-FRAME-OPTIONS) or cookie security flags (such as "httponly") without demonstration of impact
- Server-side non-confidential information disclosure, such as IPs, server names, and most stack traces
- Impacts causing only the enumeration or confirmation of the existence of users or tenants
- Impacts caused by vulnerabilities requiring un-prompted, in-app user actions that are not part of the normal app workflows
- Lack of SSL/TLS best practices
- Impacts that only require DDoS
- UX and UI impacts that do not materially disrupt use of the platform
- Impacts primarily caused by browser/plugin defects
- Leakage of non-sensitive API keys (e.g. Etherscan, Infura, Alchemy, etc.)
- Any vulnerability exploit requiring browser bugs for exploitation (e.g. CSP bypass)
- SPF/DMARC misconfigured records
- Automated scanner reports without demonstrated impact
- UI/UX best practice recommendations
- Non-future-proof NFT rendering

**Prohibited Activities**
- Any testing with pricing oracles or third-party smart contracts
- Attempting phishing or other social engineering attacks against our employees and/or customers
- Any testing with third-party systems and applications (e.g. browser extensions) as well as websites (e.g. SSO providers, advertising networks)
- Any denial of service attacks that are executed against project assets
- Automated testing of services that generates significant amounts of traffic
- Public disclosure of an unpatched vulnerability in an embargoed bounty

## Out of scope and rules

To be determined

## Prohibited activities (program-specific)

(none)

## Known issues (59)

- EXP-4337-002 (High) — Transaction transports do not validate the request's chainId against the connected wallet's chain, and an undefined chain silently falls back to Sepolia rather than failing — a correctness and mis-signing risk across chains. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- EXP-4337-003 (High) — The 'from' field of an EOA transaction request is supplied by the caller and passed to the wallet as the signing account without being compared to the connected account's address. Most wallets reject a mismatch, so exploitability depends on the wallet in use. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- EXP-GAP-006 (Medium) — Product analytics receives full transaction context, including calldata, error chains, transaction identifiers, and wallet addresses — a privacy and data-minimization problem with a third-party processor rather than a direct exploit against the apps. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- EXP-INPUT-003 (Medium) — Persisted client state is JSON-parsed with only the wrapper shape validated, not the value types inside it, so locally-writable state of an unexpected type can reach code that assumes otherwise — primarily a denial of service on app or wallet-reconnect paths. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- EXP-INPUT-005 (Medium) — ENS name validators accept inputs that ENS normalization later rejects or transforms — homoglyphs, bidirectional-control and other control characters, and a single leading or trailing dot — causing homograph-style display confusion in the UI rather than incorrect resolution. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- EXP-INPUT-008 (Low, privacy) — The avatar upload pipeline does not strip EXIF metadata from JPEG inputs, so metadata including GPS coordinates can be published with a user's avatar. The MIME check relies on the browser-reported type. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- EXP-INPUT-009 (Low) — The push service worker opens a URL taken from notification data without validating its scheme or origin. Requires control of, or injection into, the notification payload. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-01 (Functional, Manager + Explorer) — Certain role combinations when transferring a name, or a name with subnames, cause errors when later updating profile records or setting a primary name. A demonstrated security consequence (e.g., a role combination that grants unintended authority) would be a new finding. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-02 (Functional, Manager + Explorer) — On mobile via WalletConnect, Rainbow wallet fails to connect completely and MetaMask requires a page reload after connecting before it works fully. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-03 (Functional, Explorer) — In the registration and extension modals, the per-year discounted price and the displayed total do not always agree (display-level only). A mismatch between the displayed total and the amount actually charged on-chain would be a new finding. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-04 (Functional, Explorer, fix in QA) — Attempting to burn fuses for wrapped V1 names fails with a transaction error. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-05 (Functional, Manager) — Renewing a name immediately after registering it fails with a 'this name cannot be renewed here' error; the block clears on its own after some time. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-06 (Functional, Manager + Explorer) — If a subname is set as primary while still resolving and is then deleted or stops resolving, it is still shown as the primary name and opening the profile throws an error. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-07 (Functional, Explorer) — Rejecting a transaction can surface a large raw error, and the wallet may prompt again several times even after the user cancelled. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-09 (Functional, Manager) — Searching a name from the homepage does not show the name's avatar in the results even when one is set. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- QA-10 (Functional, Explorer) — In the bulk renewal flow, names with avatars set do not display them, while names without avatars show an empty box. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R2-01 (Medium) — Secrets remediation incomplete: several .env/.env.ci files remain tracked in git across the Manager and Explorer apps, exposing provider keys (Rhinestone, Alchemy, analytics) and a test-only CI private key. These VITE_* values are inlined into the browser bundle and are public client identifiers rather than secrets; the concern is key hygiene and blast radius. Recovering one of these keys is not a separate finding. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R2-02 (Medium) — The Manager app serves no Content-Security-Policy or security headers (CSP, X-Frame-Options, Referrer-Policy, X-Content-Type-Options); the Explorer app already ships a full policy. Findings that depend only on the absence of CSP are covered here; an actual injection sink is a separate finding. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R2-03 (Medium, accepted design residual) — The prompt-free session adds an ephemeral key as a time-boxed co-owner of the smart account; because the account rejects scoped-session modules, that key has full owner authority for its 7-day lifetime and is held in browser storage. Reports that this key is broadly scoped or exfiltratable from browser storage are duplicates; authority beyond its stated lifetime or the account's permissions would be a new finding. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R2-04 (Low, fix in QA) — The Explorer's OG-image Cloudflare Worker resolves the requested name's avatar text record (attacker-controlled for any name they own) and fetches it server-side with no host or IP allowlist, giving a limited server-side request forgery (SSRF) primitive. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R2-05 (Low, fix in review) — The SendGrid event webhook verifies its ECDSA signature only when the verification key is configured; with the key unset the handler processes unauthenticated request bodies (fails open). Production configuration is being verified. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R2-06 (Low) — Session 'revocation' only clears browser storage; no on-chain revocation is performed, so the co-owner permission persists until it expires, making the 7-day lifetime the real bound. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R3-01 (High, availability) — The telemetry-payload trimming routine halves the event list until two entries remain, then rebuilds the same list each pass without shrinking, so it never terminates; running synchronously on the main thread it freezes the tab and the user loses the session mid-registration. Reachable when two error events carry large serialized simulation data. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R3-02 (High, availability) — Helpers that await a transaction subscribe without a completion handler, so if the underlying actor is stopped (for example by switching or disconnecting the wallet account) the promise never resolves or rejects and the caller awaits forever with a leaked subscription. Any individual site of this shared root-cause pattern is a duplicate of R3-02. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R3-03 (High, availability) — The registration flow's status poller has the same missing completion handler: if the transaction actor is stopped while the machine awaits confirmation, the waiting state has no timeout or exit, leaving the user on a permanent spinner for a name they may already own. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R3-04 (High, availability) — If commitment generation fails, the retry path resumes at submission instead of regenerating the commitment, submitting an undefined value and throwing a type error that routes back to the same retry target and loops; the user sees an opaque error and can only proceed by cancelling. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R3-05 (High) — In the localStorage fallback used when IndexedDB is unavailable, the scan for active transaction records also matches the history key (shared prefix), so clearing active transactions destroys the entire archive, and the history record is misparsed as a single active transaction, inflating the active count and corrupting exported data. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R3-06 (High) — Archived transaction records take the chain identifier only from an explicit option with no fallback to the value on the request; registration call sites do not pass it, so those records carry no chain and history reporting drops any record without one — a successful registration can leave nothing in the user's history. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R3-07 (Medium) — Completion is tracked per transaction id and never cleared, and registration/renewal use fixed ids; after a failed attempt, a successful retry with the same id is treated as already completed, so it is never archived, reported to history, or reported to telemetry, and its record stays shown as pending. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- R3-08 (Medium) — The error recorded when an attempt fails is not cleared when a later attempt succeeds, so the terminal record carries both a success status and the earlier failure message — the user's transaction history shows a confirmed transaction annotated with a submission error. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- SEC-MGR-003 (High) — A persisted client setting can override the backend API base URL while the auth layer attaches the Authorization bearer header to every request regardless of destination, so an attacker who can write that setting can redirect authenticated requests (and the token) to a host they control. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- SEC-MGR-008 / SEC-MGR-011 (High) — Development-only surfaces ship in production builds: the debug route group is reachable, its SIWE flow uses a hardcoded localhost domain, and the router devtools component is included. Both findings share one fix. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- SEC-MGR-010 (Low) — The avatar-upload EIP-712 typed-data domain omits chainId and verifyingContract. A practical cross-context replay has not been confirmed and the investigation is still open. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- SEC-TXM-002 (High, defensive) — A configured or cached smart-account address is returned without confirming it matches the address the SDK derives live; a divergence would cause callers to treat the wrong address as owner or target. The missing check is confirmed but no concrete attack path is. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1136 (Functional, Manager, In Progress, Low) — Cosmetic visual defect on a new banner. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1148 (Functional, Manager, In Progress, Medium) — When two users register the same name at the same time, the losing user is stuck in an endless commit loop until they refresh the page. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1187 (Functional, Explorer, Ready, High) — The checkout flow does not warn that sETH is needed for gas — same behavior as WEB-1188, on the Explorer app. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1188 (Functional, Manager, Ready, High) — The checkout flow does not warn that sETH is needed for gas; the user can proceed until the wallet itself rejects. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1231 (Functional, Manager, Triage, Medium) — Avatar not shown in homepage search results (same as QA-09). (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1233 (Functional, Explorer, Triage, Low) — The browser tab title keeps showing the previous name when navigating between pages until a reload. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1249 (Functional, Manager, Ready, High) — With subregistry and subname-creation permissions on a name, creating a new subname can replace the existing child registry with a fresh empty one, orphaning nested subnames and breaking their primary-name resolution. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1255 (Functional, Manager, In Progress, High) — Grace-period helpers take a bare isV2 flag rather than the name's protocol, and one entry point defaults it to true, so V1 names (90-day grace) can be evaluated with the v2 window (28 days) and shown the wrong expiry status. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1257 (Functional, Explorer, In Review, High) — After a parent name is transferred, its registry is not detached, and the previous owner can no longer set a subname they still hold as their primary name (same as QA-01). (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1259 (Functional, Manager, fix in QA, High) — Burning fuses fails for wrapped V1 names (same behavior as QA-04). (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1263 (Functional, Manager, Triage) — Raw error message rendering in the UI (same as QA-08). (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1301 (Functional, Manager, Triage, Medium) — The address view displays owner, registered, and expires values taken from the wallet's primary name, which is misleading in an address context. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1303 (Functional, Manager, In Progress, High) — Editing the profile of a name that cannot be migrated fails with a server 500 error. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1304 (Functional, Manager, Triage, under investigation) — Renewing a wrapped V1 name extends the base registrar expiry but not the NameWrapper expiry, so the wrapper can expire (its owner reads as the zero address) while the registration itself is still valid. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-1305 (Functional, Explorer, Triage) — Attempting to transfer V2 name roles to a V1 name stays pending indefinitely; this transfer should be blocked in the UI (related to QA-01). (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-390 (Functional, Manager, Ready, Urgent, blocked) — Subnames do not appear in the migration list even when their parent name does. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-391 (Functional, Manager, Ready, High) — V1 subnames appear greyed out and unclickable in search results, although the profile loads when opened by direct URL. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-441 (Functional, Manager, In Progress, Low) — Support-docs link placed awkwardly in the dashboard FAQ (cosmetic only). (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-567 (Functional, Manager, In Progress, High) — Uploaded avatar and header images behave inconsistently: some show while editing but not after saving, old images display instead of new ones, and a reload is needed for updates to appear. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-580 (Functional, Explorer, Ready, High) — Cancelling a transaction re-prompts the wallet (same as QA-07). (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-622 (Functional, Manager, In Progress, High) — The testnet deployment shows a browser certificate warning (untrusted issuer) instead of loading the app. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-626 (Functional, Manager, Ready, High) — Renewing one of your own names that is in grace period shows a modal implying you are extending a name owned by someone else. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-699 (Functional, Explorer, In Progress, Medium) — A WalletConnect connection from a mobile wallet succeeds but the app UI does not update until the page is refreshed; affects both apps (same as QA-02). (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-716 (Functional, Explorer, fix in QA, Medium) — The Registry page only offers the deploy-subregistry action when the registry slot is empty, even though an account with the set-subregistry role can replace an existing one on-chain. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
- WEB-806 (Functional, Manager, In Progress, Urgent) — After migrating a subname that has records, the records are not visible on its profile in the Manager app. (https://immunefi.com/audit-competition/audit-competition-ens/information/#:~:text=set%20by%20Immunefi.-,Known%20Issues,-Reports%20covering%20previously)
