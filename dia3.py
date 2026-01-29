#Dia 3 – Calculadora de IMC: calcula o IMC do usuário e classifica conforme padrões de saúde.
print("-----------------------------------")
print("Calculadora de IMC")
print("-----------------------------------")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))
sexo = (input("Você é homem ou mulher? "))
imc = peso / (altura **2)

if sexo == "homem":
    if idade >= 2 and idade <= 12:
        print("Procure um pediatra para Calcular com base nas curvas de crescimento da OMS.")
    elif idade >= 13 and idade <= 59:
        print(f"Seu IMC é {imc:.2f}")
        if imc < 18.5:
            print("Você está abaixo do peso")
        elif imc > 18.5 and imc <= 24.9:
            print("Você esta no peso normal")
        elif imc >= 25 and imc <= 29.9:
            print("Você está com sobrepeso")
        elif imc >= 30 and imc <= 34.9:
            print("Você está com Obesidade grau I")
        elif imc >= 35 and imc <= 39.9:
            print("Você está com Obesidade grau II")
        else:
            print("Você está com Obesidade grau III")
    elif idade > 60:
        print(f"Seu IMC é {imc:.2f}")
        if imc <= 22:
            print("O senhor está abaixo do peso")
        elif imc > 22 and imc < 27:
            print("O senhor está no peso adequado")
        else:
            print("O senhor está acima do peso")
else:
    if idade >= 2 and idade <= 12:
        print("Procure um pediatra para Calcular com base nas curvas de crescimento da OMS.")
    elif idade >= 13 and idade <= 59:
        print(f"Seu IMC é {imc:.2f}")
        if imc < 18.5:
            print("Você está abaixo do peso")
        elif imc > 18.5 and imc <= 24.9:
            print("Você esta no peso normal")
        elif imc >= 25 and imc <= 29.9:
            print("Você está com sobrepeso")
        elif imc >= 30 and imc <= 34.9:
            print("Você está com Obesidade grau I")
        elif imc >= 35 and imc <= 39.9:
            print("Você está com Obesidade grau II")
        else:
            print("Você está com Obesidade grau III")
    elif idade > 60:
        print(f"Seu IMC é {imc:.2f}")
        if imc <= 22:
            print("A senhora está abaixo do peso")
        elif imc > 22 and imc < 27:
            print("A senhora está no peso adequado")
        else:
            print("O senhora está acima do peso")