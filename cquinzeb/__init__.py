def arquivoExiste(nome):
    try:
        a=open(nome,'rt')
        a.close()

    except FileNotFoundError:
        return False
    
    else:
        return True

def criarArquivo(nome):
    a=open(nome,'wt+')

def lerArquivo(nome):
    try:
        a=open(nome,'rt')
    
    except:
        print('\033[31[mErro ao abrir o arquivo!\033[m')

    else:
        print('-'*60)
        print('\033[34mPESSOAS CADASTRADAS\033[m'.center(35))
        print('-'*60)
        for linha in a:
            dado=linha.split(';')
            dado[1]=dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

def cadastrar(arq,n='desconhecido',i='0'):
    try:
        a=open(arq,'at')
    except:
        print('\033[31mHouve um ERRO na abertura do arquivo\033[m')
    else:
        try:
            a.write(f'{n};{i}\n')
        except:
            print('\033[31mHouve um ERRO na hora de escrever os dados\033[m')
        else:
            print(f'\033[32mNovo registro de {n} adicionado\033[m')
            a.close()
    
