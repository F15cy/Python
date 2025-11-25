# Demanar dades a l'usuari amb control de valors
while True:
    capital = float(input("Introdueix la quantitat a invertir (50000€ - 800000€): "))
    if 50000 <= capital <= 800000:
        break

while True:
    interes = float(input("Introdueix l'interès anual (%) (0.5% - 13%): "))
    if 0.5 <= interes <= 13:
        break

while True:
    anys = int(input("Introdueix el nombre d'anys (3 - 40): "))
    if 3 <= anys <= 40:
        break

# Calcular capital final
Cfinal = capital * (1 + interes/100) ** anys

# Mostrar resultat
print(f"El capital final serà: {Cfinal:.2f}€")
