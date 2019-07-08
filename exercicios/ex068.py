from random import randint
cont = int(0)

while True:
    player = int(input('Digite um valor'))
    computador = randint(0,10)
    escolha = str(input('P/I'))
    print(f'Jogador escolheu {player} e o computador {computador}')
    if((computador + player) % 2 == 0 and escolha.lower() == 'p'):
        print('Voce ganhou')
        cont += 1
    elif((computador + player) % 2 == 0 and escolha.lower() == 'i'):
        print('Voce perdeu')
        break
    elif((computador + player) % 2 == 1 and escolha.lower() == 'p'):
        print('Voce perdeu')
        break
    elif((computador + player) % 2 == 1 and escolha.lower() == 'i'):
        print('Voce ganhou')
        cont += 1
    elif(escolha.lower() != 'p' and escolha.lower() != 'i'):
        print('Escolha invalida')

print(f'voce ganhou {cont} jogadas seguidas')