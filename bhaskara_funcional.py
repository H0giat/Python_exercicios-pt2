import math
a,b,c = input().split(" ")
a= float(a)
b= float(b)
c= float(c)
if(a==0):
    print('Impossivel calcular')
else:
    delta = b*b - (4*a*c)
if delta<0:
    print('Impossivel calcular')
elif delta==0:
    raiz = -b / (2*a)
    print('Impossivel calcular')
else:
    raiz1 = (-b + math.sqrt(delta) ) / (2*a)
    raiz2 = (-b - math.sqrt(delta) ) / (2*a)
print('R1 = %.5f'%raiz1)
print('R2 = %.5f'%raiz2)
