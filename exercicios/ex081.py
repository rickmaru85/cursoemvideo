numeros = []

while True:
    numeros.append(int(input('Digite um numero:')))
    while True:
        opcao = str(input('Deseja continuar?(S/N)').lower())
        if opcao in ('sn'):
            break

    if(opcao == 'n'):
        break

print(f'Foram digitados {len(numeros)} numeros')

print(sorted(numeros,reverse=True))

if(5 in numeros):
    print(f'O numero 5 esta na posição {numeros.index(5)}')
else:
    print('Não tem numero 5')