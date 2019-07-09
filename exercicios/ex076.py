produtos = ('pizza',3.5,'hamburguer',234.0)
teste = ''

print('-'*40)
print('{:^30}'.format('Lista de precos'))
print('-'*40)

for pos,produto in enumerate(produtos):
    if(pos % 2 == 0):
        print(f'{produto:.<30} R%', end = '')
    else:
        print(f'{produto:<2.2f}')

print('-'*40)

