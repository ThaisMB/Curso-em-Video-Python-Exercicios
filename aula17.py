num= [2,5,9,1]
print(num)
num[2]=3
num.append(7)
num.insert(1,8)
print(num)
num.pop()
print(num)
num.append(2)
print(num)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores=[]
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

print('\n')

for c,v in enumerate(valores):
    print(f'Na posição {c} está {v}.')
