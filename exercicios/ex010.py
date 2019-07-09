from typing import Tuple

valor = float(input('Digite quanto tem na carteira:'))
dolar = float(327/100)

#print(type(valor))

compra = float(valor/dolar)

print('Voce pode comprar {:.2f} dolares'.format(compra))
