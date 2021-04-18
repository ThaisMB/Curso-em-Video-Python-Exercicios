def teste():
    
    a=8
    b=2
    b+=4
    global a:
    print(a)
    print(b)


teste()
a=5
print(a)

from time import sleep
for n in range (1,11):
    for c in range(0,11):
        #print('{:2} x {:2} = {:3}'.format(n, c, n*c))
        sleep(0.5)
    print(' ')
