def leiadinheiro(msg):
    while True:
        res = input(msg).strip().replace(',','.')
        if res.isdecimal():
            break
        else:
            print('erro')
    return float(res)
