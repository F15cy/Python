# Funció per comprovar si un número és primer
def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Mostrar números primers i comptar-los
prims = []
for i in range(1, 101):
    if es_primer(i):
        prims.append(i)

print("Números primers entre 1 i 100:", prims)
print("Quantitat de números primers:", len(prims))