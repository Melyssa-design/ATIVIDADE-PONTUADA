import os
os.system("clear")

#Faça um algoritmo para ler: a #descrição do produto (nome), a #quantidade adquirida e o preço #unitário. Calcular e escrever o #total (total = quantidade #adquirida * preço unitário), o #desconto e o total a pagar 
#(total a pagar = total - #desconto), sabendo-se que: 
#- Se quantidade <= 5 o desconto #será de 2% 
#- Se quantidade > 5 e quantidade <= 10 o desconto será de 3% 
#- Se quantidade > 10 o desconto #será de 5%.

nome_produto = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))


total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = total * 0.02  
elif quantidade <= 10:
    desconto = total * 0.03  
else:
    desconto = total * 0.05  

total_pagar = total - desconto

print("\nResumo da compra:")
print(f"Produto: {nome_produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:}")