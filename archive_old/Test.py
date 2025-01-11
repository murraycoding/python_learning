import pandas as pd

local = "/Users/jmutcap/OneDrive - CUEBITZ LLC/POsData.xlsx"
data = pd.read_excel(local)

df = pd.DataFrame(data)
print(df)