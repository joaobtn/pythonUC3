#import subprocess
import os


#arquivo = open("app\Desafios\Exemplos\dados.txt","r")
#conteudo = arquivo.read()
#print(conteudo)
#arquivo.close()
#leitura

try:

    with open("app\Desafios\Exemplos\dados.txt","r") as arquivo:
        conteudo = arquivo.read()
    print(conteudo)

except FileExistsError:
    print("Arquivo não encontrado!")

#sobrescrever escrita
    with open("app\Desafios\Exemplos\dados.txt","w") as arquivo:
        arquivo.write("Bem vindo ao meu mundo!")

#Adicionar novo conteúdo
    with open("app\Desafios\Exemplos\dados.txt","a") as arquivo:
        arquivo.write("Usuário logado\n")

#Abrindo em uma da minha escolha
os.startfile("app\Desafios\Exemplos\dados.txt")
# subprocess.Popen (["code","app\Desafios\Exemplos\dados.txt"])