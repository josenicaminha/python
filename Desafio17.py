import math
cateto_oposto=int(input('Digite o valor do cateto oposto:  '))
cateto_adjacente=int(input('digite o valor do cateto adjacente:  '))
num1=cateto_oposto**2+cateto_adjacente**2
#num2=cateto_adjacente**2
#num3=num1+num2
hipotenusa=math.sqrt(num1)
print('Se o cateto oposto é  {} e o cateto adjacente é {}, então o comprimento da hipotenusa é {}'.format(cateto_oposto,cateto_adjacente,hipotenusa))

