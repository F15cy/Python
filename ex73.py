from abc import ABC, abstractmethod

# Classe base Animal
class Animal(ABC):
    def __init__(self, especie, edat):
        self.especie = especie
        self.edat = edat

    @abstractmethod
    def xerrar(self):
        pass

    @abstractmethod
    def mourem(self):
        pass

    def quisoc(self):
        print(f"Sóc un {self.especie} de {self.edat} anys")

# Subclasses
class Cavall(Animal):
    def xerrar(self):
        print("Neigh!")
    def mourem(self):
        print("El cavall corre")

class Dofí(Animal):
    def xerrar(self):
        print("Click click!")
    def mourem(self):
        print("El dofí neda")

class Abella(Animal):
    def xerrar(self):
        print("Bzzzz")
    def mourem(self):
        print("L'abella vola")
    def picar(self):
        print("L'abella pica!")

class Humà(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        print("Hola!")
    def mourem(self):
        print(f"{self.nom} camina")

class Fiet(Humà):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares  # llista de noms

    def nompares(self):
        print(f"Els pares de {self.nom} són: {', '.join(self.pares)}")

class Centaure(Cavall, Humà):
    def __init__(self, especie, edat, nom):
        Humà.__init__(self, especie, edat, nom)

    def xerrar(self):
        print(f"{self.nom} diu: Neigh i hola!")
    def mourem(self):
        print(f"{self.nom} corre i camina")

class Xou:
    def xerrar(self):
        print("Showtime!")
    def mourem(self):
        print("El xou es mou")
    def quisoc(self):
        print("Sóc un xou")

# Crear elements
llista_elements = [
    Cavall("Cavall", 5),
    Dofí("Dofí", 3),
    Abella("Abella", 1),
    Humà("Humà", 30, "Joan"),
    Fiet("Humà", 5, "Nina", ["Anna", "Pere"]),
    Centaure("Centaure", 20, "CentaureX"),
    Xou()
]

# Bucle que crida els mètodes comuns
for e in llista_elements:
    e.quisoc() if hasattr(e, "quisoc") else None
    e.xerrar()
    e.mourem()
    # Mètodes específics
    if isinstance(e, Abella):
        e.picar()
    if isinstance(e, Fiet):
        e.nompares()
