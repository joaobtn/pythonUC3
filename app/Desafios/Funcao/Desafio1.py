#Crie uma função verificar_par(num) que receba um número e diga se é par ou ímpar usando if.

def verificar_par(num):
    if num % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

print("Digite um número para verificar se é par ou ímpar:")
input_num = int(input())
verificar_par(input_num)