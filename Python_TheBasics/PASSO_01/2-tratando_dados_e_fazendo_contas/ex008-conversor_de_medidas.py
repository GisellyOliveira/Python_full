# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS.

v = float(input('Quantos metros você deseja converter? '))
km = v / 1000
hm = v / 100
dam = v / 10
dc = v * 10
cm = v * 100
mm = v * 1000
print('{:.1f} metros equivale a:'.format(v))
print('{} kilômetros \n{} hectómetros \n{} decâmetros' .format(km, hm, dam))
print('{} decímetros \n{} centímetros \n{} milímetros' .format(dc, cm, mm))
