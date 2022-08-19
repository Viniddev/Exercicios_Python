def leia(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).replace(',','.')
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1;31mErro, digite um número Válido!!!\033[m")
        if ok:
            break
    return valor