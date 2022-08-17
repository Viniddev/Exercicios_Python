from datetime import date
import os
os.system('cls')
ano = date.today().year

def voto(idade= 0):
    global ano
    if (ano - idade) >= 16 and (ano - idade) < 18:
        return f'   Com {ano-idade} anos o voto é opcional'
    elif (ano - idade) >= 18 and (ano - idade) <=60:
        return f'   Com {ano-idade} anos o voto é obrigatório'
    elif (ano- idade) > 60:
        return f'   Voto opcional para a faixa de idade inserida'
    else:
        return f'   Voto negado para essa faixa de idade'


def lin():
    print('\033[1;31m¨\033[m'*60)


lin()
nasc = int(input('Digite o ano do seu nascimento: '))
print(voto(nasc))
lin()