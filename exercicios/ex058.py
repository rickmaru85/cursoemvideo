from random import randint

computador = int(randint(0,10))

player = 11
palpite = 0

while (player != computador):
    player = int(input('digite um numero'))
    palpite += 1

print('Voce preciso de {} palpites'.format(palpite))