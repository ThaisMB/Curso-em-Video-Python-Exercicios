n=int(input('Digite um número inteiro:'))


print('Escolha uma base para conversão:')

print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')

d= int(input('Sua opção:'))

if d==1:
    print('O número {} convertido para binário é {}.'.format(n, bin(n)).replace('0b',''))
elif d==2:
    print('O número {} convertido em octal é {}.'.format(n, oct(n)).replace('0o',''))
elif d==3:
    print('O número {} convertido em hexadecimal é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida: tente novamente.')
