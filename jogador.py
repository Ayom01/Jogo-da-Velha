from jogoVelha import funcoes


class Jogador:
    def __init__(self, nome, tabuleiro, eixoY, marca):
        self.nome = nome
        self.tabuleiro = tabuleiro
        self.eixoY = eixoY
        self.marca = marca

    def jogar(self):
        while True:
            x = funcoes.leiaint('Escolha um número para o eixo X: ')
            yUsu = funcoes.leiaint('Escolha um número para o eixo Y: ')
            if x != 0 and x != 1 and x != 2:
                print('\33[31mA posição do X é inválida!\33[m')
            elif yUsu != 0 and yUsu != 1 and yUsu != 2:
                print('\33[31mA posição do Y é inválida!\33[m')
            else:
                y = self.eixoY[yUsu]
                if self.tabuleiro[x][y] == ' ':
                    self.tabuleiro[x][y] = self.marca
                    break
                else:
                    print('Tente outra posição, esta já está ocupada!')
            print()
