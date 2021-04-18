from random import randint

n1= randint(0,100)
n2= randint(0,100)
n3= randint(0,100)
n4= randint(0,100)
n5= randint(0,100)


n = (n1, n2, n3, n4, n5)

print(f'Os valores sorteados foram:{n}.' )

m = sorted(n)

print(f'O maior valor sorteado foi:{m[4]}.')

print(f'O menor valor sorteado foi:{m[0]}.')