a = float(input("Escriure el primer nombre: "))
b = float(input("Escriure el segon nombre: "))
d = float(input("Escriure el tercer nombre: "))
c = a + b + d
print( "El resultat de la suma {} + {} es {}".format(a, b, c,d))
c = a * b * d
print( "El resultat de la multiplicacio {} + {} es {}".format(a, b, d, c))
if c<20:
        print("La suma es major que 20, que es {}".format(c))
else:   
        print("La suma es menor que 20, que es {}".format(c))

c = a * b * d
print("El resultat de la multiplicacio {} * {} * {} es {}".format(a, b, d, c))
if c>100:
        print("La multiplicacio es major que 100, que es {}".format(c))
else:
        print("La multiplicacio es menor que 100, que es {}".format(c))