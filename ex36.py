def es_de_traspas(any):
    if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
        return True
    else:
        return False

# Proves
print(es_de_traspas(2020))  # Ha de sortir True
print(es_de_traspas(2021))  # Ha de sortir False
print(es_de_traspas(2000))  # True
print(es_de_traspas(1900))  # False
