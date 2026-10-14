from rich import print
from rich.table import Table

table = Table(title="[bold yellow] Tabela de Preços [/]", show_lines=True, style='cyan')
# Comando 'add_column'
table.add_column("[bold red] Nome [/]", style='bold yellow')
table.add_column("[bold red]Idade[/]", style='bold yellow', justify='center')
table.add_column("[bold red]Sexo [/]", style='bold yellow')
# Comando 'add_row' 
table.add_row('Lucas', '18', 'Masculino')
table.add_row('Isadora', '17', 'Feminino')
print(table)