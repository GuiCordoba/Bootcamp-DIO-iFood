valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

totalHamburger = valorHamburguer * quantidadeHamburguer

totalBebidas = valorBebida * quantidadeBebida

precoFinal = totalHamburger + totalBebidas

troco = valorPago - precoFinal 

print(f'O preço final do pedido é R$ {precoFinal:.2f}. Seu troco é R$ {troco:.2f}.')