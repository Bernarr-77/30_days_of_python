valor1, valor2 = 0,1
usuario = int(input("Quantos termos? "))

count = 0
print(f"Sequência de Fibonacci ({usuario} termos):")
for _ in range(usuario):
    print(valor1, end=" ")
    # Atualiza os valores: o próximo é a+b, o atual vira b
    valor1, valor2 = valor2, valor1 + valor2


 