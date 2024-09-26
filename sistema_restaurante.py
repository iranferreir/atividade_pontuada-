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

picanha = 55.90
lasanha = 45.90
strogonoff = 39.90
bife_acebolado = 47.90
frango_grelhado = 53.90
peixe_assado = 64.90
bife_a_milanesa = 34.90

print("""
\n========== CARDÁPIO ===========\n
CÓDIGO |     PRATOS      |    VALOR
1      | Picanha         |   55,90 R$
2      | Lasanha         |   45,90 R$
3      | Strogonoff      |   39,90 R$
4      | Bife Acebolado  |   47,90 R$
5      | Frango Grelhado |   53,90 R$
6      | Peixe Assado    |   64,90 R$ 
7      | Bife à milanesa |   34,90 R$
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
            lista_itens.append("Picanha 55.90 R$")
            lista_compra.append(picanha)
            print("Picanha foi adiconada no seu pedido")
        case 2:
            lista_itens.append("Lasanha 45,90 R$")
            lista_compra.append(lasanha)
            print("Lasanha foi adiconada no seu pedido")
        case 3:
            lista_itens.append("Strogonoff 39,90 R$")
            lista_compra.append(strogonoff)
            print("Strogonoff foi adiconado ao seu pedido")
        case 4:
            lista_itens.append("Bife acebolado 47,90 R$")
            lista_compra.append(bife_acebolado)
            print("Bife acebolado foi adicionado ao seu pedido") 
        case 5:
            lista_itens.append("Frango Grelhado 53,90 R$")
            lista_compra.append(frango_grelhado)
            print("Frango Grelhado foi adiconado no seu pedido")
        case 6:
            lista_itens.append("Peixe Assado 64,90 R$")
            lista_compra.append(peixe_assado)
            print("Peixe Assado foi adiconado no seu pedido")
        case 7:
            lista_itens.append("Bife à Milanesa 34,90 ")
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
        case 0:
            break
while True:
    opcao3 = int(input("""Qual a sua forma de pagamento: 
1 - Pagamento à vista(10% de desconto)    
2 - Pagamento no cartão de crédito(10% de acréscimo no valor total)
=>"""))
    if opcao3 == 1 or opcao3 == 2:
        break
    else:
        print("Opção incorreta. ")

match(opcao3):
        case 1 | 2 :
            for pag in lista_itens:
                print(f"Lista de itens: {pag}")

def pagamento (total, opcao):
    soma = sum(total)
    desconto = soma * 0.1
    if opcao == 1:
        valor_final = soma - desconto
        print("Pagamento selecionado: à vista")
        print(f"Subtotal: {soma:.2f} R$")
        print(f"Desconto: {desconto:.2f} R$")
        print(f"Total a pagar: {valor_final:.2f} R$")
    else:
        valor_final = soma + desconto
        print("Pagamento selecionado: Cartão de crédito")
        print(f"Subtotal: {soma:.2f} R$")
        print(f"Acréscimo: {desconto:.2f} R$")
        print(f"Total a pagar: {valor_final:.2f} R$")

resultado = pagamento(lista_compra, opcao3)
            
        










        
