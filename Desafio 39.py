ano=int(input('Digite o ano em que você nasceu:'))
i=2023-ano
passando=i-18
faltando=18-i
if i==18:
    print('\033[1;35;42m Você deve se alistar este ano\033[m')
elif i>18:
    print('\033[1;36;43m Você já deveria ter ido se alistar, pois você está {}anos atrasado\033[m'.format(passando))
elif i<18:
    print('\033[1;37;46m Você ainda não chegou à idade de se alistar\033[m, pois faltam {} anos'.format(faltando))