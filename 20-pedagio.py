import os
os.system("cls")

print("Escolha o tipo de veículo:")
print("1 - Carro")
print("2 - Moto")
print("3 - Caminhão")

tipo = int(input("Digite a opção: "))

if tipo == 1:
    print("Pedágio: R$10")
elif tipo == 2:
    print("Pedágio: R$5")
elif tipo == 3:
    print("Pedágio: R$20")
else:
    print("Tipo inválido")