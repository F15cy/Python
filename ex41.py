# Demanar un número menor que 100
num = int(input("Introdueix un número menor que 100: "))

# Inicialitzar la suma
suma = 0

# Recórrer els números restants de 4 en 4 cap enrere
for i in range(num, 0, -4):
    suma += i**2

# Mostrar resultat
print("La suma dels quadrats és:", suma)
