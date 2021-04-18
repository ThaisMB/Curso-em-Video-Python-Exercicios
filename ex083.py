expressao = input('Digite a expressão:')
pilha= []

for s in expressao:
    if s=='(':
        pilha.append('(')
    elif s==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')


if len(pilha)==0:
    print('Sua expressão está válida!')

else:
    print('Sua expressão está errada!')

