import math
r1=int(input('Informe o tamanho da primeira reta:'))
r2=int(input('Informe o tamanho da segunda reta:'))
r3=int(input('Informe o tamanho da terceira reta:'))
if (r1+r2)>r3 and (r3+r2)>r1 and (r1+r3)>r2:
    print('Essas retas formam um triângulo')
else:
    (r1+r2)<=r3 or (r2+r3<=r1)
    print('Essas retas não formam um triângulo')

