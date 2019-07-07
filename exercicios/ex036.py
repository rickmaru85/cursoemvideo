casa = int(input('Qual valor da casa?'))
salario = int(input('Qual seu salario?'))
anos = int(input('Quantos anos deseja financiar?'))

prestacao = (salario * 0.3)
print(prestacao)


if((casa/(anos*12)) > (salario * 0.3) ):
    print('näo pode comprar')
else:
    print('a presstacao é {}'.format(float((casa/(anos*12)))))
