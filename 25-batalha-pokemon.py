import os
import random

os.system("cls")

while True:
    input("Aperte <enter> para iniciar")
    print("O jogo começou!")

    
    opcoes = input("Selecione seu monstro inicial:\n 1 - Charmander \n 2 - Squirtle \n 3 - Bulbassauro \nOpção: ")

    if opcoes == "1":
        print("Charmander foi o escolhido!")
        meu_time = "Charmander"
    elif opcoes == "2":
        print("Squirtle foi o escolhido!")
        meu_time = "Squirtle"
    else:
        print("Bulbassauro foi o escolhido!")
        meu_time = "Bulbassauro"

    input("Aperte (enter) para prosseguir:")
    print("O oponente está decidindo...")

    lista_pokes = ["Charmander", "Squirtle", "Bulbassauro"]
    rival_choice = random.choice(lista_pokes)

    while rival_choice == meu_time:
        rival_choice = random.choice(lista_pokes)

    print(f"O seu adversário optou por:", rival_choice)

    energia_player = 100
    energia_rival = 100
    rodada = 1

    print(f"Duelo confirmado: {meu_time} CONTRA {rival_choice}")

    while energia_player > 0 and energia_rival > 0:
        print(f"\n --- Rodada {rodada} ---")
        print(f"Seu Vigor: {energia_player} | Vigor do Rival: {energia_rival}")
        print("=" * 25)

        # Fase do jogador
        print("Qual sua estratégia?")
        print("1 - Golpear")
        print("2 - Regenerar")
        print("3 - Escapar")
        
        comando = input("Sua decisão: ")
        
        if comando == "1":
            energia_rival -= 10
            print(f"Você desferiu um golpe no {rival_choice}!")
        elif comando == "2":
            energia_player += 5
            print("Você usou regeneração, recuperando +5 de vigor.")
        else:
            print("Você bateu em retirada... medroso!")
            break

        if energia_rival <= 0:
            print(f"O oponente não aguenta mais lutar!")
            break

        
        lista_ia = ["investida", "investida", "investida", "investida", "investida", 
                    "recuperar", "recuperar", "recuperar", "recuperar", "sair"]
        decisao_ia = random.choice(lista_ia)

        if decisao_ia == "investida":
            energia_player -= 10
            print(f"O oponente contra-atacou o seu {meu_time}!")
        elif decisao_ia == "recuperar":
            energia_rival += 5
            print("O rival recuperou fôlego, +5 de vigor.")
        else:
            print("O oponente fugiu da luta... sem honra!")
            break
            
        rodada += 1

    if energia_player <= 0:
        print("\n[ FIM DE JOGO ] Suas forças acabaram!")
    elif energia_rival <= 0:
        print("\n[ TRIUNFO ] O campo de batalha é seu!")
            
    input("\nClique <enter> para jogar novamente")