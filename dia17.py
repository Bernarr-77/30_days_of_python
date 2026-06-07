class Banco:
    def __init__(self, nome, saldo_inicial = 0):
        self.nome = nome
        self.saldo = saldo_inicial
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.\nNovo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.\nNovo saldo: R$ {self.saldo:.2f}")
        else:
            print(f"Valor invalido ou maior que seu saldo,\nsaldo atual: {self.saldo}")

    def ver_saldo(self):
        print(f"saldo atual: {self.saldo}")

conta = Banco("Sua Conta", 1000)

print("BANCO -----------------------")
print("Insira o numero para a operação correspondente: ")
print("1 - Depositar")
print("2 - Sacar")
print("3 - Ver saldo")
print("4 - Sair")
while True:
    resposta = input("Digite a sua escolha: ")
    if resposta == "1":
        valor = float(input("Digite o valor a depositar: "))
        conta.depositar(valor)
    elif resposta == "2":
        valor = float(input("Digite o valor a sacar: "))
        conta.sacar(valor)
    elif resposta == "3":
        conta.ver_saldo()
    elif resposta == "4":
        break
    else:
        print("Opção inválida!")
