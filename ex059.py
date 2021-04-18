from time import sleep
 
opção = 0
resposta = 0
 
while opção!=5:

    n1 = int(input('Digite um número:'))
    n2 = int(input('Digite outro número:'))
    

    print('\033[32m-----Escolha uma opção:-----\033[m')
    print('\033[33m [1]\033[m \033[34m  somar \033[m')
    print('\033[33m [2]\033[m \033[34m  multiplicar \033[m')
    print('\033[33m [3]\033[m \033[34m  maior \033[m')
    print('\033[33m [4]\033[m \033[34m  novos números \033[m')
    print('\033[33m [5]\033[m \033[34m  sair do programa:\033[m')
 
    opção = int(input('<<<<<<Qual sua opção?'))

    if opção==1:

        resposta= n1+n2

        print('A soma entre {} e {} é {}.'.format(n1, n2, resposta))

    elif opção==2:

        resposta= n1*n2

        print('O resultado de {}x{} é {}.'.format(n1, n2, resposta))

    elif opção==3:

        if n1>n2:
            resposta = n1

        else:
            resposta = n2

        print('Entre {} e {}, o maior é {}.'.format(n1, n2, resposta))

    elif opção==4:

        print("Informe os números novamente:")

    elif opção==5:

        print('Finalizando...')
        sleep(3)
        print('Fim do Programa!Volte Sempre!')
        

    else:
        
        print('Opção Inválida. Tente novamente!')



 

