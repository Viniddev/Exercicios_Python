from modulos import menu
from modulos import inserir
from modulos import mostrar
import os
os.system('cls')

while True:
    menu.tela()
    n1 = inserir.leiaEscolha("Qual opção deseja? ")
    mostrar.valida(n1)

    if n1 == 3:
        break
    if n1 == 4:
        os.system('cls')