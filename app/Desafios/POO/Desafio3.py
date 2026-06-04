class Contador:
    def __init__(self):
        self.valor = 0

    def aumentar(self):
        self.valor += 1

    def diminuir(self):
        self.valor -= 1


# Testando
contador = Contador()

print(contador.valor)  

contador.aumentar()
contador.aumentar()
print(contador.valor)  

contador.diminuir()
print(contador.valor)  