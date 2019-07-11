def escreva(mensagem):
    tamanho = int(len(mensagem)) + 4
    print('-' * (tamanho))
    print(f'  {mensagem:^}')
    print(('-' * (tamanho)))


mensg = str(input('Digite uma mensagem:'))

escreva(mensg)