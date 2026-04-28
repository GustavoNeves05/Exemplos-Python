import os 
os.system("cls")

numero= int(input("digite um numero:"))
limite_da_tabuada = int(input("Digite o limite da tabuada:"))

contador = 0
while(contador <=  10):
    print(f"{numero} * {contador} = {numero * contador}")
    contador+=1