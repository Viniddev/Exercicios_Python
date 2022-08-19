def leia(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == "":
            print(f'\033[1;31mERRO: {entrada} não é um preço válido!')
        else:
            ok = True
            return float(entrada)