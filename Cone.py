#Rmaior (raio da base maior)
#rmenor (raio da base menor)
import math
h=float(input("Digite a altura: "))
R=float(input("Digite raio maior: "))
r=float(input("Digite raio menor: "))
volume=(math.pi*h)/3*(R**2+R*r+r**2)
print("O volume é igual : ", volume)
