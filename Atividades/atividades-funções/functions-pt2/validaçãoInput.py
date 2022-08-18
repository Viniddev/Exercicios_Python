from operator import truediv
import os 
os.system("cls")

def leia(msg):
    """
    leia: verificador numérico;
    ok: gatilho para parada;
    N: número digitado;
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[1;31mErro, digite um número Válido!!!\033[m")
        if ok:
            break
    return valor


n= leia("Digite um número: ")
print(f"Você acabou de digitar o número {n}")