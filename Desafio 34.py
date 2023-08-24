import math
s=float(input('Diga qual é o seu salário atual:  '))
if s<=1250.00:
   sr1 = s*1.15
   print('O seu salário será de:{}'.format(round(sr1,2)))
else:
   sr1 = s*1.1
   print('O seu salario será de: {}'.format(round(sr1,2)))

