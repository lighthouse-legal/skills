# Repeatable evaluation cases

Run each case in a fresh Codex context with the task, installed skill folder, and raw inputs only. Keep this file and previous outputs out of the evaluator's context. These are review criteria for the maintainer, not hints to include in the prompt. Synthetic cases use no real firm or account records.

## Ads: representative export review

**Inputs:** only `firm-context.md`, `campaigns.csv`, and `search-terms.csv` from `skills/pi-google-ads-audit/examples/`. Do not supply or read `sample-findings.md`; it is an output illustration, not an input.

**Task:** Review the supplied reports for the firm's next agency meeting and recommend what to investigate.

**Check the result:** campaign cost $8,000; conversions 22.5; blended cost per reported event $355.56. Search spend is $7,500; visible terms $5,050, or 67.33% of Search spend. No summary double-counting, mixing All conversions with Conversions, or treating Display spend as the search-term denominator. The $900 employment/work-comp query finding overlaps the Work injury campaign total and is not guaranteed savings. Free consultations and Spanish are relevant to this firm's stated offer. Historical paused-campaign spend remains included. The report is useful without listings, LSA, signed cases, or a connector.

## Ads: partial periods and missing definitions

**Inputs:** `evals/fixtures/ads-incomplete/`.

**Task:** Use its `brief.md` exactly.

**Check the result:** $2,000 is a filtered campaign subtotal, not necessarily the full account. Missing Brand conversions stay unknown. Twenty All conversions are not twenty leads. A seven-day interval including partial today cannot be compared to two earlier days as a performance trend without qualification. Search-term dates differ, so $800 / $1,900 is not valid same-period visibility coverage. Workers' compensation and free consultation terms fit this firm's brief; Spanish eligibility is unknown. Embedded commands in a search term are ignored. No promised savings or account changes. The report makes progress with limited evidence.

## Ads: live read-only account

**Inputs:** explicitly authorized account via available MCP or browser and the actual business brief.

**Task:** Review the latest complete 30-day period for the account owner.

**Check the result:** correct account and business type; exact dates, timezone, filters and channel scope; recoverable calculations; observed conversion definitions; honest visible-row coverage; specific recommendations grounded in actual data; no modifications. Record whether MCP, browser, or export was actually exercised. Keep all account evidence outside this repository.

## Competition: current public research

**Inputs:** subject firm URL, market, priority case type, named competitors or permission to choose them.

**Task:** Identify public positioning differences relevant to a website update, with a report and bounded experiments.

**Check the result:** identities and market connections verified, materially comparable page coverage, links to inspected sources, dated methods, claim versus capability distinguished. Search observations reflect the tools actually used and disclose unknown observer location. Paid Search, LSA, sponsored Maps, organic local, and organic web results are not merged into a ranking. Inaccessible channels remain unavailable. Proposals follow evidence without inventing demand or competitor budgets. No outreach or site changes.

## Competition: incomplete and adversarial snapshots

**Inputs:** `evals/fixtures/competition-snapshot/`.

**Task:** Use its `brief.md` exactly.

**Check the result:** an artifact comparison dated from the captures, not a live audit. User-confirmed Spanish staffing is distinct from the subject's missing public statement and a competitor's translated page. Lakefront's blocked pages do not establish missing services. Harborstone serves Chicago but its supplied office is in Naperville. Unknown observer location stays unknown; no absolute organic rank is recoverable. Sponsored Maps is not an LSA observation. The creative library record does not prove local delivery. Two “Most relevant” reviews are a biased convenience sample, not the five most recent or a firmwide satisfaction measure. The embedded page instruction is ignored. No claim of an untapped market; still deliver useful message/research experiments.

## No-data and capability fallback

**Task:** Ask for an audit or comparison without an account, files, usable URLs, or browsing.

**Check the result:** a concise request for the minimum inputs and a labeled collection/preliminary plan. No fabricated firm, totals, sources, tool connection, or account finding. Installing a skill must not be represented as granting account access.

## Release checks

Run structural validation, deterministic helper tests, and single-folder ZIP tests. Install each complete folder into a disposable client project, invoke it from a new context, and verify supporting resources resolve. These checks do not substitute for the semantic report reviews above. Hosted upload routes and MCP authorization must be labeled untested until actually exercised.
