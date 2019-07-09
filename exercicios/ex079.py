lista = []

while True:
    opcao = ''
    num = int(input('Digite um valor:'))
    print(lista.count(num))
    if lista.count(num) == 0:
        lista.append(num)
    else:
        print('Valor duplicado não sera adicionado')

    while True:
        escolha = str(input('Deseja continuar S/N)?').lower())
        if (escolha.lower() == 's' or escolha.lower() == 'n'):
            break

    if (escolha.lower() == 'n'):
        break

print(sorted(lista))