#1. Função que verifica se o número é par ou ímpar 

#Crie uma função verificar par(num) que receba um número e diga se é par ou ímpar usando if. 
def verificar_par(num):
    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")


#2. Função que retorna o maior de dois números 
#Crie uma função maior(a, b) que devolve qual número é maior usando if/else. 
def maior(a, b):
    if a > b:
        return a
    else:
        return b
    

#3. Função que calcula o fatorial usando FOR 

#Crie uma função fatorial(n) que usa um for para calcular o fatorial de um número. 
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

#4. Função que imprime números de 1 até N usando WHILE 

#Crie uma função contar(n) que utiliza um while para imprimir números até n.
def contar(n):
    i = 1
    while i <= n:
        print(i)
        i += 1

#5. Função que soma valores até o usuário digitar 0 

#Use while + break. 
def somar_valores():
    soma = 0
    while True:
        num = int(input("Digite um número (0 para sair): "))
        if num == 0:
            break
        soma += num
    print(f"A soma dos números digitados é: {soma}")


#6. Função que cria um menu simples 
#Use while para repetir e if para opções: 
#1 – Somar 
#2 – Subtrair
#0 – Sair
def menu():
    while True:
        print("Menu:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"A soma é: {num1 + num2}")
        elif escolha == '2':
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print(f"A subtração é: {num1 - num2}")
        elif escolha == '0':
            print("Saindo do menu.")
            break
        else:
            print("Opção inválida. Tente novamente.")