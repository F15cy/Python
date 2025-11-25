# Definir la funció
def hi_ha_duplicats(llista):
    return len(llista) != len(set(llista))

# Provar la funció
print(hi_ha_duplicats([1, 2, 3, 4]))      # False
print(hi_ha_duplicats([1, 2, 2, 3, 4]))   # True
