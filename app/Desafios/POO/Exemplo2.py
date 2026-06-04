class Carro:
    def __init__(self, moto, quant_rodas):
        self.moto = moto
        self.quant_rodas = quant_rodas

    def andar(self):
        return f"O carro com motor {self.moto} está andando."

    def buzinar(self):
        return "Biiiiii!"

car1 = Carro("V8", 4)

print(car1.andar())
print(car1.buzinar())