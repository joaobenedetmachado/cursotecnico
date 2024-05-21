valor = float(input('digite o valor depositado: '))
juros = float(input('digite o juros por mes: '))

valorcomjuros = (valor / 100) * juros + valor

print(valorcomjuros)