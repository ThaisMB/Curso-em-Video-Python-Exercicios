from cquinzeb import *
def cabeçalho(txt):
    print('-'*30)
    print(txt.center(30))
    print('-'*30)


def leiaInt(msg):
   while True:
        try:
            n=int(input(msg))       
        except (ValueError, TypeError):
            print('\033[31mERRO!Digite um número inteiro válido.\033[m')
            
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            print( '\033[33mO usuário não digitou nenhum número.\033[m')
            break
        else:
            arquivo=('cursoemvideo.txt')
            if not arquivoExiste(arquivo):
                criarArquivo(arquivo)
        
            if n==1:
                lerArquivo(arquivo)
                break
            if n==2:
                cabeçalho('\033[36mNOVO CADASTRO\033[m')
                nome=input('Nome:')
                idade=input('Idade:')
                cadastrar(arquivo,nome,idade)
                break
            if n==3:
                cabeçalho('\033[35mSaindo do sistema...Até logo!\033[m')
                break
            if n >4:
                print('\033[31mERRO!Digite uma opção válida!\033[m')
    



    
    