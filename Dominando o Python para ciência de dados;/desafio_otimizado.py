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

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao = 1:

        elif opcao = 2:

