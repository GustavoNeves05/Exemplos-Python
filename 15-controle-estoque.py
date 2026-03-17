import os
os.system("cls")

quantidade = int(input("Digite a quantidade de produtos em estoque: "))

if quantidade < 5:
    print("Estoque baixo!")
else:
    print("Estoque OK")