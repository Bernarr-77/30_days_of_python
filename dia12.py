# Calculadora Modular: calculadora com funções independentes para cada operação.

print("Calculadora Modular")
print("-" * 30)

def soma():
     a = float(input("Primeiro número: "))
     b = float(input("Segundo número: "))
     return f"O resultado de {a} + {b} é {a + b}"

def subtracao():
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    return f"O resultado de {a} - {b} é {a - b}"

def divisao():
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    return f"O resultado de {a} dividido {b} é {a / b}"

def multiplicacao():
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))
    return f"O resultado de {a} multiplicado por {b} é {a * b}"

operacoes = {
    1: soma,
    2: subtracao,
    3: divisao,
    4: multiplicacao
}

while True:
    print("Qual função você quer utilizar?")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("5 - Sair")
    escolha = int(input("Digite a opção que você deseja: "))
    if escolha == 5:
        print("Obrigado por usar!")
        break
    

    funcao = operacoes.get(escolha)
    if funcao: 
        print(funcao())
    else:
        print("Opção invvalida")



