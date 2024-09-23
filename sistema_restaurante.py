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

print("""
1- Feijoada  === 0001
2- Arroz carreteiro === 0002
3- Coxinha === 0003     
4- Moqueca de peixe === 0004
5- Acarajé === 0005
6- Pato no tucupi === 0006
7- Bobó de camarão === 0007
""")
codigo1 = "0001"
codigo2 = "0002"
codigo3 = "0003"
codigo4 = "0004"
codigo5 = "0005"
codigo6 = "0006"
codigo7 = "0007"

opcao = int(input("digite seu prato de comida: "))

match(opcao):
    case "codigo1": 
        print("Feijoada")        
   