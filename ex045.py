import random

from time import sleep

print("Suas opções:")

print('[0] PEDRA')
print('[1] PAPEL')
print('[2] TESOURA')

escolha = int(input('Qual é a sua jogada?'))

lista= ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(lista)

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(2)

print('-='*20)

print('Computador jogou {}'.format(computador))

if escolha==0:
    print('Jogador jogou PEDRA.')

    if computador=='TESOURA':
            print('JOGADOR VENCE!')
        
    elif computador=='PEDRA':
            print('EMPATE!')

    elif computador=='PAPEL':
            print('COMPUTADOR VENCE!')

elif escolha==1:
    print('Jogador jogou PAPEL.')

    if computador=='PEDRA':
            print('JOGADOR VENCE!')
        
    elif computador=='PAPEL':
            print('EMPATE!')

    elif computador=='TESOURA':
            print('COMPUTADOR VENCE!')

elif escolha==2:
    print('Jogador jogou TESOURA.')

    if computador=='PAPEL':
            print('JOGADOR VENCE!')

    elif computador=='TESOURA':
            print('EMPATE!')

    elif computador=='PEDRA':
            print('COMPUTADOR VENCE!')
else:
    print('\033[31m JOGADA INVÁLIDA!Tente outra vez!\033[m')