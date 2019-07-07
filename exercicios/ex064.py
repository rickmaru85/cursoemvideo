num = int(input('Digite um numero (999 para sair):'))
soma = int(0)
cont = int(0)

while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero (999 para sair):'))
print('A soma dos numeros foi {} e a quantidade de numeros foi {}'.format(soma,cont))