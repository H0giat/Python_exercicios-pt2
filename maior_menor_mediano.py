num1=float(input('Digite o primeiro número: '))
num2=float(input('Digite o segundo número: '))
num3=float(input('Digite o terceiro número: '))
if num1>num2>num3:
    print(f'{num1} é o maior, {num2} é o mediano e o {num3} é o menor')
elif num2>num3>num1:
    print(f'{num2} é o maior, {num3} é o mediano e o {num1} é o menor.')
elif num3>num2>num1:
    print(f'{num3} é o maior, {num2} é o mediano e o {num1} é o menor.')
elif num3>num1>num2:
    print(f'{num3} é o maior, {num1} é o mediano e o {num2} é o menor.')
elif num1>num3>num2:
    print(f'{num1} é o maior, {num3} é o mediano e o {num2} é o menor.')
elif num2>num1>num3:
    print(f'{num2} é o maior, {num1} é o mediano e o {num3} é o menor.')
