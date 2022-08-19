import os
from Utilidades import Dados
from Utilidades import Modulos
os.system('cls')

print('\033[1;34m*\033[m'*120)
n = Dados.leia('Digite uma quantia bancária: ')
Modulos.resumo(n, 25, 50)