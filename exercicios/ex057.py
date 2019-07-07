sexo = str('')

while sexo != 'm' and sexo != 'f':
    sexo = str(input('Digite o seu sexo').lower())
    if(sexo != 'm' and sexo != 'f'):
        print('Sexo invalido, digite novamente')