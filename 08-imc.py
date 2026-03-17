# 08-imc.py
import os
os.system("cls")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print("Seu IMC é:", round(imc, 2))

if imc < 16.9:
    print("Classificação: Muito abaixo do peso")
elif imc >= 17 and imc <= 18.4:
    print("Classificação: Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Classificação: Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Classificação: Acima do peso")
elif imc >= 30 and imc <= 34.9:
    print("Classificação: Obesidade grau I")
elif imc >= 35 and imc <= 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")