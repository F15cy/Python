def llegir_fitxer(nom_fitxer):
    try:
        with open(nom_fitxer, "r", encoding="utf-8") as f:
            contingut = f.read()
        return contingut
    except FileNotFoundError:
        print(f"Error: El fitxer '{nom_fitxer}' no existeix.")
        return None
    except Exception as e:
        print(f"Error llegint el fitxer: {e}")
        return None

# Prova
text = llegir_fitxer("exemple.txt")
if text:
    print(text)
