import os 
os.system("cls")

print("Exemplo abilitação com while")

resposta = "Sim"

while (resposta == "Sim"):


    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))


    if(idade >= 18):
        habilitacao = int(input("Possui Habilitação? (1 - sim ou 2 - Não):"))

        if(habilitacao == 1):
            print("Você pode dirigir")
        else:
            print("Você não possui Habilitação")
    else:
        print("Você é menor de idade")
    resposta = input("Você gostaria de executar novamente? (Sim ou Não:")
print("Fim do programa, espero ter ajudado:")