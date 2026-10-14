from challange010 import Transporte, Moto, Caminhao, Drone
from rich import print, inspect
from rich.table import Table


def main():
    dist = int(input('Distância do frete: '))
    
    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]

    planilha = Table(title="Fretes")
    planilha.add_column("Distância")
    planilha.add_column("Tipo")
    planilha.add_column("Frete")

    for item in viagem:
        planilha.add_row(f"{dist}km", f"{type(item).__name__}", f"{item.calc_frete()}")
    
    print(planilha)



if __name__ == "__main__":
    main()