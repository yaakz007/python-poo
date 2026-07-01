from pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        # Atributos de instância
        self.cargo = cargo 
        self.setor = setor
    
    # Métodos da classe
    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto.")