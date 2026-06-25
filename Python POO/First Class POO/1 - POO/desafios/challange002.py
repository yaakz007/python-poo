from rich.panel import Panel
from rich import print

# Criação da classe da etiqueta do produto
class Label:
    """
    Register a product and create a label for it
    """
    def __init__(self, name = "", price = 0):
        # Atributos de instância
        self.name = name
        self.price = price
        print("[bold light green]Cadastro de produto realizado com sucesso!")

    # Métodos da classe
    def label(self):
        content =  f"{self.name.center(35, " ")}"
        content += f"{'-' * 35}"
        pricecon = f"R${self.price:,.2f}"
        content += f"{pricecon.center(35, "-")}"
        label = Panel(content, title="Produto", width=39, style="bold white")
        return label
# Objetos da classe
p1 = Label("Iphone 17", 6000)
print(p1.label())
p2 = Label("Samsung Galaxy S24", 5000)
print(p2.label())