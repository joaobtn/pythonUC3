class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)


# Teste
produto = Produto("Notebook", 3000)

print(f"Preço original: R$ {produto.preco:.2f}")

produto.aplicar_desconto(10)

print(f"Preço com desconto: R$ {produto.preco:.2f}")