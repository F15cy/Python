# Definir la funció
def elimina_duplicats(llista):
    return list(set(llista))

# Exemple de prova
print(elimina_duplicats([1,2,2,3,4,4,5]))  # Retorna [1,2,3,4,5] (ordre pot variar)
