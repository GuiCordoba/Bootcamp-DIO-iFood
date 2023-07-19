numPedidos = int(input())
listaPedidos = " "

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()
    if ehVegano == 's':
        vegano = 'Vegano'
    elif ehVegano == 'n':
        vegano = 'Nao-vegano'
    listaPedidos += f'Pedido {i}: {prato} ({vegano}) - {calorias} calorias\n'

    #//TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
print(listaPedidos)