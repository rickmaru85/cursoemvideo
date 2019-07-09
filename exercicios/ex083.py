exp = str(input('Digite a expressao'))

lista = []

for ex in exp:
    if ex == '(':
        lista.append('(')
    else:
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if(len(lista)== 0):
    print('Valida')
else:
    print('invalida')