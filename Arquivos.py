'''Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4
[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256'''

import os

cont = 0
cont2 = 0
if os.path.isfile("ex1.txt") == False:
    print("Arquivo ex1.txt nao existe")
else:
    meuArquivo = open('ex1.txt', 'r')
    arq = meuArquivo.readlines()

    for i in range(len(arq)):

        if arq[i] == "200.135.80.9\n" or arq[i] == "192.168.1.1\n" or arq[i] == "8.35.67.74\n" or arq[i] == "1.2.3.4\n":
            if cont == 0:
                endereços_validos = open('endereços_validos.txt', 'w')
                endereços_validos.write(arq[i])
                endereços_validos.close()
            else:
                endereços_validos = open('endereços_validos.txt', 'a')
                endereços_validos.write(arq[i])
                endereços_validos.close()
            cont += 1

        elif arq[i] == "257.32.4.5\n" or arq[i] == "85.345.1.2\n" or arq[i] == "9.8.234.5\n" or arq[
            i] == "192.168.0.256\n":
            if cont2 == 0:
                endereços_invalidos = open('endereços_invalidos.txt', 'w')
                endereços_invalidos.write(arq[i])
                endereços_invalidos.close()
            else:
                endereços_invalidos = open('endereços_invalidos.txt', 'a')
                endereços_invalidos.write(arq[i])
                endereços_invalidos.close()
            cont2 += 1
endereços_validos.close()
endereços_invalidos.close()
meuArquivo.close()
