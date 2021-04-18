ficha=dict()
stotal=0
npartidas=0
gols=[]
time=[]

while True:
    ficha=dict()
    gols=list()
    ficha['nome']=str(input('Nome do jogador:'))
    npartidas=int(input(f'Quantas partidas {ficha["nome"]} jogou?'))
    for c in range(1,npartidas+1):
        g=int(input(f'Quantos gols na partida {c}?'))
        gols.append(g)
        stotal=stotal+g
        ficha['gols']=gols
        ficha['total']=stotal
    time.append(ficha)
    
    resposta=str(input('Quer continuar? [S / N]')).upper()
    if resposta == 'N':
        break
print('-' * 80)
print(f'\t{"cód.":^6}|\t{"nome":10}|\t{"gols":^30}\t|{"total":^10}')
print('-' * 80)
for i,pessoa in enumerate(time):
    t=len(gols)
    print(f'\t{i:^6}|\t{pessoa["nome"]:10}|',end='')
    print(f'\t{pessoa["gols"]}'.ljust(30),end='')
    print(f'\t|{pessoa["total"]:^10}')
    print('-' * 80)

while True:
    opção=int(input('Deseja ver os dados de qual jogador?(Digite 999 para parar):'))
    if opção==999:
        break    
    for n, jogador in enumerate(time):
        if opção==n:
            print(jogador)
    if opção>=len(time):
        print(f'\033[31mERRO!Não existe jogador com código {opção}!\033[m')
        
    

    



