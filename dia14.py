# Dia 14 – Conversor de Moedas**: converte valores entre moedas usando taxas simuladas.
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import Decimal
import time

conversao = CurrencyRates(force_decimal=True)


def dolar(real):
    taxa = conversao.get_rate('USD', 'BRL')
    valor_convertido = conversao.convert("BRL", "USD", real)
    simbolo = CurrencyCodes()
    moeda = simbolo.get_symbol('USD')
    return f"Cotação do Dólar: {moeda}{taxa:.2f}\nO valor desejado ({real}) convertido de BRL para USD, é {moeda}{valor_convertido:.2f}"

def euro(real):
    taxa = conversao.get_rate('EUR', 'BRL')
    valor_convertido = conversao.convert("BRL", "EUR", real)
    simbolo = CurrencyCodes()
    moeda = simbolo.get_symbol('EUR')
    return f"Cotação do Euro: {moeda}{taxa:.2f}\nO valor desejado ({real}) convertido de BRL para EUR , é {moeda}{valor_convertido:.2f}"

def libra_esterlina(real):
    taxa = conversao.get_rate('GBP', 'BRL')
    valor_convertido = conversao.convert("BRL", "GBP", real)
    simbolo = CurrencyCodes()
    moeda = simbolo.get_symbol('GBP')
    return f"Cotação da Libra: {moeda}{taxa:.2f}\nO valor desejado ({real}) convertido de BRL para GBP , é {moeda}{valor_convertido:.2f}"

operacoes = {
    1: dolar,
    2: euro,
    3: libra_esterlina,
}

while True:
    time.sleep(3)
    print("Conversor de moedas")
    print("-" * 40)

    print("Você quer converter em qual moeda?")
    print("1 - Dolar")
    print("2 - Euro")
    print("3 - Libra")
    print("4 - Sair")
    escolha = int(input("Escolha qual você quer converter: "))
    valor = Decimal(input("Digite o valor que você quer converter: "))
    if escolha == 4:
        print("Obrigado por usar")
        break

    funcao = operacoes.get(escolha)
    if funcao:
        print(funcao(valor))
    else:
        print("Opção invalida")

