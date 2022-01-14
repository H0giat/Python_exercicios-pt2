nome=[]

for n in range(5):
    x=str(input('Digite um nome: '))
    nome.append(x)
print(nome)

pos=int(input('Posição deseja: '))
print('A posição desejada coreesponde a: ',nome[pos])
