from rich import print
from rich.panel import Panel
import os


def clear():
    """Limpa o terminal (interface, não faz parte da classe)."""
    os.system('cls' if os.name == 'nt' else 'clear')


class RemoteControl:
    """
    Simula um controle remoto e o funcionamento dele.

    Canal, volume e estado ficam protegidos (_atributo) e só mudam
    por propriedades ou métodos que respeitam os limites.
    """
    # Atributos de classe (iguais para todos os controles)
    canal_min: int = 1
    canal_max: int = 6
    vol_min: int = 1
    vol_max: int = 5

    def __init__(self, canal=1, volume=2):
        # Atributos de instância protegidos; passam pelos setters (validam)
        self._canal = RemoteControl.canal_min
        self._volume = RemoteControl.vol_min
        self._estado = False
        self.canal = canal
        self.volume = volume

    # ---------- Getters e setters ----------
    @property
    def canal(self):
        return self._canal

    @canal.setter
    def canal(self, novo_canal):
        if not RemoteControl.canal_min <= novo_canal <= RemoteControl.canal_max:
            raise ValueError(
                f"Canal deve estar entre {RemoteControl.canal_min} e {RemoteControl.canal_max}."
            )
        self._canal = novo_canal

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, novo_volume):
        if not RemoteControl.vol_min <= novo_volume <= RemoteControl.vol_max:
            raise ValueError(
                f"Volume deve estar entre {RemoteControl.vol_min} e {RemoteControl.vol_max}."
            )
        self._volume = novo_volume

    @property
    def estado(self):
        # Só getter: o estado muda apenas pelo método power()
        return self._estado

    # ---------- Ações do controle ----------
    def power(self):
        self._estado = not self._estado

    def c_mais(self):
        if self._estado:
            if self._canal == RemoteControl.canal_max:
                self._canal = RemoteControl.canal_min
            else:
                self._canal += 1

    def c_menos(self):
        if self._estado:
            if self._canal == RemoteControl.canal_min:
                self._canal = RemoteControl.canal_max
            else:
                self._canal -= 1

    def v_mais(self):
        if self._estado and self._volume < RemoteControl.vol_max:
            self._volume += 1

    def v_menos(self):
        if self._estado and self._volume > RemoteControl.vol_min:
            self._volume -= 1

    # ---------- Exibição ----------
    def show_tv(self):
        if not self._estado:
            content = ":prohibited: [red]A TV está desligada[/]"
        else:
            content = "CANAL = "
            for canal in range(RemoteControl.canal_min, RemoteControl.canal_max + 1):
                if self._canal == canal:
                    content += f" [yellow on yellow] {canal} [/]"
                else:
                    content += f" {canal} "

            content += "\nVOLUME = "
            for volume in range(RemoteControl.vol_min, RemoteControl.vol_max + 1):
                if volume <= self._volume:
                    content += " [white on black] [/]"
                else:
                    content += "[black on white] [/]"
        tv = Panel(content, width=30, title="[ TV ]", style="white")
        print(tv)


if __name__ == "__main__":
    c = RemoteControl()
    aviso = ""
    while True:
        clear()
        c.show_tv()
        if aviso:
            print(aviso)
            aviso = ""
        command = input(f" < CH{c.canal} >   - VOL{c.volume} + ")
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
            case "#":  # pula direto para um canal (usa o setter)
                if c.estado:
                    try:
                        c.canal = int(input("Canal: "))
                    except ValueError:
                        aviso = (f"[red]Canal inválido. Use um número de "
                                 f"{RemoteControl.canal_min} a {RemoteControl.canal_max}.[/]")