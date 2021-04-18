from time import sleep
def maior(*num):
    m=0
    for v in num:    
        if v>m:
            m=v
    print('-='*36)
    print('Analisando os valores apresentados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    sleep(1.5)
    print(f'O maior valor digitado foi {m}.')
    sleep(2.0)

maior(12, 2, 5, 8, 9, 20)
maior(5,6,2,7,1,3)
maior()