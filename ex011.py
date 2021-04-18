l=float(input('Largura da parede:'))
a=float(input('Altura da parede:'))

area=l*a
lt=area/2

print("Sua parede tem dimensão de {:.2f} x {:.2f} e sua área é de {} m2.".format(l, a, area))
print("Você precisará de {} litros de tinta para pintar essa parede.".format(lt))
