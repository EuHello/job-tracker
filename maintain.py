#!/usr/bin/env python3

import pandas as pd
import datetime

my_file = 'data.csv'
df = pd.read_csv(my_file, sep=';')


def check_dates(value: str):
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
                print("Unable to parse date string into date class {}".format(err))
    else:
        return datetime.date.today()


df['Date'] = df['Date'].fillna(datetime.date.today())
df['Date'] = df['Date'].map(check_dates)
# df = df.sort_values(by=['Date'])

print(df)
df.to_csv(my_file, sep=';', index=False)
