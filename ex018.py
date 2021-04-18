import math

ang=float(input('Digite o ângulo para saber o valor de seu seno, de seu cosseno e de sua tangente:'))

seno= math.sin(math.radians(ang))
cos= math.cos(math.radians(ang))
tang= math.tan(math.radians(ang))

print('O seno do ângulo {}° é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2}.'.format(ang, seno, cos, tang))