# Definir la funció utilitzant zip
def concatena_llistes(llista1, llista2, connector):
    return [a + connector + b for a, b in zip(llista1, llista2)]

# Prova
llista1 = ['sub', 'supra']
llista2 = ['campió', 'campiona']
print(concatena_llistes(llista1, llista2, '-'))  # Sortida: ['sub-campió', 'supra-campiona']
