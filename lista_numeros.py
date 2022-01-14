numeros=[]
resp='s'
while(resp=='s' or resp=='S'):
    n=float(input('Digite um número: '))
    numeros.append(n)
    resp=input(f'Digite "s" para continuar: ')

acum=0
for i in range(len(numeros)):
    acum=acum+numeros[i]
media=acum/len(numeros)
print(f'A média dos valores é: {media}.')

qtd=0
for i in range(len(numeros)):
    if(numeros[i]>=0):
        qtd=qtd+1
print(f'A quantidade de números positivos é: {qtd}.')

qtd2=0
for i in range(len(numeros)):
    if(numeros[i]<0):
        qtd2=qtd2+1
print(f'A quantidade de números negativos é: {qtd2}.')

for i in range(len(numeros)):
    if(numeros[i]>media):
        print('Os números acima da média são:', numeros[i])

for i in range(len(numeros)):
    if(numeros[i]<media):
        print('Os números abaixo da média são:', numeros[i])

for i in range(len(numeros)):
    if(numeros[i]%2==0):
        print('Os números abaixo são pares:', numeros[i])

for i in range(len(numeros)):
    if (numeros[i]%2==1):
        print('Os números ímpares são:',numeros[i])

acum2=1
for i in range(len(numeros)):
    acum2=acum2*numeros[i]
print(f'O produto dos valores é: {acum2}.')