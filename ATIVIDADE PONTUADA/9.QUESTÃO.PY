import os
os.system ("clear")

# Uma financeira usa o seguinte 
# critério para conceder #empréstimos: o valor total do 
# empréstimo deve ser até dez #vezes o valor da renda mensal do solicitante e o valor da 
# prestação deve ser no máximo #30% da renda mensal do 
# solicitante. Escreva um #programa que leia a renda 
# mensal de um solicitante, o #valor total do empréstimo #solicitado e o número de,
# prestações que o solicitante #deseja pagar e informe se o 
# empréstimo pode ou não ser concedido.


renda = float(input("Digite a renda mensal do solicitante: "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: "))
num_prestacoes = int(input("Digite o número de prestações desejado: "))

limite_emprestimo = 10 * renda
prestacao_maxima = 0.3 * renda
valor_prestacao = valor_emprestimo / num_prestacoes

if valor_emprestimo <= limite_emprestimo and valor_prestacao <= prestacao_maxima:
    print("Empréstimo pode ser concedido.")
else:
    print("Empréstimo negado.")