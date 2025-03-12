import os
os.system("clear")
#Faça um algoritmo que leia os valores A, B, C 
# e imprima na tela se a soma de A + B é menor que C, 
# caso contrário, imprima que a A + B é maior que C. 

A = float(input("Digite o primeiro numero: "))
B = float(input("Digite o segundo numero: "))
C = float(input("Digite o terceiro numero: "))

if A + B <= C:
    print ("É menor que C")
else:
    print("É maior que C")
