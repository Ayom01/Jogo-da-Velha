from random import randint

tabuleiro = [[' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' ']]
linha = '-' * 5
eixoY = [0, 2, 4]


for c in range(0, 3):
    for d in range(0, 5):
        if d < 4:
            print(tabuleiro[c][d], end='')
        else:
            print(tabuleiro[c][d])
    if c < 2:
        print(linha)

try:
    for cont in range(0, 5):
        print(f'''
        \33[3{cont + 3}m''')
        while True:
            player1_x = randint(0, 2)
            player1_y_aux = randint(0, 2)
            player1_y = eixoY[player1_y_aux]
            if player1_y % 2 == 0 and tabuleiro[player1_x][player1_y] == ' ':
                break
        '''print(player1_x)
        print(player1_y)'''
        tabuleiro[player1_x][player1_y] = 'X'


        # Vertical
        contwin = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if tabuleiro[i][eixoY[j]] == 'X':
                    contwin += 1
            if contwin == 3:
                win = 'player 1'
                break
            else:
                contwin = 0
        # Horizontal
        if contwin != 3:
            contwin = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    if tabuleiro[j][eixoY[i]] == 'X':
                        contwin += 1
                if contwin == 3:
                    win = 'player 1'
                    break
                else:
                    contwin = 0
        # Diagonal
        if contwin != 3:
            contwin = i = 0
            while i != 3:
                for j in range(0, 3):
                    if tabuleiro[i][eixoY[j]] == 'X':
                        contwin += 1
                    i += 1
                if contwin == 3:
                    win = 'player 1'
                    break
                else:
                    contwin = 0
            if contwin != 3:
                i = 2
                while i != 0:
                    for j in range(0, 3):
                        if tabuleiro[i][eixoY[j]] == 'X':
                            contwin += 1
                    i -= 1
                    if contwin == 3:
                        win = 'player 1'
                        break
                    else:
                        contwin = 0

        if contwin != 3:
            if cont < 4:
                while True:
                    player2_x = randint(0, 2)
                    player2_y_aux = randint(0, 2)
                    player2_y = eixoY[player2_y_aux]
                    if player2_y % 2 == 0 and tabuleiro[player2_x][player2_y] == ' ':
                        break
                '''print(player2_x)
                print(player2_y)'''
                tabuleiro[player2_x][player2_y] = 'O'

            # Vertical
            contwin = 0
            for i in range(0, 3):
                for j in range(0, 3):
                    if tabuleiro[i][eixoY[j]] == 'O':
                        contwin += 1
                if contwin == 3:
                    win = 'player 2'
                    break
                else:
                    contwin = 0
            if contwin != 3:
                # Horizontal
                contwin = 0
                for i in range(0, 3):
                    for j in range(0, 3):
                        if tabuleiro[j][eixoY[i]] == 'O':
                            contwin += 1
                    if contwin == 3:
                        win = 'player 2'
                        break
                    else:
                        contwin = 0
            if contwin != 3:
                # Diagonal
                contwin = i = 0
                while i != 3:
                    for j in range(0, 3):
                        if tabuleiro[i][eixoY[j]] == 'O':
                            contwin += 1
                        i += 1
                    if contwin == 3:
                        win = 'player 2'
                        break
                    else:
                        contwin = 0
                if contwin != 3:
                    i = 2
                    while i != 0:
                        for j in range(0, 3):
                            if tabuleiro[i][eixoY[j]] == 'O':
                                contwin += 1
                        i -= 1
                        if contwin == 3:
                            win = 'player 2'
                            break
                        else:
                            contwin = 0

        for c in range(0, 3):
            for d in range(0, 5):
                if d < 4:
                    print(tabuleiro[c][d], end='')
                else:
                    print(tabuleiro[c][d])
            if c < 2:
                print(linha)
        if contwin == 3:
            print(f'Vencedor: {win}')
            break

except (ValueError, TypeError):
    print('\33[31mERRO! Número inteiro inválido.\33[m')
except KeyboardInterrupt:
    print('\33[31mO programa foi interrompido!.\33[m')
