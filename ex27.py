# Definir la función
def paraula_mes_llarga(llista):
    # Suponemos que la primera palabra es la más larga
    mes_llarga = llista[0]
    # Recorremos la lista
    for paraula in llista:
        if len(paraula) > len(mes_llarga):
            mes_llarga = paraula
    return mes_llarga

# Probar la función con distintos ejemplos
print(paraula_mes_llarga(["Hola", "Ramis", "IES", "Paraula"]))   # "Paraula"
print(paraula_mes_llarga(["Python", "es", "genial"]))           # "Python"
print(paraula_mes_llarga(["a", "ab", "abc", "abcd"]))           # "abcd"
print(paraula_mes_llarga(["una", "dos", "tres"]))               # "una" (cualquiera de las más largas si hay empate)
