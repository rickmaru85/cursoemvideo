num1 = int(input('Digite um numero:'))
num2 = int(input('Digite um numero:'))

opcao = 0

while opcao != 5:
    print('''O que deseja fazer com esse numero?
    1- Somar
    2- Multiplicar
    3- exibir o maior    
    4- digitar novos numeros:
    5- Para sair
    '''
    )
    opcao = int(input('Digite a opcao:'))
    if(opcao == 1):
        print('A soma é {}'.format(num1+num2))
    elif(opcao == 2):
        print('A multiplicacao é {}'.format(num1*num2))
    elif(opcao == 3):
        print('o maior numero é {}'.format(num1 if num1 > num2 else num2))
    elif(opcao == 4):
        num1 = int(input('Digite um numero:'))
        num2 = int(input('Digite um numero:'))
    elif(opcao == 5):
        print('Fim')
    else:
        print('Opcao invalida')
