print('\033[36m='*60)
print('\033[35m                 LOJAS GUANABARA')
print('\033[36m='*60)

preço= float(input('Preço das Compras: R$'))


print('\033[34m FORMAS DE PAGAMENTPO\033[m')

print('[1] à vista em dinheiro/cheque')
print('[2] à vista no cartão')
print('[3] 2x ou mais no cartão')
print('[4] 3x ou mais no cartão')

opção=int(input('Qual é a opção?'))

if opção==1:
    pfinal=float( preço -(preço*10/100))

    
elif opção==2:
    pfinal= float(preço - (preço*5/100))

elif opção==3:
    pfinal= float(preço)
    vpar=preço/2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(vpar))

elif opção==4:
    parcelas= int(input('Quantas parcelas?:'))
    pfinal= float(preço +(preço*20/100))
    vpar=pfinal/parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, vpar))

else:
    pfinal=preço
    print('\033[31m OPÇÃO INVÁLIDA:tente novamente \033[m')

print('Sua compra é de R${:.2f} e vai custar R${:.2f} no final.'.format(preço, pfinal))



