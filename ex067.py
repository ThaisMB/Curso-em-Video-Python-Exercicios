
n = 1


while True:

    n= int(input('Quer ver a tabuada de qual número?'))
    print('----'*10)

    if n<0:
        print('PROGRAMA DE TABUADA ENCERRADO!Volte Sempre!')
        break

    else:

        contador= 0

        while contador<=10:

            resultado = n*contador

            print(f'{n}x{contador}={resultado}')

            contador += 1



    

