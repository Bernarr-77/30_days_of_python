# valida CPFs com regras matemáticas.


def remover_formatacao_cpf(cpf: str) -> str:
    return "".join(caractere for caractere in cpf if caractere.isdigit())


def calcular_digito_verificador(numeros: str, peso_inicial: int) -> int:
    soma_total = 0
    peso_atual = peso_inicial

    for numero in numeros:
        soma_total += int(numero) * peso_atual
        peso_atual -= 1

    resto_divisao = soma_total % 11

    if resto_divisao < 2:
        return 0
    else:
        return 11 - resto_divisao


def validar_cpf(cpf: str) -> bool:
    cpf_limpo = remover_formatacao_cpf(cpf)


    if len(cpf_limpo) != 11:
        return False

    if cpf_limpo == cpf_limpo[0] * 11:
        return False

    nove_primeiros_digitos = cpf_limpo[:9]
    digitos_verificadores_informados = cpf_limpo[9:]


    primeiro_digito = calcular_digito_verificador(
        nove_primeiros_digitos, 10
    )


    segundo_digito = calcular_digito_verificador(
        nove_primeiros_digitos + str(primeiro_digito), 11
    )

    digitos_verificadores_calculados = (
        str(primeiro_digito) + str(segundo_digito)
    )

    return digitos_verificadores_calculados == digitos_verificadores_informados