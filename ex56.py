# Demanar dos números
num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

# Assegurar que num1 sigui el menor
if num1 > num2:
    num1, num2 = num2, num1

# Sumar tots els números entre num1 i num2 (ambdós inclosos)
suma = sum(range(num1, num2+1))

print(f"La suma dels números entre {num1} i {num2} és: {suma}")
