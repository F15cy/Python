# Definir la funció utilitzant enumerate
def llista_a_diccionari(llista):
    return {valor: idx for idx, valor in enumerate(llista)}

# Prova
llista = ['casa', 'cotxe', 'cadira', 'taula']
print(llista_a_diccionari(llista))  # Sortida: {'casa': 0, 'cotxe': 1, 'cadira': 2, 'taula': 3}
