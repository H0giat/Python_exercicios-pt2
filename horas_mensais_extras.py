nome=input('Digite seu nome: ')
hm=float(input('Digite horas mensais: '))
he=float(input('Digite suas horas extras: '))
f=int(input('Dias que faltou: '))
ht=he+(hm-f*8)
print(f'Horas trabalahadas de {nome}: {ht}.')
