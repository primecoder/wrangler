#!/usr/bin/env python3

import argparse as arg
import pandas as pd

parser = arg.ArgumentParser()
parser.add_argument("--file1")
parser.add_argument("--file2")
parser.add_argument("--outtype", nargs="*", default=["csv"], choices=["csv", "json"])

args = parser.parse_args()

if not args.file1 or not args.file2:
    parser.print_help()
    exit(-1)

data1 = pd.read_csv(args.file1)
data2 = pd.read_csv(args.file2)
data = pd.concat([data1, data2], ignore_index=True)
output_type = args.outtype[0]
if output_type == "csv":
    print(data.to_csv(index=False))
elif output_type == "json":
    print(data.to_json(orient="records"))
else:
    parser.print_help()

