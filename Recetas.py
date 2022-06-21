import pandas as pd
import pint

units = pint.UnitRegistry()

data_recipe_raw = pd.read_excel('Marplatenses.xlsx')
dic_recipe_to_fix = data_recipe_raw.to_dict(orient='records')
dic_recipe_to_fix = dic_recipe_to_fix.pop(0)

dic_recipe = {}

def recipe_fix (dic_recipe_to_fix):
    for key in dic_recipe_to_fix:
        dic_recipe_to_fix[key] = (str(dic_recipe_to_fix[key]).lower().replace("gr","g"))
        if 'g' in dic_recipe_to_fix[key] or 'l' in dic_recipe_to_fix[key] or 'u' in dic_recipe_to_fix[key]:
            print (key, dic_recipe_to_fix[key])
            if (units(dic_recipe_to_fix.get(key))).dimensionality == "[mass]":
                if (units(dic_recipe_to_fix.get(key))).units != "unified_atomic_mass_unit":
                    dic_recipe_to_fix[key] = (units(dic_recipe_to_fix.get(key)).to("kg")).magnitude
                    dic_recipe.setdefault(key,dic_recipe_to_fix[key])
                else:
                    dic_recipe_to_fix[key] = (units(dic_recipe_to_fix.get(key))).magnitude
                    dic_recipe.setdefault(key,dic_recipe_to_fix[key])
            elif (units(dic_recipe_to_fix.get(key))).dimensionality == "[length] ** 3":
                dic_recipe_to_fix[key] = (units(dic_recipe_to_fix.get(key)).to("l")).magnitude
                dic_recipe.setdefault(key,dic_recipe_to_fix[key])
    return dic_recipe

recipe_fix (dic_recipe_to_fix)

def recipe_check(dic_recipe):
    while True:
        entry = input('Ingrese el nombre del ingrediente cuya cantidad desea saber o 10 si desea volver atrás en el menú:\n')
        if entry == '10':
            break
        elif entry in dic_recipe:
            print (f'La receta necesita {dic_recipe[entry]} del ingrediente {entry}')
        else:
            print("No se encuentra ese ingrediente en la receta actual")

def recipe_update (dic_recipe):
    while True:
        entry = input('Ingrese el nombre del ingrediente cuya cantidad desea actualizar o 10 si desea volver atrás en el menú:\n')
        if entry == '10':
            break
        elif entry in dic_recipe:
            ammount = input('Ingrese la cantidad necesitada del ingrediente y su unidad (ej:800g, 260 ml):\n')
            dic_recipe[entry] = ammount
            print (f'La receta necesita {dic_recipe[entry]} del ingrediente {entry}')
            recipe_fix (dic_recipe)
            return dic_recipe
        else:
            print("No se encuentra ese ingrediente en la receta actual")

def recipe_remove (dic_recipe):
    while True:
        entry = input('Ingrese el nombre del ingrediente que desea remover de la receta o 10 si desea volver atrás en el menú:\n')
        if entry == '10':
            break
        elif entry in dic_recipe:
            dic_recipe.pop(entry)
            print (f'El ingrediente {entry} fue removido de la receta')
            recipe_fix (dic_recipe)
            return dic_recipe
        else:
            print("No se encuentra ese ingrediente en la receta actual")

def recipe_add (dic_recipe):
    while True:
        entry = input('Ingrese el nombre del ingrediente que desea agregar a la receta o 10 si desea volver atrás en el menú:\n')
        if entry == '10':
            break
        else:
            ammount = input('Ingrese la cantidad del ingrediente y su unidad (ej:800g, 260 ml):\n')
            dic_recipe[entry] = ammount
            print(f"El ingrediente {entry} fue añadido a receta con una cantidad de {ammount}")
            recipe_fix (dic_recipe)
            return dic_recipe

def recipe_main(dic_recipe):
    while True:
        print (f'Los ingredientes necesitados en la receta y sus cantidades en kg/l/u son:\n')
        for key in dic_recipe:
            print (f'{key}: {dic_recipe[key]}')
        entry = input("Ingrese 1 si desea checkear la cantidad de un ingrediente, ingrese 2 si desea actualizar la cantidad de un ingrediente, ingrese 3 si desea remover un ingrediente, ingrese 4 si desea agregar la cantidad de un ingrediente nuevo o ingrese 10 si desea salir del programa\n")
        if entry == '1':
            recipe_check(dic_recipe)
        elif entry == '2':
            recipe_update(dic_recipe)
        elif entry == '3':
            recipe_remove(dic_recipe)
        elif entry =='4':
            recipe_add(dic_recipe)
        elif entry == '10':
            print ('Terminal Cerrada')
            break
        else:
            print("No es una opcion de menu valida")
    return dic_recipe

recipe_main (dic_recipe)