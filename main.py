from jogoVelha import funcoes
from time import sleep

while True:
    # Variáveis
    tabuleiro = [[' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' ']]
    linha = '-' * 5
    eixoY = [0, 2, 4]

    menu = funcoes.menu(tabuleiro, eixoY)
    if menu == 3:
        print('\33[31mPrograma Finalizado!\33[m')
        break
    player1 = menu[0]
    player2 = menu[1]

    # Tabuleiro 1
    for c in range(0, 3):
        for d in range(0, 5):
            if d < 4:
                print(tabuleiro[c][d], end='')
            else:
                print(tabuleiro[c][d])
        if c < 2:
            print(linha)


    # Começo do jogo
    try:
        # Partida de 5 rounds
        for cont in range(0, 5):
            sleep(1)
            # Coloração
            print(f'''
            \33[3{cont + 3}m''')

            # Turno player 1
            player1.jogar()
            verifJog1 = funcoes.verificar(tabuleiro, eixoY, player1, player1.marca)

            # Turno player 2
            if verifJog1 == ' ':
                if cont < 4:
                    player2.jogar()
                    verifJog2 = funcoes.verificar(tabuleiro, eixoY, player2, 'O')

            # Impressão do tabuleiro atualizado
            for c in range(0, 3):
                for d in range(0, 5):
                    if d < 4:
                        print(tabuleiro[c][d], end='')
                    else:
                        print(tabuleiro[c][d])
                if c < 2:
                    print(linha)

            # Declaração do vencedor
            if verifJog1 != ' ':
                print(f'Vencedor: {verifJog1}')
                break
            elif verifJog2 != ' ':
                print(f'Vencedor: {verifJog2}')
                break
    # Verificação de erro
    except:
        print('\33[31mAlgo deu errado!\33[m')
