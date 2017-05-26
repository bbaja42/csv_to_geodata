#/usr/bin/env python

import pandas as pd
from jinja2 import Environment, FileSystemLoader

import argparse

parser = argparse.ArgumentParser(description='Process some csv file')
parser.add_argument('-i','--input-csv', dest='input_csv', required=True,
                    help='csv file name to be parsed')
parser.add_argument('-sk','--skip-rows', dest='skiprows', default=0,
                    help='If CSV file has some junk on top of file, skip this many rows')
parser.add_argument('-o','--output-path', dest='output_path', default="index.html",
                    help='If CSV file has some junk on top of file, skip this many rows')
parser.add_argument('-c','--column-name', dest='column_name', default="Cows",
                    help='Name of the CSV column to be used in geomap')
parser.add_argument('--country-column-name', dest='country_column_name', default="Country Name",
                    help='Column name for the country')

args = parser.parse_args()

def get_geodata_from_csv(input_csv, skiprows, column_name, country_column_name):
    '''
        parses csv file and returns a list of tuples, with format
        [
        ("Ireland", 2),
        ("Canada", 3)
        ]
    '''
    csv_as_dict =  pd.read_csv(input_csv, skiprows = int(skiprows)).to_dict()
    for k,v in csv_as_dict[country_column_name].iteritems():
        try:
            yield (v, int(csv_as_dict[column_name][k]))
        except KeyError:
            print "Failed to find column {} in csv".format(column_name)
            print "Possible columns are {}".format(csv_as_dict.keys())
            exit(1)


def create_html(output_filename, countries_score_tuples):
    context = dict(
        countries =  countries_score_tuples
    )
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html.tpl')
    with open(output_filename, 'w') as f:
        html = template.render(context)
        f.write(html)

countries_scores_tuple = list(get_geodata_from_csv(args.input_csv, args.skiprows, args.column_name, args.country_column_name))
create_html(args.output_path, countries_scores_tuple)
print "Created web page {} with content {}".format(args.output_path, countries_scores_tuple)
