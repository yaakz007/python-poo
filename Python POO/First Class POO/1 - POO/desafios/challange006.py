from rich import print

# Criação da classe
class Caneta:
    """
    Simula o funcionamento de uma caneta podendo escolher a cor, destampar e tampar a caneta.
    """
    def __init__(self, cor = "blue"):
        # Atributos de classe
        self.cor = cor
        self.situation = 1
    # Métodos de classe
    def __str__(self):
        return f"A caneta na cor {self.cor} foi criada com sucesso!"

    def destampar(self):
        self.situation = 0
    
    def tampar(self):
        self.situation = 1

    def escrever(self, frase):
        if self.situation == 0:
            return f"[bold {self.cor}]{frase}[/]"
        else:
            return f"[bold red]A caneta está tampada[/]"
    
    def quebrar_linha(self, n):
        for i in range(0, n):
            print()

# Objetos de classe
c1 = Caneta("purple")        
c1.destampar()
print(c1.escrever("meu saco é bem macio"))
c1.quebrar_linha(2)
print(c1.escrever("eu quero cagar"))
c1.tampar()
print(c1.escrever("meu cu"))