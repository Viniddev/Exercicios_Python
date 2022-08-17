import os
os.system("cls")

alunos = {}

print("\033[1;31m-*\033[m"*60)
alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['media'] = float(input('Digite a média do aluno: '))
print("\033[1;31m-*\033[m"*60)

print(f"O nome do Aluno é {alunos['nome']}")
print(f"A media do aluno é {alunos['media']}")

if alunos['media']>0 and alunos['media']<6:
    print('Aluno Aluno Reprovado!')
elif alunos['media']>=6 and alunos['media']<10:
    print('Aluno aprovado!')
elif alunos['media'] == 10:
    print('Arrasou! Media maxima alcançada!')
else:
    print('Erro na analise dos dados!')