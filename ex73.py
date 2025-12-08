from abc import ABC, abstractmethod

# ───────── CLASSE ABSTRACTA ─────────

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
        print("Som un", self.especie, "i tenc", self.edat, "anys")


# ───────── SUBCLASSES ─────────

class Cavall(Animal):
    def xerrar(self):
        print("El cavall renilla")

    def mourem(self):
        print("El cavall corre")


class Dofi(Animal):
    def xerrar(self):
        print("El dofí emet sons")

    def mourem(self):
        print("El dofí neda")


class Abella(Animal):
    def xerrar(self):
        print("L'abella zumzeja")

    def mourem(self):
        print("L'abella vola")

    def picar(self):
        print("L'abella pica!")


class Huma(Animal):
    def __init__(self, especie, edat, nom):
        super().__init__(especie, edat)
        self.nom = nom

    def xerrar(self):
        print(self.nom, "parla")

    def mourem(self):
        print(self.nom, "camina")


class Fiet(Huma):
    def __init__(self, especie, edat, nom, pares):
        super().__init__(especie, edat, nom)
        self.pares = pares

    def nompares(self):
        print("Els pares són:", self.pares)


# ───────── HERÈNCIA MÚLTIPLE ─────────

class Centaure(Cavall, Huma):
    def __init__(self, especie, edat, nom):
        Huma.__init__(self, especie, edat, nom)

    def xerrar(self):
        print(self.nom, "xerrra com un centaure")

    def mourem(self):
        print(self.nom, "corre com un cavall")


# ───────── CLASSE INDEPENDENT ─────────

class Xou:
    def xerrar(self):
        print("El xou fa un espectacle")

    def mourem(self):
        print("El xou es mou de manera estranya")

    def quisoc(self):
        print("Som un xou")


# ───────── PROGRAMA PRINCIPAL ─────────

llista = [
    Cavall("Cavall", 5),
    Dofi("Dofí", 8),
    Abella("Abella", 1),
    Huma("Humà", 30, "Joan"),
    Fiet("Humà", 6, "Pau", ["Joan", "Maria"]),
    Centaure("Centaure", 40, "Quiron"),
    Xou()
]

for element in llista:
    element.quisoc()
    element.xerrar()
    element.mourem()

    # Si és una abella, que piqui
    if isinstance(element, Abella):
        element.picar()

    # Si és un fiet, que mostri els pares
    if isinstance(element, Fiet):
        element.nompares()

    print("──────────────")
