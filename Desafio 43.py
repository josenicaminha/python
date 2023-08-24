import math

p = float(input('Informe o seu peso:'))
a = float(input('Qual é a sua altura?'))
imc: float=(p / (a ** 2))
if imc < 18.5:
    print('Preste atenção em sua alimentação, pois você está \003[0;33;46m abaixo do peso\033[m')
elif imc >= 18.5 and imc <= 24.9:
    print('\033[2;30;45m PARABÉNS!!!\033[m  Você está com o peso ideal.')
elif imc >=25 and imc <=29.9:
     print('\033[2;36;42m CUIDADO!!!\033[m Você já está acima do peso.')
elif imc >=30 and imc <=34.9:
     print('\033[4;38;41m ALERTA!!!\033[m Você está com obesidade de grau I.')
elif imc>=35 and imc <=40:
     print('\033[1;33;39m ATENÇÃO!!!!\033[m  Você se encontra com obesidade de grau II, procure um nutricionista.')
