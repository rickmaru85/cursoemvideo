pessoas = []
pessoa = []
menorpeso = maiorpeso = 0

while True:

    pessoa.append(str(input('Digite o nome da pessoa:')))
    pessoa.append(int(input('Digite o peso da pessoa:')))

    if pessoa[1] > maiorpeso:
        maiorpeso = pessoa[1]
    if pessoa[1] < menorpeso or menorpeso == 0:
        menorpeso = pessoa[1]

    pessoas.append(pessoa[:])
    pessoa.clear()

    while True:
        opcao = str(input('Deseja continuar?(S/N)').lower())
        if opcao in 'sn':
            break
    if opcao == 'n':
        break

print(pessoas)
print(f'Voce cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorpeso}. Peso de  ', end='')
for pessoa in pessoas:

    if pessoa[1] == maiorpeso:
        print(pessoa[0], end='')
print('\n')
print(f'O menor peso foi de {menorpeso}. Peso de  ', end='')
for pessoa in pessoas:

    if pessoa[1] == menorpeso:
        print(pessoa[0],end='')
