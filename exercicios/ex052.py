numero = int(input('Digite um numero para verificar'))
verifica = int(0)

for c in range(1, numero, 1):
    if (numero % c == 0 and c != 1):
        verifica = 1

if (verifica == 1):
    print('nao e primo')
else:
    print('e primo')
