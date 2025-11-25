# Definir la funció
def nums_que_comencen_per(llista):
    contador = 0
    for nom in llista:
        if nom[0].lower() == 'a':  # Comprova si la primera lletra és 'a'
            contador += 1
    return contador
 