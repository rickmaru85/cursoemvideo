grupo = []
pessoa = {}
soma = float(0)
flag = str('')
media = float(0)

while True:
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo(M/F)').upper())
        if pessoa['sexo'] in ('MF'):
            break
    pessoa['idade'] = int(input('Idade:'))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())

    while True:
        opcao = str(input('Deseja continuar?').lower().strip())
        if(opcao == 'n' or opcao == 's'):
            break
        print(opcao)
    if(opcao == 'n'):
        break

media = soma/len(grupo)
print(f'o grupo tem {len(grupo)} pessoas')
print(f'a media de idade é de {media:0.2f} anos')
for c in grupo:
    if c['sexo'] == 'F':
        if flag == '':
            print('As mulheres cadastradas foram:' , end = ' ')
            flag = 'x'
        print(c['nome'], end =' ')
if flag != 'x':
    print('Nenhuma mulher cadastrada')

print()
print('Lista de pessoas que estão acima  da média de idade:')
for c in grupo:
    if c['idade'] > media:
        for k,v in c.items():
            print(f'{k} = {v}:', end= ' ')
        print()
