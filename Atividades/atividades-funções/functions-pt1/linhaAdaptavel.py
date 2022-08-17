import os
os.system('cls')

def lin():
    print('\033[1;31m*-\033[m'*60)


def titulador(titulo):
    print()
    print('\033[1;31m*\033[m' * (len(titulo)+8))
    print(f"    {titulo.upper()}")
    print('\033[1;31m*\033[m' * (len(titulo)+8))

lin()
titulo = str(input('Qual o titulo? '))
titulador(titulo)