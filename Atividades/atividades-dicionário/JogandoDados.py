from random import randint
import time
import os

os.system("cls")
print("\033[1;31m-*\033[m"*60)

jogadas = dict()

for n in range(0,4):
    jogada = randint(1,6)
    jogadas['jogador:' , n+1] = jogada
    print(f'Jogada de numero {n+1} = {jogada}')
    time.sleep(1.5)

print("\033[1;31m-*\033[m"*60)
print(' '*50 , 'Ranking dos jogadores:')
cont = 0

for n in sorted(jogadas, key = jogadas.get, reverse=True):
    cont+=1
    print(f'{cont} colocado: jogador {n}, COM {jogadas[n]}')

print("\033[1;31m-*\033[m"*60)
print(jogadas)
