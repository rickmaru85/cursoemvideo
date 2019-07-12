def fatorial(valor,show = False):
    if(show == True and valor != 1):
        print(f'{valor} X ', end = '')
    elif(valor == 1 and show == True):
        print(f'{valor} =',end=' ')
    if(valor>1):
        result = fatorial(valor-1,show)
        result *= valor
    else:
        result = valor
    return result

print("\n\nRecursion Example Results")
print(fatorial(5,show = True))