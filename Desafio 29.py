v=int(input('Diga a que velocidade você está andando em seu carro:  '))
vp=80
v2=vp/2
if v<=vp and v>=v2:
    print('Você está viajando com segurança, parabéns! Continue assim!')
if v<=v2:
    print('Você foi multado porque está atrapalhando o trânsito, com a velocidade muito baixa')
else:
    print('Você foi multado! Exagerou na velocidade, acima de 80km/h. Tenha cuida e diminua a velocidade')

# match v:
#     case range(41,80):
#         print('ok')
#     case range(40):
#         print('multa baixa velocidade')
#     case range(81,):
#         print('multa alta velocidade')

