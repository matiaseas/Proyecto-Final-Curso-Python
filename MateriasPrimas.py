import pandas as pd

# convert into dataframe
df = pd.read_excel("KiloAmaLitroNarUnidadVer.xlsx" , index_col=0)

# convert into dictionary
raw_ing = df.to_dict()

# show dictionary on console
print(raw_ing)