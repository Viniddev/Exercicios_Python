import os
import time
os.system('cls')

def crescente(i,f,r):
    print(i, end=', ')
    while i < f:
        i+=r
        print(i, end=', ', flush = True)
        time.sleep(.4)
    print('FIM')


def decrescente(i,f,r):
    print(i, end=', ')
    while i > f:
        i-=r
        print(i, end=', ', flush = True)
        time.sleep(.4)
    print('FIM')


def lin():
    print('\033[1;31m*-\033[m'*60)


lin()
i = int(input('Digite o início: '))
f = int(input('Digite o final: '))
r = int(input('Digite a razão: '))
lin()

if r < 0:
    r *= -1
    
if r==0:
    r=1
    print('Razão não pode ser nulo. r= 1;')

if i > f:
    decrescente(i,f,r)
elif i < f:
    crescente(i,f,r)
elif i == f:
    print('Início é igual ao final!')
else:
    print('Erro na análise dos dados!')
