print("CALCULADORA SIMPLE")
print("Operaciones disponibles:")
print("1 - Sumar")
print("2 - Restar")
print("3 - Multiplicar")
print("4 - Dividir")

op = input("Elige una operación (1/2/3/4): ")

# Pedir los números (enteros o decimales)
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if op == "1":
    print("Resultado:", num1 + num2)
elif op == "2":
    print("Resultado:", num1 - num2)
elif op == "3":
    print("Resultado:", num1 * num2)
elif op == "4":
    if num2 != 0:
        print("Resultado:", num1 / num2)
    else:
        print("Error: división entre 0")
else:
    print("Opción no válida")
