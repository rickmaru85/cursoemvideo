import moeda

p = float(input('Digite o preço:R$'))
print(f'A metade de {p}  é {moeda.metade(p)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'aumentando 10% de {p} é {moeda.aumenta(p,10)}')
print(f'diminuindo 10% de {p} é {moeda.diminui(p,10)}')
