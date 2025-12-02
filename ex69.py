# Demanar la potència
potencia = int(input("Introdueix la potència: "))

# Crear la llista dels 10 primers números elevats a la potència
llista = [i**potencia for i in range(10)]
print(llista)
