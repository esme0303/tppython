from itertools import product

def nombre_facons_somme_20():
    total = 0
    for combinaison in product(range(1, 7), repeat=5):
        if sum(combinaison) == 20:
            total += 1
    return total

print(f"Nombre de façons d'obtenir 20 : {nombre_facons_somme_20()}")
