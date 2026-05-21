#Crie uma função maior(a, b) que devolve qual número é maior usando if/else.

def maior(a, b):
    if a > b:
        return a
    else:
        return b
    
    print("Digite dois números para verificar qual é maior:")
input_a = int(input("Digite o primeiro número: "))
input_b = int(input("Digite o segundo número: "))
resultado = maior(input_a, input_b)
print(f"O número maior é: {resultado}")
