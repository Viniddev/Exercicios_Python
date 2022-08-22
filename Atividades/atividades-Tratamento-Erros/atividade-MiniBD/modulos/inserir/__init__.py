def leiaEscolha(resp):
    ok = False
    while ok is not True:
        n = str(input(resp)).strip()
        if n.isnumeric():
            prov = int(n)
            if prov>4 or prov<0:
                print('Escolha inválida!')
            else:
                ok = True
                resp = prov
        else:
            print('Digite um número válido!')
    return resp
