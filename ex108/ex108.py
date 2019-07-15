import moeda

p = float(input('Digite o preço:R$'))
print(f'A metade de {moeda.moeda(p)}  é {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'aumentando 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.aumenta(p,10))}')
print(f'diminuindo 10% de {moeda.moeda(p)} é {moeda.moeda(moeda.diminui(p,10))}')
