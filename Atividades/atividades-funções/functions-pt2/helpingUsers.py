import os
from random import randint
os.system('cls')

cores = (
    '\033[m',
    '\033[1;31;40m',
    '\033[1;31;41m',
    '\033[1;31;42m',
    '\033[1;31;43m',
    '\033[1;31;44m',
    '\033[1;31;45m',
    '\033[1;31;46m',
    '\033[1;31;47m'
)

def ajuda(item):
    cor = randint(0,7)
    print(cores[cor], end='')
    help(item)
    print(cores[0], end='')


def lin():
    print('\033[1;31m*\033[m'*100)
    return ""


while True:
    lin()
    funcao = str(input("\033[1;34mExibir o manual de > \033[m"))
    if funcao == '.':
        break
    ajuda(funcao)
