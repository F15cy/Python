# Definir la función
def crear_punts(llista):
    for num in llista:
        for i in range(num):
            print(".", end="")  # imprimir los puntos en la misma línea
        print()  # salto de línea después de cada número

# Probar la función con distintos ejemplos
crear_punts([2, 3, 4])
# Salida:
# ..
# ...
# ....

print()  # para separar ejemplos

crear_punts([1, 5, 2])
# Salida:
# .
# .....
# ..
