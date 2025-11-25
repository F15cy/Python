# Demanar un número
num = input("Introdueix un número: ")

# Mostrar només els dígits parells
print("Dígits parells:", end=" ")
for d in num:
    if d.isdigit() and int(d) % 2 == 0:
        print(d, end=" ")
