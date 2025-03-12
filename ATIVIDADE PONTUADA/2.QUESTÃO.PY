import os
os.system("clear")
#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, 
# solicitar o tempo de casada (anos). Por fim, mostre os dados do usuário.

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estado_civil = input("Digite seu estado civil: ")

match sexo:
  case "Feminino" | "feminino":
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado civil: {estado_civil}")
  case "Masculino" | "masculino":
    print(f"Nome: {nome}")
    print(f"Sexo: {sexo}")
    print(f"Estado civil: {estado_civil}")
  case _:
    print ("Invalido")

match estado_civil:
  case "casada":
   tempo = input("Digite seu tempo de casada: ")
  case "casado":
   print(f"Nome: {nome}")
   print(f"Sexo: {sexo}")
   print(f"Estado civil: {estado_civil}")
  case "solteira":
   print(f"Nome: {nome}")
   print(f"Sexo: {sexo}")
   print(f"Estado civil: {estado_civil}")
  case _: 
    print("INVALIDO") 