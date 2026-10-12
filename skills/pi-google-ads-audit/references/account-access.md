# Read-only account access

Installing this skill supplies a workflow, not Google credentials or an account connection. Prefer an already configured, authorized read-only connection. If none exists, use exports; the user need not become a developer to receive an audit.

## Official Google Ads MCP

Google publishes [google-ads-mcp](https://github.com/googleads/google-ads-mcp) and an [integration guide](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server). As checked on 2026-09-25, its tools support account discovery, resource metadata, and GAQL reporting, with local stdio and hosted transport options. Follow the current official setup instructions; do not copy credentials into the report or repository. This skill does not bundle, install, or operate that server.

Discover the tools actually available in the host. Tool names can have host-specific prefixes. Establish the requested customer, manager context if relevant, currency, time zone, and accessible scope. Use resource metadata to validate fields and compatible segments; do not assume a remembered API version or UI column is available.

Fetch campaign totals first, including campaigns with historical spend even if now paused/removed when the report permits. Use explicit start/end dates, bounded projections, and complete pagination. Keep queries/results outside public working directories. If a tool limits result length, narrow or paginate instead of assuming the displayed rows are complete. Record the query or an equivalent report description, customer alias, retrieval time, row count, and completeness status.

Then fetch conversion definitions/goals and the highest-value drilldowns: search terms, keyword/ad-group detail, geographic settings and performance, devices/networks, and change history if exposed. Use campaign IDs for joins; names are not unique. Conversion-action segmentation can change row grain and repeat other metrics: retrieve action breakdowns separately and do not add their cost rows into campaign totals.

Google Ads cost fields ending in `_micros` are millionths of account currency: divide by 1,000,000 exactly once. Fractional conversions are allowed. Do not add `Conversions` and `All conversions`, or assume one equals qualified leads.

## Browser path

Use only the browser interface authorized by the user. Verify account name, date picker, time zone, selected campaigns, status filters, and active segments before reading a table. Prefer downloaded CSV reports for larger tables. Record a visible total separately from page rows. Do not multiply the current page into an estimate of unseen pages. If downloading is unavailable, cite the view and clearly limit conclusions to what was visible.

Changing a reporting date/filter to inspect data is within a read-only audit. Do not save account settings or reports, apply recommendations, enable conversions, click ads, or submit a lead form. If a login/security barrier blocks access, request the specific export that replaces it and continue with other inputs.

## Host limitations

A local stdio MCP configuration is not a remotely reachable connection for a hosted chat. Hosted clients need their own supported, authenticated remote connector configuration. Never expose a local credential file or create an unauthenticated public reporting endpoint to make a skill work. The browser, MCP, and CSV paths are alternatives; name which one you actually used.
