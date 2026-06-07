codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

if codigo == 1:
    preco_unitario = 4.00
elif codigo == 2:
    preco_unitario = 4.50
elif codigo == 3:
    preco_unitario = 5.00
elif codigo == 4:
    preco_unitario = 2.00
elif codigo == 5:
    preco_unitario = 1.50
else:
    preco_unitario = 0.00

total = preco_unitario * quantidade

print(f'Total: R$ {total:.2f}')
