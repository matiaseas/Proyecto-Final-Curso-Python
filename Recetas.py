import pandas as pd
import pint

units = pint.UnitRegistry()

data_recipe_raw = pd.read_excel('Marplatenses.xlsx')
dic_recipe_raw = data_recipe_raw.to_dict(orient='records')
dic_recipe_raw = dic_recipe_raw.pop(0)

dic_recipe = {}

for key in dic_recipe_raw:
    if (units(dic_recipe_raw.get(key))).dimensionality == "[mass]":
        if (units(dic_recipe_raw.get(key))).units != "unified_atomic_mass_unit":
            dic_recipe_raw[key] = (units(dic_recipe_raw.get(key)).to("kg")).magnitude
            dic_recipe.setdefault(key,dic_recipe_raw[key])
        else:
            dic_recipe_raw[key] = (units(dic_recipe_raw.get(key))).magnitude
            dic_recipe.setdefault(key,dic_recipe_raw[key])
    elif (units(dic_recipe_raw.get(key))).dimensionality == "[length] ** 3":
        dic_recipe_raw[key] = (units(dic_recipe_raw.get(key)).to("l")).magnitude
        dic_recipe.setdefault(key,dic_recipe_raw[key])
print (dic_recipe)