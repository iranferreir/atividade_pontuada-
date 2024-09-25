"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Arthur Fraga de Oliveira
2 - Iran Ferreira dos Santos
"""

import os

# Limpa o terminal.
os.system("cls || clear") 
lista_compra = []
formas_de_pagamento = []
a_vista = 0
lista_itens = []

picanha = 45.00
lasanha = 30.00
strogonoff = 25.00
bife_acebolado = 40.00
frango_grelhado = 45.00
peixe_assado = 55.00
bife_a_milanesa = 45.00

print("""
      1 - Picanha - R$25,00
      2 - Lasanha - R$20,00
      3 - Strogonoff - R$18,00
      4 - Bife Acebolado - R$15,00
      5 - Pão com ovo - R$5,00  
""")

while True:
    while True:
        opcao = int(input("Digite o código do seu pedido: "))
        if opcao < 1 or opcao >= 8:
            print("Opção incorreta. Tente Novamente")
        else:
            break
    match(opcao):
        case 1:
            lista_itens.append("Picanha : 45.00")
            lista_compra.append(picanha)
            print("Picanha foi adiconada no seu pedido")
        case 2:
            lista_compra.append(lasanha)
            print("Lasanha foi adiconada no seu pedido")
        case 3:
            lista_compra.append(strogonoff)
            print("Strogonoff foi adiconado ao seu pedido")
        case 4:
            lista_compra.append(bife_acebolado)
            print("Bife acebolado foi adicionado ao seu pedido") 
        case 5:
            lista_compra.append(frango_grelhado)
            print("Frango Grelhado foi adiconado no seu pedido")
        case 6:
            lista_compra.append(peixe_assado)
            print("Peixe Assado foi adiconado no seu pedido")
        case 7:
            lista_compra.append(bife_a_milanesa)
            print("Bife à milanesa a milanesa foi adiconado no seu pedido")
        case 0:
            break
    while True:
        opcao2 = int(input("""Deseja fazer mais um pedido?
1 - Sim      0 - Não
=>"""))
        if (opcao2 == 1) or (opcao2 == 0):
            break
        else:
            print("TENTE NOVAMENTE")

    match(opcao2):
        case 1:
            print("Escolha um pedido")
        case 0:
            break
while True:
    opcao3 = int(input("""Qual a sua forma de pagamento: 
    1 - Pagamento à vista(10% de desconto)    
    2 - Pagamento no cartão de crédito(10% a mais do preço total)
    =>"""))
    if opcao3 == 1 or opcao3 == 2:
        break
    else:
        print("Opção incorreta. ")

def pagamento (total:float, opcao:int):
    soma = sum(total)
    desconto = soma *0.1
    if opcao == 1:
        valor_final = soma - desconto
        print("Pagamento selecionado: à vista")
        print(f"Valor Bruto: {soma}")
        print(f"Desconto: {desconto:.2f}")
        print(f"Total a pagar: {valor_final}")
    else:
        valor_final = soma + desconto
        print("Pagamento selecionado: Cartão de crédito")
        print(f"Valor Bruto: {soma}")
        print(f"Acréscimo: {desconto:.2f}")
        print(f"Total a pagar: {valor_final}")

match(opcao3):
        case 1 | 2 :
            resultado = pagamento(lista_compra, opcao3)
            for pag in lista_itens:
                print(f"Lista de itens: {pag}")
            
        










        
