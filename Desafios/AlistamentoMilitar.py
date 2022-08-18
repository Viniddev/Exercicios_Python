# alistamento militar obrigatorio brasileiro
from datetime import date
import os
os.system('cls')
datahj = date.today().year
print('\033[1;32mALISTAMENTO\033[m \033[1;33mMILITAR\033[m \033[1;34mBRASILEIRO!!!\033[m')

print('\033[1;31m~\033[m'*67)
sexo = str(input('\033[1;31mQual o seu sexo? [F/M]\033[m '))

sexo = sexo.upper()

if sexo == "F":
    print('\033[1;31m~\033[m'*67)
    resp = str(input(
        'Alistamento \033[1;32mnão obrigatório\033[m em território nacional. \nDeseja se alistar mesmo assim? [S/N] '))
    resp = resp.upper()
    if resp == "S":
        print('Ok, então vamos às perguntas: ')
        print()
        idade = int(input("Em que ano você nasceu? "))
        print()
        if datahj-idade < 18:
            print('     Ainda não é o momento do seu alistamento. Você deverá se alistar em {}'.format(
                idade+18))
        elif datahj-idade == 18:
            print('\033[1;31mATENÇÃO!!!\033[m')
            print('     Estamos no ano do seu alistamento! \nCompareça a junta do serviço militar da sua região para formalizar sua situação.')
        elif datahj-idade > 18:
            print('\033[1;31mATENÇÃO!!!\033[m')
            print(
                '     Ja passou o prazo do seu alistamento! \nCompareça a junta militar imediatamente!!')
            print()
            print('          Você deveria ter se alistado no ano:{}! '.format(idade+18))
    else:
        print()
        print(
            'Pois então, sua situação está \033[1;32mnormalizada!\033[m. Adeus!')

elif sexo == "M":
    print('\033[1;34m~\033[m'*67)
    idade = int(input("Em que ano você nasceu? "))
    print()
    if datahj-idade < 18:
        print('     Ainda não é o momento do seu alistamento. \nVocê deverá se alistar em {}'.format(idade+18))
    elif datahj-idade == 18:
        print('\033[1;31mATENÇÃO!!!\033[m')
        print('     Estamos no ano do seu alistamento! \nCompareça a junta do serviço militar da sua região para formalizar sua situação.')
    elif datahj-idade > 18:
        print('\033[1;31mATENÇÃO!!!\033[m')
        print('     Ja passou o prazo do seu alistamento! \nCompareça a junta militar imediatamente!!')
        print()
        print('          Você deveria ter se alistado no ano:{}! '.format(idade+18))
        print()
else:
    print('\033[1;31mErro ao analisar os dados! Tente novamente mais tarde!! \033[m')
print()

print('Obrigado por usar nossos serviços! \033[1;34mFDK\033[m agradece!')
