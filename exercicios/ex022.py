nome = input('Digite seu nome:').strip()

print(nome.upper())
print(nome.lower())

print(int(len(nome)) - int(nome.count(' ')))

nomes = nome.split()

print(len(nomes[0]))