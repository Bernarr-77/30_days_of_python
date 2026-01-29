#Dia 4 – Palíndromo: verifica se uma palavra ou frase é igual quando lida ao contrário.
print("-----------------------------------")
print("Verificador de Palíndromo")
print("-----------------------------------")

def verificador(texto):
    texto_limpo = "".join(caracter for caracter in texto if caracter.isalnum())

    texto_minusculo = texto_limpo.lower()

    palindromo = texto_minusculo == texto_minusculo[::-1]
    return palindromo

palavra = input("Digite sua palavra: ")
resultado = verificador(palavra)
print(f"{palavra} é um Palíndromo? {resultado}")