from random import randint

computador = randint(0,10)
vitorias = 0

print('\033[35m-=\033[m'*30)
print('\033[36m           VAMOS JOGAR PAR OU ÍMPAR?\033[m')
print('\033[35m-=\033[m'*30)

while True:

    jogador = int(input('Digite um valor:'))
    poi = input('Par ou Ímpar? [P/I]').upper()

    total = computador+jogador 

    print('\033[35m--\033[m'*30)

    if total % 2 == 0:
        resultado = 'P'
        print(f'Você jogou {jogador} e o computador jogou {computador}.Total de {total} DEU PAR!')
        print('\033[35m--\033[m'*30)

    else:
        resultado = 'I'
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total} DEU ÍMPAR!')
        print('\033[35m--\033[m'*30)

    if poi==resultado:
        print('\033[34m Você VENCEU!\033[m \n Vamos jogar novamente...')
        vitorias += 1

    else:
        print('\033[31m Você perdeu! \033[m')
        print('\033[33m-=\033[m'*30)
        print(f'\033[31mGAME OVER!\033[mVocê venceu {vitorias} vezes!')
        break
