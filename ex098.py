from time import sleep
def contador(início, fim, passo):
    print('-='*36)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')
    if passo<0:
        passo*=-1
    if passo==0:
        passo=1
    if fim>início:
        for c in range(início,fim+1,passo):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    else:
        for c in range(início, fim-1,-(passo)):
            print(c, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
    

contador(1,10,1)
contador(10,0,2)
print('-='*36)
print('Agora é sua vez de personalizar a contagem!')
i= int(input('Início:'))
f= int(input('Fim:'))
p= int(input('Passo:'))

contador(i, f, p)
