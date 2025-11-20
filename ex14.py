print("CALCULADORA")
print("1 - Sumar")
print("2 - Restar")
print("3 - Multiplicar")
print("4 - Dividir")
print("5 - Cambio de base")

op = input("Elige una opción: ")

if op == "1":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("Resultado:", a + b)

elif op == "2":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("Resultado:", a - b)

elif op == "3":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("Resultado:", a * b)

elif op == "4":
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))
    print("Resultado:", a / b)

elif op == "5":
    num = input("Introduce el número: ")
    base_origen = int(input("Base origen (2,8,10,16): "))
    base_dest = int(input("Base destino (2,8,10,16): "))

    # pasar primero a decimal
    if base_origen == 2:
        dec = int(num, 2)
    elif base_origen == 8:
        dec = int(num, 8)
    elif base_origen == 10:
        dec = int(num)
    elif base_origen == 16:
        dec = int(num, 16)
    else:
        print("Base origen incorrecta")
        exit()

    # convertir a destino
    if base_dest == 2:
        print("Resultado:", bin(dec)[2:])
    elif base_dest == 8:
        print("Resultado:", oct(dec)[2:])
    elif base_dest == 10:
        print("Resultado:", dec)
    elif base_dest == 16:
        print("Resultado:", hex(dec)[2:].upper())
    else:
        print("Base destino incorrecta")

else:
    print("Opción no válida")