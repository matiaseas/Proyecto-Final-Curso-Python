def check(dic_ing):
    while True:
        entry = input('Ingrese el nombre del ingrediente cuyo precio desea saber o 10 si desea volver atrás en el menú:\n')
        if entry == 10:
            break
        elif entry in dic_ing:
            print (f' {entry} cuesta ${dic_ing[entry]}')
            return dic_ing
        else:
            print("No se encuentra ese ingrediente en la lista actual")

def update (dic_ing):
    while True:
        entry = input('Ingrese el nombre del ingrediente cuyo precio desea actualizar o 10 si desea volver atrás en el menú:\n')
        if entry == 10:
            break
        elif entry in dic_ing:
            cost = input('Ingrese el costo del ingrediente y su formato SIN el símbolo de pesos (ej:800 x kg, 260 x 500ml):\n')
            dic_ing[entry] = cost
            print (f' {entry} cuesta {dic_ing[entry]}')
            return dic_ing
        else:
            print("No se encuentra ese ingrediente en la lista actual")

def remove (dic_ing):
    while True:
        entry = input('Ingrese el nombre del ingrediente que desea remover de la lista o 10 si desea volver atrás en el menú:\n')
        if entry == 10:
            break
        elif entry in dic_ing:
            dic_ing.pop(entry)
            print (f'El ingrediente {entry} fue removido de la lista')
            return dic_ing
        else:
            print("No se encuentra ese ingrediente en la lista actual")

def add (dic_ing):
    while True:
        entry = input('Ingrese el nombre del ingrediente que desea agregar a la lista o 10 si desea volver atrás en el menú:\n')
        if entry == 10:
            break
        else:
            cost = input('Ingrese el costo del ingrediente y su formato SIN el símbolo de pesos (ej:800 x kg, 260 x ml): ')
            dic_ing[entry] = cost
            print(f"El ingrediente {entry} fue añadido a lista con un precio de ${cost}")
            return dic_ing

def main(dic_ing):
    while True:
        print (f'Los ingredientes cargados y sus precios por kg/l/u son:\n')
        for key in dic_ing:
            print (f'{key}: ${round(dic_ing[key], 2)}')
        entry = int(input("Ingrese 1 si desea checkear el precio de un ingrediente, ingrese 2 si desea actualizar el precio de un ingrediente, ingrese 3 si desea remover un ingrediente, ingrese 4 si desea agregar el precio de un ingrediente nuevo o ingrese 10 si desea salir del programa\n"))
        if entry == 1:
            check(dic_ing)
            fix (dic_ing)
        elif entry == 2:
            update(dic_ing)
            fix (dic_ing)
        elif entry == 3:
            remove(dic_ing)
            fix (dic_ing)
        elif entry == 4:
            add(dic_ing)
            fix (dic_ing)
        elif entry == 10:
            print ('Terminal Cerrada')
            break
        else:
            print("No es una opcion de menu valida")
    return dic_ing

main (dic_ing)