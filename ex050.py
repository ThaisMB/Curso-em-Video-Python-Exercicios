p=0

for c in range(0,6):
    n=int(input('Digite um número:'))

    if n%2==0:
        p= p+n

print('A soma dos valores pares digitados é {}.'.format(p))
