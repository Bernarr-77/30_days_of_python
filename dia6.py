import random 
import time

# numero_aleatorio = random.randint(1,100)


# while True:
#     chute_usuario = int(input("Digite um numero de 1 a 100: "))
#     contador =+ 1
#     if chute_usuario > numero_aleatorio:
#         print("Número muito alto, chute um mais baixo")
#     elif chute_usuario < numero_aleatorio:
#         print("Número muito baixo, chute um mais alto")

#     if chute_usuario == numero_aleatorio:
#         print(f"Parabéns, você acertou o numero correto em {contador} Tentativas!")
#         break
#     else:
#         print("Tente novamente")

"""
Jogo de adivinhação automático com pesquisa binaria
"""

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1 
    contador = 0
    while baixo <= alto:
        contador += 1 
        meio = (baixo + alto) // 2 
        chute = lista[meio]
        time.sleep(2)
        print(f"Esse é o chute número {contador}\nChute: {chute}")
        if chute == item:
            return f"a pesquisa binaria tentou {contador} vezes ate acertar o numero {item}"
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1 
    return f"Número {item} não encontrado na lista"

numero_aleatorio =sorted([random.randint(1,10000)for _ in range(10000)])
item_aleatorio = random.choice(numero_aleatorio)
print (pesquisa_binaria(numero_aleatorio, item_aleatorio))