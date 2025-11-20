# Usamos la función crear_punts que ya definimos
def crear_punts(llista):
    for num in llista:
        for i in range(num):
            print(".", end="")  # imprimir puntos en la misma línea
        print()  # salto de línea

# Nueva función para dibujar una imagen
def dibujar_imagen():
    print("Mi imagen de puntos:")
    # Lista de números que representan la “imagen”
    imagen = [3, 5, 2, 6, 4]
    crear_punts(imagen)

# Probar la función
dibujar_imagen()
