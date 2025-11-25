# Definir la funció
def esta_ordenada(llista):
    if llista == sorted(llista):
        return "Està ordenada de forma ascendent"
    elif llista == sorted(llista, reverse=True):
        return "Està ordenada de forma descendent"
    else:
        return "No està ordenada"

# Provar la funció
print(esta_ordenada([3,2,1]))  # Està ordenada de forma descendent
print(esta_ordenada([4,5,6]))  # Està ordenada de forma ascendent
print(esta_ordenada([1,2,3]))  # No està ordenada
