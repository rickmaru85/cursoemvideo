while True:
    num1 = int(input('Digite um numero para ver a tabuada (negativo para sair):'))
    if num1 < 0:
        break
    for c in range(1,11,1):
        print(f'{num1:3} X {c:3} = {num1 * c}')
