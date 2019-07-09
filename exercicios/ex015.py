dias = int(input('Quantos dias foi alugado?'))
km = int(input('Quantos Km rodados?'))

print('O preço a ser pago é {:.2f}'.format((dias*60)+(0.15*km)))
