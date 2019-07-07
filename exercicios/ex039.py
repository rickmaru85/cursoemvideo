import datetime

ano = int(input('Digite o ano de seu nascimento'))

atual = datetime.date.today().year
calc = atual - ano

if(atual-ano > 18):
    print('Voce esta atrasado para se alistar em {} anos'.format(abs(calc - 18)))
elif(atual-ano < 18):
    print('Voce deve se alistar em {} anos'.format(abs(calc - 18)))
else:
    print('Voce deve se alistar esse ano')