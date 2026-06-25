from rich import print
from rich.panel import Panel
import os

# Função de limpar o terminal
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Criação da classe
class RemoteControl:
    """
    Simula um controle remoto e o funciomante dele;
    """
    canal_min:int = 1
    canal_max:int = 6
    vol_min:int = 1
    vol_max:int = 5

    def __init__(self, canal=1, volume=2):
        self.canal_atual:int = canal
        self.vol_atual:int = volume
        self.estado:bool = False

    def power(self):
        self.estado = not self.estado
        clear()

    def c_mais(self):
        if self.estado:
            if self.canal_atual == RemoteControl.canal_max:
                self.canal_atual = RemoteControl.canal_min
            else:
                self.canal_atual += 1
        clear()
    
    def c_menos(self):
        if self.estado:
            if self.canal_atual == RemoteControl.canal_min:
                self.canal_atual = RemoteControl.canal_max
            else:
                self.canal_atual -= 1
        clear()
    def v_mais(self):
        if self.estado:
            if self.vol_atual != self.vol_max:
                self.vol_atual += 1
        clear()
    def v_menos(self):
        if self.estado:
            if self.vol_atual != self.vol_min:
                self.vol_atual -= 1
        clear()
    def show_tv(self):
        if not self.estado:
            content = f":prohibited: [red]A TV está desligada[/]"
        else:
            content = f"CANAL = "
            for canal in range(RemoteControl.canal_min, RemoteControl.canal_max+1):
                if self.canal_atual == canal:
                    content += f" [yellow on yellow] {canal} [/]"
                else:
                    content += f" {canal} "
            
            content += f"\nVOLUME = "
            for volume in range(RemoteControl.vol_min, RemoteControl.vol_max+1):
                if volume <= self.vol_atual:
                    content += f" [white on black] [/]"
                else:
                    content += f"[black on white] [/]"
        tv = Panel(content, width=30, title="[ TV ]", style="white")
        print(tv)

c = RemoteControl()
while True:
    c.show_tv()
    command = str(input(" < CH >   - VOL + "))
    match command:
        case "0":
            break
        case "@":
            c.power()
        case "-":
            c.v_menos()
        case "+":
            c.v_mais()
        case "<":
            c.c_menos()
        case ">":
            c.c_mais()