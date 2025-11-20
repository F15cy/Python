# Definir la función
def gran_llista(llista):
    # Suponemos que el primer número es el mayor
    major = llista[0]
    # Recorremos la lista
    for num in llista:
        if num > major:
            major = num
    return major

# Probar la función con distintos ejemplos
print(gran_llista([3, 4, 2, 3, 10]))    # 10
print(gran_llista([7, 1, 5, 9, 2]))     # 9
print(gran_llista([100, 50, 100, 30]))  # 100
print(gran_llista([-5, -2, -10]))       # -2
