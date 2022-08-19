def aumento(num):
    num = num * 1.10
    return num


def desconto(num):
    num = num * 0.90
    return num


def metade(num):
    num = num / 2
    return num


def dobro(num):
    num = num * 2
    return num


def lin():
    print("\033[1;31m**\033[m"*60)


def moeda(num, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')