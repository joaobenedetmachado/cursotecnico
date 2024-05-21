valorHora = float(input('valor da hora: '))
horastrabalhada = float(input('horas trabalhada: '))
inss = (((valorHora*horastrabalhada) / 100) * 2) - (valorHora * horastrabalhada)
print(inss)