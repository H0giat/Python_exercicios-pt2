idade=int(input('Digite sua idade: '))
if idade>=18 and idade<=69:
    print('Obrigatório.')
elif idade==16 and idade==17:
    print('Facultativo.')
elif idade<16:
    print('Não é eleitor.')
elif idade>=70:
    print('Facultativo.')
