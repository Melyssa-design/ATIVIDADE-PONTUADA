import os
os.system ("clear")

#Um posto está vendendo combustíveis com a seguinte tabela de descontos: 
#Álcool Até 25 litros, desconto de 2% por litro
#Acima de 25 litros, desconto de 4% por litro
#Gasolina Até 25 litros, desconto de 3% por litro
#Acima de 25 litros, desconto de 5% por litro.
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível 
#(codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente 
# sabendo-se que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.

litros_vendidos = float(input("Digite a quantidade de litros: " ))
tipo_de_combustivel = input("Digite o tipo de combustível\n1-Álcool. \n2-Gasolina. : """)

valor_do_alcool = 3.79
valor_da_gasolina = 6.59


match tipo_de_combustivel:
    case "Alcool" | "alcool":
        litros_vendidos <=25
        desconto = valor_do_alcool * 0.02
        valor_a_ser_pago = valor_do_alcool - desconto
        if litros_vendidos <25:
         desconto = valor_do_alcool * 0.04
         valor_a_ser_pago = valor_do_alcool - desconto    
        print(f"Valor a ser pago: {valor_a_ser_pago:.2f}")
  

    case "Gasolina" | "gasolina":
        litros_vendidos <=25
        desconto = valor_da_gasolina * 0.03
        valor_a_ser_pago = valor_da_gasolina - desconto
        if litros_vendidos <25:
         desconto = valor_do_alcool * 0.05
         valor_a_ser_pago = valor_do_alcool - desconto 
        print(f"Valor a ser pago: {valor_a_ser_pago:.2f}")
    case _:
        print("Combustivel invalido")

