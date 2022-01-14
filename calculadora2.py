num1=float(input('Digite o primeiro número: '))
num2=float(input('Digite o segundo número: '))
operador=input('Digite o operador que deseja usar: ')
if operador == '+':
    print(num1+num2)
elif operador == '-':
    print(num1-num2)
elif operador == '*':
    print(num1*num2)
elif operador == '/':
    print(num1/num2)
else:
    print('Operação inválida.')
