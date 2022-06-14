import pandas as pd
import pint

units = pint.UnitRegistry()

data_recipe = pd.read_excel('Marplatenses.xlsx')
dic_recipe = data_recipe.to_dict(orient='records')
dic_recipe = dic_recipe.pop(0)

for key in dic_recipe:
    if (units(dic_recipe.get(key))).u == "gram":
        print (f"{units(dic_recipe.get(key))} equivale a {(units(dic_recipe.get(key))).to('kg')}")
    else:
        print (units(dic_recipe.get(key)))