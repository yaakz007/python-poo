from abc import ABC, abstractmethod

def linha():
    print("-" * 30)


class BebidaQuente(ABC):
    def __init__(self):
        pass
    
    def preparar(self):
        print("Sua bebida está sendo preparada.")

    def ferver_agua(self):
        print("Estamos fervendo a água para a sua bebida.")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):
    def __init__(self):
        super().__init__()

    def misturar(self):
        return f"Estamos misturando seu café"
    
    def servir(self):
        return f"Estamos servindo seu café"

class Leite(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        return f"Estamos misturando seu leite"

    def servir(self):
        return f"Estamos servindo seu leite"
    
class Cha(BebidaQuente):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        return f"Estamos misturando seu chá"
    
    def servir(self):
        return f"Estamos servindo seu chá"


# café
c1 = Cafe()
c1.ferver_agua()
c1.preparar()
print(c1.misturar())
print(c1.servir())

linha()
# leite

l1 = Leite()
l1.ferver_agua()
l1.preparar()
print(l1.misturar())
print(l1.servir())

linha()
# chá

c2 = Cha()
c2.ferver_agua()
c2.preparar()
print(c2.misturar())
print(c2.servir())