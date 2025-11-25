# Demanar dues paraules
paraula1 = input("Introdueix la primera paraula: ").lower()
paraula2 = input("Introdueix la segona paraula: ").lower()

# Comprovar coincidències finals
if paraula1[-3:] == paraula2[-3:]:
    print("Rimen")
elif paraula1[-2:] == paraula2[-2:]:
    print("Rimen una mica")
else:
    print("No rimen")
