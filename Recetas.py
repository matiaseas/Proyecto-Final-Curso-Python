# alfajores_nuez_ganache_chocolate: {'harina':230, 'nueces_procesadas':100, 'manteca':180, 'azúcar_impalpable':100, 'huevos':1, 'chocolate_águila_rallado':40, 'crema':200, 'chocolate_águila_semiamargo':200}

# alfajores_marplatenses: {'manteca':150, 'azúcar blanca':50, 'miel':50, 'ralladura de limón':1/2, 'ralladura de naranja':1/2, 'huevo':1, 'esencia de vainilla':1, 'harina 0000':250, 'fécula':50, 'polvo de hornear':5, 'bicarbonato de sodio':2, 'cacao amargo':20}

# alfajores_sablee: {harina 0000250 azúcar impalpable110 sal1 manteca fría150 yemas2 esencia de vainilla1 dulce de leche repostero3/4}

# alfajores_chocolate_chips: {manteca200 azúcar100 vainilla1 huevos2 cacao amargo20 maicena180 harina 0000250 chips de chocolate140 dulce de leche reposteroc/n }
 
# alfajores_chocolate: {harina 0000180 cacao amargo20 manteca100 azúcar impalpable80 yemas2 crema75 chocolate semiamargo75 dulce de leche reposter300o}

# alfajores_bonobon: {huevo1 de manteca a temperatura ambiente100 azúcar100 harina leudante260 esencia de vainilla  chocolate blanco250 mantequilla de maní170 chocolate blanco300}

# alfajores_tri_shot: {100 gr de manteca media taza de azúcar impalpable (110gr) 1 huevo + esencia de vainilla 1 taza y 1/4 de harina 0000 2 editas de cacao amargo 50 gr de maní sin sal 100 gr chocolate blanco + 1 cda de pasta de maní 100 gr chocolate con leche + 1 cda de pasta de maní 250 gr chocolate con leche}
# (8 alfajores)

# alfajorcitos_coco_dulce_leche: {80g de manteca 60gr azúcar ralladura limón 2 huevos 115gr harina leudante (o 115 gr harina 0000 + ½ cdta polvo de hornear) 150gr coco rallado dulce de leche para rellenar}
# (24 alfajores pequeños)

# alfajores_dulce_membrillo_bañados_glacé: {175 gramos manteca (pomada) 175 gramos azúcar 350 gramos harina 0000 150 gramos maicena 15 gramos polvo de hornear 1 cdta esencia de vainilla 1 cucharada dulce de leche ralladura de 1 naranja 60 cc agua 1 huevo ½ kg dulce de membrillo 1 cucharada whisky o coñac 2 cucharadas agua 1 cucharada fécula de maíz 1 clara de huevo 200 gr azúcar impalpable 200 gr azúcar 80 cc agua}

# alfajor_block: {300 grs de manteca pomada 240 grs de azúcar pizca de sal 2 huevos 100 grs de maní picado 450 grs de harina 50 grs de cacao amargo 1 cdta de polvo de hornear 600 grs de chocolate semiamargo 400 grs de crema de leche 2 cdas de mantequilla de maní 500grs de chocolate con leche}

# alfajores_chocolate_chips_2: {200g de manteca 100g de azúcar 1 cdita de vainilla 2 huevos 20g de cacao amargo 180g de maicena 250g de harina 0000 140g de chips de chocolate dulce de leche repostero c/n}

import pandas as pd

# convert into dataframe
df = pd.read_excel("Marplantenses.xlsx")

# convert into dictionary
recipe_marplatenses = df.to_dict()

# show dictionary on console
print(recipe_marplatenses)