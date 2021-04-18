n=input('Qual é seu nome?')

if n== 'Gustavo':
    print ('Que nome bonito!')

elif n=='Maria' or n=='Pedro' or n=='Paulo':
    print('Seu nome é bem popular no Brasil!')

elif n in 'Joana Juliana Marisa Suzana':
    print('Que belo nome feminino!')
else: 
    print('Que nome mais normal!')
print('Tenha um bom dia, {}!'.format(n))