from random import randint

lista = []
jogo = []
num = int(0)
count = int(0)

qtd = int(input('Quantos jogos deve ser gerado?'))

for c in range(0, qtd):
    count = 0
    while True:
        num = int(randint(0,60))
        if num not in jogo:
            jogo.append(num)
            count += 1
            if count == 6:
                break
    lista.append(jogo[:])
    jogo.clear()

count = 0
for jogo in lista:
    count += 1
    print(f'Jogo {count}: {sorted(jogo)}')