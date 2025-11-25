# Demanar un número entre 1 i 20
while True:
    num = int(input("Introdueix un número (1 - 20): "))
    if 1 <= num <= 20:
        break

# Imprimir la taula de multiplicar
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
