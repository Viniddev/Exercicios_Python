# jogo 28 melhorado
import random
import math
import time
import os
os.system('cls')

tentativa = -1
choice = 11
num = random.randint(0, 10)
print("\033[1;34m°•\033[m"*33)
print("\033[1;33m    	Digite um valor entre 0 e 10! Se você acertar, ganhará \n       		10R$ - numero de tentativas!\033[m")
print("\033[1;34m°•\033[m"*33)
print()

while choice != num:
    choice = int(input("Digite um valor: "))
    tentativa += 1
    if choice > num:
        print("Hmmm...")
        time.sleep(2)
        print("\033[1;33mUm pouco menos...\033[m")
    elif choice < num:
        print("Ora, ora...")
        time.sleep(2)
        print("\033[1;31mUm pouco mais...\033[m")
    else:
        print("Bom...")
        time.sleep(1)
        print("Acho que...")
        time.sleep(1)
        print("\033[1;32mVOCÊ ACERTOU!\033[m")
print("O numero de tentativas foi: ", tentativa)
print("Sendo assim, você receberá: {}R$".format(10-tentativa))
