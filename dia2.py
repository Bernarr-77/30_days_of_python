# Dia 2 – Conversor de Temperatura: converte valores entre Celsius e Fahrenheit usando lógica condicional.

graus_celsius = int(input("Digite a temperatura da sua cidade  "))
nome_da_cidade = input("Digite o nome da sua cidade  ")

conversao = (graus_celsius * 1.8) + 3

print("-------------------------------------------------------")
print(nome_da_cidade)
print(f"°C: {graus_celsius:.1f}")
print(f"°F: {conversao:.2f}")
print("-------------------------------------------------------")
