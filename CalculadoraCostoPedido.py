from Recetas import dic_recipe
from MateriasPrimas import dic_ing

def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

for key in dic_ing and dic_recipe:
    if key in dic_ing and dic_recipe:
        print (get_num(dic_ing.get(key))*get_num(dic_recipe.get(key)))
