compra=float(input("Digite o valor da compra: "))
desconto=compra*0.2
promo=compra-desconto
if compra>=200:
    print("Ganhou desconto! Desconto total: ", desconto, ". Novo preço: ", promo)
else:
    print(compra)
