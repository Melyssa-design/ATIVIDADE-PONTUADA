#Em uma loja de CD´s existem apenas quatro tipos de preços que estão associados a cores. 
# Assim os CD´s que ficam na loja não são marcados por preços e sim por cores. 
# Desenvolva o algoritmo que a partir da entrada da cor o software mostre o preço. ,
# A loja está atualmente com a seguinte tabela de preços.  
import os
os.system ("clear")

cor = input("""Escolha uma cor de cd:
\n COR \t VALOR \n VERDE \t R$ 10,00 \n AZUL \t R$ 20,00 \n AMARELO R$ 30,00 \n VERMELHO R$ 40,00 \n
: """)

match cor:
   case "verde":
      print("Valor = 10,00")
   case "azul":
       print("Valor = 20,00")
   case "amarelo":
      print("Valor = 30,00")   
   case "vermelho":
      print("Valor = 40,00")   
   case _:
      print("invalido")