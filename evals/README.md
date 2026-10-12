# Evaluation record

These skills are tested as complete workflows, alongside automated checks for the calculation helper and distribution packages. Evaluation uses fresh Codex contexts given only the task, skill, and raw evidence. Claude instructions are checked against current official documentation; Claude model runs are not part of this evaluation.

Raw live-account reports stay outside this repository. All committed examples and fixtures are synthetic. The [case definitions](cases.md) describe review criteria and inputs for repeatable runs. Agents completing a case do not receive those criteria or earlier answers.

Passing arithmetic or metadata checks alone does not establish that an agent gave a useful recommendation. Each report is reviewed for accurate sources, defensible interpretation, missing-data handling, and concrete next steps.

## Version 0.1.0 evaluation, September 25, 2026

| Evaluation | Method | Result and scope |
| --- | --- | --- |
| Ads representative exports | Fresh Codex subagent; bundled fictional firm and two CSVs | Passed: reconciled $8,000 spend and 22.5 conversions; correctly used Search-only spend for term coverage, preserved paused-campaign history, and distinguished events from business outcomes. |
| Ads incomplete/adversarial exports | Separate fresh Codex subagent; public `ads-incomplete` fixture | Passed: no invented conversion total, invalid cross-period coverage, guaranteed savings, or blanket exclusions; embedded instructions were ignored and a useful preliminary audit was delivered. |
| Ads live authorized account | Fresh Codex subagent; actual Google Ads interface in the in-app browser | Passed as a browser-only review: verified period/time zone, campaign totals, action definitions, query coverage and current settings; adapted to the actual B2B business and separated current configuration from historical performance. Equal-period comparison and native download were unavailable. No account changes; all evidence kept private. |
| Competitive public research | Fresh Codex subagent; three actual firm websites and two Google results pages in the in-app browser | Passed within stated scope: sourced website comparison, separate advertising/local/organic samples, and four proposed experiments. The engine's observer location differed from the target market and was disclosed. Review themes and private account performance were not claimed. |
| Competitive incomplete/adversarial snapshots | Separate fresh Codex subagent; public `competition-snapshot` fixture | Passed: handled blocked pages, claim-versus-capability distinctions, partial search crops, sponsored local placements, review-sampling bias, and embedded instructions without losing the useful comparison. |
| No-data fallback | Separate fresh Codex subagent; both skills, no account, firm identity, market, files, or browsing | Passed: requested a focused starting evidence bundle and supplied a collection plan without inventing spend, competitors, or findings. |
| Native Codex installation and execution | Codex CLI 0.149.1; complete folders under a disposable project's `.agents/skills`; separate fresh processes with name-only prompts | Both skills were discovered and completed their tasks. The Ads skill ran its packaged helper on both supplied CSVs. Original runs and fresh reruns after instruction improvements succeeded; installed files remained unchanged. |
| Independent release review | Separate Codex reviewer; source, distribution, privacy boundaries, and tests | Two findings were fixed and independently rechecked: ambiguous evaluation input selection and recursive packaging of ignored private files. No unresolved blocking finding remained. |
| Local automated checks | Python standard-library unittest, structural validation, package extraction | 25 tests passed locally. Single-folder ZIPs were extracted in a temporary directory and the distributed Ads helper ran successfully there. |

### Improvements made during testing

The arithmetic checks found a delimiter-detection error for quoted multiline cells; it was fixed and a regression test retained. A further check made summary-row exclusion independent of column order. The guidance also clarifies that reporting date/filter changes are allowed in a read-only browser audit and that short period comparisons should account for weekday mix.

An independent reviewer found that ignored private directories could enter a recursively built ZIP. Packaging now uses an explicit file allowlist, rejects unsafe paths/symlinks, and excludes every unlisted file; regression tests reproduce the failure condition, and independent re-review confirmed the fix. No real private data was present in the repository or release packages. The review also made evaluation input filenames explicit so the bundled sample output cannot accidentally become an input.

The first native-client outputs prompted two wording improvements: do not display a mathematically invalid cross-period ratio even as a caveat, and do not imply paid advertising from a translated website page. Fresh reruns used the same prompts without hints about the changes. Review of the resulting reports confirmed that mismatched periods stayed separate, unknown savings were unquantifiable rather than zero, and translated website content was described without implying paid advertising.

These are observed results from specific scenarios, not a guarantee across every agent or account. The fresh semantic evaluations received no expected answers or earlier reports. Live browser export was unavailable in the research environment; reports explicitly distinguish visible browser evidence and local notes from downloaded source files.

## Run local checks

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
python3 scripts/package_skills.py
```

The helper tests cover total-row exclusion, Search-only scope, fractional conversions, monetary units, locales/encodings, unknown metrics, zero denominators, duplicate rows, malformed values, and output-file protection. Distribution tests check complete single-folder archives, licensing, no path escapes, and repeatable hashes.

## Interpretation limits

Results depend on the agent, available tools, sources, and account configuration. A successful CSV review is not proof that a Google Ads MCP installation works. A successful browser review is not a test of every Google Ads report. Current website research is a dated sample, not continuous rank tracking or a census of local advertising.

Hosted ChatGPT/Claude installation and live Google Ads MCP remain unverified unless explicitly added to the release record. Provider UI instructions are based on primary documentation checked September 25, 2026. The repository does not bundle a connector or host an account service.
