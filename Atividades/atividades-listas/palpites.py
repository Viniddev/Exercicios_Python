from random import randint 
from time import sleep 
lista = []
jogos = []
print(' '*20,'MEGA SENA!!')
print("\033[1;31m**\033[m"*30 )
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot<=quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1

print("\033[1;31m**\033[m"*30 )
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')   