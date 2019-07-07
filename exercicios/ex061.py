termo = int(input('digite o primeiro termo:'))
razao = int(input('Digite a razao'))

contador = int(10)
flag = str('')

while flag == '':
    print(termo)
    termo = termo + razao
    contador -= 1
    if contador == 0:
        contador = int(input('Deseja exibir mais quantos numero?'))
        print(contador)
        if(contador == 0):
            flag = 'x'


