import random

from time import sleep

print('Pensei em um número entre 0 e 5. Você consegue adivinhar?')


lista=[0, 1, 2, 3, 4, 5]

n= random.choice(lista)

c=int(input('Em qual número eu pensei?'))

if c==n:
 print('PROCESSANDO...')   
 sleep(5)
 print("PARABÉNS! Você acertou o número em que eu pensei!")

else:
 print('PROCESSANDO...')   
 sleep(5)
 print("GANHEI! Eu pensei no número {} e não no {}.".format(n, c))