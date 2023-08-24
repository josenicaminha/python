d=float(input('Qual a distância de sua cidade para Cascavel?'))
if d<=200:
    p1=d*0.5
    print('Como a distância da sua cidade para Cascavel é {}km, então o preço da passagem é {} reais'.format(d,p1))
else:
    p2=d*0.45
    print('Como a distância de sua cidade para Cascavel é {}km, então o preço da sua passagem é {} reais'.format(d,p2))
