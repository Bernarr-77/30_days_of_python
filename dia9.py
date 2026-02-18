# – Menu Interativo: sistema de menu em loop com múltiplas opções.

print("=" * 30)
print("Banco")
print("=" * 30)

conta = 100
def depositar():
    valor = int(input("Qual o valor que você quer adicionar? "))
    global conta
    conta += valor
    print(f"O valor de {valor} foi adicionado a sua conta")
    return f"O saldo da sua conta agora é: {conta}"

def enviar_dinheiro():
    global conta
    pessoa = input("Para quem você quer enviar dinheiro? ")
    while True:
        valor = int(input(f"Qual valor você deseja enviar para {pessoa}? "))
        if valor <= conta:
            conta -= valor
            print(f"O valor desejado foi enviado para {pessoa}")
            return f"O saldo da sua conta agora é: {conta}"
        else:
            print("Digite um número válido!")

def sacar():
        global conta
        while True:
            valor = int(input("Qual o valor que você quer sacar? "))
            if valor <= conta:
                conta -= valor
                print(f"O valor de {valor} foi sacado")
                return f"O saldo da sua conta agora é: {conta}"
            else:
                print("Digite um número válido!")
while True:
    print("=" * 30)
    print("Digite um número com a opção que vc quer:")
    print(" 1 - Adicionar saldo a conta")
    print(" 2 - Enviar dinheiro")
    print(" 3 - Sacar dinheiro")
    print(" 4 - Sair")
    print("=" * 30)
    try:
        opcao = int(input("Digite o número: "))
        if opcao < 1 or opcao > 4:
            print("Digite um número válido!")
            continue
    except ValueError:
        print("Digite um número válido!")
        continue
    
    if opcao == 1:
        print(depositar())
    elif opcao == 2:
        print (enviar_dinheiro())
    elif opcao == 3:
        print(sacar())
    else:
        break
print("Obrigado!")
