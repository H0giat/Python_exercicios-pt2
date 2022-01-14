num=[]
r='s'
while(r=='s' or r=='S'):
    xx=float(input('Digite um número: '))
    num.append(xx)
    d=input('Digite s para continuar: ').lower()

acum=0
tamanho=len(num)

for n in range(tamanho):
    acum=acum+num[n]
media=acum/tamanho
print('A média é: ', media)
for n in range(tamanho):
    if(num[n]>media):
        print('O número ',num[n], ' é maior que a média.')