import random

nome1 = input('Informe o primeiro nome:')
nome2 = input('Informe o segundo nome:')
nome3 = input('Informe o terceiro nome:')
nome4 = input('Informe o quarto nome:')


itens = [nome1,nome2,nome3,nome4]

print(random.choice(itens))

