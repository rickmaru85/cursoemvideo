jogador = {}
tot = int(0)

jogador['nome'] = str(input('Nome do jogador:'))
jogos = int(input('Quantos jogos ele participou?'))

jogador['gols'] = []

for c in range(0,jogos):
    jogador['gols'].append(int(input(f'quantos gols na partida {c+1}:')))

for gol in jogador['gols']:
    tot += gol
jogador['total'] = 6

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas!')
for k,v in enumerate(jogador['gols']):
    print(f'  => na partida {k+1}, fez {v} gols.')

print(f'Foi um total de {sum(jogador["gols"])} gols')
