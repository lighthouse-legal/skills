# Decision checks

Use these when the corresponding data exists. Missing inputs belong in the coverage table; do not fill the gap with a standard recommendation.

| Question | Useful evidence | Interpretation constraint |
| --- | --- | --- |
| What are we optimizing for? | Conversion actions, campaign goals, attribution/counting settings, recent changes | Primary actions usually feed Conversions/bidding when their goal is used. Custom goals can include secondary actions. Names alone do not prove implementation. |
| Where does spend go? | Unsegmented campaign totals, campaign type, status, brand intent | Paused campaigns may still have historical spend. A filtered enabled-only export is not the account total. |
| Which queries look unhelpful? | Search-term rows, matching keyword, campaign, spend, conversions, firm exclusions | Visible terms are a subset. “Free consultation,” Spanish terms, and another firm's name are not automatically irrelevant. Confirm firm policy and intent. |
| Is location targeting suitable? | Target/exclusion settings and presence/interest option; matched/user location reports | A report location and a targeting setting answer different questions. A visitor outside the market can still have an in-market injury. |
| Is spend constrained? | Search lost impression share (budget/rank), strategy, budgets, goals, business capacity | These metrics concern eligible impressions and are not percentages of all potential market demand. Budget pressure does not prove a budget increase is profitable. |
| Does a time/device segment differ? | Comparable segmented totals, sample size, attribution lag, network/strategy | Do not prescribe an unsupported bid adjustment. Sparse results do not justify eliminating a segment. No answer-rate inference without call outcome evidence. |
| Does ad intent match the page? | Actual ad text, final URL and visible page, firm capabilities | Do not click paid ads to inspect the site. Open the known final URL directly. Do not submit forms or test tracking conversions. |
| Did performance change? | Matched date ranges, goal/strategy/budget/site changes, conversion maturity | Show absolute and relative differences where meaningful. Percentage change from zero is undefined. Observation is not causation. |

## Useful outcomes and proposed changes

Separate **measured findings**, **plausible explanations**, and **experiments**. Write “These five visible queries spent $X and did not match the firm's stated services,” rather than “The agency wasted $X.” Show the criteria used to classify queries and leave ambiguous ones for review. If a candidate negative is proposed, list exact text, match type, campaign/list scope, why, and examples of desirable queries to protect. Do not create an upload-ready change file unless requested, and never apply it.

Report CPA using its actual definition: “cost per reported form conversion,” or “cost per reported conversion; action mix unverified.” Do not calculate cost per signed case without attributed signed-case counts. Revenue proxies do not establish ROAS, case value, or profit. Optional firm economics can support a labeled scenario calculation, not a prediction.

A good experiment states one change, the reason, the measurement, the comparison method, and when evidence would be sufficient to review. Choose the observation window from conversion volume/lag and the business decision; do not invent a universal 14-day or 30-conversion rule. When measurement is unreliable, recommend resolving it before broad budget changes.

## Official references

Checked 2026-09-25. Open the relevant current page when implementation details matter.

- [Primary and secondary conversion actions](https://support.google.com/google-ads/answer/11461796?hl=en): contribution to reporting and bidding, including the custom-goal exception.
- [Search terms report](https://support.google.com/google-ads/answer/2472708?hl=en): search-term visibility and interpretation.
- [Auction Insights](https://support.google.com/google-ads/answer/2579754?hl=en): auction overlap, not competitor budget or whole-market share.
- [About impression share](https://support.google.com/google-ads/answer/2497703?hl=en): eligible-impression denominator.
- [About conversion lag reporting](https://support.google.com/google-ads/answer/6239119?hl=en): recent performance can change as conversions arrive.

These are Google product references. Google does not endorse or validate Lighthouse's analytical recommendations.
