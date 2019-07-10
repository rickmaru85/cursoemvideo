numeros = []
pares = []
impares = []
num = int(0)


for c in range(0,7,1):
    num = int(input('Digite um valor'))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros.append(pares)
numeros.append(impares)

print(sorted(numeros[0]))
print(sorted(numeros[1]))
