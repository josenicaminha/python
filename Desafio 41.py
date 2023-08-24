import math
ano=int(input('Qual o ano em que você nasceu?'))
idade=2023-ano
if idade<=9:
    print('Você pertece à categoria mirim')
elif idade>9 and idade<=14:
    print('Você pertece à categoria infantil')
elif idade>14 and idade<=19:
    print('Você pertece à categoria junior')
elif idade>19 and idade<=20:
    print('Você pertece à categoria senior')
elif idade>20:
    print('Você pertecen à categoria master')
