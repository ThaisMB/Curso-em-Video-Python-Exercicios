t=0

n=int(input('Digite um número para saber sua tabuada:'))

for c in range(0,11):
    t=n*c
    print('{}x{}={}'.format(n,c,t))