# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M2.

larg = float(input('Quantos metros de largura tem a parede? '))
alt = float(input('Quantos metros de altura tem a parede? '))
area = larg * alt
tinta = area / 2

print('Sua parede tem a dimensão de {} * {} e, para a área de {}m², serão necessários {} litros de tinta.' .format(larg, alt, area, tinta))