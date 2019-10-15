from jogoVelha.jogador import Jogador
from jogoVelha.bot import Bot


def menu(tabuleiro, eixoY):
    print("\033[1;36m-\033[m" * 66)
    print(f"\033[1;35m{'JOGO DA VELHA':^66}\33[m")
    print('\033[1;36m-\033[m' * 66)
    while True:
        jogBot = leiaint('''
    [1] - Jogador vs Bot
    [2] - Bot vs Bot
    [3] - Sair
    R: ''')
        if jogBot == 1 or jogBot == 2 or jogBot == 3:
            break
        else:
            print('\33[31mOpção inválida, tente novamente\33[m')
        print()
    if jogBot != 3:
        if jogBot == 1:
            nome = str(input('  Escolha seu nickname: '))
            marcaImp = str(input('  Ecolha sua marca: '))
            marca = corte(marcaImp)
            player1 = Jogador(nome, tabuleiro, eixoY, marca)
        else:
            player1 = Bot('jogador 1', tabuleiro, eixoY, 'X')
        player2 = Bot('jogador 2', tabuleiro, eixoY, 'O')
        print()
        return (player1, player2)
    else:
        print()
        return jogBot


def verificar(tabuleiro, eixoY, player, simb):
    '''
    Verifica se um dos jogadores ganhou
    :param tabuleiro: Tabuleiro em formato de lista
    :param eixoY: Lista para identificar o eixoY - [0, 2, 4]
    :param player: Player/Bot a ser analizado
    :param simb: Simbolo adotado pelo player - 'X' ou 'O'
    :return: Nome do jogador vitorioso ou
    uma string vazia (' ') para indicar a falta do mesmo
    '''
    contwin = 0
    # Vertical
    for i in range(0, 3):
        for j in range(0, 3):
            if tabuleiro[i][eixoY[j]] == simb:
                contwin += 1
        if contwin == 3:
            win = player.nome
            break
        else:
            contwin = 0
    # Horizontal
    if contwin != 3:
        contwin = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if tabuleiro[j][eixoY[i]] == simb:
                    contwin += 1
            if contwin == 3:
                win = player.nome
                break
            else:
                contwin = 0
    # Diagonal
    if contwin != 3:
        contwin = i = 0
        while i != 3:
            for j in range(0, 3):
                if tabuleiro[i][eixoY[j]] == simb:
                    contwin += 1
                i += 1
            if contwin == 3:
                win = player.nome
                break
            else:
                contwin = 0
        if contwin != 3:
            i = 2
            j = 0
            while i != -1:
                while j != 3:
                    if tabuleiro[i][eixoY[j]] == simb:
                        contwin += 1
                    i -= 1
                    j += 1
                if contwin == 3:
                    win = player.nome
                    break
                else:
                    contwin = 0
    if contwin != 3:
        win = ' '
    return win


def leiaint(msg=''):
    while True:
        try:
            nI = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31mERRO! Número inteiro inválido.\33[m')
        except KeyboardInterrupt:
            print('\33[31mInforme o valor!.\33[m')
        else:
            break
    return nI


def corte(str):
    firstLetter = str[0]
    return firstLetter
