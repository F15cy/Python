def es_vocal(caracter):
    caracter = caracter.lower()
    
    if caracter in "aeiou":
        return True
    else:
        return False

# Probar la función con distintos ejemplos
print(es_vocal("a"))  # True
print(es_vocal("E"))  # True
print(es_vocal("b"))  # False
print(es_vocal("O"))  # True
print(es_vocal("z"))  # False
