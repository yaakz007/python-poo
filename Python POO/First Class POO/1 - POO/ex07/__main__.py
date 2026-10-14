from funcionarios import FuncionarioHorista, FuncionarioMensalista


def main():
    f1 = FuncionarioMensalista("Lucas Gabriel", 7450)
    f1.calc_sal()
    f1.analisar_sal()
    f2 = FuncionarioHorista("Gabriel Lucas", 75, 180)
    f2.calc_sal()
    f2.analisar_sal()


if __name__ == "__main__":
    main()