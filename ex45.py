# Demanar un número
num = int(input("Introdueix un número: "))

# Sumar els dígits
suma = sum(int(d) for d in str(num))

# Mostrar resultat i si és parell o senar
print(f"La suma dels dígits és: {suma}")
if suma % 2 == 0:
    print("La suma és parell")
else:
    print("La suma és senar")
