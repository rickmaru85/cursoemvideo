menor = 0
maior = 0

for c in range(0,5,1):
    peso = int(input('Informe seu peso:'))
    if(peso > maior or maior == 0):
        maior = peso
    if(peso < menor or menor == 0):
        menor = peso

print('O maior peso é {} e o menor peso é {}'.format(maior,menor))