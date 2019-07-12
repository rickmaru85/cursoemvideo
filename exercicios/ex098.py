def contador(inicio,fim,passo):
    if(inicio > fim and passo > 0):
        passo *= -1
    for c in range (inicio,fim, passo):
        print(c,end = ' ' )
    print()

contador(1,11,1)

contador(10, -1, -2)

ini = int(input('Digite o inicio'))
fi = int(input('Digite o final'))
pas = int(input('Digite o passo'))



contador(ini,fi,pas)