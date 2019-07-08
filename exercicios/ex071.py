valor = int(input('Quanto deseja sacar?'))
notas50 = int(0)
notas20 = int(0)
notas10 = int(0)
notas1  = int(0)

while True:
    notas50 = valor // 50
    if(valor % 50 == 0):
        break
