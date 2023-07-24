clientes = {}
contas = {}


# MÉTODO PARA CRIAR NOVO USUÁRIO/CLIENTE
def novo_cliente():

    # Solicitando o CPF
    cpf = input("Digite o CPF(apenas números) do cliente: ")
    # Utilizando o CPF como código identificador(chave primária) do cliente
    cliente_id = cpf

    # Faz a verificação caso o usuário já tenha sido cadastrado anteriormente
    if cpf not in clientes:

        # Entrada de dados de Pessoa
        nome = input("Digite o nome do cliente: ")
        nascimento = input("Digite a data de nascimento do cliente: ")

        # Entrada de dados correspondente a Residência
        logradouro = input(
            "Digite o logradouro da residência do cliente: ")
        numero = input("Digite o número da residência do cliente: ")
        bairro = input("Digite o bairro da residência do cliente: ")
        cidade = input("Digite a cidade da residência do cliente: ")
        sigla_estado = input(
            "Digite a sigla do estado o qual o cliente reside: ")

        # Posicionando as informações do endereço no formato desejado
        endereco = f"{logradouro},{numero} - {bairro} - {cidade}/{sigla_estado}"

        # Criando um objeto com as informações pertinentes ao cliente
        cliente = {"cpf": cpf, "nome": nome,
                   "nascimento": nascimento, "endereco": endereco}

        # Armazenando o cliente em seu específico campo em clientes
        clientes[cliente_id] = cliente

        print("Novo cliente cadastrado!")
        # Mostra todos od campos do cliente armazenado
        print(f"\n{clientes[cliente_id]}")

    else:
        print("O cliente já possui cadastrado!")


# MÉTODO PARA CRIAR NOVA CONTA
def nova_conta():

    # Necessário cliente(s) cadastrado(s)
    if len(clientes) != 0:

        # Inicial já solicita o cliente responsável p/ a conta
        cpf = input(
            "Digite o CPF(apenas números) do cliente o qual esta conta pertence: ")

        # Avalia se o código de identificação é válido
        if cpf in clientes:
            AGENCIA = "0001"
            nro_conta = str(len(contas) + 1)

            # Assumindo a estrutura padrão de conta junto com os dados informados
            conta = {"cliente_id": cpf, "agencia": AGENCIA, "conta": nro_conta,
                     "saldo": 0.0, "extrato": "", "limite": 500, "numero_saques": 0, "limite_saques": 3}

            # Utilizando o número da conta como código identificador(chave primária) e a armazena no dicionário de contas
            conta_id = nro_conta
            contas[conta_id] = conta

            print("Nova conta cadastrada!\n")

            # Mostra todas as contas cadastradas no CPF do responsável
            for conta in contas.values():
                if conta["cliente_id"] == cpf:
                    print(conta)
        else:
            print("Identificação inválida!")
    else:
        print("Necessário realizar o cadastro de cliente(s).")


# MÉTODO DE OPERAÇÕES
def operacoes():
    # Prossegue caso haja contas cadastradas, possibilitando navegar entre elas.
    if len(contas) != 0:
        print(f"\nEscolha uma conta p/ realizar as operações:")

        opcoes_conta = contas.keys()
        for opcao_conta in opcoes_conta:
            print(f"Número de conta [{opcao_conta}]")

        escolha_conta = input("> ")

        # Resgata todos os campos e valores registrados no dicionário de contas
        conta_id = escolha_conta
        saldo_conta = contas[conta_id]["saldo"]
        extrato_conta = contas[conta_id]["extrato"]
        limite_conta = contas[conta_id]["limite"]
        nro_saques_conta = contas[conta_id]["numero_saques"]
        lim_saques_conta = contas[conta_id]["limite_saques"]

        opcoes_operacao = """
[d] Depositar
[s] Sacar
[e] Extrato
[v] Voltar
> """

        while True:
            escolha_operacao = input(opcoes_operacao)

            if escolha_operacao == "d":
                valor_conta = float(input("Informe o valor do depósito: "))
                saldo_conta, extrato_conta = deposito(
                    saldo_conta, valor_conta, extrato_conta)

            elif escolha_operacao == "s":
                valor_conta = float(input("Informe o valor do saque: "))
                saldo_conta, extrato_conta, nro_saques_conta = saque(saldo=saldo_conta, valor=valor_conta, extrato=extrato_conta,
                                                                     limite=limite_conta, numero_saques=nro_saques_conta, limite_saques=lim_saques_conta)

            elif escolha_operacao == "e":
                extrato(saldo_conta, extrato=extrato_conta)

            elif escolha_operacao == "v":
                break

            else:
                print("Operação inválida!")

            # Atualiza os mais importantes campos da conta
            contas[conta_id]["saldo"] = saldo_conta
            contas[conta_id]["extrato"] = extrato_conta
            contas[conta_id]["numero_saques"] = nro_saques_conta

        # Mostra os campos atualizados após as operações
        print(f"\n{contas[conta_id]}")

    else:
        print("Necessário realizar o cadastro de conta(s).")


def saque(*, saldo, valor, extrato, limite=500, numero_saques, limite_saques=3):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


# PROGRAMA PRINCIPAL
def main():
    while True:

        opcoes_iniciais = """
[c] Novo cliente
[a] Nova conta
[o] Operações
[q] Sair
> """
        escolha_inicial = input(opcoes_iniciais)

        if escolha_inicial == "c":
            novo_cliente()
        elif escolha_inicial == "a":
            nova_conta()
        elif escolha_inicial == "o":
            operacoes()
        elif escolha_inicial == "q":
            break
        else:
            print("Operação inválida!")

main()