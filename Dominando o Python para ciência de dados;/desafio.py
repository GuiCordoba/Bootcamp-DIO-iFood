menu = """
Selecione uma opção:
[1] Depositar;
[2] Sacar;
[3] Extrato;
[4] Sair;
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAUQES = 3

while True:
    opcao = input(menu)
     
    if opcao == 1:
        print("Depósito")

    elif opcao == 2:
        print("saque")

    elif opcao == 3:
        print("Extrato")

    elif opcao == 4:
        break

    else:
        print("Opção inválida. Selecione um opção válida.")

print(menu)