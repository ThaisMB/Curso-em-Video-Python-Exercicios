from random import randint
from time import sleep
números=list()
def sorteia():
    print('Sorteando 5 valores da lista:',end='')
    for c in range(0,5):
        valor=randint(0,10)
        números.append(valor)
        print(valor, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')
    

def somaPar(): 
    spar=0
    for i in números:
        if i%2==0:
            spar+=i
    print(f'Somando os valores pares de {números} temos {spar}.')
sorteia()
somaPar()