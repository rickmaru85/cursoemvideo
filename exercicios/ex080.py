lista = []

for c in range(0, 5, 1):
    num = int(input('Digite um valor:'))
    if(c == 0):
        lista.append(num)
    else:
        count = 0
        for list in lista:

            if(list > num):
                break
            count += 1

        lista.insert(count, num)
        #print(lista)

print(lista)