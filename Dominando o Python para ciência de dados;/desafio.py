
menu = """
Selecione uma opção:
[1] Depositar;
[2] Sacar;
[3] Extrato;
[4] Alterar Limite de Saque;
[5] Sair;
-->"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo = + valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("ERRO! Valor inválido.")

    elif opcao == 2:
        valor = float(input("Insira o valor para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! Valor inserido excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques escedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("ERRO! Valor informado inválido.")

    elif opcao == 3:
        print("\n------------EXTRATO------------")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("-------------------------------")

    elif opcao == 4:
        print(f"Limite atual: R${limite:.2f}")
        novo_limite = float(input("Insira novo limite: R$"))
        if novo_limite > 0:
            limite = novo_limite
        else:
            print("ERRO! Valor informado inválido.")

    elif opcao == 5:
        break

    else:
        print("Opção inválida! Selecione um opção válida.")

