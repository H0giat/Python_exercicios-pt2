num_diaria=int(input('Quantas diárias pretende ficar: '))
s= 255.50
t= 360.50
d= 305.50
tipo=input('Digite o tipo da diária: ')
if tipo=='s':
    print('Valor: R$', num_diaria*s)
else:
    if tipo=='d':
        print('Valor: R$', num_diaria*d)
    else:
        if tipo=='t':
            print('Valor: R$', num_diaria*t)
        else:
            print('Tipo de diária inválido.')

