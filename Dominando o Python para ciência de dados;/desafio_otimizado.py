import textwrap

def menu():
    menu = '''\n
    Selecione uma opção:
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Alterar Limite de Saque
    [5] Nova Conta
    [6] Listar Contas
    [7] Novo Usúario   
    [8] Sair;
    -->'''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo = + valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("=== Operação realizada com sucesso ===")
    else:
        print("!!! ERRO. Valor inválido !!!")

def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print(">>> Operação falhou! Saldo insuficiente <<<")

    elif excedeu_limite:
        print(">>> Operação falhou! Valor inserido excede o limite <<<")

    elif excedeu_saques:
        print(">>> Operação falhou! Número máximo de saques escedido <<<")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
    else:
        print("!!!ERRO. Valor informado inválido!!!")

def extrato(saldo, /, *, extrato):
    print("\n------------EXTRATO------------")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("-------------------------------")

def criar_usuario(usuarios):
    cpf = input("Insira o CPF do usuário (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print(">>> CPF já pertencente a um usuário <<<")
        return

    nome = input("Insira o nome completo do usuário: ")
    data_nascimento = input("Data de nascimento do usuário (dd-mm-aaaa): ")
    endereco = input("Endereço do usuário (logradouro, nro - bairro -cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else none

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Insira o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso ===")
        return{"agencia": agencia, "numero_conta": numero_conta, "ususario": usuario}

    print(">>> Usuário não encontrado <<<")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = int(menu())

        if opcao == 1:

        elif opcao == 2:

        elif opcao == 3:

        elif opcao == 4:

        elif opcao == 5:
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1
            
        elif opcao == 6:
        
        elif opcao == 7:

        elif opcao == 8:
        
        else:

