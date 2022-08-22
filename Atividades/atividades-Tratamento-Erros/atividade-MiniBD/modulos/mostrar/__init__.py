def valida(num):
    if num == 1:
        with open("informacoes.txt", "a", encoding='utf-8') as codigo:
            nome = str(input('Digite seu nome: '))
            idade = int(input('Digite sua idade: '))
            texto = codigo.write(f'{nome:<40}{idade}\n')
    elif num == 2:
        with open('informacoes.txt', 'r', encoding='utf-8') as codigo:
            mensagem = codigo.readlines()

        print('\033[1;34m**\033[m'*60)
        print(" "*44,"\033[1;33mPESSOAS CADASTRADAS:\033[m")
        print('\033[1;34mNomes\033[m', ' '*30, '\033[1;34mIdades\033[m')
        print('\033[1;34m**\033[m'*60)
        
        for linhas in mensagem:
            print(linhas)
    else:
        print('\033[1;34mOBRIGADO POR USAR NOSSOS SERVIÇOS\033[m')