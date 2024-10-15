# Driver file for the data
# Basically from here we're getting all of our data

import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Driver file for the data')
    parser.add_argument('--data', type=str, default='data.csv', help='Path to the data file')
    return parser
