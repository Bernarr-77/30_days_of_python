"""
Tabuada Automática
"""
import time

user_number = int(input("Digite o número que você quer ver a tabuada dele: "))


for numbers in range(1,11):
    resultado = user_number * numbers
    time.sleep(1)
    print(f"{user_number} vezes {numbers} é igual a = {resultado}")
