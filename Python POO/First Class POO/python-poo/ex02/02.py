# Declaração de Classe
class Pessoa:
    """
    Essa classe cria uma pessoa, que pode ter nome e idade:

    Para usar basta utilizar o comando:
    variavel = Pessoa(nome, idade)
    """
    def __init__(self, nome = "", idade = 0):
        # Atributos de Instância # Método Construtor
        self.nome = nome
        self.idade = idade

    # Método de Instância
    def aniversario(self):
        self.idade += 1
    
    def __str__(self): # Dunder Method
        return f"{self.nome} é maneiro e tem {self.idade} anos de idade. "
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"

# Declaração de Objetos
p1 = Pessoa("Lucas", 18)
p1.aniversario()
print(Pessoa.__doc__)
print(p1.__dict__)
print(p1.__getstate__())
print(p1.__class__)