pessoa = {
    "nome" : "Ana",
    "cpf" : "542.546.212-56",
    "telefone" : 21955654759
}
print(pessoa)
print(pessoa["cpf"])
pessoa["nome"] = "Luiz" #alterei o valor
print(pessoa["nome"])

for chave, valor in pessoa.items():
    print(f"Seu {chave} é {valor}")

pessoa.update(["nome": "Jair", "cpf": "456.567.879-21", "telefone": 2197536-5689])