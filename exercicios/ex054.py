from datetime import  date

maior = 0
atual = date.today().year

for c in range(0,7,1):
    nascimento = int(input('Digite o ano de nascimento:'))
    if atual - nascimento >= 21:
        maior += 1

print('Dessa lista, a quantidade de maiores é {}'.format(maior))