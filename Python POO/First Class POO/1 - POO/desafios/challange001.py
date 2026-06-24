from rich import print

# Criar a classe "Funcionário"

class Worker:
    """
    Cria o perfil de cadastro de um funcionário e pode gerar uma apresentação formal.
    """
    def __init__(self, nome = "", setor = "", cargo = ""):
        # Atributos de classe
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        print("[bold green]Cadastro realizado com sucesso![/]")

    # Métodos da classe
    def presentation(self):
        return (f"O funcionário {self.nome} trabalha no cargo de {self.cargo} no setor {self.setor}.")

# Objetos de teste da classe
f1 = Worker("Lucas", "TI", "Programador")
print(f1.presentation())