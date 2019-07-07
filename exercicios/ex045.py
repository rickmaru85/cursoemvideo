from random import choice

digite = str(input('Escolha entre papel, pedra ou tesoura:'))

lista = ['pedra','papel','tesoura']
escolha = choice(lista)

print(escolha)


if(digite.lower() == 'pedra'):
    if(escolha == 'tesoura'):
        print('Voce ganheou')
    elif(escolha == 'papel'):
        print('voce perdeu')
    else:
        print('Empate')
elif(digite.lower() == 'papel'):
    if(escolha == 'pedra'):
        print('Voce ganheou')
    elif(escolha == 'tesoura'):
        print('voce perdeu')
    else:
        print('Empate')
elif(digite.lower() == 'tesoura'):
    if(escolha == 'papel'):
        print('Voce ganheou')
    elif(escolha == 'pedra'):
        print('voce perdeu')
    else:
        print('Empate')
else:
    print('Escolha invalida')