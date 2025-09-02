class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0  # saldo começa em 0

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")

# Exemplo de uso:
if __name__ == "__main__":
    conta1 = ContaBancaria("Jarla Giovana")
    conta1.exibir_saldo()
