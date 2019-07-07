soma = int(0)
cont = int(0)
maior = int(0)
menor = int(0)
opcao = str('')

while opcao != 'n':
    num = int(input('Digite um numero'))
    if cont == 0:
        menor = maior = num
    if menor > num:
        menor = num
    if maior < num:
        maior = num
    cont += 1
    soma += num
    opcao = str(input('Deseja continuar(S/N?').lower())

if cont == 0:
    cont = 1

print('O maior é {} o menor é {} e a media é {:0.2f}'.format(maior,menor,(soma/cont)))