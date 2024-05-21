def realtodolar(a): return a * 5
def dolartoreal(a): return a / 5
escolha = str(input('escolha se voce quer converter real ou dolar: '))
valor = float(input('digite o valor para ser convertido: '))
if escolha == 'real' : print(dolartoreal(valor), 'R$')
else : print(realtodolar(valor), '$')              
