import os
import modulos
os.system('cls')

modulos.lin()
n = float(input('Digite um número: R$'))
print(f'    {modulos.moeda(n)} Com um aumento de 10%, o valor final é {modulos.aumento(n, 10, True)}')
print(f'    {modulos.moeda(n)} Com um desconto de 25%, o valor final é {modulos.desconto(n, 25 , False)}')
print(f'    O dobro é {modulos.dobro(n, True)}')
print(f'    A metade é {modulos.metade(n, False)}')
modulos.lin()