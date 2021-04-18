def lin():
    print('-'*50)


#Programa Principal
lin()
print('                    CURSO EM VÍDEO')
lin()

def mensagem(msg):
    lin()
    print(msg)
    lin()

mensagem('                    CURSO EM VÍDEO')
mensagem('                    APRENDA PYTHON')
mensagem('                  PYTHON É MUITO BOM!')

def soma(a,b):
    s=a+b
    print(s)


 #Programa Principal
soma(7,8)
soma(5,6)
soma(2,1)

def contador(*num):
    tam=len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!')


#Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

