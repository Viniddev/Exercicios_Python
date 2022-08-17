temp = [[], []]
num= 0
while True:
    num = int(input("Digite um número: "))
    if num%2==0:
        temp[0].append(num)
    else:
        temp[1].append(num)

    resp = str(input("Deseja continuar cadastrando? [s/n] "))
    if resp in "Nn":
        break

print()
print("\033[1;31m**\033[m"*30 )
print(f'Os números pares são {sorted(temp[0])} e os numeros impares são {sorted(temp[1])}')
print("\033[1;31m**\033[m"*30 )
