import os
os.system("cls")

def escreva():
    print("Olá Mundo")

def exibir_dados(nome, idade, email):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Email: {email}")
    print("=" * 200)

def somar(num1, num2):
    resultado = num1 + num2
    return resultado

escreva()

exibir_dados("Caio", 38, "caio@gmail.com")
exibir_dados("Jorge", 16, "Jorge@gmail.com")

total = somar(10, 20)
print(f"O total será: {total}")