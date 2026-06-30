class Pessoa:
    def __init__(self, nome = "", idade = 0):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade

    # Métodos da classe
    def aniversario(self):
        self.idade += 1