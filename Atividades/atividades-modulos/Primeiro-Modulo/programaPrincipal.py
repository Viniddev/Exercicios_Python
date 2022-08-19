import modulo
import os
os.system('cls')

n = float(input('Digite um valor: R$'))
modulo.lin()
print(f"Com um acrescimo de 10%, o valor fica R${modulo.aumento(n):.2f}")
print(f"Com um desconto de 10%, o valor fica R${modulo.desconto(n):.2f}")
print(f"A metade do preço é R${modulo.metade(n):.2f}")
print(f'O dobro do preço é R${modulo.dobro(n):.2f}')
modulo.lin()