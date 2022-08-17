import os 
os.system("cls")
jogador = {}
jogadores = []
gols = []
total= gol= 0
print("\033[1;31m-*\033[m"*60)

while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['jogos']= int(input(f'Quantos jogos {jogador["nome"]} jogou na ultima rodada? '))
    for n in range(1, jogador['jogos']+1):
        gol= int(input(f'   Quantos gols marcados no \033[1;33m{n}\033[m jogo? '))
        total+=gol
        gols.append(gol)

    jogador['gols-partida']=gols[:]
    jogador['total-gols']= total
    jogadores.append(jogador.copy())
    gols.clear()
    total= 0

    resp=str(input('Deseja continuar cadastrando? [s/n] '))
    print("\033[1;31m-*\033[m"*60)
    if resp.upper() == "N":
        break
    else:
        while resp.upper() not in "SN":
            print('digite uma resposta válida')
            resp= str(input('Deseja continuar cadastrando? [S/N] '))
            if resp.upper() == "N":
                break

print('\033[1;33mCodigo e Nome', ' '*15, 'partidas', ' '*25, 'gols', ' '*15 , 'total de gols\033[m')
for k, i in enumerate(jogadores):
    print(f' {k:>5} ', end='')
    for d in i.values():
        print(f' {str(d):<25} ', end='')
    print()
print("\033[1;31m-*\033[m"*60)

while True:
    resp= int(input("Deseja ver os dados de qual jogador? (999 = stop) "))
    if resp == 999:
        break
    if resp > len(jogadores):
        print("Código de jogador inválido!!!")
    else:
        print(f'Dados do jogador \033[1;31m{jogadores[resp]["nome"]}\033[m')
        for n, d in enumerate(jogadores[resp]['gols-partida']):
            print(f'    No \033[1;34m{n+1}\033[m jogo foram marcados \033[1;33m{d}\033[m gols')

    print("\033[1;31m-*\033[m"*60)