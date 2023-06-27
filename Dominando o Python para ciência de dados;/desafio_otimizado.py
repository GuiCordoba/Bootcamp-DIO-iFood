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
        print(">>>Operação realizada com sucesso<<<")
    else:
        print("!!!ERRO. Valor inválido!!!")

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

