# triangulo
import os
os.system('cls')

print('\033[1;31m~\033[m'*67)
cat1 = int(input('Digite o valor do lado 1: '))
cat2 = int(input('Digite o valor do lado 2: '))
cat3 = int(input('Digite o valor do lado 3: '))
print('\033[1;31m~\033[m'*67)

if cat1 > cat2+cat3 or cat2 > cat1+cat2 or cat3 > cat1+cat2:
    print(
        f'É impossivel formar um triangulo com as medidas {cat1}, {cat2}, {cat3}.')
elif cat1 == cat2 and cat2 == cat3 and cat1 == cat3:
    print(
        f'O triangulo formado pelos lados {cat1}, {cat2}, {cat3}, é Equilátero.')
elif cat1 != cat2 and cat2 != cat3 and cat1 != cat3:
    print(
        f'O triangulo formado a partir dos lados é Escaleno,\n possuindo os lados: {cat1}, {cat2}, {cat3}.')
else:
    print(
        'O triangulo formado a partir dos lados: {cat1}, {cat2}, {cat3}, é Isosceles.')

print('\033[1;31m~\033[m'*67)

print('\033[1;34mObrigado por usar nossos serviços!! tenha uma boa semana!\033[m')

print('\033[1;31m~\033[m'*67)
