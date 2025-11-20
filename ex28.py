# Definir la función
def filtrar_paraules(llista, x):
    resultat = []
    for paraula in llista:
        if len(paraula) > x:
            resultat.append(paraula)
    return resultat

# Probar la función con distintos ejemplos
paraules = ["Hola", "Ramis", "IES", "Paraula", "Python"]

print(filtrar_paraules(paraules, 3))  # ['Ramis', 'Paraula', 'Python']
print(filtrar_paraules(paraules, 5))  # ['Paraula', 'Python']
print(filtrar_paraules(paraules, 6))  # []
