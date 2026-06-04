class Aluno:
    def vouEstudar(self, resposta):
        if resposta == "sim":
            print("Bom estudo!!")
        else:
            print("Acho melhor você estudar")

aluno = Aluno()

resposta = input("Você vai estudar hoje? ")
aluno.vouEstudar(resposta)