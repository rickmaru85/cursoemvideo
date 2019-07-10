matriz = []
linha = []
somapar = int(0)
somatercol = int(0)
maiorvalsegcol = int(0)

val = int(0)
for c in range(0,3,1):

    for x in range(0,3,1):
        val = int(input(f'Digite um valor para [{c},{x}]'))
        linha.append(val)
        #linha.append(int(print('Digite um valor para o ]')))

    matriz.append(linha[:])
    linha.clear()

#print(matriz)

for linha in matriz:
    for val in linha:
        print(f'[ {val} ]', end='')

    print('')
