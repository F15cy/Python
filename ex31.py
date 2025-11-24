# Pedimos el año actual
any_actual = int(input("Any actual: "))

# Inicializamos una lista con los datos de las personas
persones = []
for i in range(4):
    nom = input(f"Nom de la persona {i+1}: ")
    any_naixement = int(input(f"Any de naixement de {nom}: "))
    persones.append((nom, any_naixement))

# Imprimimos la tabla de resultados
print("Nom        Data naixement  Anys que farà aquest any")
for persona in persones:
    nom, any_naixement = persona
    edat = any_actual - any_naixement
    print(f"{nom:<10}\t{any_naixement}\t\t{edat}")
