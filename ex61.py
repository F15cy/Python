# Definir la funció utilitzant map
def lenp(frase):
    paraules = frase.split()
    return list(map(len, paraules))

# Prova
frase = "Hola soc Ramis"
print(lenp(frase))  # Sortida: [4, 3, 5]
