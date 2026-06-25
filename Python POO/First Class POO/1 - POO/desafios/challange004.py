from rich import print
from rich.panel import Panel

# Criação de classe
class Livro:
    """
    Simula um livro, e simula a ação de passar as páginas dele.
    """
    def __init__(self, title = "", pag = 0):
        # Atributos de instância
        self.title = title
        self.pag = pag
        self.pag_atual = 1 # Começa na página 1

    # Métodos de classe
    def __str__(self):
        return f"O livro {self.title} foi cadastrado com sucesso!"
    
    def virar(self, n):
        for i in range(n):
            if self.pag_atual < self.pag:
                self.pag_atual += 1
                print(f"[bold cyan]Página {self.pag_atual - 1} → {self.pag_atual}[/]")
            else:
                print(f"[bold red]Você terminou o livro [/][bold green]{self.title}[/].")
                break

# Objetos da classe
l1 = Livro("Harry Negro", 379)
l1.virar(3)
l1.virar(3)
l1.virar(3)
l1.virar(3)
l1.virar(3)
l1.virar(3)
l1.virar(3)
l1.virar(3)