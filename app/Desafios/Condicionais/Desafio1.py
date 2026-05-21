#1.	Verificação de login básico
#Pergunte ao usuário um nome de usuário.
#Se fore igual a admin, exiba Acesso permitido.
#Caso contrário, não mostro e nada por enquanto.

usuario = input("Digite o nome de usuário: ")

if usuario == "admin":
    print("Acesso permitido")
else:
    print("Acesso negado por enquanto")

