#!/usr/bin/env python3

import sys
import pandas as pd
import datetime

my_file = 'data.csv'


def fill_dates(value: str):
    if isinstance(value, datetime.date):
        return value
    elif isinstance(value, str):
        value = value.lower().strip()
        if value == 'today' or len(value) == 0:
            return datetime.date.today()
        else:
            try:
                return datetime.datetime.strptime(value, '%Y-%m-%d').date()
            except Exception as err:
                print(f'Unable to parse date string into date class {err}')
    else:
        return datetime.date.today()


def clean_words(value: str):
    if isinstance(value, str):
        value = value.lower().strip()
        return value
    elif isinstance(value, datetime.date):
        return value
    else:
        print(f'Unusual value found. type={type(value)}, value={value}')
        raise


def main():
    args = sys.argv[1:]

    if len(args) == 1 and (args[0] == '-m' or args[0] == '-s'):
        df = pd.read_csv(my_file, sep=';')

        if args[0] == '-m':
            df['Date'] = df['Date'].fillna(datetime.date.today())
            df['Date'] = df['Date'].map(fill_dates)
            df = df.map(clean_words)
            print(df.tail())
            print('Data cleaned')
            df.to_csv(my_file, sep=';', index=False)

        elif args[0] == '-s':
            df = df.sort_values(by=['Date'])
            print(df.tail())
            print('Data sorted')
            df.to_csv(my_file, sep=';', index=False)

    else:
        print('Arg not found')
        print('-m to clean/check file, -s to sort by date')


if __name__ == "__main__":
    main()
