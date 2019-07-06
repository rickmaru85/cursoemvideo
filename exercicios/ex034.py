salario = float(input('digite seu salario'))

if(salario > 1250.00):
    print('seu novo salario é {}'.format(salario + (salario * 0.1)))
else:
    print('seu novo salario é {}'.format(salario + (salario * 0.15)))


