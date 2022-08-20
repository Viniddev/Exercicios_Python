def leiaInt(i):
    while True:
        try:
            n = int(input(i))
        except:
            print(f"ERRO! Digite um numero inteiro válido!!!")
        else:
            return n
    
def leiaFloat(f):
    while True:
        try:
            n = float(input(f))
        except:
            print(f"ERRO! Digite um numero inteiro válido!!!")
        else:
            return n

def lin():
    print('\033[1;31m**\033[m'*60)