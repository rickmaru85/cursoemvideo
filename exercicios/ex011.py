largura = float(input('Digite a largura:'))
altura  = float(input('Digite a altura:'))

area = float(altura*largura)
tinta = float(area/2)

print('A parede tem {:.4f} m² e usara {:.4f} de tinta'.format(area,tinta))