import os

jogada = 0
jogador1 = 1
jogador2 = 2
maximo_jogadas = 9
jogar_de_novo = True
ganhador = False
velha = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
        ]


def tela():
    os.system('cls')
    print('   0   1   2')
    print('0:  ' + velha[0][0] + ' | ' + velha[0][1] + ' | ' + velha[0][2])
    print('   -----------')
    print('1:  ' + velha[1][0] + ' | ' + velha[1][1] + ' | ' + velha[1][2])
    print('   -----------')
    print('2:  ' + velha[2][0] + ' | ' + velha[2][1] + ' | ' + velha[2][2])
    print('jogadas: ' + str(jogada))


def jogador_joga(jogador1, jogador2):
    global jogada
    if jogador1 == 1 and jogada < maximo_jogadas:
        linha = int(input('linha: '))
        coluna = int(input('coluna: '))
        while velha[linha][coluna] != ' ' and linha > 3 or coluna > 3:
            linha = int(input('linha: '))
            coluna = int(input('coluna: '))
            break
        try:
            linha = int(input('linha: '))
            coluna = int(input('coluna: '))

            while velha[linha][coluna] != ' ':
                linha = int(input('linha: '))
                coluna = int(input('coluna: '))
            velha[linha][coluna] = 'X'
            jogador1 = 1
            jogada += 1
        except:
            print('Linha ou coluna invalida')

    if jogador2 == 2 and jogada < maximo_jogadas:
        linha = int(input('linha: '))
        coluna = int(input('coluna: '))
        while velha[linha][coluna] != ' ' and linha > 3 or coluna > 3:
            linha = int(input('linha: '))
            coluna = int(input('coluna: '))
            break
        try:
            linha = int(input('linha: '))
            coluna = int(input('coluna: '))

            while velha[linha][coluna] != ' ':
                linha = int(input('linha: '))
                coluna = int(input('coluna: '))
            velha[linha][coluna] = 'X'
            jogador2 = 1
            jogada += 1
        except:
            print('Linha ou coluna invalida')

def vitoria():
    ganhou = False
    simbolos = ['X', 'O']
    for l in simbolos:
        ganhou = False
        # verifica as linhas
        indice_linha = 0
        indice_coluna = 0
        while indice_linha < 3:
            soma = 0
            indice_coluna = 0
            while indice_coluna < 3:
                if velha[indice_linha][indice_coluna] == True:
                    soma += 1
                indice_coluna += 1
            if soma == 3:
                ganhou = True
                break
            indice_linha += 1
        if ganhou != 'n':
            break
        # verifica colunas
        indice_linha = 0
        indice_coluna = 0
        while indice_linha < 3:
            soma = 0
            indice_linha = 0
            while indice_linha < 3:
                if velha[indice_linha][indice_coluna] == True:
                    soma += 1
                indice_linha += 1
            if soma == 3:
                ganhou = True
                break
            indice_coluna += 1
        if ganhou != False:
            break

        # verifica diagonal
        soma = 0
        indice_diagonal = 0
        indicediag_coluna = 2
        while indice_diagonal < 3:
            if velha[indice_diagonal][indice_diagonal] == True:
                soma += 1
            indice_diagonal += 1
            indicediag_coluna -= 1
        if soma == 3:
            ganhou = True
            break
    return ganhou


while True:
    tela()
    vitoria()
    jogador_joga(jogador1, jogador2)
