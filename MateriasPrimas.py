import pandas as pd
import pint

units = pint.UnitRegistry()

data_ing_raw = pd.read_excel('MateriasPrimas.xlsx')
dic_ing_raw = data_ing_raw.to_dict(orient='records')
dic_ing_raw = dic_ing_raw.pop(0)

dic_ing = {}

for key in dic_ing_raw:
    dic_ing_raw[key] = (dic_ing_raw[key].replace("$","").replace("x","/")).replace("gr","g").lower().replace(" kg","1kg").replace(" l","1l").replace(" u","1u")
    if "g" in dic_ing_raw[key] and "kg" not in dic_ing_raw[key]:
        dic_ing_raw[key] = (dic_ing_raw[key].replace("g","*1000kg"))
    elif "ml" in dic_ing_raw[key]:
        dic_ing_raw[key] = (dic_ing_raw[key].replace("ml","*1000l"))
    if (units(dic_ing_raw.get(key))).dimensionality == "[mass]":
        if (units(dic_ing_raw.get(key))).units != "unified_atomic_mass_unit":
            dic_ing_raw[key] = (units(dic_ing_raw.get(key)).to("kg")).magnitude
            dic_ing.setdefault(key,dic_ing_raw[key])
        else:
            dic_ing_raw[key] = (units(dic_ing_raw.get(key))).magnitude
            dic_ing.setdefault(key,dic_ing_raw[key])
    elif (units(dic_ing_raw.get(key))).dimensionality == "[length] ** 3":
        dic_ing_raw[key] = (units(dic_ing_raw.get(key)).to("l")).magnitude
        dic_ing.setdefault(key,dic_ing_raw[key])
    print (key,dic_ing_raw.get(key))
print (dic_ing)