import os
from random import randint
from time import sleep 

os.system('cls')
lista = []
lista2 = []
soma= 0

def lin():
    print('\033[1;31m*-\033[m'*60)


def sorteia(lista):
    cont= 0
    print('Os numeros sorteados são: ',end = "")
    for cont in range(0,5):
        n= randint(0,100)
        lista.append(n)
        print(n, flush= True, end = " ")
        sleep(1.5)
    print()


def somaPar(lista):
    soma = 0
    for n in lista:
        if n%2==0:
            lista2.append(n)
            soma = n + soma
    print(f'A soma dos valores pares é {soma}')
    print(f'Os números pares sorteados são {lista2}')


lin()
sorteia(lista)
lin()
somaPar(lista)
lin()
