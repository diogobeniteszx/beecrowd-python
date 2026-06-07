salario_atual = float(input())

if salario_atual <= 2000:
    print('Isento')
else:
    if salario_atual <= 3000:
        imposto = (salario_atual - 2000) * 0.08
    elif salario_atual <= 4500:
        imposto = (3000 - 2000) * 0.08 + (salario_atual - 3000) * 0.18
    else:
        imposto = (3000 - 2000) * 0.08 + (4500 - 3000) * \
            0.18 + (salario_atual - 4500) * 0.28

    print(f'R$ {imposto:.2f}')
