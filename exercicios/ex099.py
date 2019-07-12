def maior(*num):
    maior = int(0)
    print(f'foi informado {len(num)} valores')
    for pos,c in enumerate(num):
        if c > maior or pos ==0:
            maior = c
    print(maior)

maior(1,3,2,5,4,18,23)