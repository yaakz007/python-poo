# Declaração de Classe
class Teste:
    def __init__(self):
        # Atributos de Instância # Método Construtor
        self.nome = ""
        self.idade = 0

    # Método de Instância
    def aniversario(self):
        self.idade += 1
    
    def mensagem(self):
        return f"{self.nome} é maneiro e tem {self.idade} anos de idade. "

# Declaração de Objetos
m1 = Teste()
m1.nome = str(input('Nome: '))
m1.idade = int(input('Idade: '))
m1.aniversario()
print(m1.mensagem())

m2 = Teste()
m2.nome = str(input('Nome: '))
m2.idade = int(input('Idade: '))
m2.aniversario()
print(m2.mensagem())