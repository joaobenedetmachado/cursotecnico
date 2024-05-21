menorque1500 = 0
entre1500e3000 = 0
maiorque3000 = 0
count = 0
while count < 10:
    salario = int(input('digite seu salario: '))
    if salario < 1500:
        menorque1500 = menorque1500 +1
    if salario >= 1500 and salario < 3000:
        entre1500e3000 = entre1500e3000 +1
    if salario > 3000:
        maiorque3000 = maiorque3000 +1
    count = count + 1
print(menorque1500, entre1500e3000, maiorque3000)