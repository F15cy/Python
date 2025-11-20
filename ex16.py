# Definir la función
def gran_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(gran_de_tres(5, 10, 7))    # Debe imprimir 10
print(gran_de_tres(20, 15, 25))  # Debe imprimir 25
print(gran_de_tres(8, 8, 3))     # Debe imprimir 8
print(gran_de_tres(-2, -5, -1))  # Debe imprimir -1
