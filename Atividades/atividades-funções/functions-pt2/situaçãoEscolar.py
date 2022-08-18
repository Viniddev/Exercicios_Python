import os 
os.system('cls')

def notas(*num , sit=True):
    dicionario = {}
    media = maior = menor = 0
    dicionario['notas']= num 
    dicionario['quant-notas']= len(num)
    for k, v in enumerate(num):
        media+=v
        if k == 0:
            maior = menor = v
        if v > maior:
            maior = v
        if v < menor:
            menor = v
    media = media / len(num)
    dicionario['maior-nota']= maior
    dicionario['menor-nota']= menor
    dicionario['media']= media
    if sit:
        if media < 4:
            dicionario['situação']= 'Péssimo'
        elif media >= 4 or media < 7:
            dicionario['situação']= 'Mediano'
        else:
            dicionario['situação']= 'Ótimo'
    else:
        dicionario['situação'] = '---'
    return dicionario


def lin():
    print('\033[1;31m*\033[m'*177)


lin()
situacao = notas(5,4,3,2,7,7,6,9,9,1,10, sit= True)
print(situacao)
lin()
