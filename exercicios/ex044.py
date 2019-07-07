valor = float(input('Digite o valor'))
print('Digite a condicao de pagamento onde ')
print('1- avista (dinheiro/cheque)')
print('2- a vista no cartao')
print('3 - 2x no cartao')
print('4- 3x ou mais vezes no cartao')
condicao = int(input('Escolha a condiçáo'))

if(condicao == 1):
    print('Voce deve pagar {:0.2f}'.format(valor - (valor * 0.1)))
elif(condicao == 2):
    print('Voce deve pagar {:0.2f}'.format(valor - (valor * 0.05)))
elif(condicao == 3):
    print('Voce deve pagar {:0.2f}'.format(valor))
elif(condicao == 4):
    print('voce deve pagar {:0.2f}'.format(valor + (valor *0.2 )))
else:
    print('Condicao invalida' )