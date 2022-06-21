import pandas as pd
import pint

units = pint.UnitRegistry()

data_ing_raw = pd.read_excel('MateriasPrimas.xlsx')
dic_ing_raw = data_ing_raw.to_dict(orient='records')
dic_ing_raw = dic_ing_raw.pop(0)

dic_ing = {}

def ing_fix (dic_ing_to_fix):
    for key in dic_ing_to_fix:
        dic_ing_to_fix[key] = (str(dic_ing_to_fix[key]).lower().replace("$","").replace("x","/")).replace("gr","g").replace(" kg","1kg").replace(" l","1l").replace(" u","1u")
        if 'g' in dic_ing_to_fix[key] or 'l' in dic_ing_to_fix[key] or 'u' in dic_ing_to_fix[key]:
            if "g" in dic_ing_to_fix[key] and "kg" not in dic_ing_to_fix[key]:
                dic_ing_to_fix[key] = (dic_ing_to_fix[key].replace("g","*1000kg"))
            elif "ml" in dic_ing_to_fix[key]:
                dic_ing_to_fix[key] = (dic_ing_to_fix[key].replace("ml","*1000l"))
            if (units(dic_ing_to_fix.get(key))).dimensionality == "[mass]":
                if (units(dic_ing_to_fix.get(key))).units != "unified_atomic_mass_unit":
                    dic_ing_to_fix[key] = (units(dic_ing_to_fix.get(key)).to("kg")).magnitude
                    dic_ing.setdefault(str(key),float(dic_ing_to_fix[key]))
                else:
                    dic_ing_to_fix[key] = (units(dic_ing_to_fix.get(key))).magnitude
                    dic_ing.setdefault(str(key),float(dic_ing_to_fix[key]))
            elif (units(dic_ing_to_fix.get(key))).dimensionality == "[length] ** 3":
                dic_ing_to_fix[key] = (units(dic_ing_to_fix.get(key)).to("l")).magnitude
                dic_ing.setdefault(str(key),float(dic_ing_to_fix[key]))
    return dic_ing

ing_fix (dic_ing_raw)

def ing_check(dic_ing):
    while True:
        entry = input('Ingrese el nombre del ingrediente cuyo precio desea saber o 10 si desea volver atrás en el menú:\n')
        if entry == '10':
            break
        elif entry in dic_ing:
            print (f'El ingrediente {entry} cuesta ${round(float(dic_ing[entry]),2)}')
        else:
            print("No se encuentra ese ingrediente en la lista actual")

def ing_update (dic_ing):
    while True:
        entry = input('Ingrese el nombre del ingrediente cuyo precio desea actualizar o 10 si desea volver atrás en el menú:\n')
        if entry == '10':
            break
        elif entry in dic_ing:
            cost = input('Ingrese el costo del ingrediente y su formato SIN el símbolo de pesos (ej:800 x kg, 260 x 500ml):\n')
            dic_ing[entry] = cost
            print (f' {entry} cuesta {dic_ing[entry]}')
            ing_fix (dic_ing)
            return dic_ing
        else:
            print("No se encuentra ese ingrediente en la lista actual")

def ing_remove (dic_ing):
    while True:
        entry = input('Ingrese el nombre del ingrediente que desea remover de la lista o 10 si desea volver atrás en el menú:\n')
        if entry == '10':
            break
        elif entry in dic_ing:
            dic_ing.pop(entry)
            print (f'El ingrediente {entry} fue removido de la lista')
            ing_fix (dic_ing)
            return dic_ing
        else:
            print("No se encuentra ese ingrediente en la lista actual")

def ing_add (dic_ing):
    while True:
        entry = input('Ingrese el nombre del ingrediente que desea agregar a la lista o 10 si desea volver atrás en el menú:\n')
        if entry == '10':
            break
        else:
            cost = input('Ingrese el costo del ingrediente y su formato SIN el símbolo de pesos (ej:800 x kg, 260 x ml):\n')
            dic_ing[entry] = cost
            print(f"El ingrediente {entry} fue añadido a lista con un precio de ${cost}")
            ing_fix (dic_ing)
            return dic_ing

def ing_main(dic_ing):
    while True:
        print (f'Los ingredientes cargados y sus precios por kg/l/u son:\n')
        for key in dic_ing:
            print (f'{key}: ${round(float(dic_ing[key]), 2)}')
        entry = input("Ingrese 1 si desea checkear el precio de un ingrediente, ingrese 2 si desea actualizar el precio de un ingrediente, ingrese 3 si desea remover un ingrediente, ingrese 4 si desea agregar el precio de un ingrediente nuevo o ingrese 10 si desea salir del programa\n")
        if entry == '1':
            ing_check(dic_ing)
        elif entry == '2':
            ing_update(dic_ing)
        elif entry == '3':
            ing_remove(dic_ing)
        elif entry =='4':
            ing_add(dic_ing)
        elif entry == '10':
            print ('Terminal Cerrada')
            break
        else:
            print("No es una opcion de menu valida")
    return dic_ing