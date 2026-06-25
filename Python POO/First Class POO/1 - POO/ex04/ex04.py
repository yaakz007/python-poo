from rich import print, inspect

# Aula de herança


class Pessoa:
    def __init__(self, nome = "", idade = 0):
        # Atributos de instância
        self.nome = nome 
        self.idade = idade

    # Métodos da classe
    def aniversario(self):
        self.idade += 1


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        # Atributos de instância
        self.curso = curso
        self.turma = turma

    # Métodos da classe
    def matricula(self):
        print(f"{self.nome} acabou de se matricular.")


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        # Atributos de instância
        self.especialidade = especialidade
        self.nivel = nivel
    
    # Métodos da classe
    def dar_aula(self):
        print(f"O professor {self.nome} começou a dar aula.")


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        # Atributos de instância
        self.cargo = cargo 
        self.setor = setor
    
    # Métodos da classe
    def bater_ponto(self):
        print(f"{self.nome} bateu o ponto.")

a1 = Aluno("Lucas", 18, "Engenharia de Software", "T01")
a1.aniversario()
inspect(a1, methods=True)