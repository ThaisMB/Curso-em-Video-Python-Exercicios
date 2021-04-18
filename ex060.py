n = int(input('Digite um número para saber seu fatorial:'))
f = 1



for c in range(n,0, -1):
      f = f*c
      print('{}'.format(c), end='')
      print('x' if c>1 else'=', end='')
print('{}'.format(f))

