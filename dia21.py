with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("segunda linha\n")

with open("exemplo.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("Viaja nao zz")