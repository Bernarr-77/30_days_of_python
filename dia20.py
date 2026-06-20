"""
criar jogo de rpg com classes

passos:
1 - criar classe personagem
com os atributos:
id
nome
vida
dano
velocidade

2 - criar funcao:
para criar o personagem com stats aleatorios com o usario passando somente o nome
3 - mostrar o personagem
4 - criar um personagem aleatorio do computador
5 - criar uma classe para ataques com 3 opçoes sendo herdada do personagem
6 - dar 4 ataques para o usuario escolher
7 - dar 4 ataques para o bot
8 - funcao de luta com while true
9 - luta com turno, basendo com vida -=ataque com o usario mais rapido atacando primeiro e so acabando quando alguem perder
10 - bot ataca aleatoriamente, usario escolhe ataque
"""
from itertools import count
import random
from faker import Faker

fake = Faker("pt_BR")

class Personagem:
    id_contador = count(1)

    def __init__(self, nome):
        self.id = next(Personagem.id_contador)
        self.nome = nome
        self.vida = random.randint(400, 500)
        self.quantidade_soco = 0
        self.ataques = {1: self.soco, 2: self.chute, 3: self.super_soco}

    def soco(self, alvo):
        dano = random.randint(110,150)
        alvo.vida -= dano
        return alvo.vida

    def chute(self, alvo):
        dano = random.randint(120,170)
        alvo.vida -= dano
        return alvo.vida

    def super_soco(self, alvo):
        dano = random.randint(190,220)
        limite = 1
        if self.quantidade_soco < limite:
            alvo.vida -= dano
            self.quantidade_soco += 1
            return alvo.vida
        return "Não pode usar denovo"


class Bot:
    id_contador = count(1)

    def __init__(self):
        self.id = next(Bot.id_contador)
        self.nome = fake.name()
        self.vida = random.randint(400, 500)
        self.quantidade_soco = 0
        self.ataques = {1: self.soco, 2: self.chute, 3: self.super_soco}

    def soco(self, alvo):
        dano = random.randint(110,150)
        alvo.vida -= dano
        return alvo.vida


    def chute(self, alvo):
        dano = random.randint(120,170)  
        alvo.vida -= dano
        return alvo.vida

    def super_soco(self, alvo):
        dano = random.randint(190,220)
        limite = 1
        if self.quantidade_soco < limite:
            alvo.vida -= dano
            self.quantidade_soco += 1
            return alvo.vida
        return None
    
ataque_bot = True
ataque_user = False
user = Personagem(nome="Bernardin")
bot = Bot()
while True:

    if ataque_user == False:
        print(f"Sua vez!    sua vida: {user.vida}")
        print("Escolha seu ataque:")
        print("1 - soco")
        print("2 - chute")
        print("3 - super soco")
        escolha = int(input("qual? "))
        if escolha == 1:
            ataque = user.ataques.get(escolha)
            ataque(bot)
            ataque_user = True
            ataque_bot = False
        elif escolha == 2:
            ataque = user.ataques.get(escolha)
            ataque(bot)
            ataque_user = True
            ataque_bot = False
        elif escolha == 3:
            verificacao = user.quantidade_soco
            if verificacao > 0:
                print("Você ja usou super soco, use outro")
            else:
                ataque = user.ataques.get(escolha)
                ataque(bot)
                ataque_user = True
                ataque_bot = False
        else:
            print("Escolha opçao coprrespondente")
    verificar_vida_bot = bot.vida
    if verificar_vida_bot <= 0:
        print(f"{user.nome} Ganhou a luta, Parabens!")
        break

    if ataque_bot == False:
        print(f"Vida do {bot.nome}: {bot.vida}")
        ataque_aleatorio = random.randint(1, 3)
        if ataque_aleatorio == 1:
            ataque = bot.ataques.get(ataque_aleatorio)
            ataque(user)
            print(f"Bot usou soco")
            ataque_user = False
            ataque_bot = True
        elif ataque_aleatorio == 2:
            ataque = bot.ataques.get(ataque_aleatorio)
            ataque(user)
            print(f"Bot usou chute")
            ataque_user = False
            ataque_bot = True
        elif ataque_aleatorio == 3:
            verificacao = bot.quantidade_soco
            if verificacao > 0:
                ataque_aleatorio = random.randint(1,2)
            else:
                ataque = bot.ataques.get(ataque_aleatorio)
                ataque(user)
                print(f"Bot usou super soco")
                ataque_user = False
                ataque_bot = True
    verificar_vida_user = user.vida
    if verificar_vida_user <= 0:
        print(f"{bot.nome} ganhou a luta")
        break
        
        
        
