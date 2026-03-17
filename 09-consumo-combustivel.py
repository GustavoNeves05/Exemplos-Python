import os
os.system("cls")

km = float(input("Digite quantos quilômetros foram percorridos: "))
litros = float(input("Digite a quantidade de litros de combustível gastos: "))

consumo_medio = km / litros

print(f"O consumo médio do veículo é {consumo_medio:.2f} km/l")