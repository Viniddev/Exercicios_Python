import os
os.system("cls")

jogador = {}
gols = []
gol = total = 0

jogador['nome']= str(input('Qual o nome do jogador? '))
jogador['partidas']= int(input(f'Quantas partidas {jogador["nome"]} jogou na ultima rodada? '))
print("\033[1;31m-*\033[m"*60)

for n in range(1, jogador['partidas']+1):
    gol= int(input(f'   Quantos gols no \033[1;31m{n}\033[m jogo? '))
    total+=gol
    gols.append(gol)

print("\033[1;31m-*\033[m"*60)
jogador['gols']= gols
jogador['total']= total
print(jogador)
print("\033[1;31m-*\033[m"*60)
for k, v in jogador.items():
    print(f'O campo \033[1;31m{k}\033[m teve o valor \033[1;33m{v}\033[m')

print("\033[1;31m-*\033[m"*60)

print(f'\033[1;34mO jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas:\033[m ')
for n in enumerate(gols):
    print(f'    Na \033[1;31m{n[0]+1}\033[m partida marcou \033[1;34m{n[1]}\033[m gols')