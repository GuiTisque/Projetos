from datetime import datetime

class Banco:
    def __init__(self, saldo_inicial=0, limite_diario=1000):
        self.saldo = saldo_inicial
        self.transacoes = []
        self.limite_diario = limite_diario
        self.saque_diario = 0
        self.ultimo_acesso = datetime.now().day

    def deposito(self, valor):
        self.saldo += valor
        self.transacoes.append(f'Depósito: R${valor:.2f}')

    def saque(self, valor):
        hoje = datetime.now().day
        if hoje != self.ultimo_acesso:
            self.saque_diario = 0
            self.ultimo_acesso = hoje

        if self.saque_diario < 3 and valor <= self.limite_diario and self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(f'Saque: R${valor:.2f}')
            self.saque_diario += 1
        elif self.saque_diario >= 3:
            print("Limite de saques diários excedido.")
        elif valor > self.limite_diario:
            print(f"Valor máximo de saque diário permitido é de R${self.limite_diario:.2f}.")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print("Extrato bancário:")
        for transacao in self.transacoes:
            print(transacao)
        print(f"Saldo atual: R${self.saldo:.2f}")

    def saldo_atual(self):
        return self.saldo

def main():
    banco = Banco()

    while True:
        print("\nBem-vindo ao Banco Python")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Saldo")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a ser depositado: "))
            banco.deposito(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a ser sacado: "))
            banco.saque(valor)
        elif opcao == '3':
            banco.extrato()
        elif opcao == '4':
            print(f"Saldo atual: R${banco.saldo_atual():.2f}")
        elif opcao == '5':
            print("Obrigado por utilizar nossos serviços.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
