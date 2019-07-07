from datetime import  date

nascimento = int(input('Digite o ano de seu nascimento'))

idade = date.today().year - nascimento

if(idade <= 9):
    print('Categoria mirim')
elif(idade <= 14):
    print('Categoria infantil')
elif(idade <= 19):
    print('categoria junior')
elif(idade <= 20):
    print('categoria senior')
else:
    print('categoria master')