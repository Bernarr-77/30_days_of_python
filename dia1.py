# Dia 1 – Calculadora Simples: aplicação de terminal para realizar operações matemáticas básicas,
#  reforçando entrada, processamento e saída de dados.


print("Calculadora Simples")

escolha_usuario = input("Qual operação matematica você quer realizar?\n digite + ou - :      ")
while True:
    if escolha_usuario == "+":
        try:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
        except ValueError:
            print("Digite um número válido")
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
        Resultado = (num1 + num2)
        print(f"a soma de {num1} + {num2} é igual a: {Resultado}")

    elif escolha_usuario == "-":
        try:
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
        except ValueError:
            print("Digite um número válido")
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
        Resultado = (num1 - num2)
        print(f"a subtração de {num1} - {num2} é igual a: {Resultado}")
    else:
        break
