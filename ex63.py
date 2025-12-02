# Definir la funció utilitzant filter
def paraules_per_lletra(llista, lletra):
    return list(filter(lambda paraula: paraula.lower().startswith(lletra.lower()), llista))

# Prova
paraules = ["maria", "manta", "peu", "mà"]
print(paraules_per_lletra(paraules, 'p'))  # Sortida: ['peu']
