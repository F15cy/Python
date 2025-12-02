def index_paraula(llista, paraula):
    for i in range(len(llista)):
        if llista[i] == paraula:
            return i
    return -1

# Exemple
ll = ["ana", "casa", "hola", "ramis"]
print(index_paraula(ll, "hola"))   # 2
print(index_paraula(ll, "pep"))    # -1
