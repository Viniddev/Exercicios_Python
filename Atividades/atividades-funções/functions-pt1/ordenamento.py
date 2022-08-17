import os
os.system('cls')
lista = []

def ordenador(* num):
    cont = 0
    maior= menor= 0
    for val in num:
        cont+=1
        if cont == 1:
            maior = menor = val
        if val > maior:
            maior = val
        if val < menor:
            menor = val
    print(f'O maior numero é {maior} e o menor é {menor}')
    print(f'Foram informados {cont} valores')


ordenador(4,3,22,5,56,43,12,0,19)

