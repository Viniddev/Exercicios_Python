def aumento(num, taxa = 0, formatar = False):
    res = num + (num* taxa / 100)
    return res if formatar is False else moeda(res)


def desconto(num, taxa = 0, formatar = False):
    res = num - (num* taxa / 100)
    return res if formatar is False else moeda(res)



def metade(num, formatar = False):
    num = num / 2
    return num if formatar is False else moeda(num)


def dobro(num, formatar = False):
    num = num * 2
    return num if formatar is False else moeda(num)


def lin():
    print("\033[1;31m**\033[m"*60)


def moeda(num, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')
