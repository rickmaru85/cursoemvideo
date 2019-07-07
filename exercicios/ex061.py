termo = int(input('digite o primeiro termo:'))
razao = int(input('Digite a razao'))

contador = int(10)
flag = str('')

while contador == 0:
    print(termo)
    termo = termo + razao
    contador -= 1

