# conversor de bases numericas + while
import os
from datetime import datetime

hora = datetime.now().hour

if hora >= 4 and hora < 12:
    print('Bom dia! Bem vindo ao Conversor!')
elif hora >= 12 and hora < 18:
    print('Boa tarde! Bem vindo ao Conversor!')
elif hora >= 18 and hora < 23:
    print('Boa noite! Bem vindo ao Conversor!')
else:
    print('Vai dormir, menino maluco! Programamos à luz do dia!!')

conclusao = "SIM"

while conclusao == "SIM":
    print('Veja as possibilidades abaixo: ')
    print('\033[1;31m~\033[m'*67)
    #print('[=] -> Posiciona o sinal do número \033[1;31mmais à esquerda\033[m.')
    print('[b] -> Converte o número desejado para \033[1;31mbinário\033[m.')
    print('[x] -> Converte o número desejado para \033[1;31mhexadecimal\033[m.')
    print('[o] -> Converte o número desejado para \033[1;31moctal\033[m.')
    #print('[d] -> Converte o número desejado para \033[1;31mdecimal\033[m.')
    print('[E] -> Converte o número desejado para a \033[1;31mbase científica\033[m.')
    print('[X] -> Converte o número desejado para \033[1;31mhexadecimal em maiúsculas\033[m. ')
    print('\033[1;31m~\033[m'*67)
    choice = str(input('Qual sua escolha? '))
    # if choice== "=":
    #print('\033[1;31mOpção escolhida com sucesso!\033[m')
    #num=float(input("Qual numero deseja converter? "))
    #print('Por meio da conversão, o valor final será: \033[1;31m{}\033[m' .format(format(num, '=')))
    if choice == "b":
        print('\033[1;31mOpção escolhida com sucesso!\033[m')
        num = int(input("Qual numero deseja converter? "))
        print('Por meio da conversão, o valor final será: \033[1;31m{}\033[m' .format(
            format(num, 'b')))
    elif choice == "x":
        print('\033[1;31mOpção escolhida com sucesso!\033[m')
        num = int(input("Qual numero deseja converter? "))
        print('Por meio da conversão, o valor final será: \033[1;31m{}\033[m' .format(
            format(num, 'x')))
    elif choice == "o":
        print('\033[1;31mOpção escolhida com sucesso!\033[m')
        num = int(input("Qual numero deseja converter? "))
        print('Por meio da conversão, o valor final será: \033[1;31m{}\033[m' .format(
            format(num, 'o')))
    # elif choice=="d":
        #print('\033[1;31mOpção escolhida com sucesso!\033[m')
        #num=int(input("Qual numero deseja converter? "))
        #print('Por meio da conversão, o valor final será: \033[1;31m{}\033[m' .format(format(num, 'd')))
    elif choice == "E":
        print('\033[1;31mOpção escolhida com sucesso!\033[m')
        num = int(input("Qual numero deseja converter? "))
        print('Por meio da conversão, o valor final será: \033[1;31m{}\033[m' .format(
            format(num, 'E')))
    elif choice == "X":
        print('\033[1;31mOpção escolhida com sucesso!\033[m')
        num = int(input("Qual numero deseja converter? "))
        print('Por meio da conversão, o valor final será: \033[1;31m{}\033[m' .format(
            format(num, 'X')))
    else:
        print(
            '\033[1;31mErro na interpretação dos dados, tente novamente mais tarde!\033[m')
    print()
    conclusao = str(input('Deseja continuar convertendo?[sim/nao] '))
    conclusao = conclusao.upper()
    if conclusao == 'SIM':
        os.system('cls')
        print()
    elif conclusao == 'NAO':
        print('Encerrando Sistema...')
        print()
    else:
        print('Erro na identificação dos valores! Tente novamente mais tarde!')
print()
print('Obrigado por usar nossos serviços! \033[1;34mFDK\033[m agradece!')
