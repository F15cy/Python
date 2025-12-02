import os

# Crear el directori
directori = "/home/cicles/AO/Prova"
os.makedirs(directori, exist_ok=True)

# Canviar a aquest directori
os.chdir(directori)

# Crear i escriure els noms dels alumnes
alumnes = ["izan", "fabian", "justin", "moha", "luca", "edgar", "iker", "ian"]
with open("Ex12.txt", "w", encoding="utf-8") as f:
    for nom in alumnes:
        f.write(nom + "\n")

# Afegir el nom del professor
professors = ["joan carreras"]
with open("Ex12.txt", "a", encoding="utf-8") as f:
    for nom in professors:
        f.write(nom + "\n")

# Llegir tot el contingut i posar-lo dins una llista
with open("Ex12.txt", "r", encoding="utf-8") as f:
    llista_noms = [linea.strip() for linea in f]

print(llista_noms)
 