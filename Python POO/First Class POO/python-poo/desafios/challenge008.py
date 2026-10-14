from abc import ABC, abstractmethod
from math import pi

class Poligono(ABC):
    def __init__(self, lados = 0):
        # Atributos de instância
        self.qtd_lados = lados
    
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado = 0):
        super().__init__(4)
        # Atributos de insância
        self.lado = lado

    def perimetro(self):
        return f"O perímetro do quadrado é {self.lado * 4}"
    
    def area(self):
        return f"A área do quadrado é {self.lado ** 2}"


class Circulo(Poligono):
    def __init__(self, raio = 0): # Circulo não tem lado
        super().__init__(0)
        # Atributos de instância
        self.raio = raio

    def perimetro(self):
        return f"O perímetro do circulo é {self.raio * pi * 2:,.2f}"
    
    def area(self):
        return f"A área do circulo é {pi * self.raio ** 2:,.2f}"
    

q1 = Quadrado(8)
print(q1.area())
print(q1.perimetro())

c1 = Circulo(5)
print(c1.area())
print(c1.perimetro())