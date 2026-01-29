print("=" * 30)
print("pagina de login")
print("=" * 30)



def verificação(nome, password):
    nome_fixo = "Bernardo"
    senha_fixa = "123498765"
    if nome == nome_fixo and password == senha_fixa: 
        return "acesso liberado"
    else: 
        return "Usuario nao encontrado ou senha incorreta, tente novamente"

while True:
    usuario = str(input("Digite o nome do usuario: "))

    senha = str(input("Digite sua senha:"))

    print(verificação(usuario,senha))

    resultado = verificação(usuario, senha)
    if resultado == "acesso liberado":
        break
    else:
        pass

