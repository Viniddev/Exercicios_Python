import os
os.system('cls')

def area(a, b):
    s= 0
    s= a*b
    print(f"O terreno de dimensões {a}m X {b}m tem área igual a {s} m^2")


def lin():
    print('\033[1;31m*-\033[m'*60)


lin()
c= float(input('Qual o comprimento do lote? '))
l= float(input('Qual a largura do lote? '))
area(c, l)
lin()