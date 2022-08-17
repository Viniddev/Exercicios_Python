import os
os.system('cls')

alunos = []
temp = []
print("\033[1;31m**\033[m"*30 )
while True:
    temp.append(str(input("\033[1;33mDigite o nome do aluno: \033[m")))
    temp.append(float(input('Digite a nota \033[1;31m1\033[m: ')))
    temp.append(float(input('Digite a nota \033[1;31m2\033[m: ')))

    alunos.append(temp[:])
    temp.clear()

    resp = str(input('Deseja continuar cadastrando? \033[1;31m[s/n]\033[m '))
    if resp not in "Ss":
        break

print("\033[1;31m**\033[m"*30 )
print('\033[1;34mNúmero', ' '*10, 'Média', ' '*10, 'Nome\033[m')
for n, o in enumerate(alunos):
    print(' '*3, n , ' '*12 , (o[1]+o[2])/2 , ' '*10 , o[0])

while True:
    print("\033[1;31m**\033[m"*30 )
    opc = int(input('Deseja mostrar as notas de qual aluno? [999= stop]  '))
    if opc == 999:
        print('\033[1;31mEncerrando!\033[m')
        break
    if opc<= len(alunos)-1:
        print(f'Notas do aluno {alunos[opc][0]} são {alunos[opc][1]} e {alunos[opc][2]} ')
     