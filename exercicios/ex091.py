from random import randint
from operator import itemgetter

jogo = {}
jogos = []


for c in range(1,5):
    nome = 'jogador' + str(c)
    jogo['jogador'] = nome
    jogo['resultado'] = int(randint(1,6))
    jogos.append(jogo.copy())

jogos = sorted(jogos,reverse=True,key = itemgetter('resultado'))

for pos,jogo in enumerate(jogos):
    print(f'O {pos+1}º lugar: {jogo["jogador"]} com {jogo["resultado"]} ')