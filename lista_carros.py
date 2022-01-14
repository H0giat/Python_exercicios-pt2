placa=['AAA-1A11','BBB-2B222', 'CCC-3C333', 'DDD-4D444', 'EEE-5E555']
nome=['ONIX', 'FIAT UNO', 'CELTA', 'CORSA', 'HILUX']
ano=[2021,2020,1970,2000,2021]
cor=['CINZA','VERMELHO','ROXO ALELUIA', 'AMARELO', 'ROSA']
preco=[68000.00, 45000.00, 28000,00, 50000.00,110000.00]
nda=[1,2,2,5,1]
nome_ultimo_dono=['Douglas', 'Bruno', 'Ademar', 'Gabriel','Emanueli']
'''
placa=[]
nome=[]
ano=[]
cor=[]
preco=[]
nda=[]    # número de donos anteriosres
nome_ultimo_dono=[]
'''
'''
num_veiculos=int(input('Digite o número de veículos a serem inseridos: '))

for i in range(num_veiculos):
    pp=input('Digite a placa do carro: ')
    placa.append(pp)
    nn=input('Digite o nome do veículo: ')
    nome.append(nn)
    an=str(input('Digite o ano do carro: '))
    ano.append(an)
    cc=input('Digite a cor do carro: ')
    cor.append(cc)
    pr=float(input('Digite o preço do carro: '))
    preco.append(pr)
    tl=str(input('Digite o número de telefone do último dono: '))
    nda.append(tl)
    nd=input('Digite o nome do último dono do carro: ')
    nome_ultimo_dono.append(nd)
'''
for i in range(len(placa)):
    print(f'O dono do carro {nome[i]} é o {nome_ultimo_dono[i]}.\nA placa do carro é {placa[i]} e o ano é {ano[i]}.\nA cor do carro é {cor[i]} e o preço é de R${preco[i]}.\nO telefone do último dono é {nda[i]}.')

cor2=input(f'Digite a cor para verificação em estoque: ').upper
for i in range(len(cor)):
    if(cor[i]==cor2):
        print(f'O dono do carro {nome[i]} é o {nome_ultimo_dono[i]}.\nA placa do carro é {placa[i]} e o ano é {ano[i]}.\nA cor do carro é {cor[i]} e o preço é de R${preco[i]}.\nO telefone do último dono é {nda[i]}.')


ano2=int(input(f'Digite o ano mínimo do veículo para verificação em estoque: '))

for i in range(len(ano)):
    if(ano[i]>=ano2):
        print(f'O dono do carro {nome[i]} é o {nome_ultimo_dono[i]}.\nA placa do carro é {placa[i]} e o ano é {ano[i]}.\nA cor do carro é {cor[i]} e o preço é de R${preco[i]}.\nO telefone do último dono é {nda[i]}.')


preco_menor=float(input(f'Digite o preço abaixo do valor popular: '))

for i in range(len(preco)):
    if(preco[i]<preco_menor):
        print(f'O dono do carro {nome[i]} é o {nome_ultimo_dono[i]}.\nA placa do carro é {placa[i]} e o ano é {ano[i]}.\nA cor do carro é {cor[i]} e o preço é de R${preco[i]}.\nO telefone do último dono é {nda[i]}.')


preco_media1=float(input(f'Digite o menor preço para busca mais precisa: '))
preco_media2=float(input(f'Digite o maior preço para busca mais precisa: '))


for i in range(len(preco)):
    if(preco[i]<preco_media1 and preco[i]>preco_media2):
        print(f'O dono do carro {nome[i]} é o {nome_ultimo_dono[i]}.\nA placa do carro é {placa[i]} e o ano é {ano[i]}.\nA cor do carro é {cor[i]} e o preço é de R${preco[i]}.\nO telefone do último dono é {nda[i]}.')
