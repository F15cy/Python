import random
import time

# Funció on expliquem què passa
def intro():
    print ("""En una època on els gegants governen Menorca. Nosaltres necessitem menjar,
Estem seguint el rastre de l'olor del menjar, però ens trobem en una cruïa.
Al final de cada camí hi ha un talaiot, en un viuen els gegants bons que ens convidaran
i en l'altre són uns caníbals afamats, i ens menjaran just ens vegin.
""")

# Funció on demanem a quin talaiot volem anar
def canviTalaiot():
    talaiot = ""
    while talaiot != "1" and talaiot != "2":
        talaiot = input("A quin Talaiot vols anar? Introdueixi 1 o 2: ")
    return talaiot

# Funció que ens indica si compartiran el menjar o serem nosaltres el seu àpat
def trobada(canviTalaiot):
    print ("T'estas apropant al talaiot...")
    time.sleep(1)
    print ("Està fosc i és tenebrós...")
    time.sleep(1)
    print ("Un gran gegant salta davant teu, t'agafa i ...")
    time.sleep(1)
    gegantamic = random.randint (1, 2)
    if canviTalaiot == str(gegantamic):
        print ("Et convida a menjar...")
        return True  # Jugador guanya punts
    else:
        print ("Se't menja d'un mos...ÑAMÑAMÑAM")
        return False  # Jugador perd

# Funció principal amb punts
partidaNova = "si"
punts = 0
while partidaNova.lower() in ("s", "si"):
    intro()
    nTalaiot = canviTalaiot()
    if trobada(nTalaiot):
        punts += 1
        print(f"Punts actuals: {punts}")
    else:
        print(f"Has perdut! Total punts aconseguits: {punts}")
        break  # Acaba la partida si es menja
    partidaNova = input("Vols tornar a mejar (jugar)? Introdueixi si o no: ")
print(f"Partida acabada. Punts totals: {punts}")