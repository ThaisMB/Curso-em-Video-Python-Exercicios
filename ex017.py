import math

co=float(input('Digite o comprimento do cateto oposto:'))
ca=float(input('Digite o comprimento do cateto adjacente:'))

h= math.hypot(co,ca)

print('A hipotenusa desse triângulo mede {}.'.format(h))