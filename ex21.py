def es_palindrom(cadena):
    cadena = cadena.lower()
    if cadena == cadena[::-1]:
        return True
    else:
        return False

print(es_palindrom("radar"))   # True
print(es_palindrom("ara"))     # True
print(es_palindrom("civic"))   # True
print(es_palindrom("rallar"))  # True
print(es_palindrom("tapat"))   # True
print(es_palindrom("simis"))   # True
print(es_palindrom("refer"))   # True
print(es_palindrom("python"))  # False
print(es_palindrom("hola"))    # False
