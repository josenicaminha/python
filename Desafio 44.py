import math
p=str(input('Informe o nome do produto:  '))
vp=float(input('Diga o valor do produto: ' ))
cpg=int(input('Escolha a melhor condição de pagamento para você:'
              '1. À vista ou pix;'
              '2. À vista no cartão;'
              '3. Em até 2x no cartão;'
              '4. Em 3x ou mais no cartão.'))
primeiro=vp-(vp * .1)
segundo=vp-(vp * .05)
terceiro=vp
quarto=vp+(vp * .2)
if cpg==1:
   print('Como o valor do {} é {} e a condição de pagamento é à vista ou pix, você pagará {}'.format(p,vp,primeiro))
elif cpg==2:
    print('Como o valor do {} é {} e a condição de pagamento é à vista no cartão, você pagará {}'.format(p,vp, segundo))
elif cpg==3:
    print('Como o valor do {} é {} e a condição de pagamento é em 2x no cartão, você pagará {}'.format(p,vp, terceiro))
elif cpg==4:
    print('Como o valor do {} é {} e a condição de pagamento é em 3x ou mais, você pagará {}'.format(p,vp, quarto))
