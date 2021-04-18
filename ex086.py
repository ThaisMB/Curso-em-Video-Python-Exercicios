matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0,3):
    for p in range(0,3):
        matriz[i][p]=(input(f'Digite um valor para a posição {i},{p}:'))

for i in range(0,3):
    for p in range(0,3):
        print(f'[{matriz[i][p]:>5}]',end='')
    print()
