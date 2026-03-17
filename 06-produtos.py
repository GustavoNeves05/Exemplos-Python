import os
os.system("cls")

descricao = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco = float(input("Digite o preço unitário: "))

# cálculo do total sem desconto
total = quantidade * preco

# cálculo do desconto
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade > 5 and quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05

# total a pagar
total_pagar = total - desconto

# saída
print("\nProduto:", descricao)
print("Total sem desconto:", total)
print("Desconto:", desconto)
print("Total a pagar:", total_pagar)