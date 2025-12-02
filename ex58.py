# Definir la funció
def elements_parells(llista):
    return [llista[i] for i in range(len(llista)) if i % 2 == 1]

# Provar la funció
paraules = ["una", "dos", "tres", "quatre", "cinc"]
print(elements_parells(paraules))  # Sortida: ['dos', 'quatre']
