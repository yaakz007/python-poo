
from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    salario_minimo = 1612
    inss = 7.5

    def __init__(self, nome=None):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.salario_minimo

        msg = (
            f"O salário de [blue]{self.nome}[/] é de "
            f"[green]R${self.salario:.2f}[/] e corresponde a "
            f"[yellow]{base:.1f} salários mínimos[/]."
        )

        painel = Panel(
            msg,
            title="Análise de salário",
            width=60
        )

        print(painel)


class FuncionarioHorista(Funcionario):
    def __init__(self, nome=None, valor_hora=7.37, qtd_horas=220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_horas
        self.salario_bruto = valor_hora * qtd_horas

    def calc_sal(self):
        desconto = self.salario_bruto * Funcionario.inss / 100
        self.salario = self.salario_bruto - desconto


class FuncionarioMensalista(Funcionario):
    def __init__(self, nome=None, salario_bruto=Funcionario.salario_minimo):
        super().__init__(nome)
        self.salario_bruto = salario_bruto

    def calc_sal(self):
        desconto = self.salario_bruto * Funcionario.inss / 100
        self.salario = self.salario_bruto - desconto