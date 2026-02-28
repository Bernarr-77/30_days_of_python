# Dia 15 – Analisador de Texto**: extrai métricas básicas de um texto.

texto = str(input("Digite o texto: "))
palavras = texto.split()
contador = len(palavras)
contador_caracteres = len(texto.replace(" ", ""))

print(f"O total de palavras que tem na frase são: {contador}! \nO total de caracteres na frase são: {contador_caracteres}")