print('-='*20)
print('           GERADOR DE P.A.          ')
print('-='*20)

a1 = int(input('Digite o 1º termo:'))
r = int(input('Digite a razão da P.A.:'))
c= a1

print(a1, end = ' ')

while c!=a1+(9*r):
    c= c+r
    print(c, end = ' ')

t = int(input('\nQuantos termos a mais você quer mostrar?'))
a = 0

a1 = c

while a < t:
    a += 1

    while c!=a1+(t*r):

        c=c+r
        print(c, end = ' ')


tm=10+t
print('\nProgressão finalizada com {} termos mostrados!'.format(tm))
