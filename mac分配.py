import pandas as pd

def read_xlsx():
    df = pd.read_excel(r"G:\mac\22.xlsx")
  
    a = df.iloc[0:150000]
    b = df.iloc[150000:len(df)]
    #print(b)
    a.to_excel(r"G:\mac\1.xlsx",index=False)
    b.to_excel(r"G:\mac\2.xlsx",index=False)
if __name__ == "__main__":
    read_xlsx()