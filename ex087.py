matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar=0
ster=0
msl=0
i=0
p=0
for i in range(0,3):
    for p in range(0,3):
        matriz[i][p]=(int(input(f'Digite um valor para a posição {i},{p}:')))
        
       
        
        

print('=-'*30)
for i in range(0,3):
    for p in range(0,3):
        print(f'[{matriz[i][p]:>5}]',end='')
    print()
print('=-'*30)

while matriz[i][p]%2==0:
    spar+=matriz[i][p]
print(f'A soma dos valores pares é {spar}.')
 
while p==2:
    ster+=matriz[i][2]
print(f'A soma dos valores da terceira coluna é {ster}.')

if  matriz[1][p]>msl:
    msl=matriz[1][p]
print(f'O maior valor da segunda linha é {msl}.')