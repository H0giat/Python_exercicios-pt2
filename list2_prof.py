numeros=[]
r="s"
while(r=="s" or r=='S'):
  xx=float(input("Digite o número "))
  numeros.append(xx)
  r=input("\nDigite s para continuar ").lower()

acum=0
tamanho=len(numeros)

for n in range(tamanho):
  acum= acum+numeros[n]
media= acum/tamanho
print('A média é:', media)
for n in range(tamanho):
  if(numeros[n]>media):
    print('O número ', numeros[n], ' é maior que a média')