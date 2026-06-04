#Criando base(planta do objeto)

class Carro:
    def __init__(self,moto,quant_rodas):
        self.moto = moto
        self.quant_rodas = quant_rodas

#Criando objeto
car1 = Carro("v8",4)
car2 = Carro("V6",4)

#Mostrar informações do objeto
print("Carro 1 tem o moto:", car1.moto)
print("Carro 1 tem o moto: ",car2.moto)
car3 = Carro()
car3.moto = "v12" #atribuindo valor a propriedade do objeto
print(car3.moto)
car3.andar() #executando a função(ação) do objeto

#Sem valores obrigatórios
def __init__(self):
    pass

#Iniciar classe com valores padrão
class funcionários:
    nome = ""
    idade = 0
    cargo = "" 

#Outro exemplo

def andar(self):
    print(f"O carro está andando") #ira ativar para informar que o carro está andando

class Cliente:
    def __int__(self, nome,cpf,telefone,email):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email

#Criando objeto

cliente = Cliente(nome="Maria",cpf="108.526.058-52",telefone="5324-5654",email="jasfaf@gmail.com")

print("Nome cliente: ", cliente.nome)
print("CPF cliente: ", cliente.cpf)
print("Telefone cliente: ", cliente.telefone)
print("Telefone cliente: ", cliente.email)

class Aluno:
    def estudar():
        for i in range(5):
            print("Estou estudando")

class Aluno:
    def vouEstudar(resposta):
        if resposta =="sim":
            print("Bom estudo!!")
        else:
            print("Acho melhor você estudar")


aluno = Aluno()
aluno.estudar()
resposta = input("Você vai estudar hoje")
aluno.vouEstudar(resposta)


