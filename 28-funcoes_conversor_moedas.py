import os
os.system("cls")


def exibir_menu():
    print("=== Conversor de Moedas ===")
    print("[1] - Converter Dolar -> Real")
    print("[2] - Converter Real -> Dolar")
    print("[3] - Sair")


def limpar_tela():
    os.system("cls")


def converter_dolar_para_real(quantia_dolar, cotacao):
    total_reais = quantia_dolar * cotacao
    return total_reais


def converter_real_para_dolar(quantia_real, cotacao):
    total_dolares = quantia_real / cotacao
    return total_dolares


def Sair():
    exit()