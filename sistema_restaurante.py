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

opcao = int(input("Digite o código do seu pedido: "))

match(opcao):
    case 1:
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
    case _:
        print("Opção incorreta. Tente Novamente")
while True:
    opcao2 = input("Deseja fazer mais um pedido?")
    print("""1 - Sim
             2 - Não""")
        df

        
