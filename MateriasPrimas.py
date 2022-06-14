import pandas as pd
import pint

units = pint.UnitRegistry()

data_ing = pd.read_excel('MateriasPrimas.xlsx')
dic_ing = data_ing.to_dict(orient='records')

dic_ing = dic_ing.pop(0)

for key in dic_ing:
    print (units(dic_ing.get(key)))