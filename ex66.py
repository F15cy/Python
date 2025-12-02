# Definir la funció utilitzant enumerate
def coincideix_valor_index(llista):
    return sum(1 for idx, valor in enumerate(llista) if idx == valor)

# Prova
llista = [0, 2, 3, 3, 4]
print(coincideix_valor_index(llista))  # Sortida: 3
