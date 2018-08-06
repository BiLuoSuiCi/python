import pandas as pd

df = pd.read_excel('2.xlsx')

a = list(df['imei'])

a = [str(x) for x in a]

print(a)