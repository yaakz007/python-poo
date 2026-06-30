from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        # Atributos de instância
        self.curso = curso
        self.turma = turma

    # Métodos da classe
    def matricula(self):
        print(f"{self.nome} acabou de se matricular.")