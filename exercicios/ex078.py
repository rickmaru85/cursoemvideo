lista = []

for c in range(0,5,1):
    lista.append(int(input('Digite um numero:')))

print(lista)

print(f'O maior numero é {max(lista)} e a sua posição foi {lista.index(max(lista))}')
print(f'O menor numero é {min(lista)} e a sua posição foi {lista.index(min(lista))}')