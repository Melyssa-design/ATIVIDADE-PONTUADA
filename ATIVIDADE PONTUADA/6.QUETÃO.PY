import os
os.system ("clear")

#Escreva um programa que leia do teclado as duas notas de um aluno, 
# calcule e exiba a média aritmética das notas. 
# O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado 
# (média superior ou igual a 6,0), média até 4,0, 
# o aluno está em recuperação, caso a média seja inferior a 4,0 o aluno será reprovado.

primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

media = (primeira_nota + segunda_nota)/2

if media >= 6:
  print("Parabéns")
elif media >=4:
  print("Está em recuperação")   
else:
   print("Está reprovado")     

print(f"Media: {media}")