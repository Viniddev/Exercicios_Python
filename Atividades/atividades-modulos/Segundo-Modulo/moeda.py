import os
import main
os.system('cls')

main.lin()
n = float(input('Digite um número: R$'))
print(f'    {main.moeda(n)} Com um aumento de 10%, o valor final é {main.moeda(main.aumento(n))}')
print(f'    {main.moeda(n)} Com um desconto de 10%, o valor final é {main.moeda(main.desconto(n))}')
print(f'    O dobro é {main.moeda(main.dobro(n))}')
print(f'    A metade é {main.moeda(main.metade(n))}')
main.lin()