estados = {}
brasil = []

for c in range(0,2):
    estados['uf'] = str(input('Unidade Federativa: '))
    estados['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estados.copy())

for e in brasil:
    for v in e.values():
        print(f'{v}', end=' ')
    print()