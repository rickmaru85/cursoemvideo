numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('Digite um numero:')))

    while True:
        opcao = str(input('Deseja continuar?(S/N').lower())
        if(opcao in 'sn'):
            break
    if(opcao == 'n'):
        break

for num in numeros:
    if(num% 2 == 0):
        pares.append(num)
    else:
        impares.append(num)

print(numeros)
print(pares)
print(impares)