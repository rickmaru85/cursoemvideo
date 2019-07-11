def contador(inicio,fim,passo):
    for c in range (inicio,fim+1, passo):
        print(c)


ini = int(input('Digite o inicio'))
fi = int(input('Digite o final'))
pas = int(input('Digite o passo'))

contador(ini,fi,pas)