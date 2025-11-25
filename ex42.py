# Demanar un número entre 1 i 900000
while True:
    num = int(input("Introdueix un número (1 - 900000): "))
    if 1 <= num <= 900000:
        break

# Comptar el nombre de dígits
digits = len(str(num))

# Mostrar resultat
print(f"El número té {digits} dígits.")
