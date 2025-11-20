def sumar_llista(lista):
    total = 0
    for num in lista:
        total += num
    return total
def multiplicar_llista(lista):
    total = 1
    for num in lista:
        total *= num
    return total
llista1 = [1, 2, 3, 4]
llista2 = [5, 6, 2]
llista3 = [7]

print("Sumar lista1:", sumar_llista(llista1))        
print("Multiplicar lista1:", multiplicar_llista(llista1))  

print("Sumar lista2:", sumar_llista(llista2))        
print("Multiplicar lista2:", multiplicar_llista(llista2))  

print("Sumar lista3:", sumar_llista(llista3))       
print("Multiplicar lista3:", multiplicar_llista(llista3))  
