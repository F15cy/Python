# Definir la funció per controlar divisió per zero
def dividir(a, b):
    if b == 0:
        print("Error: No es pot dividir per zero!")
        return None
    return a / b

# Prova
print(dividir(10, 2))  # 5.0
print(dividir(10, 0))  # Error: No es pot dividir per zero!
