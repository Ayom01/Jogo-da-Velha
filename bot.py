from random import randint


class Bot:
    def __init__(self, nome, tabuleiro, eixoY, marca):
        self.nome = nome
        self.tabuleiro = tabuleiro
        self.eixoY = eixoY
        self.marca = marca

    def jogar(self):
        while True:
            player1_x = randint(0, 2)
            player1_y_aux = randint(0, 2)
            player1_y = self.eixoY[player1_y_aux]
            if player1_y % 2 == 0 and self.tabuleiro[player1_x][player1_y] == ' ':
                break
        self.tabuleiro[player1_x][player1_y] = self.marca
