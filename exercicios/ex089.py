alunos = []
aluno = []
notas = []
nota = int(0)

while True:
    nome = str(input('nome:'))
    nota1 = float(input('nota 1:'))
    nota2 = float(input('nota 2:'))

    notas.append(nota1)
    notas.append(nota2)

    aluno.append(nome)
    aluno.append(notas[:])

    alunos.append(aluno[:])

    notas.clear()
    aluno.clear()

    while True:
        opcao = str(input('Deseja continuar?(S/N)').lower())
        if(opcao in ('sn')):
            break
    if(opcao == 'n'):
        break

print('-'*30)

for pos,aluno in enumerate(alunos):
    nota1 = 0
    print(f'\n{pos}  ',end= '')
    for po, notas in enumerate(aluno):
#        print(f'{notas}  ' , end='')
        if po == 0:
            print(f'{notas}  ' , end = '')
            nota = 0
        elif po == 1:
            nota1 = 0
            for nota in notas:
                nota1 += nota
            nota2 = nota1/2
            print(f'{nota2}',end = '')

opcao = int(input('Mostrar a nota de qual aluno?'))

print(f'As notas de {alunos[opcao][0]} sáo {alunos[opcao][1]}')