import random

# Generar un codi secret de 4 xifres aleatori
codi_secret = [random.randint(0,9) for _ in range(4)]

print("Benvingut al MasterMind simplificat!")
print("Introdueix codis de 4 xifres fins que encertis el codi.")

guanyat = False
while not guanyat:
    intent = input("Introdueix un codi de 4 xifres: ")
    
    if len(intent) != 4 or not intent.isdigit():
        print("Cal que sigui un codi de 4 xifres!")
        continue

    intent_nums = [int(x) for x in intent]

    # Comptar els encerts exactes (mateixa posició)
    encerts = sum([1 for i in range(4) if intent_nums[i] == codi_secret[i]])

    # Comptar coincidències (número correcte però posició incorrecta)
    coincidencies = 0
    codi_restant = []
    intent_restant = []
    for i in range(4):
        if intent_nums[i] != codi_secret[i]:
            codi_restant.append(codi_secret[i])
            intent_restant.append(intent_nums[i])
    for num in intent_restant:
        if num in codi_restant:
            coincidencies += 1
            codi_restant.remove(num)

    print(f"Encerts: {encerts}, Coincidències: {coincidencies}")

    if encerts == 4:
        guanyat = True
        print("Felicitats! Has endevinat el codi!")
