#!/usr/bin/env python3
"""
CSV profiling script.
"""

import csv, sys, statistics

def profile(csvfile):
    with open(csvfile, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        print("Empty file.")
        return
    cols = reader.fieldnames
    nrows = len(rows)
    print(f"Rows: {nrows}")
    print(f"Columns: {', '.join(cols)}")
    for col in cols:
        values = [r[col] for r in rows]
        missing = sum(1 for v in values if v == '')
        unique = len(set(values))
        nums = []
        for v in values:
            try: