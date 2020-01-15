'''Uma escola te contratou para fazer um software em Python.
Eles querem que você crie um script que exiba o seguinte menu:

0. Sair
1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
2. Inserir aluno e nota
3. Alterar a nota de um aluno
4. Consultar nota de um aluno específico
5. Apagar um aluno da lista
6. Dar a média da turma

Onde a professora que vai fornecer o nome e nota dos alunos. Quantos ela quiser. Quantas vezes quiser.
Implemente esse script usando um dicionário.'''
notas = {}
print('Selecione a opção desejada:\n')
opção = int(input(
    '0.Sair\n1.Exibir lista de alunos com suas notas (cada aluno tem uma nota)\n2. Inserir aluno e nota\n3. Alterar a nota de um aluno\n4. Consultar nota de um aluno específico\n5. Apagar um aluno da lista\n6. Dar a média da turma\n'))
while opção != 0 and opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5 and opção != 6:
    print('ERRO!OPÇÃO DIGITADA NÃO É VÁLIDA!')
    print('Selecione a opção desejada:\n')
    opção = int(input(
        '0.Sair\n1.Exibir lista de alunos com suas notas (cada aluno tem uma nota)\n2. Inserir aluno e nota\n3. Alterar a nota de um aluno\n4. Consultar nota de um aluno específico\n5. Apagar um aluno da lista\n6. Dar a média da turma\n'))

while opção != 0:
    if opção == 1:
        for nome in notas.keys():
            print('Aluno(a):', nome, '\nNota:', notas[nome], '\n')

    elif opção == 2:
        aluno = input('Digite o nome do aluno que deseja inserir:')
        nota = float(input('Digite a nota do aluno '))
        if notas.get(aluno):
            print('O aluno já foi cadastrado!\n')
            print('Aluno(a):', aluno, '\n Nota:', notas[aluno])
            op = input('Deseja cadastrar um novo aluno?\n1.Sim\n2.Não\n')
            while op != '1' and op != '2':
                print('OPÇÃO INVÁLIDA!')
                op = input('Deseja cadastrar um novo aluno?\n1.Sim\n2.Não\n')
            while op == '1':
                aluno = input('Digite o nome do aluno que deseja inserir:')
                nota = float(input('Digite a nota do aluno '))
                if notas.get(aluno):
                    print('O aluno já foi cadastrado!\n')
                    print('Aluno(a):', aluno, '\nNota:', notas[aluno])
                else:
                    print('Aluno cadastrado com sucesso!')
                    notas[aluno] = nota
                    op = input('Deseja cadastrar um novo aluno?\n1.Sim\n2.Não\n')
                    while op != '1' and op != '2':
                        print('OPÇÃO INVÁLIDA!')
                        op = input('Deseja cadastrar um novo aluno?\n1.Sim\n2.Não\n')
        else:
            print('Aluno cadstrado com sucesso!')
            notas[aluno] = nota
            op = input('Deseja cadastrar um novo aluno?\n1.Sim\n2.Não\n')
            while op != '1' and op != '2':
                print('OPÇÃO INVÁLIDA!')
                op = input('Deseja cadastrar um novo aluno?\n1.Sim\n2.Não\n')
            while op == '1':
                aluno = input('Digite o nome do aluno que deseja inserir:')
                nota = float(input('Digite a nota do aluno '))
                if notas.get(aluno):
                    print('O aluno já foi cadastrado!\n')
                    print('Aluno(a):', aluno, '\nNota:', notas[aluno])
                else:
                    print('Aluno cadstrado com sucesso!')
                    notas[aluno] = nota
                    op = input('Deseja cadastrar um novo aluno?\n1.Sim\n2.Não\n')
                    while op != '1' and op != '2':
                        print('OPÇÃO INVÁLIDA!')
                        op = input('Deseja cadastrar um novo aluno?\n1.Sim\n2.Não\n')
    elif opção == 3:
        aluno = input('Digite o nome do aluno: ')
        while notas.get(aluno) == None and op != '1':
            print('ERRO!ALUNO NÃO CADASTRADO!')
            op = input('Deseja digitar novamente?\n1.Sim\n2.Não\n')
            while op != '1' and op != '2':
                print('ERRO!OPÇÃO DIGITADA NÃO É VÁLIDA!!!')
                op = input('Deseja digitar novamente?\n1.Sim\n2.Não\n')
            aluno = input('Digite o nome do aluno: ')
        if notas.get(aluno):
            print('Aluno(a):', aluno, '\nNota:', notas[aluno])
            nota = float(input('Digite a nova nota do aluno:'))
            notas[aluno] = nota
    elif opção == 4:
        aluno = input('Digite o nome do aluno: ')
        op = '0'
        while notas.get(aluno) == None and op != '2':
            print('ERRO!ALUNO NÃO CADASTRADO!')
            op = input('Deseja digitar novamente?\n1.Sim\n2.Não\n')
            while op != '1' and op != '2':
                print('ERRO!OPÇÃO DIGITADA NÃO É VÁLIDA!!!')
                op = input('Deseja digitar novamente?\n1.Sim\n2.Não\n')
            if op == '1':
                aluno = input('Digite o nome do aluno: ')
        if notas.get(aluno) != None:
            print('Aluno(a):', aluno, '\nNota:', notas[aluno])
    elif opção == 5:
        aluno = input('Digite o nome do aluno: ')
        while notas.get(aluno) == None and op != '1':
            print('ERRO!ALUNO NÃO CADASTRADO!')
            op = input('Deseja digitar novamente?\n1.Sim\n2.Não\n')
            while op != '1' and op != '2':
                print('ERRO!OPÇÃO DIGITADA NÃO É VÁLIDA!!!')
                op = input('Deseja digitar novamente?\n1.Sim\n2.Não\n')
            aluno = input('Digite o nome do aluno: ')
        if notas.get(aluno):
            notas.pop(aluno)
            print('Cadastro excluído com sucesso!')
    elif opção == 6:
        soma = 0
        i = 0
        for aluno in notas.keys():
            soma += notas[aluno]
            i += 1
        media = soma / i
        print('A média dos alunos é de :', media)
    opção = int(input(
        '\n0.Sair\n1.Exibir lista de alunos com suas notas (cada aluno tem uma nota)\n2. Inserir aluno e nota\n3. Alterar a nota de um aluno\n4. Consultar nota de um aluno específico\n5. Apagar um aluno da lista\n6. Dar a média da turma\n'))
    while opção != 0 and opção != 1 and opção != 2 and opção != 3 and opção != 4 and opção != 5 and opção != 6:
        print('ERRO!OPÇÃO DIGITADA NÃO É VÁLIDA!')
        print('Selecione a opção desejada:\n')
        opção = int(input(
            '0.Sair\n1.Exibir lista de alunos com suas notas (cada aluno tem uma nota)\n2. Inserir aluno e nota\n3. Alterar a nota de um aluno\n4. Consultar nota de um aluno específico\n5. Apagar um aluno da lista\n6. Dar a média da turma\n'))
print()
