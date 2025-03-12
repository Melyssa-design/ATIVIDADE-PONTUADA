import os
os.system("clear")

#Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. 
#O programa deve calcular o resultado da operação escolhida aplicado a A e B. 
# Por exemplo, se a operação escolhida foi * e A = 1 e B = 3, 
# o programa deve fornecer como resultado o valor de 1*3, que é 3.

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite Segundo numero: "))
operador = input("Digite a operação desejada (+ - * /): ")


match operador:
    case "+":
        resultado = primeiro_numero + segundo_numero
    case "-":   
        resultado = primeiro_numero - segundo_numero
    case "*":
        resultado = primeiro_numero * segundo_numero
    case "/":
        resultado = primeiro_numero / segundo_numero

    case _:
     print("opção invalida")

print(f"\nPrimeiro número: {primeiro_numero}")
print(f"Operador: {operador}")
print(f"Segundo número: {segundo_numero}")
print(f"Resultado: {resultado}")
