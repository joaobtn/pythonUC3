class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# Criando um objeto
p1 = Pessoa("Maria", 25)

# Imprimindo os dados
print("Nome:", p1.nome)
print("Idade:", p1.idade)