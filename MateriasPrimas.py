import pandas as pd

# convert into dataframe
df = pd.read_excel("PRECIOS SÍA.xlsx")

# convert into dictionary
raw_ing = df.to_dict()

# show dictionary on console
print(raw_ing)