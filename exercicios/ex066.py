num1 = int(0)
soma = int(0)
cont = int(0)

while True:
    num1 = int(input('Digite um numero (999 para sair):'))
    if(num1 == 999):
        break
    soma += num1
    cont += 1

print(f'Foi digitado {cont} numeros e a soma enre eles é {soma}')