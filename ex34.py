# Funció que compta quants noms comencen per una lletra donada
def nums_que_comencen_per(llista, lletra):
    contador = 0
    for nom in llista:
        if nom[0].lower() == lletra.lower():
            contador += 1
    return contador

# Programa per demanar la lletra
lletra = input("Introdueix una lletra: ")
noms = ["Anna", "Pol", "Aina", "maria", "Arnau"]
print(nums_que_comencen_per(noms, lletra))
