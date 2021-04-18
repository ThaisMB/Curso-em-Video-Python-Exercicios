from random import randint

from time import sleep

palpite = 0

chute = 11

print('Pensei em um número entre 0 e 10. Você consegue adivinhar?')

computador = randint(0,10)



while chute!=computador:

    chute = int(input('Em qual número eu pensei?'))

    print('\033[33m PROCESSANDO... \033[m')
    sleep(2)
        
    if computador>chute:
        print('\033[31m Mais...Tente outra vez!\033[m]')

    elif computador<chute:
        print('\033[31m Menos...Tente outra vez!\033[m')

    palpite += 1


print('\033[36m PARABÉNS!Acertou com {} tentativas!\033[m'.format(palpite))

