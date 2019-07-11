jogador = {}
jogadores = []
tot = int(0)
opt = int(0)
while True:
    jogador['nome'] = str(input('Nome do jogador:'))
    jogos = int(input('Quantos jogos ele participou?'))

    jogador['gols'] = []

    for c in range(0,jogos):
        jogador['gols'].append(int(input(f'quantos gols na partida {c+1}:')))

    tot = int(0)
    for gol in jogador['gols']:
        tot += gol
    jogador['total'] = 6
    jogadores.append(jogador.copy())
    while True:
        opcao = str(input('Deseja ccontinuar?').lower())
        if(opcao == 's' or opcao == 'n'):
            break
    if opcao == 'n':
        break

for pos,jogador in enumerate(jogadores):
    print(pos,end = ' ')
    for val in jogador.values():
        print(f'{val:>3}' , end = ' ')
    print()

while True:
    opt = int(input('Deseja mostrar os dados de qual jogadro?'))
    if opt == 999:
       break
    print(f'Dados do jogador {jogadores[opt]["nome"]}')
    for pos,val in enumerate(jogadores[opt]['gols']):
        print(f' => na partida {pos+1}, fez {val} gols.')


