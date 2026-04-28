import os
os.system("cls")

def somar(numero1, numero2):  
    return numero1 + numero2

def subtrair(numero1, numero2):  # padronizado para minúsculo
    return numero1 - numero2

def Multiplicar(numero1, numero2):
    resultado = numero1 * numero2
    return resultado

def Dividir(numero1, numero2):
    resultado = numero1 / numero2
    return resultado

def encerrar_programa():
    print("Operação inválida")
    input("Pressione Enter para finalizar")
    exit()

print("Seja bem vindo a super calculadora 2.0 pro max")

numero1 = int(input("Informe primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

print("Escolha uma das opções abaixo:")
print("[1] - Somar")
print("[2] - Subtrair")
print("[3] - Multiplicar")
print("[4] - Dividir")

opcao = int(input("Escolha uma opção: "))  

if opcao == 1:
    print(f"A soma é: {somar(numero1, numero2)}") 
elif opcao == 2:
    print(f"A subtração é: {subtrair(numero1, numero2)}")
elif opcao == 3:
    print(f"A multiplicação é: {Multiplicar(numero1, numero2)}")
elif opcao == 4:
    print(f"A Divisão é: {Dividir(numero1, numero2)}")
else:
    encerrar_programa()
