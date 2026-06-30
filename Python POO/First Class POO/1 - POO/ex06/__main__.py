from rich import print, inspect
from pessoa import Pessoa
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno("Lucas", 18, "Engenharia de Software", "T01")
    a1.aniversario()
    a1.matricula()

    p1 = Professor("Jośe", 62, "Matemática", "Mestre")
    p1.aniversario()
    p1.dar_aula()

    f1 = Funcionario("Cláudia", 51, "Cordenadora", "Financeiro")
    f1.aniversario()
    f1.bater_ponto()

if __name__ == "__main__":
    main()