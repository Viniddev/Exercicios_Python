matrix = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0,3):
    for j in range(0,3):
        matrix[i][j] = int(input(f'Digite um número para a posição [{i} , {j}]: '))

for i in range(0, 3):
    for j in range(0, 3):
        print(f'\033[1;31m[{matrix[i][j]:^5}]\033[m' , end='')
    print()