matrix = [[0,0,0],[0,0,0],[0,0,0]]
num=soma=col=maior=menor=0

for l in range(0,3):
    for c in range(0,3):
        matrix[l][c]= int(input(f'Digite um numero para a posição \033[1;33m[{l} , {c}]\033[m: '))
        num = matrix[l][c]
        if num%2==0:
            soma+=num
        if c==2:
            col+=num
        if l==1:
            if c==0:
                maior=menor=num
            if num>maior:
                maior=num
            if num<menor:
                menor=num

print()
print("\033[1;31m**\033[m"*30 )
print(f'a soma dos valores da terceira coluna é {col}')
print(f'a soma de todos os valores pares digitados é {soma}')
print(f'o maior numero da segunda linha é {maior}')
print(f'o menor valor da segunda linha é {menor}')
print("\033[1;31m**\033[m"*30 )
print()

for l in range(0,3):
    for c in range(0,3):
        print(f'\033[1;31m[{matrix[l][c]:^5}]\033[m', end='')
    print()
