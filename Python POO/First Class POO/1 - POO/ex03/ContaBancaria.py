class Banco:
    """
Cria uma conta bancária e permite fazer saques e depósitos.
    """
    def __init__(self, id = 0, nome_titular = "", saldo = 0):
        # Atributos da classe
        self.id = id
        self.titular = nome_titular
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}.")
    
    # Métodos da classe
    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} na conta."

    def saque(self, valor):
        if valor > self.saldo:
            print('\033[31mErro: Saldo insuficiente.\033[m')
        else:
            self.saldo -= valor
    
    def deposito(self, valor):
        self.saldo += valor
    
eu = Banco(112, "Lucas", 7346)
eu.saque(3075)
eu.deposito(54)
print(eu)