import random


class dado:
    def __init__(self):
        d = 1

    def lançar(self):
        self.d = random.randint(1, 6)
        return self.d


op = 1
dado = dado()
print('Lançamento de dados')
while op == 1:
    j = dado.lançar()
    print('O resultado do lançamento do dado foi : ', j)
    op = int(input('Deseja jogar novamente?\n1.Sim \n0.Não\n'))
