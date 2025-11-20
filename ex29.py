# Definir la función
def comptar_majuscules(cadena):
    contador = 0
    for lletra in cadena:
        if lletra.isupper():  # Comprueba si la letra es mayúscula
            contador += 1
    return contador

# Probar la función con distintos ejemplos
print(comptar_majuscules("Hola Mundo"))        # 2 (H, M)
print(comptar_majuscules("Python es Genial"))  # 3 (P, G)
print(comptar_majuscules("hola"))              # 0
print(comptar_majuscules("123ABC"))            # 3 (A, B, C)
