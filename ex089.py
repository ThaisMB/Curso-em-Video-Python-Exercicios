turma=[]
while True:
    nome=(str(input('Nome:')))
    n1=(float(input('Nota 1:')))
    n2=(float(input('Nota 2:')))
    media=(n1+n2)/2
    turma.append([nome,[n1,n2], media])

    resposta=(input('Quer continuar? [S / N]'))
    if resposta in 'Nn':
        break
print(turma)
print('=-'*30)
print('-'*20)
print(f'{"No.":<5}{"Nome":<10}{"Média":>9}')
for c,v in enumerate(turma):
    print(f'{c:<5}{v[0]:<10}{v[2]:>8.1f}')

while True:
    resposta=int(input('Mostrar notas de qual aluno?(999 interrompe):'))
    if resposta<=len(turma)-1:
        print(f'As notas de {turma[resposta][0]} são:{turma[resposta][1]}')

    if resposta==999:
            print('FINALIZANDO...')
            break