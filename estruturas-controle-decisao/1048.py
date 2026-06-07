salario_atual = float(input())

if salario_atual <= 400.00:
    percentual_reajuste = 15
elif salario_atual <= 800.00:
    percentual_reajuste = 12
elif salario_atual <= 1200.00:
    percentual_reajuste = 10
elif salario_atual <= 2000.00:
    percentual_reajuste = 7
else:
    percentual_reajuste = 4

valor_reajuste = salario_atual * percentual_reajuste / 100
novo_salario = salario_atual + valor_reajuste

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {valor_reajuste:.2f}')
print(f'Em percentual: {percentual_reajuste} %')
