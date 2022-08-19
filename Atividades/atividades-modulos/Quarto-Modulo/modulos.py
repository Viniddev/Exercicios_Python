def resumo(num, aum, desc, formato= True):
    titulo = 'Resumo Dos Dados:'
    lin()
    print(f'{titulo}')
    lin()
    print(f"    Com um aumento de {aum}% o preço final é {aumento(num, aum, True)}")
    print(f"    Com um desconto de {desc}% o preço final é {desconto(num, desc, True)}")
    print(f"    O dobro do valor é {dobro(num, True)}")
    print(f"    A metade do valor é {metade(num, True)}")


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
