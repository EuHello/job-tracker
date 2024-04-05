#!/usr/bin/env python3

import sys
import pandas as pd

my_file = 'data.csv'


def main():
    args = sys.argv[1:]

    if len(args) == 2 and (args[0] == '-c' or args[0] == '-j'):
        df = pd.read_csv(my_file, sep=';')
        search_term = args[1]

        if args[0] == '-c':
            print(f'Searching for Company names similar to: {search_term} ...')
            results = df.loc[df['Company'].str.contains(search_term)]
            if len(results) > 0:
                print(results)
            else:
                print("No similar Company names found")

        elif args[0] == '-j':
            print(f'Searching for Job Titles similar to: {search_term} ...')
            results = df.loc[df['Job Title'].str.contains(search_term)]
            if len(results) > 0:
                print(results)
            else:
                print("No similar Job Titles found")

    else:
        print('arg not found')
        print('-c to search for Company name, -j to search for job title')


if __name__ == "__main__":
    main()
