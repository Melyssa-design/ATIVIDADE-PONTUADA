import os
os.system("clear")

#Uma fruteira está vendendo frutas com a seguinte tabela de preços: 
#Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00, 
# receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs 
# adquiridas e escreva o valor a ser pago pelo cliente.

quantidade_morango = float(input("Digite a quantidade de morangos (em kg): "))
quantidade_maca = float(input("Digite a quantidade de maçãs (em kg): "))
    
if quantidade_morango <= 5:
    preco_morango = quantidade_morango * 2.50
else:
    preco_morango = quantidade_morango * 2.20
      
if quantidade_maca <= 5:
    preco_maca = quantidade_maca * 1.80
else:
    preco_maca = quantidade_maca * 1.50
    
valor_total = preco_morango + preco_maca
    
if quantidade_morango + quantidade_maca >= 10 or valor_total > 15.00:
    desconto = valor_total * 0.10
    valor_total_com_desconto = valor_total - desconto
    print(f"Desconto de 10% aplicado: R$ {desconto:.2f}")
    print(f"Valor total a pagar com desconto: R$ {valor_total_com_desconto:.2f}")
else:
    print(f"Valor total a pagar: R$ {valor_total:.2f}")
