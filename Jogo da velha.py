print('              Jogo da Velha              \n\n')

jog1 = input('Escolha o caracter para o jog 1(x ou o) ')
while jog1 != 'x' and jog1 != 'o' and jog1 != 'X' and jog1 != 'O':
    print('ERRO!opção digitada não é valida!')
    jog1 = input('Escolha a opção para o jog 1(x ou o) ')
if jog1 == 'x' or jog1 == 'X':
    jog2 = 'o'
else:
    jog2 = 'x'
print('jogador 1 =', jog1)
print('jogador 2 =', jog2)
cont = int(input('Deseja alterar os caracteres? \n 1-Sim \n 0-Não\n'))
while cont == True:
    jog1 = input('Escolha o caracter para o jog 1(x ou o) ')
    print('jog1')
    while jog1 != 'x' and jog1 != 'o' and jog1 != 'X' and jog1 != 'O':
        print('ERRO!opção digitada não é valida!')
        jog1 = input('Escolha o caracter para o jog 1(x ou o) ')

    if jog1 == 'x' or jog1 == 'X':
        jog2 = 'o'
    else:
        jog2 = 'x'
    print('jogador 1 =', jog1)
    print('jogador 2 =', jog2)
    cont = int(input('Deseja alterar os caracteres? \n 1-Sim \n 0-Não\n'))

jogo = [['*', '*', '*'],
        ['*', '*', '*'],
        ['*', '*', '*']
        ]

ganhou = False
erro = 0
jogadas = 0
ganhador = 'nenhum'
while ganhou == False and jogadas != 9:
    for linha in range(3):
        for coluna in range(3):
            print("%c" % jogo[linha][coluna], end='')
        print()
    if ganhador == 'nenhum':
        l = int(input('Jogador 1:\n Digite a linha desejada:\n'))
        while l != 1 and l != 2 and l != 3:
            print('ERRO!VALOR DIGITADO NÃO É UM VALOR VÁLIDO')
            l = int(input('Jogador 1:\n Digite a linha desejada:\n'))
        l = l - 1
        c = int(input('Jogador 1:\n Digite a coluna desejada:\n'))
        while c != 1 and c != 2 and c != 3:
            print('ERRO!VALOR DIGITADO NÃO É UM VALOR VÁLIDO')
            c = int(input('Jogador 1:\n Digite a coluna desejada:\n'))
        c = c - 1
        if jogo[l][c] != '*':
            erro = 1
            while erro == 1:
                print('ERRO!LINHA E COLUNA JÁ FOI SELECIONADA!\n')
                l = int(input('Jogador 1:\n Digite a linha desejada:\n'))
                while l != 1 and l != 2 and l != 3:
                    print('ERRO!VALOR DIGITADO NÃO É UM VALOR VÁLIDO')
                    l = int(input('Jogador 1:\n Digite a linha desejada:\n'))
                l = l - 1
                c = int(input('Jogador 1:\n Digite a coluna desejada:\n'))
                while c != 1 and c != 2 and c != 3:
                    c = int(input('Jogador 1:\n Digite a coluna desejada:\n'))
                c = c - 1
                if jogo[l][c] != '*':
                    erro = 1
                else:
                    erro = 0
                    jogo[l][c] = jog1
                    jogadas += 1
        else:
            erro = 0
            jogo[l][c] = jog1
            jogadas += 1
        j = 0
        for linha in range(3):
            if jogo[linha][j] == jog1 and jogo[linha][j + 1] == jog1 and jogo[linha][j + 2] == jog1:
                ganhou = True
                ganhador = 'Jogador 1'
        if jogo[0][j] == jog1 and jogo[1][j] == jog1 and jogo[2][j] == jog1:
            ganhou = True
            ganhador = 'Jogador 1'
        elif jogo[0][j + 1] == jog1 and jogo[1][j + 1] == jog1 and jogo[2][j + 1] == jog1:
            ganhou = True
            ganhador = 'Jogador 1'
        elif jogo[0][j + 2] == jog1 and jogo[1][j + 2] == jog1 and jogo[2][j + 2] == jog1:
            ganhou = True
            ganhador = 'Jogador 1'
        elif jogo[0][j] == jog1 and jogo[1][j + 1] == jog1 and jogo[2][j + 2] == jog1:
            ganhou = True
            ganhador = 'Jogador 1'
        elif jogo[0][j + 2] == jog1 and jogo[1][j + 1] == jog1 and jogo[2][j] == jog1:
            ganhou = True
            ganhador = 'Jogador 1'
        if ganhador != 'Jogador 1':
            for linha in range(3):
                for coluna in range(3):
                    print("%c" % jogo[linha][coluna], end='')
                print()
            l = int(input('Jogador 2:\n Digite a linha desejada:\n'))
            while l != 1 and l != 2 and l != 3:
                print('ERRO!VALOR DIGITADO NÃO É UM VALOR VÁLIDO')
                l = int(input('Jogador 2:\n Digite a linha desejada:\n'))
            l = l - 1
            c = int(input('Jogador 2:\n Digite a coluna desejada:\n'))
            while c != 1 and c != 2 and c != 3:
                print('ERRO!VALOR DIGITADO NÃO É UM VALOR VÁLIDO')
                c = int(input('Jogador 2:\n Digite a coluna desejada:\n'))
            c = c - 1
            if jogo[l][c] != '*':
                erro = 1
                while erro == 1:
                    print('ERRO!LINHA E COLUNA JÁ FOI SELECIONADA!\n')
                    l = int(input('Jogador 2:\n Digite a linha desejada:\n'))
                    while l != 1 and l != 2 and l != 3:
                        print('ERRO!VALOR DIGITADO NÃO É UM VALOR VÁLIDO')
                        l = int(input('Jogador 2:\n Digite a linha desejada:\n'))
                    l = l - 1
                    c = int(input('Jogador 2:\n Digite a coluna desejada:\n'))
                    while c != 1 and c != 2 and c != 3:
                        c = int(input('Jogador 2:\n Digite a coluna desejada:\n'))
                    c = c - 1
                    if jogo[l][c] != '*':
                        erro = 1
                    else:
                        erro = 0
                        jogo[l][c] = jog2
                        jogadas += 1
            else:
                erro = 0
                jogo[l][c] = jog2
            jogadas += 1
            j = 0
            for linha in range(3):
                if jogo[linha][j] == jog2 and jogo[linha][j + 1] == jog2 and jogo[linha][j + 2] == jog2:
                    ganhou = True
                    ganhador = 'Jogador 2'
            if jogo[0][j] == jog2 and jogo[1][j] == jog2 and jogo[2][j] == jog2:
                ganhou = True
                ganhador = 'Jogador 2'
            elif jogo[0][j + 1] == jog2 and jogo[1][j + 1] == jog2 and jogo[2][j + 1] == jog2:
                ganhou = True
                ganhador = 'Jogador 2'
            elif jogo[0][j + 2] == jog2 and jogo[1][j + 2] == jog2 and jogo[2][j + 2] == jog2:
                ganhou = True
                ganhador = 'Jogador 2'
            elif jogo[0][j] == jog2 and jogo[1][j + 1] == jog2 and jogo[2][j + 2] == jog2:
                ganhou = True
                ganhador = 'Jogador 2'
            elif jogo[0][j + 2] == jog2 and jogo[1][j + 1] == jog1 and jogo[2][j] == jog2:
                ganhou = True
                ganhador = 'Jogador 2'

        else:
            pass
    else:
        continue

if ganhador != 'nenhum':
    print('O ganhador foi o ', ganhador)
else:
    print('O jogo deu empate!')
