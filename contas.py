"""
Escreva um em Python que solicite ao usuário os valores de três
contas de consumo (p.ex. água, luz e telefone) e o valor de seu salário.
Verifique se o salário é suficiente para pagar as três contas,
caso não seja apresente a mensagem “Salário insuficiente!”.
Caso seja, apresente o valor que restou do salário após pagar as contas.
"""

luz=float(input("Digite o valor da conta de luz: "))
agua=float(input("Digite o valor da conta de água: "))
telefone=float(input("Digite o valor da conta de telefone: "))
salario=float(input("Digite seu salário: "))
suficiente=salario-(luz+agua+telefone)
if salario>luz+agua+telefone:
    print("O valor restante é: ", suficiente, "")
else:
    print("Salário insuficiente.")
