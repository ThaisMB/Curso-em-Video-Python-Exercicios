def leiaInt(msg):
    while True:
        try:
            print('\033[36m=\033[m'*60)
            n=int(input(msg))       
        except (ValueError, TypeError):
            print('\033[31mERRO!Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[33mEntrada de dados interrompida pelo usuário.')
            print( 'Você não digitou nenhum número.\033[m')
            break
        else:
            print(f'\033[32mVocê  acabou de digitar o número {n}.\033[m')
            break
           
def leiaFloat(msg):
    while True:
        try:
            print('\033[35m><\033[m'*30)
            n=float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO!Digite um número válido!\033[m')
        except(KeyboardInterrupt):
            print('\n\033[33mO usuário interrompeu a entrada de dados!\033[m')
            print('\033[33mNenhum valor digitado!\033[m')
            break
        else:
            print(f'\033[34mVocê digitou o valor {n}.\033[m')
            break

           

num=leiaInt('Digite um número inteiro:')
real=leiaFloat("Digite um número real:")


