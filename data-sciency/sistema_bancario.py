'''
As 3 primeiras operações implementadas para o sistema bancário proposto como desafio.
'''


menu_de_operacoes = """[d] Depositar 
[s] Sacar 
[e] Extrato 
[q] Sair\n"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu_de_operacoes)

# Operação de Depósito
    if opcao == "d" :
        valor_deposito = float(input("Digite um valor positivo para depósito.\n"))

        if valor_deposito > 0 :
            saldo += valor_deposito
            extrato += f"Depósito de R$ {valor_deposito:.2f}\n"
            print("Depósito efetuado!")
        else :
            print("Valor inválido!")

# Operação de Saque
    elif opcao == "s" :
        valor_saque = float(input("Digite um valor para saque limitado a R$500.00 por operação.\n"))

        if valor_saque > limite_saque:
            print("Excedido valor para operação de saque.")

        elif valor_saque > saldo :
            print("Saldo insuficiente!")

        elif numero_saques >= LIMITE_SAQUES :
            print("Excedido limite de saques diários.")
        
        elif valor_saque > 0 :
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque de R$ {valor_saque:.2f}\n"
            print("Saque efetuado!")

        else :
            print("Valor inválido!")

# Operação Extrato 
    elif opcao == "e" :
        print("EXTRATO".center(35,"-"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual de R$ {saldo:.2f}")
        print("-" * 35)

# Operação de Término
    elif opcao == "q" :
        print("Saiu do sistema!")
        break

# Entrada inválida.
    else :
        print("Operação inválida!")

            
