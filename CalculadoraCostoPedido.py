from Recetas import dic_recipe
from MateriasPrimas import dic_ing

cost = 0

for key, value in dic_recipe.items():
    if key in dic_ing:
        print (f"{key} : {dic_recipe[key]}*{dic_ing[key]}")
        cost = cost + (dic_recipe[key] * dic_ing[key])

value = cost * 2.5
print (f"El costo para producir el pedido es de {round(cost, 2)} pesos")
print (f"El valor a cobrar al cliente es de {round(value, 2)} pesos")

