#/usr/bin/env python

import pandas as pd

import argparse

parser = argparse.ArgumentParser(description='Process some csv file')
parser.add_argument('-f','--file', dest='filename', required=True,
                    help='csv file name to be parsed')
parser.add_argument('-sk','--skip_rows', dest='skiprows', default=0,
                    help='If CSV file has some junk on top of file, skip this many rows')

args = parser.parse_args()

print pd.read_csv(args.filename, skiprows = int(args.skiprows))
