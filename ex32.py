# Definir la funció
def mostrar_majors_que(tupla, numero):
    for num in tupla:
        if num > numero:
            print(num)

# Demanar al usuari la tupla de números
tupla = tuple(map(int, input("Introdueix els números separats per espais: ").split()))

# Mostrar els números majors que 18
print(f"Els números majors que 18 són:")
mostrar_majors_que(tupla, 18)
