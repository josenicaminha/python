import time
input('\033[1;30;45m INICIAREMOS UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFÍCIOS\033[m')
esc=int(input('Se você deseja que os fogos sejam acionados, digite 1, caso não queira digite 2 :    '))
if esc==2:
  print('\033[1;30;47m Obrigado! Como você não deseja ouvir os fogos, eu não irei acioná-los\033[m')
else:
    x=10
    while x >0:
          print(x)
          time.sleep(1)
          x -= 1  # uso x-=1 no lugar de x=x-1
    print('DIVIRTA-SE:\033[1;30;45m FOGO!!!!!\033[m')
    print('\033[1;36;48OBRIGADO PELA SUA PARTICIPAÇÃO\033[m')