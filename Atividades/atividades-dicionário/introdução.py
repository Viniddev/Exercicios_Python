pessoas = {
    "nome" : "jose",
    "idade" : 22,
    "sexo" : "masc",
    "profissão" : "programador"
}
pessoas2 = {
    "nome" : "alex",
    "idade" : 27,
    "sexo" : "não declarado",
    "profissão" : "programador"
}
turma = []
turma.append(pessoas)
turma.append(pessoas2)

for i, j in enumerate(turma):
    print(f'{i+1} = {j}')

#print(pessoas.values())
#print(pessoas.items())
#print(pessoas.keys())
#for keys, values in pessoas.items():
#    print(f'{keys} = {values}')