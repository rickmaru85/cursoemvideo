aluno = {}

aluno['nome'] = str(input('Digite o nome:'))
aluno['nota'] = int(input('Digite a nota:'))

if(aluno['nota'] > 6):
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

for k,v in aluno.items():
    print(f'O {k} é igual a {v}')