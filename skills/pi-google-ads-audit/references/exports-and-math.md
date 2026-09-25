# Exports and reproducible arithmetic

## Ask for the smallest useful evidence set

Start with a campaign performance CSV and a description/screenshot of conversion actions. Add search terms when available. Use Google Ads' table download control with the chosen date range and filters; do not ask for a client list or call transcripts. The exported files are supplied to the user's chosen AI service, whose data controls apply. Keep identifiers out of public issues and example reports.

| Report | Useful columns / accompanying context |
| --- | --- |
| Campaigns | Campaign ID/name, status, type, cost, clicks, impressions, Conversions; All conversions separately if useful. Date range, currency, account time zone, status/campaign/network filters. |
| Search terms | Search term, campaign and ad-group IDs/names, matching keyword if available, cost, clicks, Conversions. Same dates and scope as the campaign denominator. |
| Conversion definitions | Action name and purpose, primary/secondary, source, counting, goals used by campaigns, known lag. A written description is sufficient for a preliminary audit. |
| Optional detail | Devices, networks, geographic settings, search impression share/lost share, changes, previous comparable period. Ask only for what would change the decision. |

The campaign file and search-term file describe overlapping spend. Do not concatenate them. A campaign's daily budget is a setting, not its actual daily spend. Names may repeat across accounts/campaigns; retain IDs privately where joins require them.

## Bundled local helper

Python 3.10+; standard library only. From the installed skill directory:

```sh
python3 scripts/summarize_ads_csv.py examples/campaigns.csv --currency USD
```

With a real export, write results to a private destination outside the public repository:

```sh
python3 scripts/summarize_ads_csv.py /path/to/campaigns.csv \
  --currency USD --output /path/to/private/campaign-summary.json
```

The helper never makes a network request and never changes the input. It refuses to overwrite an existing output file. Its output includes original cell text, so the output is as private as the input.

It accepts English headers with common Google aliases (`Cost`, `Clicks`, `Impr.`, `Conversions`, `All conv.`) and flat API-style `metrics.cost_micros` headers. It locates a header after up to 29 preamble rows and recognizes comma, tab, or semicolon delimiters; UTF-8 and BOM-marked UTF-16 are supported. For decimal-comma exports, pass `--number-format eu`; ambiguous numbers such as `1,234` require checking the export's locale. `--delimiter tab`/`comma`/`semicolon` resolves delimiter ambiguity. It does not infer currency from a dollar sign; pass the actual account currency.

Summary rows with a non-metric label of `Total` or `Total: …` are preserved separately, never added to detail totals. Check those excluded rows: a genuine campaign or query named exactly `Total` or starting `Total:` needs manual disambiguation. Null/dash values remain unknown. Cost in micros is converted once; fractional conversions are preserved. Numbers are emitted as decimal strings to avoid floating-point rounding. Ratios are recomputed from totals; zero-denominator ratios are null. CTR is clicks divided by impressions. The helper deliberately does not compute Google's cross-channel conversion rate because its interaction denominator can differ from clicks.

It rejects mixed currencies, duplicate headers, identical detail rows, conversion-action segmented cost tables, unsupported numeric formats, and malformed rows. It does **not** prove the report is unfiltered, verify date coverage, detect every overlapping row grain, classify query intent, or reconcile differently scoped summary rows. Inspect its warnings and reconcile those yourself. If it rejects a legitimate unsupported export, preserve the original, explain the limitation, and normalize a private copy explicitly or calculate in the host's code tool. Do not silently drop problematic rows or turn missing values into zero.

## Reconciliation rules

1. Record source file, report scope, exact dates, currency, time zone, and row grain. If any are unknown, say so.
2. Keep each report separate. Compare campaign detail totals with the matching reported total. Investigate differences from filters, hidden/removed campaigns, pagination, segments, or excluded terms.
3. Cost per reported conversion = total cost / total reported conversions, only when both cover the same scope and the denominator is positive. Never average row CPAs.
4. Search-term visibility by spend = visible search-term detail cost / matching campaign cost. Label the unseen remainder; it is not automatically wasted spend. Do not use an all-channel denominator for a Search-only file.
5. For period changes, use equal/comparable inclusive periods and consistent conversion definitions. Keep today's partial data out of a complete-period comparison. Prefer matched weekdays for short windows, or disclose a different weekday mix; equal length alone does not remove that difference. A zero baseline gives an absolute change and an undefined percentage change.
6. Tie each conclusion back to a source row/view and formula. Use reasonable display rounding only after calculation. Never report a missing metric as measured zero.
