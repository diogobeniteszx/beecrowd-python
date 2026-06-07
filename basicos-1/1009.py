vendedor = input()
salario_fixo = float(input())
vendas = float(input())

salario_total = salario_fixo + (vendas * 0.15)

print(f'TOTAL = R$ {salario_total:.2f}')
