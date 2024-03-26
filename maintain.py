import pandas as pd
import datetime

my_file = 'data.csv'

df = pd.read_csv(my_file)

df['Date'] = df['Date'].map({
    'today': datetime.date.today(),
    '': datetime.date.today()
})

df['Date'] = df['Date'].fillna(datetime.date.today())

print(df)

df.to_csv(my_file, index=False)
