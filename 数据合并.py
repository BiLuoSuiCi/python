import pandas as pd 
import os,re

a = '0'
b = 252031
d = []

for i in range(4000):
    c = b + i
    c = a + str(c)
    d.append(c)

    print(c)

df = pd.DataFrame(d)

df.to_excel("IDE.xlsx")
print(df)