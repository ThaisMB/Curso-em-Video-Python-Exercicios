preco=float(input('Qual o preço do prduto? R$'))
desconto=preco*5/100

print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(preco, preco-desconto))