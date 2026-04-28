


def main():
    exibir_menu()
    limpar_tela()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        quantia_dolar = float(input("Informe a quantidade de dolares: "))
        cotacao = float(input("Informe a cotação: "))
        print(converter_dolar_para_real(quantia_dolar, cotacao))

    elif opcao == 2:
        quantia_real = float(input("Informe a quantidade de reais: "))
        cotacao = float(input("Informe a cotação: "))
        print(converter_real_para_dolar(quantia_real, cotacao))

    elif opcao == 3:
        Sair()


main()