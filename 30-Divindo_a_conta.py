import os
os.system("cls")

def calcular(total, pessoas):
    return total / pessoas

def encerrar_programa():
    print("Valor inválido")
    input("Pressione Enter para finalizar")
    exit()

print("Seja bem vindo ao App Minha Conta!")

total = float(input("Informe o valor da conta: "))
pessoas = int(input("Digite o número de pessoas: "))

print("\n=== Pressione Enter para calcular ===")
input()

if pessoas > 0:
    resultado = calcular(total, pessoas)
    print(f"Total da conta: R$ {total:.2f}")
    print(f"Número de Pessoas: {pessoas}")
    print(f"Valor por pessoa: R$ {resultado:.2f}")
else:
    encerrar_programa()