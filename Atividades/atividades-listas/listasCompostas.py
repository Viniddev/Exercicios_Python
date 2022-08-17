temp = []
final = []
maior = menor = 0

while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))

    final.append(temp[:])
    if len(final) == 1:
        maior= temp[1]
        menor= temp[1]

    if temp[1] > maior:
        maior = temp[1]
    if temp[1] < menor:
        menor = temp[1]

    temp.clear()
    resp = str(input('Deseja continuar cadastrando? [s/n] '))
    if resp in "Nn":
        break

print("\033[1;31m**\033[m"*30 )
print(f'O número de pessoas cadastradas foi: {len(final)}')
print(f'O maior peso foi {maior} e quem o obteve foi: ', end="")
for n in final:
    if n[1] == maior:
        print(n[0], end=' | ')

print()
print(f'O menor peso foi {menor} e foi obtido por:', end="")
for n in final:
    if n[1] == menor:
        print(n[0], end=' | ')

print()
print("\033[1;31m**\033[m"*30 )