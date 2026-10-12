#!/usr/bin/env python3
"""Summarize one Google Ads performance CSV locally, without dependencies.

This is arithmetic and input validation, not an account audit or CSV converter.
Use one non-overlapping report grain. See references/exports-and-math.md.
"""

import argparse
import csv
import io
import json
import re
import sys
from decimal import Decimal
from pathlib import Path


ALIASES = {
    "cost": {"cost", "spend", "cost_micros", "metrics.cost_micros"},
    "clicks": {"clicks", "metrics.clicks"},
    "impressions": {"impr.", "impressions", "metrics.impressions"},
    "conversions": {"conversions", "conv.", "metrics.conversions"},
    "all_conversions": {"all conv.", "all conversions", "metrics.all_conversions"},
    "currency": {"currency", "currency code", "customer.currency_code"},
}
MISSING = {"", "--", "—", "–", "n/a", "na", "null"}
METRICS = ("cost", "clicks", "impressions", "conversions", "all_conversions")


def header_key(value):
    return " ".join(value.strip().lower().split())


def mapped_columns(headers):
    result = {}
    for index, header in enumerate(headers):
        key = header_key(header)
        for metric, aliases in ALIASES.items():
            if key in aliases:
                if metric in result:
                    raise ValueError(f"Ambiguous columns for {metric}; supply just one.")
                result[metric] = index
    return result


def read_table(path, delimiter=None):
    raw = Path(path).read_bytes()
    encoding = "utf-16" if raw[:2] in (b"\xff\xfe", b"\xfe\xff") else "utf-8-sig"
    content = raw.decode(encoding)
    candidates = [delimiter] if delimiter else [",", "\t", ";"]
    matches = []
    for candidate in candidates:
        reader = csv.reader(io.StringIO(content), delimiter=candidate, strict=True)
        rows = []
        try:
            for row in reader:
                rows.append((reader.line_num, row))
        except csv.Error:
            # A wrong delimiter can invalidate otherwise well-formed quoted cells.
            continue
        for index, (_, row) in enumerate(rows[:30]):
            keys = {header_key(cell) for cell in row}
            if keys & ALIASES["cost"] and keys & ALIASES["clicks"]:
                mapping = mapped_columns(row)
                matches.append((index, rows, mapping, candidate))
                break
    if len(matches) != 1:
        raise ValueError("Expected one table with Cost (or cost_micros) and Clicks headers; "
                         "check delimiter, language, and export format.")
    index, rows, mapping, delimiter = matches[0]
    headers = rows[index][1]
    if len({header_key(h) for h in headers}) != len(headers):
        raise ValueError("Duplicate column names; export a single report without comparison columns.")
    if any("conversion action" in header_key(h) or "conversion_action" in header_key(h)
           for h in headers):
        raise ValueError("Conversion-action segmented costs can repeat. Use an unsegmented "
                         "performance export and analyze conversion actions separately.")
    return headers, rows[index + 1:], mapping, delimiter


def number(value, style, currency, integer=False, micros=False):
    value = value.strip()
    if value.lower() in MISSING:
        return None
    codes = re.findall(r"[A-Za-z]{3}", value)
    if any(code.upper() != currency for code in codes):
        raise ValueError("Currency code does not match --currency.")
    value = re.sub(rf"\b{re.escape(currency)}\b", "", value, flags=re.IGNORECASE).strip()
    for symbol, allowed in (("€", {"EUR"}), ("£", {"GBP"}), ("¥", {"JPY", "CNY"}),
                            ("$", {"USD", "CAD", "AUD", "NZD", "SGD", "HKD", "MXN"})):
        if symbol in value:
            if currency not in allowed:
                raise ValueError("Currency symbol does not match --currency.")
            value = value.replace(symbol, "").strip()
    decimal, thousands = (".", ",") if style == "us" else (",", ".")
    plain = r"\d+"
    grouped = rf"\d{{1,3}}(?:{re.escape(thousands)}\d{{3}})+"
    pattern = rf"(?:{plain}|{grouped})(?:{re.escape(decimal)}\d+)?"
    if not re.fullmatch(pattern, value):
        raise ValueError("Unsupported number or locale; use --number-format us/eu explicitly. "
                         "Negative, bounded, non-finite, and percentage values are not accepted.")
    result = Decimal(value.replace(thousands, "").replace(decimal, "."))
    if integer and result != result.to_integral_value():
        raise ValueError("Clicks and impressions must be whole numbers.")
    return result / Decimal(1_000_000) if micros else result


def ratio(numerator, denominator, multiplier=1):
    if numerator is None or denominator in (None, 0):
        return None
    return numerator / denominator * multiplier


def text_number(value):
    if isinstance(value, Decimal):
        return format(value, "f")
    raise TypeError(type(value).__name__)


def summarize(path, currency, style="us", delimiter=None):
    if not re.fullmatch(r"[A-Z]{3}", currency):
        raise ValueError("--currency must be an uppercase three-letter account currency code.")
    headers, input_rows, mapping, delimiter = read_table(path, delimiter)
    detail, summaries, warnings = [], [], []
    seen = set()
    micros = "micros" in header_key(headers[mapping["cost"]])
    for line, cells in input_rows:
        if not any(cell.strip() for cell in cells):
            continue
        if len(cells) != len(headers):
            raise ValueError(f"Line {line}: column count differs from the header; "
                             "remove report footnotes or re-export.")
        raw_row = dict(zip(headers, cells))
        metric_indexes = {mapping[key] for key in METRICS if key in mapping}
        is_total = any(re.match(r"^total(?:\s*:|\s*$)", cell.strip(), flags=re.I)
                       for index, cell in enumerate(cells) if index not in metric_indexes)
        if "currency" in mapping:
            row_currency = cells[mapping["currency"]].strip().upper()
            if row_currency not in ("", "--", "—", currency):
                raise ValueError(f"Line {line}: mixed or mismatched account currencies.")
        try:
            metrics = {metric: number(cells[mapping[metric]], style, currency,
                                      integer=metric in ("clicks", "impressions"),
                                      micros=metric == "cost" and micros)
                       if metric in mapping else None for metric in METRICS}
        except ValueError as exc:
            raise ValueError(f"Line {line}: {exc}") from exc
        record = {"source_line": line, "raw": raw_row, **metrics}
        if is_total:
            summaries.append(record)
            continue
        key = tuple(cells)
        if key in seen:
            raise ValueError(f"Line {line}: identical detail row repeated; resolve duplicates "
                             "or export identifiers/segments before aggregating.")
        seen.add(key)
        detail.append(record)
    if not detail:
        raise ValueError("No detail rows. A summary-only or empty export is not a detailed report.")
    totals, known_sums, coverage = {}, {}, {}
    for metric in METRICS:
        values = [row[metric] for row in detail]
        known = [value for value in values if value is not None]
        known_sums[metric] = sum(known, Decimal(0)) if known else None
        coverage[metric] = {"known_rows": len(known), "total_rows": len(detail)}
        totals[metric] = known_sums[metric] if len(known) == len(values) else None
        if metric in mapping and len(known) < len(values):
            warnings.append(f"{metric}: unknown values; total and dependent ratios are null.")
    ratios = {"average_cpc": ratio(totals["cost"], totals["clicks"]),
              "ctr_percent": ratio(totals["clicks"], totals["impressions"], 100),
              "cost_per_reported_conversion": ratio(totals["cost"], totals["conversions"])}
    if summaries:
        warnings.append("Summary rows were excluded. Compare their scopes manually before "
                        "treating detail totals as complete account totals.")
    warnings.append("Totals describe these detail rows only. Verify dates, filters, row grain, "
                    "and completeness before comparing reports or calling this an account total.")
    return {"source_file": Path(path).name, "currency": currency, "number_format": style,
            "delimiter": "tab" if delimiter == "\t" else delimiter,
            "cost_input_unit": "micros" if micros else "account_currency",
            "detail_row_count": len(detail), "totals": totals, "known_value_sums": known_sums,
            "coverage": coverage, "ratios": ratios, "detail_rows": detail,
            "excluded_summary_rows": summaries, "warnings": warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--currency", required=True, help="Account currency, e.g. USD")
    parser.add_argument("--number-format", choices=("us", "eu"), default="us")
    parser.add_argument("--delimiter", choices=("comma", "tab", "semicolon"))
    parser.add_argument("--output", type=Path, help="Private destination; stdout if omitted")
    args = parser.parse_args()
    delimiters = {"comma": ",", "tab": "\t", "semicolon": ";"}
    try:
        if args.output and args.output.resolve() == args.input.resolve():
            raise ValueError("Output must differ from the input file.")
        result = summarize(args.input, args.currency, args.number_format,
                           delimiters.get(args.delimiter))
        output = json.dumps(result, default=text_number, indent=2, ensure_ascii=False) + "\n"
        if args.output:
            with args.output.open("x", encoding="utf-8") as handle:
                handle.write(output)
        else:
            print(output, end="")
    except (ValueError, OSError, UnicodeError, csv.Error) as exc:
        print(f"Cannot summarize: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
