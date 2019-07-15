import moeda

p = float(input('Digite o preço:R$'))
print(f'A metade de {moeda.moeda(p)}  é {moeda.metade(p,True)}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'aumentando 10% de {moeda.moeda(p)} é {moeda.aumenta(p,10,True)}')
print(f'diminuindo 10% de {moeda.moeda(p)} é {moeda.diminui(p,10,True)}')
