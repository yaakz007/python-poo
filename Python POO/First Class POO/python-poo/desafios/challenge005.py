from rich import print
from rich.panel import Panel

# Criação da classe
class Gamer:
    """
    Cria uma ficha de um gamer com seu nome, nick e jogos favoritos;
    """
    def __init__(self, nome = "", nick = "", *jogos):
        # Atributos de instância
        self.nome = nome
        self.nick = nick 
        self.jogos = jogos
    
    # Métodos da classe
    def add_fav(self):
        content = f"Nome: {self.nome}\n"
        content += f"Jogos favoritos:\n"
        for n in sorted(self.jogos):
            content += f"🎮 {n}\n"
        label = Panel(content, title=f"Player <{self.nick}>", width=50, style="bold cyan")
        return label

# Objetos de classe
p1 = Gamer("Lucas", "kzz017", "Fortnite", "God of War", "Minecraft", "Cyberpunk 2077", "The Last of Us Part: II", "Red Dead Redemption 2")
print(p1.add_fav())

p2 = Gamer("Isadora", "isaaa", "Block Blast", "Fortnite", "Roblox", "Minecraft", "The Last of Us Part: II")
print(p2.add_fav())