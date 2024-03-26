import pandas as pd
import datetime

my_file = 'data.csv'
df = pd.read_csv(my_file)


def check_dates(value: str):
    today = datetime.date.today()
    if value is None:
        return today
    if value == 'today':
        return str(today)
    else:
        return value


df['Date'] = df['Date'].fillna(datetime.date.today())
df['Date'] = df['Date'].map(check_dates)
df = df.sort_values(by=['Date'])

print(df)
df.to_csv(my_file, index=False)
