from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import os

# Criação das funções do programa

console = Console()

# Criação de uma função pra limpar o terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Criação da tabela do mini programa
tables = Table(title="[bold orange] Cadastro de Pessoas [/]", show_lines=True, style='purple')
tables.add_column('Nome', style='green')
tables.add_column('Idade', style='green', justify='center')
tables.add_column('Sexo', style='green', justify='center')
#print(tables)

# Criação da classe

class Pessoa:
    """
    Cria/preenche o cadastro de uma pessoa;
    """
    def __init__(self, nome, idade, sexo):
        # Atributos da classe
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

# Out class

pessoas = []

# Criação do mini programa

while True:
    clear()
    conteudo = Text("Cadastro de Pessoas", style="bold orange1", justify="center")
    print(Panel(conteudo, style='purple', width=30, height=3))

    # Verificação do nome como string
    while True:
        nome = console.input('[bold blue]Nome: [/]')
        if not nome.isalpha():
            print('[bold red] O campo "Nome" só pode conter letras. [/]')
            continue
        else: 
            break
    
    # Verificação da idade como int
    try:
        idade = int(console.input('[bold blue]Idade: [/]'))
    except ValueError:
        print('[bold red]Idade precisa ser um número.[/]')

    # Verificação do campo sexo como M ou F
    while True:
        sexo = console.input('[bold blue]Sexo [M/F]: [/]').upper()
        if sexo == 'M' or sexo == 'F':
            break
        else:
            print('[bold red]Digite apenas [M] para Masculino ou [F] para Feminino.[/]')
    
    # Guardar pessoa/cadastrar pessoa como objeto;
    pessoa = Pessoa(nome, idade, sexo)
    pessoas.append(pessoa)

    # Verificação de continuação
    while True:
        continuar = console.input("[bold blue]Cadastrar outro? (s/n): [/]").lower()
        if continuar == 's' or continuar == 'n':
            break
        else:
            print('[bold red]Digite apenas [S] para sim ou [N] para não.[/]')

    if continuar == 'n':
        break

# Criação da tabela;
table = Table(title='[bold orange] Pessoas Cadastradas [/]', show_lines=True, style='purple')

# Criação das colunas da tabela;
table.add_column('[bold orange] Nome [/]', style='green')
table.add_column('[bold orange] idade [/]', style='green')
table.add_column('[bold orange] Sexo [/]', style='green')

# Uso do comando for para percorrer a lista de dicionários e preenche-la
for i in pessoas:
    table.add_row(i.nome, str(i.idade), i.sexo)
clear()
print(table)