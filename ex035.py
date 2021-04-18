print("-=-"*20) 

print ('\33[35m              Analisador de Triângulos          \33[m')
print("-=-"*20)

s1 = float(input('\33[33m Primeiro segmento:\33[m'))
s2 = float(input('\33[34m Segundo segmento: \33[m'))
s3 = float(input('\33[36m Terceiro segmento:\33[m'))

if s1 < s2+s3 and s2 < s1+s3 and s3 < s2+s1:

    print ('\33[32m Os segmentos acima PODEM FORMAR un TRIÂNGULO!\33[m')

else:

    print ('\33[31m Os segmentos acima NÂO PODEM FORMAR um TRIÂNGULO!\33[m')