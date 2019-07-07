idadeant = int(0)
media = int(0)
mulheresnovas = int(0)
nomevelho = str('')

for c in range(0,4,1):
    nome = str(input('Digite seu nome'))
    idade = int(input('Digite a sua idade?'))
    sexo = str(input('Digite seu sexo'))
    media += idade
    if idade > idadeant and 'm' == sexo.lower():
        nomevelho = nome
        idadeant = idade
    if (sexo.lower() == 'f' and idade < 20):
        mulheresnovas += 1



media = media/4
print('a medida de idade do grupo é {}'.format(media))
print(' o homem mais velho é {} '.format(nomevelho))
print('e a quantidade de mulheres abaixo de 20 é {}'.format(mulheresnovas))