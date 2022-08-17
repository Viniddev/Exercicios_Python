from operator import truediv
import os 
from time import sleep
os.system('cls')

def fatorial(num, valid=0):
    tot = 1
    if valid:
        for n in range(num, 0, -1):
            tot = tot*n
            if n > 1:
                print(n, end = " X ", flush=True)
                sleep(.5)
            if n == 1:
                print(n, end=" = ", flush= True)
                sleep(.5)
        print(tot)
    else:
        for n in range(num, 1, -1):
            tot = tot*n
        print(f'{fat}! = {tot}')
    return ''



def lin():
    print('\033[1;31m*\033[m'*120)


lin()
fat = int(input('Qual numero deseja ver o fatorial? '))
tela = str(input('Deseja mostrar os valores na tela? [s/n] '))

if tela.upper() == "S":
    print(fatorial(fat, valid = True))
    lin()
elif tela.upper() == "N":
    print(fatorial(fat, valid = False))
    lin()
else:
    while tela.upper() not in "SN":
        lin()
        print('Digite uma resposta válida! ')
        tela = str(input('Deseja ver os calculos na tela? [s/n] '))
        if tela.upper() == "S":
            print(fatorial(fat, valid = True))
        if tela.upper() == "N":
            print(fatorial(fat, valid = False))
        