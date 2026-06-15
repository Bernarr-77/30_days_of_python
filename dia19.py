from itertools import count


class Estoque:
    id_contador = count(1)
    produtos = {}

    def __init__(self, nome, valor, quantidade):
        self.id = next(Estoque.id_contador)
        self.nome = nome
        self.valor = valor
        self.quantidade = quantidade
        Estoque.produtos[self.id] = self

    def adicionar(self, nome, valor, quantidade) -> str:
        if valor > 0:
            self.nome = nome
            self.valor = valor
            self.quantidade = quantidade
            return f"Produto adicionado com sucesso\n{self.id}\n{self.nome}\n{self.valor}\n{self.quantidade}"

    @classmethod
    def buscar_item(cls, nome):
        for produto in cls.produtos.values():
            if produto.nome == nome:
                return f"ID: {produto.id}, Nome: {produto.nome}, Valor: {produto.valor}, Quantidade: {produto.quantidade}"
        return "Produto não encontrado"

    @classmethod
    def deletar_item(cls, id):
        if id in cls.produtos:
            del cls.produtos[id]
            return f"Produto com ID {id} removido com sucesso"
        return "Produto não encontrado"


if __name__ == "__main__":
    while True:
        nome = input("Nome do produto (enter para sair): ").strip()
        if not nome:
            break

        try:
            valor = float(input("Valor do produto: "))
            quantidade = int(input("Quantidade do produto: "))
        except ValueError:
            print("Entrada inválida. Digite um número para valor e inteiro para quantidade.")
            continue

        if valor <= 0 or quantidade < 0:
            print("Valor deve ser maior que 0 e quantidade não pode ser negativa.")
            continue

        produto = Estoque(nome, valor, quantidade)
        print(f"Produto adicionado com sucesso. ID = {produto.id}\n")

    print("\nProdutos cadastrados:")
    for produto in Estoque.produtos.values():
        print(f"ID: {produto.id}, Nome: {produto.nome}, Valor: {produto.valor}, Quantidade: {produto.quantidade}")
