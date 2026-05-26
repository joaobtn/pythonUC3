#Faça um jogo para o usuário adivinhar qual a palavra secreta. Ex:forca / o usuário poderá digitar uma letra / Quando o usuário digitar a letra, você vai conferir se a letra digitada está na palavra secreta (função len) / se a letra digitada não estiver na palavra exiba "*" / se a letra digitada estiver na palavra secreta, exiba a letra. / faça contagem de tentativas do usuário.

# JOGO DA FORCA

palavra_secreta = "python"
letras_acertadas = ""
tentativas = 0

print("=== JOGO DA FORCA ===")

while True:

    letra_digitada = input("Digite uma letra: ").lower()
    tentativas += 1

    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ""

  
    for letra in palavra_secreta:

        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += "*"

    print("Palavra:", palavra_formada)

   
    if len(palavra_formada) == len(palavra_secreta):

        if palavra_formada == palavra_secreta:
            print("\nParabéns! Você acertou!")
            print("Tentativas:", tentativas)
            break