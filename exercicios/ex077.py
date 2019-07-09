palavras = ('acabate','mamao','manga')

vogais = ('a', 'e','i','o','u')

for palavra in palavras:
    print(f'na palavra {palavra} a vogais sáo:', end = '' )
    for c in range(0,len(palavra)):
        if( palavra[c] in vogais):
            print(palavra[c], end = '')
    print('\n')