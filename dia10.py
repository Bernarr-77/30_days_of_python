# Dia 10 – Contador de Palavras: analisa uma frase e conta palavras.

texto = str(input("Digite a palavra ou texto: "))
letras = texto.split()
contador = len(letras)

print(f"O total de palavras que tem na frase são: {contador}!")