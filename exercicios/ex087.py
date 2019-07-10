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

for po,linha in enumerate(matriz):
    for pos,val in enumerate(linha):
        print(f'[ {val} ]', end='')
        if val % 2 == 0:
            somapar += val
        if pos == 2:
            somatercol += val
        if (po == 1 and pos == 0 ) or ( val > maiorvalsegcol and po == 1):
            maiorvalsegcol = val
    print('')

print(f'A soma dos pares é {somapar}')
print(f'A soma da terceira coluna é {somatercol}')
print(f'O maior valor da segunda linha é {maiorvalsegcol}')