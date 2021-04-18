from time import sleep
c=('\033[m',         #0- sem cores
   '\033[0,30,41m',  #1- vermelho
   '\033[0,30,42m',  #2- verde
   '\033[0,30,43m',  #3- amarelo
   '\033[0,30,44m',  #4- azul
   '\033[0,30,45m',  #5- magenta
   '\033[0,30,46m',  #6- ciano
   '\033[7,30m',     #7- branco
   );

def ajuda(com):
    help(com)

def título(msg,cor=0):
    tam=len(msg)+4
    print('~'*tam)   
    print(f'  {msg}  ')
    print('~'*tam)  
        



while True:
    título('SISTEMA DE AJUDA PyHELP',2)
    comando = input('Função ou Biblioteca >')
    if comando.upper()=='FIM':
        break
    if comando.upper() != 'FIM':
        título(f'Acessando o manual do comando "{comando}"...',3)
        sleep(1.0)
        print(c[6], end='')
        print(ajuda(comando))
        print(c[0],end='')
        sleep(1)
    

título('ATÉ LOGO!',1)




