from rich import print
from rich.panel import Panel

# Criação da classe

class Churrasco:
    """
    Cria uma média de gastos em um churrasco de acordo com a quantidade de convidados;
    """
    def __init__(self, title = "", quant = 0):
        # Atributos de classe
        self.title = title
        self.quant = quant
    
    # Métodos de classe
    def __str__(self):
        return f"O churrasco {self.title} foi cadastrado com sucesso!"
    
    def alalyse(self):
        totmeat = (self.quant * 400) / 1000
        p = totmeat * 82.40
        ppp = p / self.quant
        ok = f"Analisando {self.title} com {self.quant} convidados.\n"
        ok += f"Cada participante comerá 0.4Kg e cada Kg custa R$82.40\n"
        ok += f"Recomendo comprar um total de {totmeat:g}Kg de carne\n"
        ok += f"O custo total será de R${p:,.2f}\n"
        ok += f"Resultando em R${ppp:,.2f} por pessoa"
        label = Panel(ok, title=f"{self.title}", style="bold white", width=60)
        return label


# Objetos da classe
c1 = Churrasco()
c1.title = input("Qual o nome do evento? ")
c1.quant = int(input('Quantas pessoas vão comparecer ao evento? '))
print(c1.alalyse())