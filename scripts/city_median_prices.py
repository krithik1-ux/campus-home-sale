#!/usr/bin/env python3
"""Make data/city_median_sale_prices.json for index.html.

Run from anywhere:
    python3 scripts/city_median_prices.py

Reads data/college_town_home_sales.csv and writes data/city_median_sale_prices.json.
It never writes to the dataset files.

The rule: a sale is left out if its sale_price is blank or under $10,000.
Every count and median in the output is computed here from the CSV.
"""

import csv
import json
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "college_town_home_sales.csv"
OUTPUT = ROOT / "data" / "city_median_sale_prices.json"
MIN_SALE_PRICE = 10000


def main():
    rows_in_source = 0
    rows_blank_price = 0
    rows_under_min = 0
    prices_by_city = defaultdict(list)

    # Read every column as text. The price is then converted with int(),
    # because the data sheet says sale_price is a whole number of dollars.
    with SOURCE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rows_in_source += 1
            raw = row["sale_price"].strip()
            if raw == "":
                rows_blank_price += 1
                continue
            price = int(raw)
            if price < MIN_SALE_PRICE:
                rows_under_min += 1
                continue
            prices_by_city[(row["city"].strip(), row["state"].strip())].append(price)

    cities = []
    for (city, state), prices in prices_by_city.items():
        median = statistics.median(prices)
        cities.append({
            "city": city,
            "state": state,
            "sales": len(prices),
            "median_sale_price": median,
        })
    # Largest median first, so the chart and table read top to bottom.
    cities.sort(key=lambda c: (-c["median_sale_price"], c["city"]))

    output = {
        "source": "data/college_town_home_sales.csv",
        "rule": "Sales with a blank sale_price, or a sale_price under $10,000, are left out.",
        "min_sale_price": MIN_SALE_PRICE,
        "rows_in_source": rows_in_source,
        "rows_blank_price": rows_blank_price,
        "rows_under_min_price": rows_under_min,
        "rows_used": sum(c["sales"] for c in cities),
        "city_count": len(cities),
        "cities": cities,
    }

    with OUTPUT.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(output, f, indent=2)
        f.write("\n")

    print(f"Wrote {OUTPUT.relative_to(ROOT)}")
    print(f"Rows in source: {rows_in_source:,}")
    print(f"Left out: {rows_blank_price:,} blank, {rows_under_min:,} under ${MIN_SALE_PRICE:,}")
    print(f"Rows used: {output['rows_used']:,} in {output['city_count']} cities")


if __name__ == "__main__":
    main()
