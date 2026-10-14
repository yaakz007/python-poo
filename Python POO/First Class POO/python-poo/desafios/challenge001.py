from rich import print

# Criar a classe "Funcionário"

class Worker:
    """
    Cria o perfil de cadastro de um funcionário e pode gerar uma apresentação formal.
    """
    # Atributos de classe
    empresa = "WEG"

    def __init__(self, nome = "", setor = "", cargo = ""):
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        print("[bold green]Cadastro realizado com sucesso![/]")

    # Métodos da classe
    def presentation(self):
        return (f"O funcionário [bold blue]{self.nome}[/] trabalha no cargo de [green]{self.cargo}[/] no setor [yellow]{self.setor}[/] da empresa {Worker.empresa}")

# Objetos de teste da classe
f1 = Worker("Lucas", "TI", "Programador")
print(f1.presentation())