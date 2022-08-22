def valida(num):
    if num == 1:
        with open("informacoes.txt", "a", encoding='utf-8') as codigo:
            nome = str(input('Digite o nome: '))
            idade = int(input('Digite a idade: '))
            sexo = str(input('Digite qual o sexo [F/M]: '))
            texto = codigo.write(f'{nome:<40}{idade:<20}{sexo.upper()}\n')
    elif num == 2:
        with open('informacoes.txt', 'r', encoding='utf-8') as codigo:
            mensagem = codigo.readlines()

        print('\033[1;34m**\033[m'*60)
        print(" "*44, "\033[1;33mPESSOAS CADASTRADAS:\033[m")
        print('\033[1;34mNomes\033[m', ' '*30,
              '\033[1;34mIdades\033[m', ' '*13, '\033[1;34mSexo\033[m')
        print('\033[1;34m**\033[m'*60)

        for linhas in mensagem:
            print(linhas)
    else:
        print('\033[1;34mOBRIGADO POR USAR NOSSOS SERVIÇOS\033[m')
