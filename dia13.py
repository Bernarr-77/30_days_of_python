# Dia 13 – Gerador de Senhas**: cria senhas seguras com critérios configuráveis.

import random


def gerar_senha(maiscula, especiais):
    caractere = "abcdefghijklmnopqrstuvwxyz"
    if maiscula:
        caractere += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if especiais:
        caractere += "@#.,"
    caractere += "123456789"
    senha_gerada = "".join(random.choices(caractere, k=10,))
    return f"A senha gerada foi: {senha_gerada}"

print("Gerador de senhas")

maiusculas = input("Você quer letras maiúsculas? (s/n): ").lower() == "s"
caractere_especiais = input("Você quer caracteres especiais? (s/n): ").lower() == "s"
print(gerar_senha(maiusculas, caractere_especiais))

