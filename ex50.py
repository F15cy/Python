import random

# Definir la funció
def llista_20_elements():
    return [random.randint(1, 100) for _ in range(20)]

# Provar la funció i comprovar duplicats
llista = llista_20_elements()
print("Llista generada:", llista)

# Funció per comprovar duplicats
def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))

print("Hi ha duplicats?", hi_ha_duplicats(llista))
