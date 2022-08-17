from datetime import datetime 
import os
os.system("cls")

ano = datetime.now().year

funcionario = {}

funcionario['nome']= str(input('Qual o nome do funcionário? '))
funcionario['ano-nasc']= int(input('Qual o ano de nascimento? '))
funcionario['carteira-trabalho']= int(input('Numero da carteira de trabalho: [0 = não tem]: '))
funcionario['idade']= ano - funcionario['ano-nasc']

if funcionario['carteira-trabalho'] == 0:
    print("\033[1;31m-*\033[m"*60)
    print(f'O nome do funcionário é: {funcionario["nome"]}')
    print(f'O funcionário tem {ano - funcionario["ano-nasc"]} anos')
    print(f'O funcionário não tem carteira assinada!')
else:
    print("\033[1;31m-*\033[m"*60)
    funcionario['contratacao']= int(input('Qual o ano da efetivação da contratação? '))
    funcionario['salario']= float(input('Qual o salário do funcionario? '))
    print("\033[1;31m-*\033[m"*60)
    print(f'O nome do funcionário é: {funcionario["nome"]}')
    print(f'O funcionário tem {ano - funcionario["ano-nasc"]} anos')
    print(f'{funcionario["nome"]} tem a carteira de trabalho de numero {funcionario["carteira-trabalho"]}')
    funcionario['aposentadoria']= (funcionario['contratacao']+40) - funcionario['ano-nasc']
    print(f'{funcionario["nome"]} Possui um salário de {funcionario["salario"]} e vai se aposentar com {funcionario["aposentadoria"]} anos')

print("\033[1;31m-*\033[m"*60)
print(funcionario)