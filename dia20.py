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
    ataques = {
        1: soco,
        2: chute,
        3: super_soco
    }

    def __init__(self,nome,vida,velocidade):
        self.id = next(Personagem.id_contador)
        self.nome = nome
        self.vida = vida
        self.velocidade = velocidade
        Personagem.ataques[self.id] = self

    def criar_personagem_usuario(self, nome):
        self.vida = random.randint(400,500)
        self.ataques = Personagem.ataques
        self.nome = nome
        self.velocidade = random.randint(100,200)

    def personagem_bot(self):
        self.nome = fake.name()
        self.ataques = Personagem.ataques
        self.velocidade = random.randint(100,200)



