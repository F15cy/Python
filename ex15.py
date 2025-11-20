# Definir la función
def gran(a, b):
    if a > b:
        return a
    else:
        return b

# Probar la función con distintos ejemplos
print(gran(5, 10))   # Debe imprimir 10
print(gran(20, 7))   # Debe imprimir 20
print(gran(15, 15))  # Debe imprimir 15
print(gran(-3, 4))   # Debe imprimir 4
