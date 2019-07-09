a =  ('Palmeiras','Santos','Flamengo','Internacional','Atlético-MG','Goiás','Botafogo','Bahia','São Paulo','Corinthians')
b = ('Grêmio','Athletico-PR','Ceará','Fortaleza','Vasco','Fluminense','Chapecoense','Cruzeiro','CSA','Avaí')

times = a+b

print('os 5 Primeiros')
for count in range(0,5):
    print(times[count])


#print(times[-1])
print('O 4 ultimos')
for count in range(1,5):
    print(times[count*-1])

#timess = times.sort()

print('Ordem alfabetica')
for time in sorted(times):
   print(time)

print('Chapecoense esta na posicao')
print(times.index('Chapecoense'))