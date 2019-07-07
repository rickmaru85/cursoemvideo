palavra = str(input('Digite uma frase')).strip()

palavra = palavra.replace(" ", "")
teste = 0
contador = 1

for c in range(0,len(palavra),1):
    contador += 1
    print(palavra[len(palavra)-abs((contador - 1))])
    print(palavra[c])
    if(palavra[c] != palavra[len(palavra)-abs((contador - 1))]):
        teste = 1

if(teste == 0):
    print('pal')
else:
    print('nao')

