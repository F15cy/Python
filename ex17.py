def longitud(objeto):
    contador = 0
    for _ in objeto:
        contador += 1
    return contador

lista1 = [1, 2, 3, 4, 5]
lista2 = ["a", "b", "c"]
print("Longitud de lista1:", longitud(lista1))  
print("Longitud de lista2:", longitud(lista2))  


cadena1 = "Hola"
cadena2 = "Python es divertido"
print("Longitud de cadena1:", longitud(cadena1))  
print("Longitud de cadena2:", longitud(cadena2))  
