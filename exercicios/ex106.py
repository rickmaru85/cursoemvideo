def ajuda(comand):
    print('\33-'*30)
    print(help(comand))


while True:
    comando = input('Digite um comando')
    if comando.upper() == 'FIM':
        break
    ajuda(comando)
