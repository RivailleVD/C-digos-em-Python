#from math import hypot
co = float(input('Cateto oposto '))
ca = float(input('Cateto Adjacence '))
hi = (co ** 2 + ca ** 2) ** (1/2)
#hi = math.hypot(co , ca)
print('A hypotenusa vai medir {:.2f}'.format(hi))