def crear_llista_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            return f.read().split()
    except FileNotFoundError:
        print("Error: fitxer no trobat:", nom_fitxer)
        return []
    except Exception as e:
        print("Error llegint fitxer:", e)
        return []

# Prova
llista = crear_llista_fitxer("text.txt")
print(llista)
