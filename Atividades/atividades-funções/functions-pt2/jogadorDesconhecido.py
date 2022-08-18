import os
os.system('cls')

def show(n=" ", g=0):
    if n == "":
        n= '<desconhecido>'
    if g == "":
        g= 0
    return f'O jogador {n} marcou {g} gols na ultima partida'


def lin():
    print("\033[1;31m*\033[m"*60)


lin()
nome = str(input("Digite o nome do jogador: "))
gols = str(input("Quantos gols ele marcou no ultimo jogo? "))
if gols.isnumeric():
    gols = int(gols)

lin()
print(show(n=nome, g=gols))
lin()
