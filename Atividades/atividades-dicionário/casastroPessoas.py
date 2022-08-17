import os 
os.system("cls")

media = 0
pessoas = {}
grupo = []
mulheres = []

print("\033[1;31m-*\033[m"*60)
while True:
    pessoas['nome']= str(input('Digite o \033[1;31mNome\033[m: '))
    pessoas['idade']= int(input(f'Digite a Idade de \033[1;31m{pessoas["nome"]}\033[m: '))

    media += pessoas['idade']

    pessoas['sexo']= str(input('Qual o Sexo \033[1;31m[f/m]:\033[m '))
    while pessoas['sexo'].upper() not in "MF":
        print('Digite uma resposta valida!')
        pessoas['sexo']= str(input('Qual o Sexo \033[1;31m[f/m]:\033[m '))

    if pessoas['sexo'].upper() == 'F':
        mulheres.append(pessoas['nome'])

    grupo.append(pessoas.copy())
    pessoas.clear()

    resp= str(input('deseja continuar cadastrando \033[1;31m[s/n]:\033[m '))
    if resp.upper() == "N":
        print("\033[1;31m-*\033[m"*60)
        break
    else:
        while resp.upper() not in "SN":
            print('Digite uma resposta valida! ')
            resp= str(input('Deseja continuar cadastrando [s/n]: '))
            if resp.upper() == "N":
                break

media= media/len(grupo)
print(f'A) Foram cadastradas \033[1;33m{len(grupo)}\033[m pessoas')
print(f'B) A média das idades é \033[1;33m{media:.2f}\033[m anos')
print(f'C) As mulheres cadastradas são:\033[1;31m', end='')
for i, v in enumerate(mulheres):
    print(v, end=' ')
print("\033[m")

print('D) Lista das pessoas que estão acima da média: ')
for n, i in enumerate(grupo):
    if i['idade'] > media:
        print(f'\033[1;34m    Nome: {i["nome"]} | Sexo: {i["sexo"]} | Idade: {i["idade"]} \033[m')

