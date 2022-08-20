from modulos import leiaInt
from modulos import leiaFloat
from modulos import lin
import os
os.system('cls')

lin()
i = leiaInt('Digite um número Inteiro: ')
f = leiaFloat('Digite um número Real: ')
lin()
print(f'O número inteiro digitado foi {i} e o real foi {f}')