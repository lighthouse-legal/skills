# Optional advertising exports

Read this only when the user supplies Auction Insights or related advertising data. It enriches a public report; missing account data is never a blocker. Do not request a password or connect/change an account for this workflow.

## Establish the scope before interpreting

Record the supplied filename, date received, reporting period and timezone, campaign type/network, campaign/ad-group/keyword scope, filters, device/time segments, and the subject firm's row. If a relevant field is missing, say so and ask only what is needed to interpret the export. Continue independent public research while awaiting clarification. Preserve the original values; separate report date from website access dates.

An Auction Insights export concerns overlapping ad auctions under that account's settings and reporting scope. It is not a list of every competitor or a measure of the local market. Google describes its eligibility and metric definitions in [Use auction insights to compare performance](https://support.google.com/google-ads/answer/2579754?hl=en), checked September 25, 2026. Check current definitions if the export uses unfamiliar columns.

| Metric | Interpretation to preserve |
| --- | --- |
| Impression share | Impressions relative to estimated eligible impressions within the report's scope; not all local searches |
| Overlap rate | How often another advertiser appeared when the subject's ad appeared |
| Position above rate | How often the other advertiser was above the subject when both appeared |
| Outranking share | The subject's relative auction outcome, including times its ad showed and the other's did not |
| Top / absolute top rates | Where observed ad impressions appeared under the platform's metric definitions; not traffic or market share |

Competitor eligibility can differ from the subject's. Google's reporting has activity thresholds, so missing rows or unavailable metrics must not be interpreted as zero. Keep Search, Shopping, and Performance Max segments identifiable. Do not combine incompatible channel data into one competitor rank.

## Handle the file faithfully

- Keep `<10%` or other censored values as bounds, not exact numbers. A dash, blank, or suppressed value is unknown, not zero.
- Preserve segment keys. Do not sum percentages, take an unweighted average of percentage rows, or double-count an aggregate row alongside its components. If denominators needed for a valid calculation are absent, present segments separately.
- Verify which firm/domain belongs to which row. A domain or payer label does not prove ownership of every similarly named firm.
- For comparisons across periods, note changes in campaign scope, targeting, filters, and device mix. Do not attribute a change to a competitor action without additional evidence.
- Refer to the source rows/cells for all derived figures and show any calculations. If the environment cannot read the file, request a readable CSV/table and report that limit.

Do not infer competitor spend, CAC, signed cases, profitability, or demand from these metrics. Third-party estimates supplied by the user stay explicitly attributed estimates with date, methodology, geography, and limitations; do not promote them to actual business results. The firm's own supplied costs may be described within their documented scope, but they do not reveal a competitor's economics.

Keep private exports and account identifiers out of a public report by default. Use redacted summaries when appropriate and identify the source as a private supplied artifact. No raw export or result belongs in this public skill repository.
